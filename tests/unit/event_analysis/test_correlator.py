"""Unit tests for EventCorrelator — groups related events by likely root cause."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.event import ClassifiedEvent, EventCategory, EventSeverity
from hexawyn.domain.services.event_analysis.correlator import CorrelatedIncident, EventCorrelator

_BASE_TIME = datetime(2024, 1, 1, 15, 0, 0, tzinfo=UTC)


def _event(
    reason: str,
    involved_object: str,
    offset_minutes: float = 0,
    severity: EventSeverity = EventSeverity.CRITICAL,
) -> ClassifiedEvent:
    return ClassifiedEvent(
        event_type="Warning",
        reason=reason,
        message=reason,
        severity=severity,
        category=EventCategory.RESOURCE,
        namespace="staging",
        involved_object=involved_object,
        count=1,
        first_timestamp=_BASE_TIME + timedelta(minutes=offset_minutes),
        last_timestamp=_BASE_TIME + timedelta(minutes=offset_minutes),
    )


class TestEventCorrelatorSamePodGrouping:
    def test_same_pod_events_within_minutes_correlated_as_one_incident(self) -> None:
        """TC3: 5 events all from same pod in 2 minutes → correlated as single incident."""
        events = [_event("OOMKilling", "pod/payment-api", offset_minutes=i * 0.5) for i in range(5)]
        correlator = EventCorrelator()

        incidents = correlator.correlate(events)

        assert len(incidents) == 1
        assert incidents[0].involved_objects == ["pod/payment-api"]
        assert len(incidents[0].events) == 5  # noqa: PLR2004


class TestEventCorrelatorGroupsByReasonNotPod:
    def test_same_reason_across_ten_pods_grouped_by_reason(self) -> None:
        """Edge case: same event type from 10 different pods → grouped by REASON not by pod."""
        events = [_event("OOMKilling", f"pod/worker-{i}") for i in range(10)]
        correlator = EventCorrelator()

        incidents = correlator.correlate(events)

        assert len(incidents) == 1
        assert incidents[0].reason == "OOMKilling"
        assert len(incidents[0].involved_objects) == 10  # noqa: PLR2004

    def test_different_reasons_produce_separate_incidents(self) -> None:
        events = [
            _event("OOMKilling", "pod/a"),
            _event("BackOff", "pod/b"),
        ]
        correlator = EventCorrelator()

        incidents = correlator.correlate(events)

        assert len(incidents) == 2  # noqa: PLR2004
        assert {i.reason for i in incidents} == {"OOMKilling", "BackOff"}


class TestEventCorrelatorRootCauseNarrative:
    def test_single_object_incident_narrative_mentions_object(self) -> None:
        events = [_event("OOMKilling", "pod/payment-api") for _ in range(3)]
        correlator = EventCorrelator()

        incidents = correlator.correlate(events)

        assert "pod/payment-api" in incidents[0].likely_root_cause

    def test_multi_object_incident_narrative_mentions_shared_root_cause(self) -> None:
        events = [_event("OOMKilling", f"pod/worker-{i}") for i in range(10)]
        correlator = EventCorrelator()

        incidents = correlator.correlate(events)

        assert "shared root cause" in incidents[0].likely_root_cause.lower()


class TestEventCorrelatorEmptyInput:
    def test_empty_events_returns_empty_incidents(self) -> None:
        correlator = EventCorrelator()

        incidents = correlator.correlate([])

        assert incidents == []
        assert isinstance(incidents, list)


class TestCorrelatedIncidentIsDataclass:
    def test_fields(self) -> None:
        incident = CorrelatedIncident(
            reason="OOMKilling",
            events=[_event("OOMKilling", "pod/a")],
            involved_objects=["pod/a"],
            likely_root_cause="Repeated 'OOMKilling' events on pod/a",
        )
        assert incident.reason == "OOMKilling"
        assert len(incident.events) == 1
