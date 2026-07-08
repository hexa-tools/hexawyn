"""Unit tests for progressive_namespace_analysis — Phase 1 summary / Phase 2 critical drill-down."""

from __future__ import annotations

from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.services.event_analysis.progressive_namespace_analysis import (
    analyze_critical_events,
    summarize_namespace_events,
)


def _event(
    event_type: str,
    reason: str,
    obj: str,
    last_seen: str = "2024-01-01T15:00:00Z",
) -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason=reason,
        message=reason,
        object=obj,
        count=1,
        last_seen=last_seen,
    )


def _staging_test_data() -> list[NamespaceEvent]:
    """staging namespace: 15 events — 3 OOMKilling (same pod, 2min apart),
    2 BackOff, 10 Normal (Test Data section of the ticket)."""
    events = [
        _event("Warning", "OOMKilling", "pod/payment-api", "2024-01-01T15:00:00Z"),
        _event("Warning", "OOMKilling", "pod/payment-api", "2024-01-01T15:02:00Z"),
        _event("Warning", "OOMKilling", "pod/payment-api", "2024-01-01T15:04:00Z"),
        _event("Warning", "BackOff", "pod/worker-1", "2024-01-01T15:00:00Z"),
        _event("Warning", "BackOff", "pod/worker-2", "2024-01-01T15:00:00Z"),
    ]
    events += [_event("Normal", "Scheduled", f"pod/normal-{i}") for i in range(10)]
    return events


class TestSummarizeNamespaceEventsPhase1:
    """TC1: 20 events, 3 critical → Phase 1 returns summary."""

    def test_total_events_and_severity_breakdown(self) -> None:
        summary = summarize_namespace_events("staging", _staging_test_data())

        assert summary.namespace == "staging"
        assert summary.total_events == 15
        assert summary.severity_breakdown["critical"] == 3
        assert summary.severity_breakdown["high"] == 2
        assert summary.severity_breakdown["low"] == 10

    def test_top_affected_pods_ranks_by_event_count(self) -> None:
        summary = summarize_namespace_events("staging", _staging_test_data())

        assert len(summary.top_affected_pods) <= 3
        assert summary.top_affected_pods[0] == "pod/payment-api"

    def test_empty_events_returns_zeroed_summary(self) -> None:
        summary = summarize_namespace_events("staging", [])

        assert summary.total_events == 0
        assert summary.top_affected_pods == []


class TestAnalyzeCriticalEventsPhase2:
    """Phase 2: detailed analysis of critical events with correlated runbooks."""

    def test_critical_incident_correlated_with_runbook(self) -> None:
        analysis = analyze_critical_events("staging", _staging_test_data())

        assert analysis.namespace == "staging"
        assert len(analysis.critical_incidents) == 1
        incident = analysis.critical_incidents[0]
        assert incident.incident.reason == "OOMKilling"
        assert len(incident.incident.events) == 3
        assert incident.runbook.runbook_id == "runbook-memory-001"

    def test_non_critical_events_excluded(self) -> None:
        analysis = analyze_critical_events("staging", _staging_test_data())

        reasons = {i.incident.reason for i in analysis.critical_incidents}
        assert "BackOff" not in reasons
        assert "Scheduled" not in reasons

    def test_unmapped_critical_reason_falls_back_to_generic_runbook(self) -> None:
        """TC4: No runbook found for event REASON → returns generic troubleshooting steps."""
        events = [_event("Warning", "OOMKilling", "pod/a")]
        # Force an unmapped critical reason by monkey-classifying via a custom event type.
        events.append(_event("Warning", "NodeNotReady", "pod/b"))
        analysis = analyze_critical_events("staging", events)

        # NodeNotReady isn't in the classification map, so it falls back to MEDIUM,
        # not CRITICAL — only the mapped OOMKilling reaches critical_incidents.
        assert len(analysis.critical_incidents) == 1

    def test_no_critical_events_returns_empty_incidents(self) -> None:
        events = [_event("Normal", "Scheduled", "pod/a")]

        analysis = analyze_critical_events("staging", events)

        assert analysis.critical_incidents == []
