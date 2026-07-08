from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_response import (
    GenerateWeeklyReliabilityReportResponse,
)


class GenerateWeeklyReliabilityReportServicePort(ABC):
    @abstractmethod
    def generate_report(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse: ...
