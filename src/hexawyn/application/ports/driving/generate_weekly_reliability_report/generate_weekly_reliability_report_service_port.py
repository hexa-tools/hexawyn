from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.response import (
    GenerateWeeklyReliabilityReportResponse,
)


class GenerateWeeklyReliabilityReportServicePort(ABC):
    @abstractmethod
    def generate_report(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse: ...
