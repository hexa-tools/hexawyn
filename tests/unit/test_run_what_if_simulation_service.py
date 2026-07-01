from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_command import (
    RunWhatIfSimulationCommand,
)
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_response import (
    RunWhatIfSimulationResponse,
)
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_service_port import (
    RunWhatIfSimulationServicePort,
)
from hexawyn.domain.models.simulation import RiskLevel


class TestRunWhatIfSimulationCommand:
    def test_is_frozen(self) -> None:
        cmd = RunWhatIfSimulationCommand(
            target_service="auth-service",
            namespace="production",
            proposed_replicas=1,
        )
        with pytest.raises(AttributeError):
            cmd.target_service = "other"  # type: ignore[misc]

    def test_required_fields(self) -> None:
        cmd = RunWhatIfSimulationCommand(
            target_service="auth-service",
            namespace="production",
            proposed_replicas=1,
        )
        assert cmd.target_service == "auth-service"
        assert cmd.namespace == "production"
        assert cmd.proposed_replicas == 1

    def test_optional_fields_default_to_none(self) -> None:
        cmd = RunWhatIfSimulationCommand(
            target_service="auth-service",
            namespace="staging",
            proposed_replicas=3,
        )
        assert cmd.current_replicas is None
        assert cmd.current_cpu_utilization is None

    def test_all_fields_populated(self) -> None:
        cmd = RunWhatIfSimulationCommand(
            target_service="payment-service",
            namespace="production",
            proposed_replicas=2,
            current_replicas=5,
            current_cpu_utilization=40.0,
        )
        assert cmd.current_replicas == 5
        assert cmd.current_cpu_utilization == 40.0


class TestRunWhatIfSimulationResponse:
    def test_default_values(self) -> None:
        resp = RunWhatIfSimulationResponse()
        assert resp.target_service == ""
        assert resp.risk == RiskLevel.LOW
        assert resp.affected_services == []

    def test_from_impact_report_maps_services_to_names(self) -> None:
        from hexawyn.domain.models.simulation import ImpactReport, ServiceImpact

        report = ImpactReport(
            target_service="auth-service",
            namespace="production",
            current_replicas=3,
            proposed_replicas=1,
            risk=RiskLevel.HIGH,
            affected_services=[
                ServiceImpact(
                    name="checkout-service",
                    calls_per_second=450,
                    estimated_latency_delta_percent=35,
                ),
                ServiceImpact(
                    name="payment-service", calls_per_second=200, estimated_latency_delta_percent=15
                ),
            ],
            estimated_latency_increase_percent=35.0,
            error_risk="potential 503s",
            pdb_violation=True,
            hpa_detected=False,
            circular_dependency=False,
            recommendation="Do not scale below 2",
        )
        resp = RunWhatIfSimulationResponse.from_impact_report(report)
        assert resp.target_service == "auth-service"
        assert resp.risk == RiskLevel.HIGH
        assert resp.affected_services == ["checkout-service", "payment-service"]
        assert resp.estimated_latency_increase_percent == 35.0
        assert resp.pdb_violation is True
        assert resp.recommendation == "Do not scale below 2"


class TestRunWhatIfSimulationServicePort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(RunWhatIfSimulationServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            RunWhatIfSimulationServicePort()  # type: ignore[abstract]


class TestRunWhatIfSimulationUseCase:
    def test_delegates_to_service_port(self) -> None:
        from hexawyn.application.use_case.run_what_if_simulation.run_what_if_simulation_use_case import (
            RunWhatIfSimulationUseCase,
        )

        fake_service = MagicMock(spec=RunWhatIfSimulationServicePort)
        expected = RunWhatIfSimulationResponse(
            target_service="auth-service",
            namespace="production",
            risk=RiskLevel.HIGH,
            affected_services=["checkout-service"],
        )
        fake_service.simulate.return_value = expected

        use_case = RunWhatIfSimulationUseCase(service=fake_service)
        cmd = RunWhatIfSimulationCommand(
            target_service="auth-service",
            namespace="production",
            proposed_replicas=1,
        )
        result = use_case.execute(cmd)

        assert result.risk == RiskLevel.HIGH
        assert "checkout-service" in result.affected_services
        fake_service.simulate.assert_called_once_with(cmd)


class TestRunWhatIfSimulationService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.service.run_what_if_simulation_service import (
            RunWhatIfSimulationService,
        )

        mock_port = MagicMock()
        service = RunWhatIfSimulationService(simulation_port=mock_port)
        assert isinstance(service, RunWhatIfSimulationServicePort)

    def test_simulate_high_risk_scenario(self) -> None:
        from hexawyn.application.ports.driven.what_if_simulation_port import (
            DependentServiceData,
        )
        from hexawyn.application.service.run_what_if_simulation_service import (
            RunWhatIfSimulationService,
        )

        mock_port = MagicMock()
        mock_port.get_current_replicas.return_value = 3
        mock_port.get_current_cpu_utilization.return_value = 62.0
        mock_port.get_service_topology.return_value = {
            "auth-service": [
                DependentServiceData(name="checkout-service", calls_per_second=450),
                DependentServiceData(name="payment-service", calls_per_second=200),
            ],
        }
        mock_port.get_pdb_info.return_value = {"min_available": 2}
        mock_port.get_hpa_info.return_value = None
        mock_port.get_dependency_graph.return_value = {}

        service = RunWhatIfSimulationService(simulation_port=mock_port)
        cmd = RunWhatIfSimulationCommand(
            target_service="auth-service",
            namespace="production",
            proposed_replicas=1,
        )
        result = service.simulate(cmd)

        assert result.risk == RiskLevel.HIGH
        assert result.pdb_violation is True
        assert result.hpa_detected is False
        assert result.affected_services == ["checkout-service", "payment-service"]
        assert result.target_service == "auth-service"
        assert result.proposed_replicas == 1
        assert result.current_replicas == 3

    def test_simulate_uses_provided_replicas_over_port(self) -> None:
        from hexawyn.application.service.run_what_if_simulation_service import (
            RunWhatIfSimulationService,
        )

        mock_port = MagicMock()
        mock_port.get_current_replicas.return_value = 5
        mock_port.get_current_cpu_utilization.return_value = 20.0
        mock_port.get_service_topology.return_value = {}
        mock_port.get_pdb_info.return_value = None
        mock_port.get_hpa_info.return_value = None
        mock_port.get_dependency_graph.return_value = {}

        service = RunWhatIfSimulationService(simulation_port=mock_port)
        cmd = RunWhatIfSimulationCommand(
            target_service="auth-service",
            namespace="staging",
            proposed_replicas=5,
            current_replicas=1,
            current_cpu_utilization=20.0,
        )
        result = service.simulate(cmd)

        assert result.risk == RiskLevel.LOW
        assert result.current_replicas == 1
        assert result.proposed_replicas == 5
