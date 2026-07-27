from __future__ import annotations

from hexawyn.application.ports.driven.gitops_drift_audit_port import AuditEventRaw


def index_audit_events(events: list[AuditEventRaw]) -> dict[tuple[str, str, str, str], str]:
    return {
        (event["kind"], event["name"], event["namespace"], event["timestamp"]): event["actor"]
        for event in events
    }
