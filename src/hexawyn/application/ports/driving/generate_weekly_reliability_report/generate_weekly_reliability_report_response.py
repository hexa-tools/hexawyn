from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.weekly_reliability_report import WeeklyReliabilityReport


@dataclass
class GenerateWeeklyReliabilityReportResponse:
    result: WeeklyReliabilityReport
