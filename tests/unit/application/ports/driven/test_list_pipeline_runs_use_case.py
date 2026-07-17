from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo, TektonPort
from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_response import (
    ListPipelineRunsResponse,
)
from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_service_port import (
    ListPipelineRunsServicePort,
)
from hexawyn.application.service.list_pipeline_runs_service import ListPipelineRunsService
from hexawyn.application.use_case.list_pipeline_runs.list_pipeline_runs_use_case import (
    ListPipelineRunsUseCase,
)
from hexawyn.domain.errors import ServiceNotFoundError


def _run(
    name: str,
    status: str,
    start_time: str | None = "2024-01-15T10:00:00Z",
    duration_seconds: int | None = 270,
    triggered_by: str | None = "github-push",
) -> PipelineRunInfo:
    minutes = duration_seconds // 60 if duration_seconds else 0
    seconds = duration_seconds % 60 if duration_seconds else 0
    duration = f"{minutes}m{seconds}s" if duration_seconds else None
    return {
        "name": name,
        "status": status,
        "start_time": start_time,
        "duration": duration,
        "duration_seconds": duration_seconds,
        "triggered_by": triggered_by,
    }


_SUCCEEDED = _run("payment-run-1", "Succeeded", "2024-01-15T10:00:00Z", 270)
_FAILED = _run("payment-run-2", "Failed", "2024-01-15T09:00:00Z", 300)
_CANCELLED = _run("payment-run-3", "Cancelled", "2024-01-15T08:00:00Z", None)


class TestListPipelineRunsCommand:
    def test_is_frozen(self) -> None:
        cmd = ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        with pytest.raises(AttributeError):
            cmd.service_name = "other"  # type: ignore[misc]

    def test_default_limit_is_ten(self) -> None:
        cmd = ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        assert cmd.limit == 10

    def test_custom_limit(self) -> None:
        cmd = ListPipelineRunsCommand(service_name="payment-service", namespace="ci", limit=5)
        assert cmd.limit == 5


class TestListPipelineRunsResponse:
    def test_default_runs_is_empty(self) -> None:
        resp = ListPipelineRunsResponse()
        assert resp.runs == []

    def test_default_outliers_is_empty(self) -> None:
        resp = ListPipelineRunsResponse()
        assert resp.outliers == []

    def test_default_note_is_none(self) -> None:
        resp = ListPipelineRunsResponse()
        assert resp.note is None


