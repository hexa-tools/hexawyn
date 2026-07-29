from __future__ import annotations

from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    WeeklyReliabilityReportPort,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.response import (
    GenerateWeeklyReliabilityReportResponse,
)
from hexawyn.domain.services.reliability_report.weekly_reliability_report_engine import (
    WeeklyReliabilityReportEngine,
)


class GenerateWeeklyReliabilityReportUseCase:
    def __init__(self, reliability_port: WeeklyReliabilityReportPort) -> None:
        self._port = reliability_port
        self._engine = WeeklyReliabilityReportEngine()

    def generate_report(
        self, command: GenerateWeeklyReliabilityReportCommand
    ) -> GenerateWeeklyReliabilityReportResponse:
        services_raw = self._port.fetch_service_reliability(command.window_days)  # type: ignore
        incidents_raw = self._port.fetch_incidents(command.window_days)  # type: ignore

        services: list[dict[str, object]] = [dict(s) for s in services_raw]
        incidents: list[dict[str, object]] = [dict(i) for i in incidents_raw]

        result = self._engine.compute(services, incidents)
        return GenerateWeeklyReliabilityReportResponse(result=result)  # type: ignore
