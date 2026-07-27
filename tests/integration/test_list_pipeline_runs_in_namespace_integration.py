"""Integration tests: ListPipelineRunsInNamespaceUseCase → service → adapter.

These tests use a real VanillaAdapter driven by a fake CRD client, exercising
the full stack without touching a real Kubernetes cluster.
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.service.list_pipeline_runs_in_namespace_service import (
    ListPipelineRunsInNamespaceService,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_use_case import (  # noqa: E501
    ListPipelineRunsInNamespaceUseCase,
)
from hexawyn.domain.errors import (
    InsufficientPermissionsError,
    TektonNotInstalledError,
)
from kubernetes.client.exceptions import ApiException


def _crd_item(  # noqa: PLR0913
    name: str,
    succeeded: str,
    reason: str,
    start_time: str | None = "2024-01-15T10:00:00Z",
    completion_time: str | None = None,
    pipeline_ref_name: str = "deploy-payment",
) -> dict[str, object]:
    conditions: list[dict[str, object]] = [
        {"type": "Succeeded", "status": succeeded, "reason": reason, "message": ""}
    ]
    status: dict[str, object] = {"conditions": conditions}
    if start_time:
        status["startTime"] = start_time
    if completion_time:
        status["completionTime"] = completion_time
    return {
        "metadata": {"name": name},
        "spec": {"pipelineRef": {"name": pipeline_ref_name}},
        "status": status,
    }


def _fake_crd_api(items: list[dict[str, object]]) -> MagicMock:
    crd_api = MagicMock()
    crd_api.list_namespaced_custom_object.return_value = {"items": items}
    return crd_api


def _build_use_case(crd_api: MagicMock) -> ListPipelineRunsInNamespaceUseCase:
    adapter = VanillaAdapter("test-cluster", crd_api=crd_api)
    service = ListPipelineRunsInNamespaceService(tekton_port=adapter)
    return ListPipelineRunsInNamespaceUseCase(service=service)


class TestListPipelineRunsInNamespaceIntegration:
    def test_vanilla_adapter_implements_tekton_port(self) -> None:
        from hexawyn.application.ports.driven.tekton_port import TektonPort

        adapter = VanillaAdapter("test-cluster", crd_api=MagicMock())
        assert isinstance(adapter, TektonPort)

    def test_tc1_five_runs_failed_first(self) -> None:
        items = [
            _crd_item("run-fail-1", "False", "Failed", "2024-01-15T09:55:00Z"),
            _crd_item("run-running", "Unknown", "Running", "2024-01-15T09:48:00Z"),
            _crd_item("run-ok-1", "True", "Succeeded", "2024-01-15T09:00:00Z"),
            _crd_item("run-fail-2", "False", "Failed", "2024-01-15T08:00:00Z"),
            _crd_item("run-ok-2", "True", "Succeeded", "2024-01-15T07:00:00Z"),
        ]
        use_case = _build_use_case(_fake_crd_api(items))

        result = use_case.execute(ListPipelineRunsInNamespaceCommand(namespace="tekton"))

        statuses = [r["status"] for r in result.runs]
        first_failed = statuses.index("Failed")
        first_running = statuses.index("Running")
        first_succeeded = statuses.index("Succeeded")
        assert first_failed < first_running < first_succeeded

    def test_tc1_all_five_runs_returned(self) -> None:
        items = [_crd_item(f"run-{i}", "True", "Succeeded") for i in range(5)]
        use_case = _build_use_case(_fake_crd_api(items))

        result = use_case.execute(ListPipelineRunsInNamespaceCommand(namespace="tekton"))

        assert len(result.runs) == 5  # noqa: PLR2004

    def test_tc2_empty_namespace_note_not_error(self) -> None:
        use_case = _build_use_case(_fake_crd_api([]))

        result = use_case.execute(ListPipelineRunsInNamespaceCommand(namespace="tekton"))

        assert result.runs == []
        assert result.note is not None
        assert "tekton" in result.note

    def test_tc3_stuck_detection(self) -> None:
        stuck_start = (datetime.now(UTC) - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        item = _crd_item("run-stuck", "Unknown", "Running", stuck_start)
        use_case = _build_use_case(_fake_crd_api([item]))

        result = use_case.execute(ListPipelineRunsInNamespaceCommand(namespace="tekton"))

        assert "run-stuck" in result.stuck_runs

    def test_tc4_rbac_403_raises_insufficient_permissions(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.side_effect = ApiException(
            status=403, reason="Forbidden"
        )
        use_case = _build_use_case(crd_api)

        with pytest.raises(InsufficientPermissionsError):
            use_case.execute(ListPipelineRunsInNamespaceCommand(namespace="tekton"))

    def test_tekton_not_installed_404(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.side_effect = ApiException(
            status=404, reason="Not Found"
        )
        use_case = _build_use_case(crd_api)

        with pytest.raises(TektonNotInstalledError):
            use_case.execute(ListPipelineRunsInNamespaceCommand(namespace="tekton"))

    def test_pipeline_ref_extracted_from_spec(self) -> None:
        item = _crd_item("run-ok", "True", "Succeeded", pipeline_ref_name="my-pipeline")
        use_case = _build_use_case(_fake_crd_api([item]))

        result = use_case.execute(ListPipelineRunsInNamespaceCommand(namespace="tekton"))

        assert result.runs[0]["pipeline_ref"] == "my-pipeline"

    def test_limit_applied_end_to_end(self) -> None:
        items = [_crd_item(f"run-{i}", "True", "Succeeded") for i in range(20)]
        use_case = _build_use_case(_fake_crd_api(items))

        result = use_case.execute(ListPipelineRunsInNamespaceCommand(namespace="tekton", limit=5))

        assert len(result.runs) == 5  # noqa: PLR2004
