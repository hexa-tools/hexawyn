from __future__ import annotations

from unittest.mock import MagicMock  # noqa: F401

from hexawyn.application.use_case.cluster.run_what_if_simulation.command import (
    RunWhatIfSimulationCommand,
)
from hexawyn.application.use_case.cluster.run_what_if_simulation.response import (
    RunWhatIfSimulationResponse,
)
from hexawyn.application.use_case.cluster.run_what_if_simulation.run_what_if_simulation_use_case import (  # noqa: E501
    RunWhatIfSimulationUseCase,  # noqa: F401
)


class TestRunWhatIfSimulationUseCase:
    def test_command_accepts_fields(self) -> None:
        cmd = RunWhatIfSimulationCommand(
            target_service="api-gateway",
            namespace="default",
            proposed_replicas=5,
        )

        assert cmd.target_service == "api-gateway"
        assert cmd.namespace == "default"
        assert cmd.proposed_replicas == 5  # noqa: PLR2004

    def test_response_from_impact_report(self) -> None:
        from hexawyn.domain.models.simulation import ImpactReport, RiskLevel, ServiceImpact

        impact = ImpactReport(
            target_service="api-gateway",
            namespace="default",
            current_replicas=3,
            proposed_replicas=5,
            risk=RiskLevel.LOW,
            affected_services=[
                ServiceImpact(name="auth-svc", calls_per_second=100.0),
            ],
            estimated_latency_increase_percent=5.0,
            error_risk="none",
            recommendation="safe to proceed",
        )

        response = RunWhatIfSimulationResponse.from_impact_report(impact)

        assert response.target_service == "api-gateway"
        assert response.risk == "0"
        assert response.risk_level == 0
        assert len(response.affected_services) == 1
        assert response.recommendation == "safe to proceed"

    def test_command_defaults(self) -> None:
        cmd = RunWhatIfSimulationCommand()

        assert cmd.target_service == ""
        assert cmd.namespace == ""
        assert cmd.proposed_replicas == 1
        assert cmd.current_replicas is None
