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
