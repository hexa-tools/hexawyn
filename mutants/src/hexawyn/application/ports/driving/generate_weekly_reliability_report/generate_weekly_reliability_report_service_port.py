from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.response import (
    GenerateWeeklyReliabilityReportResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GenerateWeeklyReliabilityReportServicePort(ABC):
    @abstractmethod
    def generate_report(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse: ...
