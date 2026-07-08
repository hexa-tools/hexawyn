from __future__ import annotations

from hexawyn.domain.models.incident_triage import IncidentTriageReport


def format_report_as_markdown(report: IncidentTriageReport) -> str:
    """Renders an IncidentTriageReport as plain Markdown — pasteable as-is
    into Confluence (markdown macro) or Notion (native markdown import)."""
    sections = [
        f"# Incident Report — {report.namespace}",
        f"_Window: last {report.time_window_minutes} minutes_",
    ]

    if report.insufficient_data:
        sections.append(
            "\n**Insufficient data** — no events, logs, pod restarts, or pipeline "
            "runs were found for this window.\n\nChecked:\n"
            + "\n".join(f"- {item}" for item in report.data_checked)
        )
        return "\n\n".join(sections)

    sections.append(_timeline_section(report))
    sections.append(_impact_section(report))
    sections.append(_root_cause_section(report))
    sections.append(_remediation_section(report))
    return "\n\n".join(sections)


def _timeline_section(report: IncidentTriageReport) -> str:
    lines = [
        "## Timeline",
        "| Timestamp | Source | Object | Reason | Message |",
        "|---|---|---|---|---|",
    ]
    for entry in report.timeline:
        lines.append(
            f"| {entry.timestamp} | {entry.source} | {entry.object} | {entry.reason} | {entry.message} |"
        )
    return "\n".join(lines)


def _impact_section(report: IncidentTriageReport) -> str:
    lines = ["## Impact Assessment"]
    lines.append(f"- **Affected services:** {', '.join(report.impact.affected_services) or 'none'}")
    lines.append(f"- **Estimated user impact:** {report.impact.estimated_user_impact or 'unknown'}")
    if report.resolved:
        lines.append(f"- **Resolved:** {report.resolution_time}")
        lines.append(f"- **MTTR:** {report.mttr_minutes} minutes")
    else:
        lines.append(f"- **Status:** ongoing ({report.impact.duration_minutes} minutes so far)")
    if report.ntp_drift_detected:
        lines.append(f"- **Clock drift warning:** {report.ntp_drift_note}")
    if report.cross_namespace_correlation:
        lines.append("- **Cross-namespace correlation:**")
        lines.extend(f"  - {entry}" for entry in report.cross_namespace_correlation)
    return "\n".join(lines)


def _root_cause_section(report: IncidentTriageReport) -> str:
    lines = ["## Root Cause"]
    if not report.root_causes:
        lines.append("No root cause identified.")
        return "\n".join(lines)
    for index, candidate in enumerate(report.root_causes, start=1):
        lines.append(
            f"{index}. **{candidate.description}** "
            f"(category: {candidate.category.value}, confidence: {candidate.confidence:.2f})"
        )
        lines.extend(f"   - {evidence}" for evidence in candidate.evidence)
    return "\n".join(lines)


def _remediation_section(report: IncidentTriageReport) -> str:
    lines = ["## Remediation Steps"]
    if not report.remediation_steps:
        lines.append("No remediation steps available.")
        return "\n".join(lines)
    lines.extend(f"- {step}" for step in report.remediation_steps)
    return "\n".join(lines)
