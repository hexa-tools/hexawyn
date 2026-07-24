from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.use_case.generate_incident_triage_report.command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.use_case.generate_incident_triage_report.response import (
    GenerateIncidentTriageReportResponse,
)


class GenerateIncidentTriageReportUseCase:
    def __init__(self, port: PipelineRunLogsPort) -> None:
        self._port = port

    def execute(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        return GenerateIncidentTriageReportResponse()
