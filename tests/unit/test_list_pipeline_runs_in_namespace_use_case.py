from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.tekton_port import NamespacedPipelineRunInfo, TektonPort
from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_response import (
    ListPipelineRunsInNamespaceResponse,
)
from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_service_port import (
    ListPipelineRunsInNamespaceServicePort,
)
from hexawyn.application.service.list_pipeline_runs_in_namespace_service import (
    ListPipelineRunsInNamespaceService,
)
from hexawyn.application.use_case.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_use_case import (
    ListPipelineRunsInNamespaceUseCase,
)
from hexawyn.domain.errors import InsufficientPermissionsError, TektonNotInstalledError


def _run(
    name: str,
    status: str,
    start_time: str | None = "2024-01-15T10:00:00Z",
    duration_seconds: int | None = 270,
    pipeline_ref: str = "deploy-pipeline",
) -> NamespacedPipelineRunInfo:
    return {
        "name": name,
        "status": status,
        "start_time": start_time,
        "duration": f"{duration_seconds // 60}m{duration_seconds % 60}s"
        if duration_seconds
        else None,
        "duration_seconds": duration_seconds,
        "pipeline_ref": pipeline_ref,
    }


_FAILED_1 = _run("deploy-payment-v3", "Failed", "2024-01-15T09:55:00Z", 300, "deploy-payment")
_FAILED_2 = _run("deploy-auth-v1", "Failed", "2024-01-15T08:00:00Z", 240, "deploy-auth")
_RUNNING_1 = _run("deploy-checkout-v5", "Running", "2024-01-15T09:48:00Z", None, "deploy-checkout")
_SUCCEEDED_1 = _run("deploy-billing-v2", "Succeeded", "2024-01-15T09:00:00Z", 180, "deploy-billing")
_SUCCEEDED_2 = _run("deploy-catalog-v1", "Succeeded", "2024-01-15T08:30:00Z", 210, "deploy-catalog")


class TestListPipelineRunsInNamespaceCommand:
    def test_is_frozen(self) -> None:
        cmd = ListPipelineRunsInNamespaceCommand(namespace="tekton")
        with pytest.raises(AttributeError):
            cmd.namespace = "other"  # type: ignore[misc]

    def test_default_limit_is_one_hundred(self) -> None:
        cmd = ListPipelineRunsInNamespaceCommand(namespace="tekton")
        assert cmd.limit == 100

    def test_custom_limit(self) -> None:
        cmd = ListPipelineRunsInNamespaceCommand(namespace="tekton", limit=50)
        assert cmd.limit == 50


class TestListPipelineRunsInNamespaceResponse:
    def test_default_runs_is_empty(self) -> None:
        resp = ListPipelineRunsInNamespaceResponse()
        assert resp.runs == []

    def test_default_stuck_runs_is_empty(self) -> None:
        resp = ListPipelineRunsInNamespaceResponse()
        assert resp.stuck_runs == []

    def test_default_note_is_none(self) -> None:
        resp = ListPipelineRunsInNamespaceResponse()
        assert resp.note is None


