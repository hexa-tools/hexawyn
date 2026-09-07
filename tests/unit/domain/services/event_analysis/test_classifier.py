"""Unit tests for the Progressive Event Analyzer."""

from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.event import ClassifiedEvent, EventCategory, EventSeverity
from hexawyn.domain.services.event_analysis.classifier import (
    CorrelationAnalysis,
    DetailedAnalysis,
    EventOverview,
    ProgressiveEventAnalyzer,
)


def _make_event(  # noqa: PLR0913
    event_type: str = "Warning",
    reason: str = "OOMKilled",
    message: str = "Memory cgroup out of memory",
    severity: EventSeverity = EventSeverity.CRITICAL,
    category: EventCategory = EventCategory.RESOURCE,
    namespace: str = "production",
    involved_object: str = "Pod/api-1",
    count: int = 1,
    timestamp: datetime | None = None,
) -> ClassifiedEvent:
    return ClassifiedEvent(
        event_type=event_type,
        reason=reason,
        message=message,
        severity=severity,
        category=category,
        namespace=namespace,
        involved_object=involved_object,
        count=count,
        first_timestamp=timestamp,
        last_timestamp=timestamp,
    )


class TestEventOverview:
    def setup_method(self) -> None:
        self.events = [
            _make_event(severity=EventSeverity.CRITICAL, reason="OOMKilled"),
            _make_event(severity=EventSeverity.CRITICAL, reason="CrashLoopBackOff"),
            _make_event(severity=EventSeverity.HIGH, reason="FailedMount"),
            _make_event(severity=EventSeverity.MEDIUM, reason="BackOff"),
            _make_event(severity=EventSeverity.LOW, reason="Pulled"),
        ]
        self.analyzer = ProgressiveEventAnalyzer(self.events)

    def test_total_events_count(self) -> None:
        overview = self.analyzer.get_overview()
        assert isinstance(overview, EventOverview)
        assert overview.total_events == 5  # noqa: PLR2004

    def test_critical_count(self) -> None:
        overview = self.analyzer.get_overview()
        assert overview.critical_count == 2  # noqa: PLR2004

    def test_severity_distribution(self) -> None:
        overview = self.analyzer.get_overview()
        assert overview.severity_distribution["critical"] == 2  # noqa: PLR2004
        assert overview.severity_distribution["high"] == 1

    def test_top_events_limited(self) -> None:
        overview = self.analyzer.get_overview(max_items=2)
        assert len(overview.top_events) == 2  # noqa: PLR2004

    def test_top_events_sorted_by_severity(self) -> None:
        overview = self.analyzer.get_overview()
        assert overview.top_events[0].severity == EventSeverity.CRITICAL

    def test_drill_down_suggestions(self) -> None:
        overview = self.analyzer.get_overview()
        assert len(overview.drill_down_suggestions) > 0

    def test_empty_events_graceful(self) -> None:
        analyzer = ProgressiveEventAnalyzer([])
        overview = analyzer.get_overview()
        assert overview.total_events == 0
        assert overview.top_events == []


