from unittest.mock import MagicMock

from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_command import (  # noqa: E501
    ReportNightInterventionsCommand,
)
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_response import (  # noqa: E501
    ReportNightInterventionsResponse,
)
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_service_port import (  # noqa: E501
    ReportNightInterventionsServicePort,
)
from hexawyn.domain.models.engineer_workload import NightInterventionReport


class TestReportNightInterventionsUseCase:
    def test_delegates(self) -> None:
        from hexawyn.application.use_case.report_night_interventions.report_night_interventions_use_case import (  # noqa: E501
            ReportNightInterventionsUseCase,
        )

        service = MagicMock(spec=ReportNightInterventionsServicePort)
        expected = ReportNightInterventionsResponse(
            result=NightInterventionReport(period_label="Ce mois")
        )
        service.report.return_value = expected
        use_case = ReportNightInterventionsUseCase(service=service)

        response = use_case.execute(ReportNightInterventionsCommand())

        assert response is expected
