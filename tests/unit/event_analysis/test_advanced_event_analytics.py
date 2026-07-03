"""Unit tests for generate_advanced_event_analytics — 6h advanced analytics report."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.services.event_analysis.advanced_event_analytics import (
    generate_advanced_event_analytics,
)

_STORM_TIME = datetime(2024, 1, 1, 14, 32, 0, tzinfo=UTC)


def _event(
    reason: str,
    obj: str,
    when: datetime,
    event_type: str = "Warning",
) -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason=reason,
        message=reason,
        object=obj,
        count=1,
        last_seen=when.isoformat().replace("+00:00", "Z"),
    )


def _storm_events(
    count: int, span_seconds: float, start: datetime = _STORM_TIME
) -> list[NamespaceEvent]:
    step = span_seconds / max(count - 1, 1)
    return [
        _event("BackOff", f"pod/worker-{i}", start + timedelta(seconds=i * step))
        for i in range(count)
    ]


class TestAdvancedEventAnalyticsStorm:
    """TC1: Event storm detected at 14:32 (80 events in 90s) → flagged with timeline spike."""

    def test_storm_flagged_with_timeline_spike(self) -> None:
        events = _storm_events(80, span_seconds=90)

        report = generate_advanced_event_analytics("data-pipeline", events)

        assert len(report.storms) == 1
        assert report.storms[0].event_count == 80
        spike_minutes = [b for b in report.timeline if b.is_spike]
        assert len(spike_minutes) > 0
        assert spike_minutes[0].minute == "2024-01-01T14:32"


class TestAdvancedEventAnalyticsCorrelation:
    """TC2: 5 pods all showing BackOff at same time → correlated as single downstream failure."""

    def test_same_reason_across_pods_correlated_as_one_incident(self) -> None:
        events = [_event("BackOff", f"pod/worker-{i}", _STORM_TIME) for i in range(5)]

        report = generate_advanced_event_analytics("data-pipeline", events)

        assert len(report.correlated_incidents) == 1
        incident = report.correlated_incidents[0]
        assert incident.reason == "BackOff"
        assert len(incident.involved_objects) == 5
        assert incident.event_count == 5

    def test_normal_events_excluded_from_correlation(self) -> None:
        events = [_event("Scheduled", "pod/a", _STORM_TIME, event_type="Normal")]

        report = generate_advanced_event_analytics("data-pipeline", events)

        assert report.correlated_incidents == []


class TestAdvancedEventAnalyticsCleanReport:
    """TC3: Normal 6h period with low event volume → clean report, no storms detected."""

    def test_low_volume_period_has_no_storms(self) -> None:
        events = [
            _event("BackOff", "pod/a", _STORM_TIME + timedelta(minutes=i * 30)) for i in range(10)
        ]

        report = generate_advanced_event_analytics("data-pipeline", events)

        assert report.storms == []
        assert report.sampling_applied is False

    def test_empty_events_returns_zeroed_report(self) -> None:
        report = generate_advanced_event_analytics("data-pipeline", [])

        assert report.total_events == 0
        assert report.timeline == []
        assert report.storms == []
        assert report.top_reasons == []
        assert report.correlated_incidents == []


class TestAdvancedEventAnalyticsSampling:
    """TC4: Namespace with 10000+ events in 6h → sampling applied, storm detection still accurate."""

    def test_large_volume_applies_sampling_but_keeps_accurate_counts(self) -> None:
        # Baseline lives an hour after the storm so no baseline timestamp can ever
        # fall inside the storm's own 120s detection window.
        storm = _storm_events(80, span_seconds=90, start=_STORM_TIME)
        baseline = [
            _event(
                "BackOff",
                f"pod/worker-{i % 50}",
                _STORM_TIME + timedelta(hours=1, minutes=i),
            )
            for i in range(6000)
        ]
        events = baseline + storm

        report = generate_advanced_event_analytics("data-pipeline", events)

        assert report.sampling_applied is True
        assert report.total_events == len(events)
        assert len(report.storms) == 1
        assert report.storms[0].event_count == 80

        incident = report.correlated_incidents[0]
        assert incident.event_count == len(baseline) + 80
        assert len(incident.sample_events) <= 50


class TestAdvancedEventAnalyticsTopReasons:
    def test_top_reasons_ranked_by_count(self) -> None:
        events = [_event("BackOff", f"pod/{i}", _STORM_TIME) for i in range(340)]
        events += [_event("OOMKilling", f"pod/{i}", _STORM_TIME) for i in range(12)]

        report = generate_advanced_event_analytics("data-pipeline", events)

        assert report.top_reasons[0].reason == "BackOff"
        assert report.top_reasons[0].count == 340
        assert report.top_reasons[1].reason == "OOMKilling"
        assert report.top_reasons[1].count == 12

    def test_normal_events_excluded_from_top_reasons(self) -> None:
        events = [
            _event("Scheduled", "pod/a", _STORM_TIME, event_type="Normal") for _ in range(100)
        ]
        events.append(_event("BackOff", "pod/b", _STORM_TIME))

        report = generate_advanced_event_analytics("data-pipeline", events)

        reasons = {r.reason for r in report.top_reasons}
        assert "Scheduled" not in reasons


class TestAdvancedEventAnalyticsOutOfOrderTimestamps:
    def test_out_of_order_timestamps_sorted_before_analysis(self) -> None:
        """Edge case: event timestamps out of order → sorted before analysis."""
        events = list(reversed(_storm_events(80, span_seconds=90)))

        report = generate_advanced_event_analytics("data-pipeline", events)

        assert len(report.storms) == 1
        assert report.storms[0].event_count == 80
