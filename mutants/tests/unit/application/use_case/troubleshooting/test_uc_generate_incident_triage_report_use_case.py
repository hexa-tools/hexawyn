from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.generate_incident_triage_report.command import (  # noqa: E501
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.use_case.troubleshooting.generate_incident_triage_report.generate_incident_triage_report_use_case import (  # noqa: E501
    GenerateIncidentTriageReportUseCase,
)
from hexawyn.application.use_case.troubleshooting.generate_incident_triage_report.response import (  # noqa: E501
    GenerateIncidentTriageReportResponse,
)


class TestGenerateIncidentTriageReportUseCase:
    def test_execute_returns_response(self) -> None:
        events = MagicMock()
        events.list_events.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]
        k8s.list_pods.return_value = []
        pod_logs = MagicMock()
        pod_logs.fetch_logs.return_value = []
        tekton = MagicMock()
        tekton.list_pipeline_runs_in_namespace.return_value = []
        plr = MagicMock()

        use_case = GenerateIncidentTriageReportUseCase(
            events_port=events,
            k8s_port=k8s,
            pod_logs_port=pod_logs,
            tekton_port=tekton,
            pipeline_run_logs_port=plr,
        )
        result = use_case.execute(GenerateIncidentTriageReportCommand(namespace="default"))

        assert isinstance(result, GenerateIncidentTriageReportResponse)
