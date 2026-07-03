from hexawyn.domain.models.constants import LogAnalysisConstants
from hexawyn.domain.models.log import (
    DeduplicatedLine,
    LogAnalysisContext,
    LogAnalysisResult,
    RankedEvent,
)
from hexawyn.domain.services.log_analysis.analyzer import AdaptiveLogProcessor
from hexawyn.domain.services.log_analysis.event_severity import (
    SEVERITY_ORDER,
    classify_event_severity,
)
from hexawyn.domain.services.log_analysis.log_deduplicator import deduplicate_lines
from hexawyn.domain.services.log_analysis.noise_filter import is_noise
from hexawyn.domain.services.log_analysis.pattern_reducer import (
    extract_error_patterns,
    reduce_logs_for_summarization,
)
from hexawyn.domain.services.log_analysis.strategy_port import LogAnalysisStrategy
from hexawyn.domain.services.log_analysis.summarizer import generate_summary

__all__ = [
    "LogAnalysisStrategy",
    "SmartSummaryStrategy",
    "StreamingStrategy",
    "HybridStrategy",
    "RealtimeLogWatchStrategy",
    "StrategySelector",
]

_log_constants = LogAnalysisConstants()
_REDUCED_CHUNK_SIZE = 500


class SmartSummaryStrategy(LogAnalysisStrategy):
    """Deduplicates, filters noise, and ranks unique events by severity.

    Concrete SMART implementation of LogAnalysisStrategy (ILogAnalysisStrategy,
    ECA-14). No I/O — deduplication, noise filtering, and severity
    classification are all pure functions from this package.
    """

    def supports(self, context: LogAnalysisContext) -> bool:
        if context.urgency == "critical" and context.time_sensitive:
            return False
        return context.log_size_estimate >= _log_constants.smart_summary_min_lines

    def analyze(self, logs: list[str], context: LogAnalysisContext) -> LogAnalysisResult:
        if not logs:
            observed_at = context.observed_at or "unknown time"
            return LogAnalysisResult(
                summary=f"No logs available (observed at {observed_at}).",
                strategy_used="smart_summary",
            )

        deduped = deduplicate_lines(logs)
        visible = deduped if context.include_noise else [d for d in deduped if not is_noise(d.line)]

        ranked_events = sorted(
            (
                RankedEvent(line=d.line, count=d.count, severity=classify_event_severity(d.line))
                for d in visible
            ),
            key=lambda event: SEVERITY_ORDER[event.severity],
            reverse=True,
        )

        severity = self._count_severity(logs)
        patterns = [event.line for event in ranked_events]
        recommendations = self._build_recommendations([p.lower() for p in patterns], severity)
        summary, confidence = self._build_summary(logs, deduped, ranked_events)
        token_reduction_percentage = self._token_reduction_percentage(logs, patterns)

        return LogAnalysisResult(
            summary=summary,
            patterns=patterns,
            recommendations=recommendations,
            severity=severity,
            confidence=confidence,
            strategy_used="smart_summary",
            token_reduction_percentage=token_reduction_percentage,
            ranked_events=ranked_events,
        )

    @staticmethod
    def _build_summary(
        logs: list[str], deduped: list[DeduplicatedLine], ranked_events: list[RankedEvent]
    ) -> tuple[str, float]:
        if not ranked_events:
            return (
                f"Analyzed {len(logs)} log lines — no meaningful events after noise filtering.",
                0.9,
            )
        top = ranked_events[0]
        filtered_count = len(deduped) - len(ranked_events)
        noise_note = f" ({filtered_count} filtered as noise)" if filtered_count else ""
        summary = (
            f"Reduced {len(logs)} lines to {len(ranked_events)} unique meaningful events"
            f"{noise_note}. Top: [{top.count}x] {top.severity} — {top.line}"
        )
        confidence = min(0.95, 0.6 + 0.02 * len(ranked_events))
        return summary, confidence

    @staticmethod
    def _token_reduction_percentage(logs: list[str], reduced_lines: list[str]) -> float:
        raw_tokens = AdaptiveLogProcessor.estimate_tokens_from_lines(logs)
        if raw_tokens == 0:
            return 0.0
        reduced_tokens = AdaptiveLogProcessor.estimate_tokens_from_lines(reduced_lines)
        return max(0.0, (1 - reduced_tokens / raw_tokens) * 100)

    @staticmethod
    def _build_recommendations(patterns: list[str], severity: str) -> list[str]:
        if not patterns:
            return []
        recs: list[str] = []
        for pattern in patterns:
            if "oomkilled" in pattern:
                recs.append("Increase memory limit for affected containers")
            elif "crashloop" in pattern or "backoff" in pattern.lower():
                recs.append("Check container startup command and image pull policy")
            elif "timeout" in pattern:
                recs.append("Review probe timeout and initial delay settings")
            elif "denied" in pattern:
                recs.append("Review RBAC permissions for the service account")
        if severity == "critical":
            recs.append("Investigate immediately — critical error rate detected")
        return recs


