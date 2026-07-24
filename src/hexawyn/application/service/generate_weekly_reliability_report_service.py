from __future__ import annotations

from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    WeeklyReliabilityReportPort,
)
from hexawyn.application.use_case.generate_weekly_reliability_report.command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.generate_weekly_reliability_report.response import (
    GenerateWeeklyReliabilityReportResponse,
)
from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_service_port import (
    GenerateWeeklyReliabilityReportServicePort,
)
from hexawyn.domain.services.reliability_report.weekly_reliability_report_engine import (
    WeeklyReliabilityReportEngine,
)


class GenerateWeeklyReliabilityReportService(GenerateWeeklyReliabilityReportServicePort):
    def __init__(self, reliability_port: WeeklyReliabilityReportPort) -> None:
        self._port = reliability_port
        self._engine = WeeklyReliabilityReportEngine()

    def generate_report(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)
        incidents_raw = self._port.fetch_incidents(command.window_days)

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)