class TestDetailedAnalysis:
    def setup_method(self) -> None:
        self.events = [
            _make_event(
                severity=EventSeverity.CRITICAL,
                category=EventCategory.RESOURCE,
                reason="OOMKilled",
                namespace="prod",
            ),
            _make_event(
                severity=EventSeverity.HIGH,
                category=EventCategory.NETWORKING,
                reason="FailedMount",
                namespace="prod",
            ),
            _make_event(
                severity=EventSeverity.MEDIUM,
                category=EventCategory.SCHEDULING,
                reason="FailedScheduling",
                namespace="staging",
            ),
            _make_event(
                severity=EventSeverity.LOW,
                category=EventCategory.LIFECYCLE,
                reason="Pulled",
                namespace="prod",
            ),
        ]
        self.analyzer = ProgressiveEventAnalyzer(self.events)

    def test_returns_detailed_analysis(self) -> None:
        result = self.analyzer.get_detailed_analysis()
        assert isinstance(result, DetailedAnalysis)
        assert len(result.events) > 0

    def test_filter_by_severity(self) -> None:
        result = self.analyzer.get_detailed_analysis(
            event_filters={"severity": EventSeverity.CRITICAL}
        )
        assert len(result.events) == 1
        assert result.events[0].reason == "OOMKilled"

    def test_filter_by_category(self) -> None:
        result = self.analyzer.get_detailed_analysis(
            event_filters={"category": EventCategory.RESOURCE}
        )
        assert len(result.events) == 1

    def test_filter_by_namespace(self) -> None:
        result = self.analyzer.get_detailed_analysis(event_filters={"namespace": "prod"})
        assert len(result.events) == 3  # noqa: PLR2004

    def test_temporal_patterns(self) -> None:
        result = self.analyzer.get_detailed_analysis()
        assert isinstance(result.temporal_patterns, list)

    def test_recommendations_for_critical_events(self) -> None:
        result = self.analyzer.get_detailed_analysis(
            event_filters={"severity": EventSeverity.CRITICAL}
        )
        assert len(result.recommendations) > 0

    def test_empty_events_graceful(self) -> None:
        analyzer = ProgressiveEventAnalyzer([])
        result = analyzer.get_detailed_analysis()
        assert result.events == []
        assert result.recommendations == []


class TestCorrelationAnalysis:
    def setup_method(self) -> None:
        now = datetime.now(UTC)
        self.events = [
            _make_event(
                severity=EventSeverity.CRITICAL,
                reason="OOMKilled",
                involved_object="Pod/api-1",
                category=EventCategory.RESOURCE,
                timestamp=now - timedelta(minutes=30),
            ),
            _make_event(
                severity=EventSeverity.HIGH,
                reason="FailedMount",
                involved_object="Pod/api-1",
                category=EventCategory.STORAGE,
                timestamp=now - timedelta(minutes=25),
            ),
            _make_event(
                severity=EventSeverity.CRITICAL,
                reason="CrashLoopBackOff",
                involved_object="Pod/api-1",
                category=EventCategory.FAILURE,
                timestamp=now - timedelta(minutes=20),
            ),
            _make_event(
                severity=EventSeverity.LOW,
                reason="Pulled",
                involved_object="Pod/worker-2",
                category=EventCategory.LIFECYCLE,
                timestamp=now - timedelta(hours=5),
            ),
        ]
        self.analyzer = ProgressiveEventAnalyzer(self.events)

    def test_returns_correlation_analysis(self) -> None:
        result = self.analyzer.get_correlation_analysis()
        assert isinstance(result, CorrelationAnalysis)
        assert len(result.correlations) > 0

    def test_cascade_detection(self) -> None:
        result = self.analyzer.get_correlation_analysis()
        assert len(result.cascades) > 0

    def test_root_cause_group(self) -> None:
        result = self.analyzer.get_correlation_analysis()
        assert result.root_cause_group is not None

    def test_insights_included(self) -> None:
        result = self.analyzer.get_correlation_analysis()
        assert len(result.insights) > 0

    def test_events_without_timestamps_handled(self) -> None:
        events_no_ts = [
            _make_event(severity=EventSeverity.HIGH, reason="NoTimestamp"),
            _make_event(severity=EventSeverity.LOW, reason="AlsoNoTime"),
        ]
        analyzer = ProgressiveEventAnalyzer(events_no_ts)
        result = analyzer.get_correlation_analysis()
        assert len(result.correlations) == 0
        assert result.root_cause_group is None

    def test_single_event_no_correlation(self) -> None:
        analyzer = ProgressiveEventAnalyzer(
            [_make_event(severity=EventSeverity.CRITICAL, reason="Solo")]
        )
        result = analyzer.get_correlation_analysis()
        assert len(result.correlations) == 0

    def test_empty_events_graceful(self) -> None:
        analyzer = ProgressiveEventAnalyzer([])
        result = analyzer.get_correlation_analysis()
        assert result.correlations == []
        assert result.cascades == []