class StreamingStrategy(LogAnalysisStrategy):
    """Chunk-based analysis — best for time-sensitive troubleshooting."""

    def supports(self, context: LogAnalysisContext) -> bool:
        if context.urgency == "critical" and context.time_sensitive:
            return True
        return (
            context.request_type == "troubleshooting"
            and context.log_size_estimate >= _log_constants.streaming_min_lines
        )

    def analyze(self, logs: list[str], context: LogAnalysisContext) -> LogAnalysisResult:
        if not logs:
            return LogAnalysisResult(
                summary="No log data to analyze.",
                strategy_used="streaming",
            )

        chunks = self._chunk_logs(logs, _log_constants.streaming_chunk_size)
        all_patterns: list[str] = []
        chunk_summaries: list[str] = []

        for i, chunk in enumerate(chunks):
            chunk_patterns = self._extract_patterns(chunk)
            all_patterns.extend(chunk_patterns)

            error_count = sum(1 for line in chunk if "error" in line.lower())
            if error_count > 0:
                chunk_summaries.append(
                    f"Chunk {i + 1}/{len(chunks)}: {error_count} errors detected"
                )

        deduped = list(dict.fromkeys(all_patterns))[:5]
        severity = self._count_severity(logs)
        total_errors = sum(1 for line in logs if "error" in line.lower())

        summary = (
            f"Streaming analysis of {len(logs)} lines across {len(chunks)} chunks. "
            f"Total errors: {total_errors}. " + " ".join(chunk_summaries[:3])
        )

        recommendations = self._build_streaming_recommendations(deduped, severity)

        return LogAnalysisResult(
            summary=summary,
            patterns=deduped,
            recommendations=recommendations,
            severity=severity,
            confidence=min(0.90, 0.5 + len(deduped) * 0.1),
            strategy_used="streaming",
        )

    @staticmethod
    def _chunk_logs(logs: list[str], chunk_size: int) -> list[list[str]]:
        return [logs[i : i + chunk_size] for i in range(0, len(logs), chunk_size)]

    @staticmethod
    def _build_streaming_recommendations(patterns: list[str], severity: str) -> list[str]:
        recs: list[str] = []
        for pattern in patterns:
            if "oomkilled" in pattern:
                recs.append("Increase memory limit for affected containers")
            elif "crashloop" in pattern or "backoff" in pattern.lower():
                recs.append("Check container startup command and image pull policy")
            elif "image" in pattern.lower() and "pull" in pattern.lower():
                recs.append("Verify image registry connectivity and credentials")
        if severity == "critical":
            recs.insert(0, "IMMEDIATE ACTION: Critical errors detected in stream")
        return recs