class TestListPipelineRunsServicePort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(ListPipelineRunsServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            ListPipelineRunsServicePort()  # type: ignore[abstract]


class TestListPipelineRunsUseCase:
    def test_delegates_to_service_port(self) -> None:
        fake_service = MagicMock(spec=ListPipelineRunsServicePort)
        expected = ListPipelineRunsResponse(runs=[_SUCCEEDED])
        fake_service.list_pipeline_runs.return_value = expected

        use_case = ListPipelineRunsUseCase(service=fake_service)
        result = use_case.execute(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.runs == [_SUCCEEDED]

    def test_passes_command_to_service(self) -> None:
        fake_service = MagicMock(spec=ListPipelineRunsServicePort)
        fake_service.list_pipeline_runs.return_value = ListPipelineRunsResponse()

        cmd = ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        ListPipelineRunsUseCase(service=fake_service).execute(cmd)

        fake_service.list_pipeline_runs.assert_called_once_with(cmd)


class TestListPipelineRunsService:
    def test_implements_service_port(self) -> None:
        service = ListPipelineRunsService(tekton_port=MagicMock())
        assert isinstance(service, ListPipelineRunsServicePort)

    # TC1: 10 runs, 8 successes → 80% success rate
    def test_tc1_success_rate_eighty_percent(self) -> None:
        runs = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{15 - i:02d}T10:00:00Z", 270) for i in range(8)
        ]
        runs += [
            _run("run-f1", "Failed", "2024-01-01T10:00:00Z", 300),
            _run("run-f2", "Failed", "2024-01-02T10:00:00Z", 300),
        ]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.stats.success_rate == 80.0
        assert result.stats.succeeded_runs == 8
        assert result.stats.failed_runs == 2
        assert result.stats.total_runs == 10

    # TC1: average duration calculated
    def test_tc1_average_duration_calculated(self) -> None:
        runs = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{15 - i:02d}T10:00:00Z", 270) for i in range(10)
        ]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.stats.average_duration_seconds == 270.0

    # TC2: 1 run took 45min vs average 5min → flagged as outlier
    def test_tc2_outlier_detected_at_twice_average(self) -> None:
        runs = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{15 - i:02d}T10:00:00Z", 300) for i in range(9)
        ]
        runs.append(_run("run-outlier", "Succeeded", "2024-01-01T10:00:00Z", 2700))
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert "run-outlier" in result.outliers

    def test_tc2_normal_run_not_flagged_as_outlier(self) -> None:
        runs = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{15 - i:02d}T10:00:00Z", 300) for i in range(10)
        ]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.outliers == []

    # TC3: fewer than 10 runs → note added
    def test_tc3_note_added_when_fewer_than_limit(self) -> None:
        runs = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{10 - i:02d}T10:00:00Z", 270) for i in range(3)
        ]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.note is not None
        assert "3" in result.note

    def test_tc3_no_note_when_exactly_limit_runs(self) -> None:
        runs = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{15 - i:02d}T10:00:00Z", 270) for i in range(10)
        ]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.note is None

    # TC4: ServiceNotFoundError propagates
    def test_tc4_service_not_found_propagates(self) -> None:
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.side_effect = ServiceNotFoundError(service_name="ghost-svc")
        service = ListPipelineRunsService(tekton_port=tekton)

        with pytest.raises(ServiceNotFoundError):
            service.list_pipeline_runs(
                ListPipelineRunsCommand(service_name="ghost-svc", namespace="ci")
            )

    # Edge: cancelled runs excluded from success rate denominator
    def test_cancelled_runs_excluded_from_success_rate(self) -> None:
        runs = [
            _run("run-ok", "Succeeded", "2024-01-15T10:00:00Z", 270),
            _run("run-cancelled", "Cancelled", "2024-01-14T10:00:00Z", None),
        ]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.stats.success_rate == 100.0
        assert result.stats.cancelled_runs == 1

    # Runs sorted by start_time descending
    def test_runs_sorted_most_recent_first(self) -> None:
        old = _run("run-old", "Succeeded", "2024-01-01T10:00:00Z", 270)
        new = _run("run-new", "Succeeded", "2024-01-15T10:00:00Z", 270)
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = [old, new]
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.runs[0]["name"] == "run-new"
        assert result.runs[1]["name"] == "run-old"

    # Fastest/slowest tracking
    def test_fastest_and_slowest_run_tracked(self) -> None:
        fast = _run("run-fast", "Succeeded", "2024-01-15T10:00:00Z", 60)
        slow = _run("run-slow", "Succeeded", "2024-01-14T10:00:00Z", 600)
        med = _run("run-med", "Succeeded", "2024-01-13T10:00:00Z", 300)
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = [fast, slow, med]
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.stats.fastest_run_name == "run-fast"
        assert result.stats.slowest_run_name == "run-slow"

    # Runs without duration excluded from fastest/slowest
    def test_runs_without_duration_excluded_from_stats(self) -> None:
        runs = [
            _run("run-ok", "Succeeded", "2024-01-15T10:00:00Z", 270),
            _run("run-cancelled", "Cancelled", "2024-01-14T10:00:00Z", None),
        ]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.stats.fastest_run_name == "run-ok"
        assert result.stats.slowest_run_name == "run-ok"

    # No duration data → average is None, no outliers
    def test_no_duration_data_yields_none_average(self) -> None:
        runs = [_run("run-cancelled", "Cancelled", "2024-01-15T10:00:00Z", None)]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert result.stats.average_duration_seconds is None
        assert result.outliers == []

    # Limit applied: only first N returned
    def test_service_applies_limit(self) -> None:
        runs = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{15 - i:02d}T10:00:00Z", 270) for i in range(15)
        ]
        tekton = MagicMock(spec=TektonPort)
        tekton.list_pipeline_runs.return_value = runs
        service = ListPipelineRunsService(tekton_port=tekton)

        result = service.list_pipeline_runs(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci", limit=5)
        )

        assert len(result.runs) == 5
