from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    WeeklyReliabilityReportPort,
)
from hexawyn.application.use_case.generate_weekly_reliability_report.command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.generate_weekly_reliability_report.response import (
    GenerateWeeklyReliabilityReportResponse,
)


class GenerateWeeklyReliabilityReportUseCase:
    def __init__(self, reliability_port: WeeklyReliabilityReportPort) -> None:
        self._port = reliability_port

    def execute(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        return GenerateWeeklyReliabilityReportResponse()
