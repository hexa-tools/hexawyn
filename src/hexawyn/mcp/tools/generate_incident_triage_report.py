"""MCP tool: generate_incident_triage_report — automated incident triage/RCA
report composing namespace events, pod logs, pod status, and pipeline-failure
RCA into a shareable Confluence/Notion-ready document."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.use_case.generate_incident_triage_report.generate_incident_triage_report_use_case import (
    GenerateIncidentTriageReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def generate_incident_triage_report(
    namespace: str,
    time_window_minutes: int = 120,
    related_namespaces: list[str] | None = None,
) -> dict[str, object]:
    from hexawyn.application.service.generate_incident_triage_report_service import (
        GenerateIncidentTriageReportService,
    )
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        service = GenerateIncidentTriageReportService(
            events_port=build_namespace_events_adapter(),
            k8s_port=build_k8s_adapter(),
            pod_logs_port=build_pod_logs_adapter(),
            tekton_port=build_tekton_adapter(),
            pipeline_run_logs_port=build_pipeline_run_logs_adapter(),
        )
        r = GenerateIncidentTriageReportUseCase(service=service).execute(
            GenerateIncidentTriageReportCommand(
                namespace=namespace,
                time_window_minutes=time_window_minutes,
                related_namespaces=related_namespaces or [],
            )
        )
        return {
            "namespace": r.namespace,
            "time_window_minutes": r.time_window_minutes,
            "timeline": r.timeline,
            "root_causes": r.root_causes,
            "impact": r.impact,
            "remediation_steps": r.remediation_steps,
            "resolved": r.resolved,
            "resolution_time": r.resolution_time,
            "mttr_minutes": r.mttr_minutes,
            "ntp_drift_detected": r.ntp_drift_detected,
            "ntp_drift_note": r.ntp_drift_note,
            "cross_namespace_correlation": r.cross_namespace_correlation,
            "insufficient_data": r.insufficient_data,
            "data_checked": r.data_checked,
            "formatted_report": r.formatted_report,
            "error": r.error,
        }
    except Exception as exc:
        return {"namespace": namespace, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(generate_incident_triage_report)
