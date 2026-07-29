"""Unit tests for VanillaTektonAdapter."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.tekton_adapter import (
    VanillaTektonAdapter,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    PipelineNotFoundError,
    ServiceNotFoundError,
    TektonNotInstalledError,
)


class _FakeCRDApi:
    def __init__(self, data: dict | None = None, exc: Exception | None = None):
        self._data = data or {}
        self._exc = exc

    def list_namespaced_custom_object(self, **kwargs: object) -> dict:
        if self._exc:
            raise self._exc
        return self._data


class TestVanillaTektonAdapter:
    def test_list_task_runs_empty_raises_pipeline_not_found(self) -> None:
        api = _FakeCRDApi({"items": []})
        adapter = VanillaTektonAdapter(crd_api=api)
        with pytest.raises(PipelineNotFoundError):
            adapter.list_task_runs("my-pipeline", "ns")

    def test_list_pipeline_runs_empty_raises_service_not_found(self) -> None:
        api = _FakeCRDApi({"items": []})
        adapter = VanillaTektonAdapter(crd_api=api)
        with pytest.raises(ServiceNotFoundError):
            adapter.list_pipeline_runs("my-svc", "ns")

    def test_list_pipeline_runs_in_namespace_empty(self) -> None:
        api = _FakeCRDApi({"items": []})
        adapter = VanillaTektonAdapter(crd_api=api)
        result = adapter.list_pipeline_runs_in_namespace("ns", limit=10)
        assert result == []

    def test_list_pipeline_runs_in_namespace_403(self) -> None:
        from kubernetes.client.exceptions import ApiException

        api = _FakeCRDApi(exc=ApiException(status=403, reason="Forbidden"))
        adapter = VanillaTektonAdapter(crd_api=api)
        with pytest.raises(InsufficientPermissionsError):
            adapter.list_pipeline_runs_in_namespace("ns", limit=10)

    def test_list_pipeline_runs_in_namespace_404(self) -> None:
        from kubernetes.client.exceptions import ApiException

        api = _FakeCRDApi(exc=ApiException(status=404, reason="Not Found"))
        adapter = VanillaTektonAdapter(crd_api=api)
        with pytest.raises(TektonNotInstalledError):
            adapter.list_pipeline_runs_in_namespace("ns", limit=10)

    def test_list_pipeline_runs_in_namespace_generic_error(self) -> None:
        api = _FakeCRDApi(exc=ConnectionError("no route"))
        adapter = VanillaTektonAdapter(crd_api=api)
        with pytest.raises(ClusterUnreachableError):
            adapter.list_pipeline_runs_in_namespace("ns", limit=10)

    def test_to_task_run_info(self) -> None:
        api = _FakeCRDApi()
        adapter = VanillaTektonAdapter(crd_api=api)
        item: dict = {
            "metadata": {"name": "task-run-1"},
            "spec": {"taskRef": {"name": "build-task"}},
            "status": {
                "conditions": [
                    {
                        "type": "Succeeded",
                        "status": "True",
                        "reason": "Succeeded",
                    }
                ],
                "startTime": "2024-01-01T00:00:00Z",
                "completionTime": "2024-01-01T00:05:00Z",
            },
        }
        result = adapter._to_task_run_info(item)
        assert result["name"] == "task-run-1"
        assert result["task_ref"] == "build-task"
        assert result["status"] == "Succeeded"

    @patch("kubernetes.client.CustomObjectsApi")
    def test_crd_api_lazy_init(self, mock_api_class: MagicMock) -> None:
        adapter = VanillaTektonAdapter(crd_api=None)
        mock_instance = MagicMock()
        mock_api_class.return_value = mock_instance
        api = adapter._crd_api_client()
        assert api is mock_instance


class TestTaskRunStatus:
    def test_status_is_none(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._task_run_status(None) == "NotStarted"

    def test_empty_conditions(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._task_run_status({"conditions": []}) == "NotStarted"

    def test_non_mapping_condition(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._task_run_status({"conditions": ["not-a-dict"]}) == "NotStarted"

    def test_unknown_no_reason(self) -> None:
        adapter = VanillaTektonAdapter()
        result = adapter._task_run_status(
            {
                "conditions": [{"type": "Succeeded", "status": "Unknown", "reason": "Pending"}],
            }
        )
        assert result == "NotStarted"

    def test_succeeded(self) -> None:
        adapter = VanillaTektonAdapter()
        result = adapter._task_run_status(
            {"conditions": [{"type": "Succeeded", "status": "True", "reason": "Succeeded"}]}
        )
        assert result == "Succeeded"

    def test_failed(self) -> None:
        adapter = VanillaTektonAdapter()
        result = adapter._task_run_status(
            {"conditions": [{"type": "Succeeded", "status": "False", "reason": "Error"}]}
        )
        assert result == "Failed"

    def test_running(self) -> None:
        adapter = VanillaTektonAdapter()
        result = adapter._task_run_status(
            {"conditions": [{"type": "Succeeded", "status": "Unknown", "reason": "Running"}]}
        )
        assert result == "Running"

    def test_timeout(self) -> None:
        adapter = VanillaTektonAdapter()
        result = adapter._task_run_status(
            {"conditions": [{"type": "Succeeded", "status": "False", "reason": "DeadlineExceeded"}]}
        )
        assert result == "Timeout"


class TestExtractFailingStep:
    def test_status_is_none_returns_none(self) -> None:
        adapter = VanillaTektonAdapter()
        step, error = adapter._extract_failing_step(None, "Failed")
        assert step is None
        assert error is None

    def test_not_failed_not_timeout(self) -> None:
        adapter = VanillaTektonAdapter()
        step, error = adapter._extract_failing_step(
            {"steps": [{"name": "s", "terminated": {"exitCode": 1}}]},
            "Succeeded",
        )
        assert step is None
        assert error is None

    def test_step_not_mapping_is_skipped(self) -> None:
        adapter = VanillaTektonAdapter()
        step, error = adapter._extract_failing_step(
            {"steps": ["not-a-dict"]},
            "Failed",
        )
        assert step is None
        assert error is None

    def test_no_failing_step_found(self) -> None:
        adapter = VanillaTektonAdapter()
        step, error = adapter._extract_failing_step(
            {"steps": [{"name": "ok", "terminated": {"exitCode": 0}}]},
            "Failed",
        )
        assert step is None
        assert error is None


class TestCrdHelpers:
    def test_items_not_list(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._crd_items({"items": "not-a-list"}) == []

    def test_str_data_is_none(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._crd_str(None, "key") == ""

    def test_str_value_not_string(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._crd_str({"key": 123}, "key") == ""


class TestExtractPipelineRef:
    def test_spec_is_none(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._extract_pipeline_ref(None) == "inline"

    def test_no_pipeline_ref_no_pipeline_spec(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._extract_pipeline_ref({}) == "unknown"

    def test_pipeline_spec_present(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._extract_pipeline_ref({"pipelineSpec": {}}) == "inline"


class TestExtractTriggeredBy:
    def test_metadata_is_none(self) -> None:
        adapter = VanillaTektonAdapter()
        assert adapter._extract_triggered_by(None) is None
