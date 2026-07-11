from unittest.mock import MagicMock

from hexawyn.application.ports.driven.engineer_workload_port import (
    EngineerWorkloadPort,
    MonthNightData,
)
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_command import (  # noqa: E501
    ReportNightInterventionsCommand,
)


def _months() -> list[MonthNightData]:
    return [
        MonthNightData(month="2026-04", night_intervention_count=42, total_nights=30),
        MonthNightData(month="2026-07", night_intervention_count=24, total_nights=30),
    ]


class TestReportNightInterventionsService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_service_port import (  # noqa: E501
            ReportNightInterventionsServicePort,
        )
        from hexawyn.application.service.report_night_interventions_service import (
            ReportNightInterventionsService,
        )

        service = ReportNightInterventionsService(
            workload_port=MagicMock(spec=EngineerWorkloadPort)
        )

        assert isinstance(service, ReportNightInterventionsServicePort)

    def test_report_returns_result(self) -> None:
        from hexawyn.application.service.report_night_interventions_service import (
            ReportNightInterventionsService,
        )

        port = MagicMock(spec=EngineerWorkloadPort)
        port.get_night_intervention_data.return_value = _months()
        service = ReportNightInterventionsService(workload_port=port)

        response = service.report(ReportNightInterventionsCommand())

        assert response.result.avg_interventions_per_night <= 2.0
