from unittest.mock import MagicMock

from hexawyn.application.ports.driven.disruption_risk_port import (
    DisruptionRiskPort,
    RiskEventRaw,
)
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_command import (  # noqa: E501
    CheckDisruptionRisksCommand,
)


def _risks() -> list[RiskEventRaw]:
    return [
        RiskEventRaw(
            business_service_name="moteur",
            risk_type="memory_saturation",
            predicted_date="2026-09-20",
            days_from_now=3,
            detail="Saturation",
        )
    ]


class TestCheckDisruptionRisksService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_service_port import (  # noqa: E501
            CheckDisruptionRisksServicePort,
        )
        from hexawyn.application.service.check_disruption_risks_service import (
            CheckDisruptionRisksService,
        )

        service = CheckDisruptionRisksService(
            disruption_risk_port=MagicMock(spec=DisruptionRiskPort)
        )

        assert isinstance(service, CheckDisruptionRisksServicePort)

    def test_check_returns_result(self) -> None:
        from hexawyn.application.service.check_disruption_risks_service import (
            CheckDisruptionRisksService,
        )

        port = MagicMock(spec=DisruptionRiskPort)
        port.get_disruption_risks.return_value = _risks()
        service = CheckDisruptionRisksService(disruption_risk_port=port)

        response = service.check(CheckDisruptionRisksCommand())

        assert response.result.has_risks is True
