from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_command import (
    RunWhatIfSimulationCommand,
)
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_response import (
    RunWhatIfSimulationResponse,
)
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_service_port import (
    RunWhatIfSimulationServicePort,
)
from hexawyn.application.use_case.run_what_if_simulation.run_what_if_simulation_use_case import (
    RunWhatIfSimulationUseCase,
)
from hexawyn.domain.models.simulation import RiskLevel


class TestRunWhatIfSimulationUseCase:
    def test_delegates_to_service_port(self) -> None:
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