class HybridStrategy(LogAnalysisStrategy):
    """Deterministic pattern extraction, then a natural-language summary.

    Concrete HYBRID implementation of LogAnalysisStrategy (ILogAnalysisStrategy,
    ECA-14). No real LLM call is made anywhere in this repo (see
    docs/use-cases/58-hybrid-log-analysis.md) — generate_summary() is the
    isolated, documented seam where a real Anthropic/local-model adapter
    would plug in later without changing this class's contract.
    """

    def __init__(self, token_processor: AdaptiveLogProcessor | None = None) -> None:
        self._token_processor = token_processor or AdaptiveLogProcessor()

    def supports(self, context: LogAnalysisContext) -> bool:
        if context.request_type == "investigation":
            return context.log_size_estimate >= _log_constants.hybrid_min_lines
        if context.follow_up_analysis:
            return context.log_size_estimate >= _log_constants.hybrid_min_lines
        return False

    def analyze(self, logs: list[str], context: LogAnalysisContext) -> LogAnalysisResult:
        if not logs:
            return LogAnalysisResult(
                summary="No log data to analyze.",
                strategy_used="hybrid",
            )

        classifications = extract_error_patterns(logs)
        reduced_lines = reduce_logs_for_summarization(logs)
        severity = self._count_severity(logs)

        summary, degraded = self._summarize(reduced_lines, severity)

        patterns = [c.pattern for c in classifications]
        recommendations = SmartSummaryStrategy._build_recommendations(patterns, severity)
        total_matches = sum(c.count for c in classifications)
        confidence = 0.4 if degraded else min(0.95, 0.6 + 0.01 * total_matches)

        return LogAnalysisResult(
            summary=summary,
            patterns=patterns,
            recommendations=recommendations,
            severity=severity,
            confidence=confidence,
            strategy_used="hybrid",
            token_reduction_percentage=self._token_reduction_percentage(logs, reduced_lines),
            degraded=degraded,
        )

    def _summarize(self, reduced_lines: list[str], severity: str) -> tuple[str, bool]:
        reduced_tokens = AdaptiveLogProcessor.estimate_tokens_from_lines(reduced_lines)
        if self._token_processor.can_process_more(reduced_tokens):
            return generate_summary(reduced_lines, severity)

        chunks = [
            reduced_lines[i : i + _REDUCED_CHUNK_SIZE]
            for i in range(0, len(reduced_lines), _REDUCED_CHUNK_SIZE)
        ]
        chunk_summaries: list[str] = []
        any_degraded = False
        for chunk in chunks:
            chunk_summary, chunk_degraded = generate_summary(chunk, severity)
            chunk_summaries.append(chunk_summary)
            any_degraded = any_degraded or chunk_degraded
        return " ".join(chunk_summaries), any_degraded

    @staticmethod
    def _token_reduction_percentage(logs: list[str], reduced_lines: list[str]) -> float:
        raw_tokens = AdaptiveLogProcessor.estimate_tokens_from_lines(logs)
        if raw_tokens == 0:
            return 0.0
        reduced_tokens = AdaptiveLogProcessor.estimate_tokens_from_lines(reduced_lines)
        return max(0.0, (1 - reduced_tokens / raw_tokens) * 100)


class RealtimeLogWatchStrategy(LogAnalysisStrategy):
    """Concrete ILogAnalysisStrategy for the real-time pod-log-watch use case (ECA-16).

    Named distinctly from StreamingStrategy (which means the >10000-line
    batch-chunked volume tier) to avoid colliding with that already-shipped
    concept — see docs/use-cases/59-realtime-log-watch.md. This class does
    not itself watch or buffer logs; it summarizes the sampled lines
    collected by application/service/watch_pod_logs_service.py after a
    live kubernetes.watch.Watch session ends.
    """

    def supports(self, context: LogAnalysisContext) -> bool:
        return context.request_type == "realtime_watch"

    def analyze(self, logs: list[str], context: LogAnalysisContext) -> LogAnalysisResult:
        if not logs:
            return LogAnalysisResult(
                summary="No log data to analyze.",
                strategy_used="realtime_watch",
            )

        classifications = extract_error_patterns(logs)
        severity = self._count_severity(logs)
        patterns = [c.pattern for c in classifications]

        if classifications:
            top = classifications[0]
            summary = (
                f"Observed {len(logs)} sampled lines; top recurring pattern: "
                f"'{top.pattern}' ({top.count}x)."
            )
            total_matches = sum(c.count for c in classifications)
            confidence = min(0.95, 0.6 + 0.01 * total_matches)
        else:
            summary = f"Observed {len(logs)} sampled lines; no recurring error patterns detected."
            confidence = 0.6

        return LogAnalysisResult(
            summary=summary,
            patterns=patterns,
            severity=severity,
            confidence=confidence,
            strategy_used="realtime_watch",
        )


class StrategySelector:
    """Selects the appropriate log analysis strategy for a given context.

    Iterates through registered strategies and picks the first that
    supports the context. Order matters: more specific strategies
    should be checked first.
    """

    _strategies: list[LogAnalysisStrategy] = [
        HybridStrategy(),
        StreamingStrategy(),
        SmartSummaryStrategy(),
    ]

    @classmethod
    def select(cls, context: LogAnalysisContext) -> LogAnalysisStrategy:
        for strategy in cls._strategies:
            if strategy.supports(context):
                return strategy
        return SmartSummaryStrategy()
