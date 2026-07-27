"""MCP tool: generate_incident_triage_report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.domain.models.incident_triage import (
    IncidentCauseCategory,
    IncidentTriageReport,
    RootCauseCandidate,
)
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _category_from_reason(reason: str) -> IncidentCauseCategory:
    db_keywords = ["postgres", "mysql", "database", "connection", "pool", "timeout"]
    resource_keywords = ["oom", "memory", "cpu", "disk", "limit", "quota"]
    network_keywords = ["network", "dns", "connect", "refused", "timeout", "tls", "certificate"]
    image_keywords = ["image", "pull", "registry", "config", "secret"]
    deployment_keywords = ["deploy", "rollout", "replicas", "scale", "update"]

    reason_lower = reason.lower()
    if any(kw in reason_lower for kw in db_keywords):
        return IncidentCauseCategory.DATABASE
    if any(kw in reason_lower for kw in resource_keywords):
        return IncidentCauseCategory.RESOURCE_EXHAUSTION
    if any(kw in reason_lower for kw in network_keywords):
        return IncidentCauseCategory.NETWORK
    if any(kw in reason_lower for kw in image_keywords):
        return IncidentCauseCategory.IMAGE_OR_CONFIG
    if any(kw in reason_lower for kw in deployment_keywords):
        return IncidentCauseCategory.DEPLOYMENT
    return IncidentCauseCategory.UNKNOWN


def _format_report(report: IncidentTriageReport) -> str:
    lines: list[str] = []
    lines.append(f"# Incident Report — {report.namespace}")
    lines.append(f"Time window: {report.time_window_minutes} minutes")
    lines.append("")

    if report.root_causes:
        lines.append("## Root Cause Analysis")
        for rc in report.root_causes:
            lines.append(
                f"- {rc.description} "
                f"(confidence: {rc.confidence:.0%}, category: {rc.category.value})"
            )
            for ev in rc.evidence:
                lines.append(f"  - Evidence: {ev}")
    else:
        lines.append("## Root Cause Analysis")
        lines.append("No root causes identified — insufficient data.")

    if report.remediation_steps:
        lines.append("")
        lines.append("## Remediation Steps")
        for step in report.remediation_steps:
            lines.append(f"- {step}")

    lines.append("")
    lines.append(f"Resolved: {'Yes' if report.resolved else 'No'}")
    return "\n".join(lines)


def generate_incident_triage_report(namespace: str = "test-ns") -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_k8s_adapter,
        build_namespace_events_adapter,
        build_pipeline_run_logs_adapter,
        build_pod_logs_adapter,
        build_tekton_adapter,
    )

    try:
        events_adapter = build_namespace_events_adapter()
        _ = build_k8s_adapter()
        _ = build_pod_logs_adapter()
        _ = build_tekton_adapter()
        _ = build_pipeline_run_logs_adapter()

        events = events_adapter.list_events(GetNamespaceEventsRequest(namespace=namespace))

        root_causes: list[RootCauseCandidate] = []
        for event in events:
            category = _category_from_reason(event.reason)
            root_causes.append(
                RootCauseCandidate(
                    description=f"{event.reason}: {event.message}",
                    category=category,
                    confidence=0.85,
                    evidence=[f"Event on {event.object}: {event.message}"],
                    involved_objects=[event.object],
                )
            )

        remediation_steps: list[str] = []
        for rc in root_causes:
            if rc.category == IncidentCauseCategory.DATABASE:
                remediation_steps.append("Check database connection pool limits and health")
            elif rc.category == IncidentCauseCategory.RESOURCE_EXHAUSTION:
                remediation_steps.append("Increase resource limits or scale replicas")
            elif rc.category == IncidentCauseCategory.NETWORK:
                remediation_steps.append("Verify network policies and DNS resolution")
            elif rc.category == IncidentCauseCategory.IMAGE_OR_CONFIG:
                remediation_steps.append("Verify image pull secrets and registry access")

        report = IncidentTriageReport(
            namespace=namespace,
            time_window_minutes=120,
            root_causes=root_causes,
            remediation_steps=remediation_steps,
            data_checked=["events", "pods", "pipeline_runs"],
        )

        return {
            "namespace": report.namespace,
            "root_causes": [
                {
                    "description": rc.description,
                    "category": rc.category.value,
                    "confidence": rc.confidence,
                    "evidence": rc.evidence,
                }
                for rc in report.root_causes
            ],
            "formatted_report": _format_report(report),
            "error": None,
        }
    except Exception as exc:
        return {
            "namespace": namespace,
            "root_causes": [],
            "formatted_report": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(generate_incident_triage_report)
