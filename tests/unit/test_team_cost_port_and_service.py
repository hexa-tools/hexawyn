"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.team_cost_port import (
    NamespaceResourceData,
    TeamCostPort,
)
from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_command import (
    ComputeTeamCostCommand,
)
from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_response import (
    ComputeTeamCostResponse,
)
from hexawyn.application.ports.driving.compute_team_cost.compute_team_cost_service_port import (
    ComputeTeamCostServicePort,
)
from hexawyn.application.service.compute_team_cost_service import (
    ComputeTeamCostService,
)
from hexawyn.application.use_case.compute_team_cost.compute_team_cost_use_case import (
    ComputeTeamCostUseCase,
)
from hexawyn.domain.models.team_cost import TeamCostReport


class TestTeamCostPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(TeamCostPort)

    def test_concrete_impl_must_implement(self) -> None:
        class Bad(TeamCostPort):
            pass

        with pytest.raises(TypeError):
            Bad()  # type: ignore[abstract]


class TestComputeTeamCostCommand:
    def test_defaults(self) -> None:
        cmd = ComputeTeamCostCommand()
        assert cmd.cpu_price_per_core_hour == 0.03

    def test_custom_pricing(self) -> None:
        cmd = ComputeTeamCostCommand(
            cpu_price_per_core_hour=0.04,
            memory_price_per_gb_hour=0.02,
            storage_price_per_gb_month=0.15,
        )
        assert cmd.storage_price_per_gb_month == 0.15

    def test_is_frozen(self) -> None:
        cmd = ComputeTeamCostCommand()
        with pytest.raises(Exception):
            cmd.cpu_price_per_core_hour = 0.05  # type: ignore[misc]


class TestComputeTeamCostResponse:
    def test_holds_result(self) -> None:
        inner = TeamCostReport(month="2026-07")
        resp = ComputeTeamCostResponse(result=inner)
        assert resp.result is inner


class TestComputeTeamCostService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=TeamCostPort)
        port.fetch_namespace_resources.return_value = []
        return port

    def test_calls_port_for_current_and_previous_month(self) -> None:
        port = self._mock_port()
        service = ComputeTeamCostService(cost_port=port)

        service.compute(ComputeTeamCostCommand())

        assert port.fetch_namespace_resources.call_count == 2

    def test_returns_response_with_result(self) -> None:
        port = MagicMock(spec=TeamCostPort)
        port.fetch_namespace_resources.return_value = [
            NamespaceResourceData(
                namespace="payments-prod",
                team_label="payments",
                cpu_cores=20.0,
                memory_gb=80.0,
                storage_gb=100.0,
                month="2026-07",
                days_active=31,
            ),
        ]
        service = ComputeTeamCostService(cost_port=port)

        response = service.compute(ComputeTeamCostCommand())

        assert isinstance(response, ComputeTeamCostResponse)
        assert isinstance(response.result, TeamCostReport)
        assert len(response.result.teams) == 1
        assert response.result.teams[0].team_name == "payments"


class TestComputeTeamCostUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=ComputeTeamCostServicePort)
        inner = TeamCostReport(month="07-2026", total_cost=1000.0)
        service.compute.return_value = ComputeTeamCostResponse(result=inner)
        use_case = ComputeTeamCostUseCase(service=service)

        result = use_case.execute(ComputeTeamCostCommand())

        service.compute.assert_called_once()
        assert result.result is inner