class TestDetailedAnalysisBurst:
    def test_burst_pattern_detected(self) -> None:
        ts = datetime.now(UTC)
        events = [
            _make_event(
                reason="e1",
                severity=EventSeverity.HIGH,
                timestamp=ts,
            ),
            _make_event(
                reason="e2",
                severity=EventSeverity.HIGH,
                timestamp=ts + timedelta(milliseconds=10),
            ),
            _make_event(
                reason="e3",
                severity=EventSeverity.HIGH,
                timestamp=ts + timedelta(milliseconds=500),
            ),
            _make_event(
                reason="e4",
                severity=EventSeverity.HIGH,
                timestamp=ts + timedelta(milliseconds=510),
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        result = analyzer.get_detailed_analysis()
        assert result.temporal_patterns
        assert any("Burst" in p for p in result.temporal_patterns)


class TestRecommendationStorage:
    def test_storage_recommendation(self) -> None:
        events = [
            _make_event(
                severity=EventSeverity.LOW,
                category=EventCategory.STORAGE,
                reason="VolumeBindingFailed",
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        result = analyzer.get_detailed_analysis()
        assert any("Storage" in r for r in result.recommendations)


class TestCascadeEdgeCases:
    def test_cascade_break_between_cascades(self) -> None:
        ts = datetime.now(UTC)
        events = [
            _make_event(
                reason="e1",
                involved_object="pod/b",
                timestamp=ts,
            ),
            _make_event(
                reason="e2",
                involved_object="pod/b",
                timestamp=ts + timedelta(minutes=5),
            ),
            _make_event(
                reason="e3",
                involved_object="pod/b",
                timestamp=ts + timedelta(minutes=10),
            ),
            _make_event(
                reason="e4",
                involved_object="pod/c",
                timestamp=ts + timedelta(minutes=60),
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        result = analyzer.get_correlation_analysis()
        assert len(result.cascades) == 1
        assert len(result.cascades[0]) == 3  # noqa: PLR2004


class TestModerateResourceImpact:
    def test_moderate_resource_impact_single_oom(self) -> None:
        events = [
            _make_event(
                reason="OOMKilled",
                category=EventCategory.RESOURCE,
                severity=EventSeverity.CRITICAL,
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        result = analyzer.get_detailed_analysis()
        assert "Moderate resource impact" in result.resource_impact


class TestOverviewEqualityDiscriminators:
    def test_full_overview_equality(self) -> None:
        events = [
            _make_event(
                severity=EventSeverity.CRITICAL, reason="OOMKilled", category=EventCategory.RESOURCE
            ),
            _make_event(
                severity=EventSeverity.CRITICAL, reason="CrashLoop", category=EventCategory.RESOURCE
            ),
            _make_event(
                severity=EventSeverity.HIGH, reason="Failed", category=EventCategory.NETWORKING
            ),
            _make_event(
                severity=EventSeverity.MEDIUM, reason="BackOff", category=EventCategory.FAILURE
            ),
            _make_event(
                severity=EventSeverity.LOW, reason="Pulled", category=EventCategory.LIFECYCLE
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)

        overview = analyzer.get_overview(max_items=2)

        assert overview.total_events == 5  # noqa: PLR2004
        assert overview.critical_count == 2  # noqa: PLR2004
        assert overview.high_count == 1
        assert overview.medium_count == 1
        assert overview.low_count == 1
        assert overview.severity_distribution == {
            "critical": 2,  # noqa: PLR2004
            "high": 1,
            "medium": 1,
            "low": 1,
        }
        assert overview.category_distribution["resource"] == 2  # noqa: PLR2004
        assert overview.category_distribution["networking"] == 1
        assert [e.reason for e in overview.top_events] == ["OOMKilled", "CrashLoop"]
        assert overview.drill_down_suggestions == [
            "Investigate 2 critical events",
            "Drill into resource events (2)",
        ]

    def test_overview_zero_counts_when_empty_severity(self) -> None:
        events = [_make_event(severity=EventSeverity.LOW, reason="Pulled")]
        analyzer = ProgressiveEventAnalyzer(events)
        overview = analyzer.get_overview()
        assert overview.critical_count == 0
        assert overview.high_count == 0
        assert overview.medium_count == 0


class TestDrillDownSuggestionsDiscriminators:
    def test_critical_high_and_top_category(self) -> None:
        result = ProgressiveEventAnalyzer._build_drill_down_suggestions(
            {"critical": 2, "high": 3, "medium": 0, "low": 0},  # noqa: PLR2004
            {"resource": 3, "failure": 1},  # noqa: PLR2004
        )
        assert result == [
            "Investigate 2 critical events",
            "Drill into resource events (3)",
            "Review 3 high-severity events for patterns",
        ]

    def test_no_critical_only_top_category(self) -> None:
        result = ProgressiveEventAnalyzer._build_drill_down_suggestions(
            {"critical": 0, "high": 1, "medium": 0, "low": 0},
            {"failure": 1},
        )
        assert result == ["Drill into failure events (1)"]

    def test_high_exactly_two_not_reviewed(self) -> None:
        result = ProgressiveEventAnalyzer._build_drill_down_suggestions(
            {"critical": 0, "high": 2, "medium": 0, "low": 0},  # noqa: PLR2004
            {"failure": 1},
        )
        assert result == ["Drill into failure events (1)"]


class TestRecommendationsDiscriminators:
    def test_critical_resource_full_list(self) -> None:
        events = [_make_event(severity=EventSeverity.CRITICAL, category=EventCategory.RESOURCE)]
        result = ProgressiveEventAnalyzer._build_recommendations(events)
        assert result == [
            "IMMEDIATE ACTION: 1 critical events — investigate root cause",
            "Resource constraints detected — review pod limits and node capacity",
        ]

    def test_low_resource_only(self) -> None:
        events = [_make_event(severity=EventSeverity.LOW, category=EventCategory.RESOURCE)]
        result = ProgressiveEventAnalyzer._build_recommendations(events)
        assert result == ["Resource constraints detected — review pod limits and node capacity"]

    def test_networking_recommendation(self) -> None:
        events = [_make_event(severity=EventSeverity.LOW, category=EventCategory.NETWORKING)]
        result = ProgressiveEventAnalyzer._build_recommendations(events)
        assert result == ["Network issues found — check CNI plugin and service configurations"]

    def test_storage_recommendation_exact(self) -> None:
        events = [_make_event(severity=EventSeverity.LOW, category=EventCategory.STORAGE)]
        result = ProgressiveEventAnalyzer._build_recommendations(events)
        assert result == ["Storage issues detected — verify PV/PVC bindings and CSI driver"]

    def test_no_message_category_monitoring(self) -> None:
        events = [_make_event(severity=EventSeverity.LOW, category=EventCategory.LIFECYCLE)]
        result = ProgressiveEventAnalyzer._build_recommendations(events)
        assert result == ["No critical issues — continue monitoring"]

    def test_two_critical_count_exact(self) -> None:
        events = [
            _make_event(severity=EventSeverity.CRITICAL, category=EventCategory.FAILURE),
            _make_event(severity=EventSeverity.CRITICAL, category=EventCategory.HEALTH),
        ]
        result = ProgressiveEventAnalyzer._build_recommendations(events)
        assert result[0] == "IMMEDIATE ACTION: 2 critical events — investigate root cause"


class TestResourceImpactDiscriminators:
    def test_three_oom_high(self) -> None:
        events = [_make_event(reason="OOMKilled") for _ in range(3)]
        result = ProgressiveEventAnalyzer._assess_resource_impact(events)
        assert result == "High resource impact — multiple OOM events across pods"

    def test_two_oom_moderate(self) -> None:
        events = [_make_event(reason="OOMKilled") for _ in range(2)]
        result = ProgressiveEventAnalyzer._assess_resource_impact(events)
        assert result == "Moderate resource impact — OOM event detected"

    def test_one_oom_moderate(self) -> None:
        events = [_make_event(reason="OOMKilled")]
        result = ProgressiveEventAnalyzer._assess_resource_impact(events)
        assert result == "Moderate resource impact — OOM event detected"

    def test_resource_without_oom_low(self) -> None:
        events = [_make_event(reason="Evicted")]
        result = ProgressiveEventAnalyzer._assess_resource_impact(events)
        assert result == "Low resource impact — resource events without memory pressure"

    def test_non_resource_no_impact(self) -> None:
        events = [_make_event(category=EventCategory.NETWORKING, reason="Failed")]
        result = ProgressiveEventAnalyzer._assess_resource_impact(events)
        assert result == "No resource impact detected"

    def test_oom_uppercase_reason_detected(self) -> None:
        events = [_make_event(reason="OOMKILLED")]
        result = ProgressiveEventAnalyzer._assess_resource_impact(events)
        assert result == "Moderate resource impact — OOM event detected"


class TestTemporalPatternsDiscriminators:
    def _ts(self, base: datetime, offset: timedelta) -> ClassifiedEvent:
        return _make_event(timestamp=base + offset)

    def test_burst_three_of_four_intervals(self) -> None:
        base = datetime.now(UTC)
        events = [
            self._ts(base, timedelta(seconds=0)),
            self._ts(base, timedelta(seconds=1)),
            self._ts(base, timedelta(seconds=2)),
            self._ts(base, timedelta(seconds=3)),
            self._ts(base, timedelta(seconds=63)),
        ]
        result = ProgressiveEventAnalyzer._detect_temporal_patterns(events)
        assert result == ["Burst pattern detected: 3 events within close succession"]

    def test_steady_stream_exact_message(self) -> None:
        base = datetime.now(UTC)
        events = [
            self._ts(base, timedelta(seconds=0)),
            self._ts(base, timedelta(seconds=1)),
            self._ts(base, timedelta(seconds=2)),
        ]
        result = ProgressiveEventAnalyzer._detect_temporal_patterns(events)
        assert result == ["Steady event stream — average interval: 1s"]

    def test_single_event_no_pattern(self) -> None:
        result = ProgressiveEventAnalyzer._detect_temporal_patterns(
            [_make_event(timestamp=datetime.now(UTC))]
        )
        assert result == []

    def test_two_events_no_timestamps_no_pattern(self) -> None:
        events = [_make_event(timestamp=None), _make_event(timestamp=None)]
        result = ProgressiveEventAnalyzer._detect_temporal_patterns(events)
        assert result == []

    def test_untimed_events_filtered_out(self) -> None:
        base = datetime.now(UTC)
        events = [
            _make_event(timestamp=None),
            self._ts(base, timedelta(seconds=0)),
            self._ts(base, timedelta(seconds=1)),
            _make_event(timestamp=None),
        ]
        result = ProgressiveEventAnalyzer._detect_temporal_patterns(events)
        assert result == ["Steady event stream — average interval: 1s"]


class TestCorrelationFindDiscriminators:
    def test_correlation_strength_rounds_to_two_decimals(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(reason="r1", involved_object="Pod/x", timestamp=base),
            _make_event(
                reason="r2", involved_object="Pod/x", timestamp=base + timedelta(seconds=137)
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        correlations = analyzer.get_correlation_analysis().correlations
        assert correlations == [
            {
                "event_a_reason": "r1",
                "event_b_reason": "r2",
                "involved_object": "Pod/x",
                "strength": 0.54,  # noqa: PLR2004
            }
        ]

    def test_correlation_beyond_window_excluded(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(reason="r1", involved_object="Pod/x", timestamp=base),
            _make_event(
                reason="r2", involved_object="Pod/x", timestamp=base + timedelta(minutes=10)
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        assert analyzer.get_correlation_analysis().correlations == []

    def test_correlation_different_object_excluded(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(reason="r1", involved_object="Pod/x", timestamp=base),
            _make_event(
                reason="r2", involved_object="Pod/y", timestamp=base + timedelta(seconds=30)
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        assert analyzer.get_correlation_analysis().correlations == []


class TestCascadeDetectionDiscriminators:
    def test_three_events_cascade(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(reason="c1", involved_object="Pod/c", timestamp=base),
            _make_event(
                reason="c2", involved_object="Pod/c", timestamp=base + timedelta(minutes=5)
            ),
            _make_event(
                reason="c3", involved_object="Pod/c", timestamp=base + timedelta(minutes=10)
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        cascades = analyzer.get_correlation_analysis().cascades
        assert len(cascades) == 1
        assert [e.reason for e in cascades[0]] == ["c1", "c2", "c3"]


class TestRootCauseDiscriminator:
    def test_most_common_category_value(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(
                category=EventCategory.RESOURCE,
                involved_object="Pod/a",
                timestamp=base,
            ),
            _make_event(
                category=EventCategory.RESOURCE,
                involved_object="Pod/a",
                timestamp=base + timedelta(seconds=30),
            ),
            _make_event(
                category=EventCategory.NETWORKING,
                involved_object="Pod/a",
                timestamp=base + timedelta(seconds=60),
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        assert analyzer.get_correlation_analysis().root_cause_group == "resource"


class TestCorrelationInsightsDiscriminators:
    def test_cascade_insight_exact(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        cascade = [
            _make_event(reason="c1", involved_object="Pod/c", timestamp=base),
            _make_event(
                reason="c2", involved_object="Pod/c", timestamp=base + timedelta(minutes=5)
            ),
            _make_event(
                reason="c3", involved_object="Pod/c", timestamp=base + timedelta(minutes=10)
            ),
        ]
        result = ProgressiveEventAnalyzer._generate_correlation_insights([], [cascade])
        assert result == ["Cascade #1 on Pod/c: started with 'c1' → ended with 'c3' (3 events)"]

    def test_strongest_correlation_insight(self) -> None:
        correlations = [
            {
                "event_a_reason": "a1",
                "event_b_reason": "b1",
                "involved_object": "o1",
                "strength": 0.5,
            },
            {
                "event_a_reason": "a2",
                "event_b_reason": "b2",
                "involved_object": "o2",
                "strength": 0.9,
            },
        ]
        result = ProgressiveEventAnalyzer._generate_correlation_insights(correlations, [])
        assert result == ["Strongest correlation: a2 ↔ b2 on o2"]

    def test_no_correlations_no_cascades_message(self) -> None:
        result = ProgressiveEventAnalyzer._generate_correlation_insights([], [])
        assert result == ["No significant correlations or cascades found"]

    def test_both_cascade_and_correlation_insights(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        cascade = [
            _make_event(reason="c1", involved_object="Pod/c", timestamp=base),
            _make_event(
                reason="c2", involved_object="Pod/c", timestamp=base + timedelta(minutes=5)
            ),
            _make_event(
                reason="c3", involved_object="Pod/c", timestamp=base + timedelta(minutes=10)
            ),
        ]
        correlations = [
            {
                "event_a_reason": "c1",
                "event_b_reason": "c2",
                "involved_object": "Pod/c",
                "strength": 1.0,
            }
        ]
        result = ProgressiveEventAnalyzer._generate_correlation_insights(correlations, [cascade])
        assert result == [
            "Cascade #1 on Pod/c: started with 'c1' → ended with 'c3' (3 events)",
            "Strongest correlation: c1 ↔ c2 on Pod/c",
        ]


class TestOverviewMaxItemsDiscriminator:
    def test_default_max_items_truncates_to_five(self) -> None:
        events = [_make_event(reason=f"e{i}") for i in range(6)]
        analyzer = ProgressiveEventAnalyzer(events)
        overview = analyzer.get_overview()
        assert len(overview.top_events) == 5  # noqa: PLR2004


class TestDrillDownCriticalOneDiscriminator:
    def test_exactly_one_critical_still_suggested(self) -> None:
        result = ProgressiveEventAnalyzer._build_drill_down_suggestions(
            {"critical": 1, "high": 0, "medium": 0, "low": 0},
            {"failure": 1},
        )
        assert result == [
            "Investigate 1 critical events",
            "Drill into failure events (1)",
        ]


class TestTemporalTwoEventsDiscriminator:
    def test_two_timed_events_produce_steady_pattern(self) -> None:
        base = datetime.now(UTC)
        events = [
            _make_event(timestamp=base),
            _make_event(timestamp=base + timedelta(seconds=1)),
        ]
        result = ProgressiveEventAnalyzer._detect_temporal_patterns(events)
        assert result == ["Steady event stream — average interval: 1s"]


class TestTemporalBurstBoundaryDiscriminator:
    def test_bursts_exactly_half_is_steady(self) -> None:
        base = datetime.now(UTC)
        events = [
            _make_event(timestamp=base),
            _make_event(timestamp=base + timedelta(seconds=1)),
            _make_event(timestamp=base + timedelta(seconds=2)),
            _make_event(timestamp=base + timedelta(seconds=102)),
            _make_event(timestamp=base + timedelta(seconds=202)),
        ]
        result = ProgressiveEventAnalyzer._detect_temporal_patterns(events)
        assert result == ["Steady event stream — average interval: 50s"]


class TestCascadeObjectChangeDiscriminator:
    def test_object_change_breaks_cascade_even_within_window(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(reason="c1", involved_object="Pod/a", timestamp=base),
            _make_event(
                reason="c2", involved_object="Pod/b", timestamp=base + timedelta(minutes=1)
            ),
            _make_event(
                reason="c3", involved_object="Pod/a", timestamp=base + timedelta(minutes=2)
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        cascades = analyzer.get_correlation_analysis().cascades
        assert cascades == []

    def test_gap_exactly_window_is_inclusive(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(reason="c1", involved_object="Pod/c", timestamp=base),
            _make_event(
                reason="c2", involved_object="Pod/c", timestamp=base + timedelta(minutes=30)
            ),
            _make_event(
                reason="c3", involved_object="Pod/c", timestamp=base + timedelta(minutes=31)
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        cascades = analyzer.get_correlation_analysis().cascades
        assert len(cascades) == 1
        assert [e.reason for e in cascades[0]] == ["c1", "c2", "c3"]


class TestCorrelationTimelessMiddleDiscriminator:
    def test_untimed_event_between_timed_does_not_stop_search(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(reason="a", involved_object="Pod/x", timestamp=base),
            _make_event(reason="untimed", involved_object="Pod/x", timestamp=None),
            _make_event(
                reason="b", involved_object="Pod/x", timestamp=base + timedelta(seconds=30)
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        correlations = analyzer.get_correlation_analysis().correlations
        assert [c["event_a_reason"] for c in correlations] == ["a"]
        assert correlations[0]["event_b_reason"] == "b"

    def test_leading_untimed_event_does_not_block_correlations(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(reason="untimed", involved_object="Pod/x", timestamp=None),
            _make_event(reason="a", involved_object="Pod/x", timestamp=base),
            _make_event(
                reason="b", involved_object="Pod/x", timestamp=base + timedelta(seconds=30)
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        correlations = analyzer.get_correlation_analysis().correlations
        assert [c["event_a_reason"] for c in correlations] == ["a"]
        assert correlations[0]["event_b_reason"] == "b"


class TestCorrelationAnalysisInsightsWiring:
    def test_insights_include_cascade_and_strongest(self) -> None:
        base = datetime(2026, 1, 1, 0, 0, tzinfo=UTC)
        events = [
            _make_event(reason="c1", involved_object="Pod/c", timestamp=base),
            _make_event(
                reason="c2", involved_object="Pod/c", timestamp=base + timedelta(minutes=5)
            ),
            _make_event(
                reason="c3", involved_object="Pod/c", timestamp=base + timedelta(minutes=10)
            ),
        ]
        analyzer = ProgressiveEventAnalyzer(events)
        insights = analyzer.get_correlation_analysis().insights
        assert insights == [
            "Cascade #1 on Pod/c: started with 'c1' → ended with 'c3' (3 events)",
            "Strongest correlation: c1 ↔ c2 on Pod/c",
        ]


class TestRootCauseEmptyDiscriminator:
    def test_empty_events_root_cause_none_direct(self) -> None:
        analyzer = ProgressiveEventAnalyzer([])
        assert analyzer._identify_root_cause_group() is None