class TestListPipelineRunsInNamespaceServicePort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(ListPipelineRunsInNamespaceServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            ListPipelineRunsInNamespaceServicePort()  # type: ignore[abstract]


class TestListPipelineRunsInNamespaceUseCase:
    def test_delegates_to_service_port(self) -> None:
        fake = MagicMock(spec=ListPipelineRunsInNamespaceServicePort)
        expected = ListPipelineRunsInNamespaceResponse(runs=[_FAILED_1])
        fake.list_pipeline_runs_in_namespace.return_value = expected

        result = ListPipelineRunsInNamespaceUseCase(service=fake).execute(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        assert result.runs == [_FAILED_1]

    def test_passes_command_to_service(self) -> None:
        fake = MagicMock(spec=ListPipelineRunsInNamespaceServicePort)
        fake.list_pipeline_runs_in_namespace.return_value = ListPipelineRunsInNamespaceResponse()

        cmd = ListPipelineRunsInNamespaceCommand(namespace="tekton")
        ListPipelineRunsInNamespaceUseCase(service=fake).execute(cmd)

        fake.list_pipeline_runs_in_namespace.assert_called_once_with(cmd)


class TestListPipelineRunsInNamespaceService:
    def test_implements_service_port(self) -> None:
        service = ListPipelineRunsInNamespaceService(tekton_port=MagicMock())
        assert isinstance(service, ListPipelineRunsInNamespaceServicePort)

    # TC1: 5 PipelineRuns — failed shown first
    def test_tc1_failed_runs_shown_first(self) -> None:
        runs = [_RUNNING_1, _SUCCEEDED_1, _FAILED_1, _SUCCEEDED_2, _FAILED_2]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = runs
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        statuses = [r["status"] for r in result.runs]
        assert statuses.index("Failed") < statuses.index("Running")
        assert statuses.index("Running") < statuses.index("Succeeded")

    def test_tc1_all_five_runs_returned(self) -> None:
        runs = [_RUNNING_1, _SUCCEEDED_1, _FAILED_1, _SUCCEEDED_2, _FAILED_2]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = runs
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        assert len(result.runs) == 5

    def test_tc1_within_same_status_most_recent_first(self) -> None:
        runs = [_FAILED_2, _FAILED_1]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = runs
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        failed = [r for r in result.runs if r["status"] == "Failed"]
        assert failed[0]["name"] == "deploy-payment-v3"
        assert failed[1]["name"] == "deploy-auth-v1"

    # TC2: empty namespace → informative note
    def test_tc2_empty_namespace_returns_note(self) -> None:
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = []
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        assert result.runs == []
        assert result.note is not None
        assert "tekton" in result.note

    def test_tc2_non_empty_namespace_has_no_note(self) -> None:
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = [_SUCCEEDED_1]
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        assert result.note is None

    # TC3: Running > 1h → stuck
    def test_tc3_running_over_one_hour_flagged_as_stuck(self) -> None:
        stuck_start = (datetime.now(UTC) - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
        stuck = _run("deploy-checkout-stuck", "Running", stuck_start, None)
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = [stuck]
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        assert "deploy-checkout-stuck" in result.stuck_runs

    def test_tc3_running_under_one_hour_not_stuck(self) -> None:
        recent_start = (datetime.now(UTC) - timedelta(minutes=12)).strftime("%Y-%m-%dT%H:%M:%SZ")
        fresh = _run("deploy-checkout-fresh", "Running", recent_start, None)
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = [fresh]
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        assert "deploy-checkout-fresh" not in result.stuck_runs

    def test_tc3_succeeded_run_never_stuck(self) -> None:
        old_start = (datetime.now(UTC) - timedelta(hours=5)).strftime("%Y-%m-%dT%H:%M:%SZ")
        old = _run("deploy-old", "Succeeded", old_start, 270)
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = [old]
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        assert result.stuck_runs == []

    # TC4: RBAC denied propagates
    def test_tc4_rbac_error_propagates(self) -> None:
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.side_effect = InsufficientPermissionsError(
            "Access denied to namespace 'tekton'"
        )
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        with pytest.raises(InsufficientPermissionsError):
            service.list_pipeline_runs_in_namespace(
                ListPipelineRunsInNamespaceCommand(namespace="tekton")
            )

    # Tekton not installed propagates
    def test_tekton_not_installed_propagates(self) -> None:
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.side_effect = TektonNotInstalledError()
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        with pytest.raises(TektonNotInstalledError):
            service.list_pipeline_runs_in_namespace(
                ListPipelineRunsInNamespaceCommand(namespace="tekton")
            )

    # Edge: pending run (no start time) shown with Pending status
    def test_pending_run_no_start_time_included(self) -> None:
        pending = _run("deploy-pending", "Pending", None, None)
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = [pending]
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton")
        )

        assert len(result.runs) == 1
        assert result.runs[0]["status"] == "Pending"

    # Edge: limit applied
    def test_limit_applied(self) -> None:
        runs = [_run(f"run-{i}", "Succeeded", f"2024-01-{15 - i:02d}T10:00:00Z") for i in range(20)]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs_in_namespace.return_value = runs
        service = ListPipelineRunsInNamespaceService(tekton_port=tekton)

        result = service.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="tekton", limit=5)
        )

        assert len(result.runs) == 5
