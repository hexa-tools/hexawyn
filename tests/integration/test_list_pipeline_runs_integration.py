"""Integration tests for list_pipeline_runs — service + use_case full stack."""

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo, TektonPort
from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.service.list_pipeline_runs_service import ListPipelineRunsService
from hexawyn.application.use_case.list_pipeline_runs.list_pipeline_runs_use_case import (
    ListPipelineRunsUseCase,
)
from hexawyn.domain.errors import ServiceNotFoundError


def _run(
    name: str,
    status: str,
    start_time: str | None,
    duration_seconds: int | None,
    triggered_by: str | None = "github-push",
) -> PipelineRunInfo:
    return {
        "name": name,
        "status": status,
        "start_time": start_time,
        "duration": f"{duration_seconds // 60}m{duration_seconds % 60}s"
        if duration_seconds
        else None,
        "duration_seconds": duration_seconds,
        "triggered_by": triggered_by,
    }


class TestListPipelineRunsIntegration:
    @pytest.mark.integration
    def test_tc1_ten_runs_eighty_percent_success_rate(self) -> None:
        """TC1: 10 runs, 8 successes → 80% success rate, average duration calculated."""
        runs = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{15 - i:02d}T10:00:00Z", 270) for i in range(8)
        ]
        runs += [
            _run("run-f1", "Failed", "2024-01-01T10:00:00Z", 300),
            _run("run-f2", "Failed", "2024-01-02T10:00:00Z", 300),
        ]

        mock_port = MagicMock(spec=TektonPort)
        mock_port.list_pipeline_runs.return_value = runs

        service = ListPipelineRunsService(tekton_port=mock_port)
        use_case = ListPipelineRunsUseCase(service=service)
        response = use_case.execute(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert response.stats.success_rate == 80.0
        assert response.stats.total_runs == 10
        assert response.stats.succeeded_runs == 8
        assert response.stats.failed_runs == 2
        assert response.stats.average_duration_seconds is not None

    @pytest.mark.integration
    def test_tc2_outlier_run_flagged(self) -> None:
        """TC2: 1 run took 45min vs average 5min → flagged as outlier."""
        normal = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{15 - i:02d}T10:00:00Z", 300) for i in range(9)
        ]
        outlier = _run("run-outlier", "Succeeded", "2024-01-01T10:00:00Z", 2700)

        mock_port = MagicMock(spec=TektonPort)
        mock_port.list_pipeline_runs.return_value = normal + [outlier]

        service = ListPipelineRunsService(tekton_port=mock_port)
        use_case = ListPipelineRunsUseCase(service=service)
        response = use_case.execute(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert "run-outlier" in response.outliers
        assert len([r for r in response.runs if r["name"] not in response.outliers]) == 9

    @pytest.mark.integration
    def test_tc3_fewer_than_ten_runs_note_added(self) -> None:
        """TC3: Fewer than 10 runs → returns all with 'only N runs available' note."""
        runs = [
            _run(f"run-{i}", "Succeeded", f"2024-01-{10 - i:02d}T10:00:00Z", 270) for i in range(3)
        ]

        mock_port = MagicMock(spec=TektonPort)
        mock_port.list_pipeline_runs.return_value = runs

        service = ListPipelineRunsService(tekton_port=mock_port)
        use_case = ListPipelineRunsUseCase(service=service)
        response = use_case.execute(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert len(response.runs) == 3
        assert response.note is not None
        assert "3" in response.note

    @pytest.mark.integration
    def test_tc4_service_not_found_propagates(self) -> None:
        """TC4: Service not found → ServiceNotFoundError propagates through use case."""
        mock_port = MagicMock(spec=TektonPort)
        mock_port.list_pipeline_runs.side_effect = ServiceNotFoundError(service_name="ghost-svc")

        service = ListPipelineRunsService(tekton_port=mock_port)
        use_case = ListPipelineRunsUseCase(service=service)

        with pytest.raises(ServiceNotFoundError) as exc_info:
            use_case.execute(ListPipelineRunsCommand(service_name="ghost-svc", namespace="ci"))

        assert exc_info.value.service_name == "ghost-svc"

    @pytest.mark.integration
    def test_cancelled_runs_excluded_from_rate_full_stack(self) -> None:
        """Edge: cancelled runs not counted in success/failure rate."""
        runs = [
            _run("run-ok-1", "Succeeded", "2024-01-15T10:00:00Z", 270),
            _run("run-ok-2", "Succeeded", "2024-01-14T10:00:00Z", 270),
            _run("run-cancelled", "Cancelled", "2024-01-13T10:00:00Z", None),
        ]

        mock_port = MagicMock(spec=TektonPort)
        mock_port.list_pipeline_runs.return_value = runs

        service = ListPipelineRunsService(tekton_port=mock_port)
        use_case = ListPipelineRunsUseCase(service=service)
        response = use_case.execute(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        assert response.stats.success_rate == 100.0
        assert response.stats.cancelled_runs == 1

    @pytest.mark.integration
    def test_multiple_triggered_by_actors_preserved(self) -> None:
        """Edge: different users triggering → each run shows its actor."""
        runs = [
            _run("run-alice", "Succeeded", "2024-01-15T10:00:00Z", 270, triggered_by="alice"),
            _run("run-bob", "Succeeded", "2024-01-14T10:00:00Z", 270, triggered_by="bob"),
        ]

        mock_port = MagicMock(spec=TektonPort)
        mock_port.list_pipeline_runs.return_value = runs

        service = ListPipelineRunsService(tekton_port=mock_port)
        use_case = ListPipelineRunsUseCase(service=service)
        response = use_case.execute(
            ListPipelineRunsCommand(service_name="payment-service", namespace="ci")
        )

        actors = [r["triggered_by"] for r in response.runs]
        assert "alice" in actors
        assert "bob" in actors

    @pytest.mark.integration
    def test_vanilla_adapter_implements_tekton_port(self) -> None:
        adapter = VanillaAdapter("test-cluster")
        assert isinstance(adapter, TektonPort)
        assert hasattr(adapter, "list_pipeline_runs")
