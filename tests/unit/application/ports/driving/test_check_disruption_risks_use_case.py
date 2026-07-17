from unittest.mock import MagicMock

from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_command import (  # noqa: E501
    CheckDisruptionRisksCommand,
)
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_response import (  # noqa: E501
    CheckDisruptionRisksResponse,
)
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_service_port import (  # noqa: E501
    CheckDisruptionRisksServicePort,
)
from hexawyn.domain.models.disruption_risk import DisruptionRiskReport


class TestCheckDisruptionRisksUseCase:
    def test_delegates(self) -> None:
        from hexawyn.application.use_case.check_disruption_risks.check_disruption_risks_use_case import (  # noqa: E501
            CheckDisruptionRisksUseCase,
        )

        service = MagicMock(spec=CheckDisruptionRisksServicePort)
        expected = CheckDisruptionRisksResponse(result=DisruptionRiskReport(period_label="Semaine"))
        service.check.return_value = expected
        use_case = CheckDisruptionRisksUseCase(service=service)

        response = use_case.execute(CheckDisruptionRisksCommand())

        assert response is expected
