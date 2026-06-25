from collections import Counter
from dataclasses import dataclass, field
from datetime import timedelta

from hexawyn.domain.models.constants import EventAnalysisConstants
from hexawyn.domain.models.event import ClassifiedEvent, EventCategory, EventSeverity

_cfg = EventAnalysisConstants()


@dataclass
class EventOverview:
    """Level 1 — quick overview of the event landscape."""

    total_events: int = 0
    critical_count: int = 0
    high_count: int = 0
    medium_count: int = 0
    low_count: int = 0
    top_events: list[ClassifiedEvent] = field(default_factory=list)
    severity_distribution: dict[str, int] = field(default_factory=dict)
    category_distribution: dict[str, int] = field(default_factory=dict)
    drill_down_suggestions: list[str] = field(default_factory=list)


@dataclass
class DetailedAnalysis:
    """Level 2 — detailed breakdown with filters and patterns."""

    events: list[ClassifiedEvent] = field(default_factory=list)
    temporal_patterns: list[str] = field(default_factory=list)
    resource_impact: str = ""
    recommendations: list[str] = field(default_factory=list)


@dataclass
class CorrelationAnalysis:
    """Level 3 — cross-event correlation and cascade detection."""

    correlations: list[dict[str, str | float]] = field(default_factory=list)
    cascades: list[list[ClassifiedEvent]] = field(default_factory=list)
    root_cause_group: str | None = None
    insights: list[str] = field(default_factory=list)


