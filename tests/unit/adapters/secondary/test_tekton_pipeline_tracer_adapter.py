from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.tekton_pipeline_tracer_adapter import (
    TektonPipelineTracerAdapter,
    _extract_status,
    _to_task_run_record,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    PipelineNotFoundError,
    TektonNotInstalledError,
)


class TestTektonPipelineTracerAdapter:
    def test_get_pipeline_run_success(self) -> None:
        adapter = TektonPipelineTracerAdapter()
        raw = {
            "metadata": {"name": "pr-1", "namespace": "ci"},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True"}],
                "startTime": "2026-01-01T00:00:00Z",
            },
            "spec": {"pipelineRef": {"name": "pipe-1"}},
        }
        mock_api = MagicMock()
        mock_api.get_namespaced_custom_object.return_value = raw

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            record = adapter.get_pipeline_run("ci", "pr-1")

            assert record["name"] == "pr-1"
            assert record["pipeline_ref"] == "pipe-1"

    def test_get_pipeline_run_not_found_raises(self) -> None:
        adapter = TektonPipelineTracerAdapter()

        class NotFoundError(Exception):
            status = 404

        mock_api = MagicMock()
        mock_api.get_namespaced_custom_object.side_effect = NotFoundError("not found")

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            with pytest.raises(PipelineNotFoundError):
                adapter.get_pipeline_run("ci", "pr-missing")

    def test_get_pipeline_run_forbidden_raises(self) -> None:
        adapter = TektonPipelineTracerAdapter()

        class ForbiddenError(Exception):
            status = 403

        mock_api = MagicMock()
        mock_api.get_namespaced_custom_object.side_effect = ForbiddenError("denied")

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            with pytest.raises(InsufficientPermissionsError):
                adapter.get_pipeline_run("ci", "pr-1")

    def test_get_pipeline_run_other_error_raises_cluster_unreachable(self) -> None:
        adapter = TektonPipelineTracerAdapter()

        class GenericError(Exception):
            pass

        mock_api = MagicMock()
        mock_api.get_namespaced_custom_object.side_effect = GenericError("boom")

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            with pytest.raises(ClusterUnreachableError):
                adapter.get_pipeline_run("ci", "pr-1")

    def test_list_task_runs_for_pipeline_success(self) -> None:
        adapter = TektonPipelineTracerAdapter()
        raw_item = {
            "metadata": {"name": "task-1", "namespace": "ci"},
            "status": {
                "conditions": [{"type": "Succeeded", "status": "True"}],
                "startTime": "2026-01-01T00:00:00Z",
            },
            "spec": {},
        }
        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.return_value = {"items": [raw_item]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            records = adapter.list_task_runs_for_pipeline("ci", "pr-1")

            assert len(records) == 1
            assert records[0]["name"] == "task-1"

    def test_list_task_runs_not_found_raises_tekton_not_installed(self) -> None:
        adapter = TektonPipelineTracerAdapter()

        class NotFoundError(Exception):
            status = 404

        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.side_effect = NotFoundError("not found")

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            with pytest.raises(TektonNotInstalledError):
                adapter.list_task_runs_for_pipeline("ci", "pr-1")

    def test_list_task_runs_forbidden_raises(self) -> None:
        adapter = TektonPipelineTracerAdapter()

        class ForbiddenError(Exception):
            status = 403

        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.side_effect = ForbiddenError("denied")

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            with pytest.raises(InsufficientPermissionsError):
                adapter.list_task_runs_for_pipeline("ci", "pr-1")

    def test_list_task_runs_other_error_raises_cluster_unreachable(self) -> None:
        adapter = TektonPipelineTracerAdapter()

        class GenericError(Exception):
            pass

        mock_api = MagicMock()
        mock_api.list_namespaced_custom_object.side_effect = GenericError("boom")

        with patch("kubernetes.client.CustomObjectsApi", return_value=mock_api):
            with pytest.raises(ClusterUnreachableError):
                adapter.list_task_runs_for_pipeline("ci", "pr-1")


class TestExtractStatusCancelledTask:
    def test_cancelled_task_run(self) -> None:
        assert (
            _extract_status(
                [
                    {
                        "type": "Succeeded",
                        "status": "False",
                        "reason": "TaskRunCancelled",
                    }
                ]
            )
            == "Cancelled"
        )


class TestToTaskRunRecordFailureReason:
    def test_failure_reason_extracted(self) -> None:
        raw = {
            "metadata": {"name": "task-x", "namespace": "ns"},
            "status": {
                "conditions": [
                    {
                        "type": "Succeeded",
                        "status": "False",
                        "message": "step failed",
                    }
                ],
            },
            "spec": {},
        }
        record = _to_task_run_record(raw, "pr-1")
        assert record["failure_reason"] == "step failed"
