from hexawyn.domain.models.constants import LogAnalysisConstants
from hexawyn.domain.models.log import LogAnalysisContext, LogAnalysisResult
from hexawyn.domain.services.log_analysis.strategy_port import LogAnalysisStrategy

__all__ = [
    "LogAnalysisStrategy",
    "SmartSummaryStrategy",
    "StreamingStrategy",
    "HybridStrategy",
    "StrategySelector",
]

_log_constants = LogAnalysisConstants()


class SmartSummaryStrategy(LogAnalysisStrategy):
    """Summarizes log content — best for large logs in monitoring mode."""

    def supports(self, context: LogAnalysisContext) -> bool:
        if context.urgency == "critical" and context.time_sensitive:
            return False
        return context.log_size_estimate >= _log_constants.smart_summary_min_lines

    def analyze(self, logs: list[str], context: LogAnalysisContext) -> LogAnalysisResult:
        if not logs:
            return LogAnalysisResult(
                summary="No log data to analyze.",
                strategy_used="smart_summary",
            )

        error_count = sum(1 for line in logs if "error" in line.lower())
        warning_count = sum(1 for line in logs if "warning" in line.lower())
        total_lines = len(logs)

        patterns = self._extract_patterns(logs)
        severity = self._count_severity(logs)

        if error_count == 0 and warning_count == 0:
            summary = f"Analyzed {total_lines} log lines — no errors or warnings detected."
            confidence = 0.95
        elif error_count > total_lines * 0.1:
            summary = (
                f"High error rate: {error_count} errors in {total_lines} lines. "
                f"Top pattern: {patterns[0] if patterns else 'unknown'}."
            )
            confidence = 0.85
        else:
            summary = (
                f"Moderate activity: {error_count} errors, {warning_count} warnings "
                f"in {total_lines} lines."
            )
            confidence = 0.80

        recommendations = self._build_recommendations(patterns, severity)

        return LogAnalysisResult(
            summary=summary,
            patterns=patterns,
            recommendations=recommendations,
            severity=severity,
            confidence=confidence,
            strategy_used="smart_summary",
        )

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
    """Combines summary and streaming — best for deep investigations."""

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

        smart = SmartSummaryStrategy()
        streaming = StreamingStrategy()

        summary_result = smart.analyze(logs, context)
        stream_result = streaming.analyze(logs, context)

        combined_patterns = list(dict.fromkeys(summary_result.patterns + stream_result.patterns))[
            :5
        ]

        combined_recs = list(
            dict.fromkeys(summary_result.recommendations + stream_result.recommendations)
        )

        combined_summary = (
            f"[SUMMARY] {summary_result.summary} " f"[STREAM] {stream_result.summary}"
        )

        avg_confidence = (summary_result.confidence + stream_result.confidence) / 2

        return LogAnalysisResult(
            summary=combined_summary,
            patterns=combined_patterns,
            recommendations=combined_recs,
            severity=summary_result.severity,
            confidence=avg_confidence,
            strategy_used="hybrid",
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