class ProgressiveEventAnalyzer:
    """Three-level progressive disclosure for Kubernetes event analysis.

    Level 1 — get_overview(): top events, severity/category distribution,
    drill-down suggestions.

    Level 2 — get_detailed_analysis(): filtered events by severity,
    category, or namespace, with temporal patterns and recommendations.

    Level 3 — get_correlation_analysis(): event-to-event correlations,
    failure cascade detection within a time window, root cause grouping.
    """

    def __init__(self, classified_events: list[ClassifiedEvent]) -> None:
        self._events = classified_events

    def get_overview(self, max_items: int = 5) -> EventOverview:
        if not self._events:
            return EventOverview()

        severity_counts: dict[str, int] = {}
        for sev in EventSeverity:
            severity_counts[sev.value] = sum(1 for e in self._events if e.severity == sev)

        category_counts: dict[str, int] = {}
        for cat in EventCategory:
            category_counts[cat.value] = sum(1 for e in self._events if e.category == cat)

        sorted_events = sorted(
            self._events,
            key=lambda e: list(EventSeverity).index(e.severity),
        )

        suggestions = self._build_drill_down_suggestions(severity_counts, category_counts)

        return EventOverview(
            total_events=len(self._events),
            critical_count=severity_counts.get("critical", 0),
            high_count=severity_counts.get("high", 0),
            medium_count=severity_counts.get("medium", 0),
            low_count=severity_counts.get("low", 0),
            top_events=sorted_events[:max_items],
            severity_distribution=severity_counts,
            category_distribution=category_counts,
            drill_down_suggestions=suggestions,
        )

    def get_detailed_analysis(
        self,
        event_filters: dict[str, str | EventSeverity | EventCategory] | None = None,
    ) -> DetailedAnalysis:
        if not self._events:
            return DetailedAnalysis()

        filtered = self._apply_filters(self._events, event_filters or {})

        temporal_patterns = self._detect_temporal_patterns(filtered)
        recommendations = self._build_recommendations(filtered)
        resource_impact = self._assess_resource_impact(filtered)

        return DetailedAnalysis(
            events=filtered,
            temporal_patterns=temporal_patterns,
            resource_impact=resource_impact,
            recommendations=recommendations,
        )

    def get_correlation_analysis(
        self,
        seed_event_id: str | None = None,
    ) -> CorrelationAnalysis:
        if not self._events:
            return CorrelationAnalysis()

        correlated_pairs = self._find_correlations()
        cascades = self._detect_cascades()
        root_cause = self._identify_root_cause_group() if correlated_pairs else None
        insights = self._generate_correlation_insights(correlated_pairs, cascades)

        return CorrelationAnalysis(
            correlations=correlated_pairs,
            cascades=cascades,
            root_cause_group=root_cause,
            insights=insights,
        )

    @staticmethod
    def _apply_filters(
        events: list[ClassifiedEvent],
        filters: dict[str, str | EventSeverity | EventCategory],
    ) -> list[ClassifiedEvent]:
        result = events
        if "severity" in filters:
            result = [e for e in result if e.severity == filters["severity"]]
        if "category" in filters:
            result = [e for e in result if e.category == filters["category"]]
        if "namespace" in filters:
            result = [e for e in result if e.namespace == filters["namespace"]]
        return result

    @staticmethod
    def _build_drill_down_suggestions(
        severity_counts: dict[str, int],
        category_counts: dict[str, int],
    ) -> list[str]:
        suggestions: list[str] = []

        if severity_counts.get("critical", 0) > 0:
            suggestions.append(f"Investigate {severity_counts['critical']} critical events")

        top_category = max(category_counts, key=lambda k: category_counts[k])
        if category_counts[top_category] > 0:
            suggestions.append(
                f"Drill into {top_category} events ({category_counts[top_category]})"
            )

        if severity_counts.get("high", 0) > 2:
            suggestions.append(
                f"Review {severity_counts['high']} high-severity events for patterns"
            )

        return suggestions

    @staticmethod
    def _detect_temporal_patterns(
        events: list[ClassifiedEvent],
    ) -> list[str]:
        patterns: list[str] = []
        if len(events) < 2:
            return patterns

        timed_events = [e for e in events if e.first_timestamp is not None]
        if len(timed_events) < 2:
            return patterns

        sorted_events = sorted(
            timed_events,
            key=lambda e: e.first_timestamp,  # type: ignore[arg-type,return-value]
        )

        intervals: list[float] = []
        for i in range(1, len(sorted_events)):
            a = sorted_events[i - 1].first_timestamp
            b = sorted_events[i].first_timestamp
            if a is not None and b is not None:
                intervals.append((b - a).total_seconds())

        if intervals:
            avg_interval = sum(intervals) / len(intervals)
            burst_threshold = avg_interval * 0.3
            bursts = sum(1 for iv in intervals if iv < burst_threshold)

            if bursts > len(intervals) * 0.5:
                patterns.append(f"Burst pattern detected: {bursts} events within close succession")
            else:
                patterns.append(f"Steady event stream — average interval: {avg_interval:.0f}s")

        return patterns

    @staticmethod
    def _build_recommendations(
        events: list[ClassifiedEvent],
    ) -> list[str]:
        recs: list[str] = []

        severity_groups: dict[EventSeverity, int] = {}
        for e in events:
            severity_groups[e.severity] = severity_groups.get(e.severity, 0) + 1

        category_groups: dict[EventCategory, int] = {}
        for e in events:
            category_groups[e.category] = category_groups.get(e.category, 0) + 1

        if EventSeverity.CRITICAL in severity_groups:
            recs.append(
                f"IMMEDIATE ACTION: {severity_groups[EventSeverity.CRITICAL]} "
                "critical events — investigate root cause"
            )

        if EventCategory.RESOURCE in category_groups:
            recs.append("Resource constraints detected — review pod limits and node capacity")

        if EventCategory.NETWORKING in category_groups:
            recs.append("Network issues found — check CNI plugin and service configurations")

        if EventCategory.STORAGE in category_groups:
            recs.append("Storage issues detected — verify PV/PVC bindings and CSI driver")

        if not recs:
            recs.append("No critical issues — continue monitoring")

        return recs

    @staticmethod
    def _assess_resource_impact(
        events: list[ClassifiedEvent],
    ) -> str:
        resource_events = [e for e in events if e.category == EventCategory.RESOURCE]
        if not resource_events:
            return "No resource impact detected"

        oom_count = sum(1 for e in resource_events if "oom" in e.reason.lower())

        if oom_count > 2:
            return "High resource impact — multiple OOM events across pods"
        if oom_count > 0:
            return "Moderate resource impact — OOM event detected"
        return "Low resource impact — resource events without memory pressure"

    def _find_correlations(self) -> list[dict[str, str | float]]:
        correlations: list[dict[str, str | float]] = []
        window = timedelta(minutes=_cfg.correlation_time_window_minutes)

        for i, event_a in enumerate(self._events):
            if event_a.first_timestamp is None:
                continue
            for event_b in self._events[i + 1 :]:
                if event_b.first_timestamp is None:
                    continue
                delta = abs(event_a.first_timestamp - event_b.first_timestamp)
                if delta <= window and event_a.involved_object == event_b.involved_object:
                    strength = 1.0 - (delta.total_seconds() / window.total_seconds())
                    correlations.append(
                        {
                            "event_a_reason": event_a.reason,
                            "event_b_reason": event_b.reason,
                            "involved_object": event_a.involved_object,
                            "strength": round(strength, 2),
                        }
                    )

        return correlations[: _cfg.max_correlated_events]

    def _detect_cascades(self) -> list[list[ClassifiedEvent]]:
        cascades: list[list[ClassifiedEvent]] = []
        window = timedelta(minutes=_cfg.failure_cascade_window_minutes)
        min_events = _cfg.failure_cascade_min_events

        timed_events = [e for e in self._events if e.first_timestamp is not None]
        sorted_events = sorted(
            timed_events,
            key=lambda e: e.first_timestamp,  # type: ignore[arg-type,return-value]
        )

        cascade: list[ClassifiedEvent] = []
        for event in sorted_events:
            if not cascade:
                cascade = [event]
                continue

            if event.first_timestamp is not None and cascade[-1].first_timestamp is not None:
                gap = event.first_timestamp - cascade[-1].first_timestamp
                if gap <= window and event.involved_object == cascade[-1].involved_object:
                    cascade.append(event)
                else:
                    if len(cascade) >= min_events:
                        cascades.append(cascade)
                    cascade = [event]

        if len(cascade) >= min_events:
            cascades.append(cascade)

        return cascades

    def _identify_root_cause_group(self) -> str | None:
        if not self._events:
            return None

        category_counter: Counter[EventCategory] = Counter(e.category for e in self._events)
        if not category_counter:
            return None

        top_category = category_counter.most_common(1)[0][0]
        return top_category.value

    @staticmethod
    def _generate_correlation_insights(
        correlations: list[dict[str, str | float]],
        cascades: list[list[ClassifiedEvent]],
    ) -> list[str]:
        insights: list[str] = []

        if cascades:
            for i, cascade in enumerate(cascades):
                start_reason = cascade[0].reason
                end_reason = cascade[-1].reason
                obj = cascade[0].involved_object
                insights.append(
                    f"Cascade #{i + 1} on {obj}: "
                    f"started with '{start_reason}' → ended with '{end_reason}' "
                    f"({len(cascade)} events)"
                )

        if correlations:
            strongest = max(correlations, key=lambda c: float(c["strength"]))
            insights.append(
                f"Strongest correlation: {strongest['event_a_reason']} ↔ "
                f"{strongest['event_b_reason']} on {strongest['involved_object']}"
            )

        if not insights:
            insights.append("No significant correlations or cascades found")

        return insights
