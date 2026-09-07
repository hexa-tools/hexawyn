"""Unit tests for generate_summary — deterministic stand-in for LLM summarization.

Note: this repo makes no real LLM API call (see docs/use-cases/58-hybrid-log-analysis.md).
generate_summary is the isolated seam where a real Anthropic/local-model adapter
would plug in later.
"""

from __future__ import annotations

from hexawyn.domain.services.log_analysis.summarizer import generate_summary


class TestGenerateSummaryWithPatterns:
    def test_summarizes_top_recurring_pattern(self) -> None:
        reduced_lines = [
            "[45x] refused to redis:6379 — e.g. 'Error: connection refused to redis:6379'",
            "[3x] timeout to postgres — e.g. 'Error: timeout to postgres'",
        ]

        summary, degraded = generate_summary(reduced_lines, severity="high")

        assert degraded is False
        assert "45" in summary
        assert "refused" in summary

    def test_critical_severity_uses_urgent_language(self) -> None:
        reduced_lines = ["[10x] OOMKilled container — e.g. 'Error: OOMKilled container api'"]

        summary, _ = generate_summary(reduced_lines, severity="critical")

        assert "immediate" in summary.lower()


class TestGenerateSummaryNoAnomalies:
    """TC2: 0 errors detected by pattern extractor → summarizer confirms no anomalies."""

    def test_healthy_sample_confirms_no_anomalies(self) -> None:
        reduced_lines = ["pod scheduled successfully", "readiness probe succeeded"]

        summary, degraded = generate_summary(reduced_lines, severity="low")

        assert degraded is False
        assert "no anomalies" in summary.lower()


class TestGenerateSummaryDegraded:
    """TC3 analog: nothing to summarize → pattern-only fallback with warning flag."""

    def test_empty_input_is_degraded(self) -> None:
        summary, degraded = generate_summary([], severity="low")

        assert degraded is True
        assert len(summary) > 0


class TestGenerateSummaryUnrecognizedFormat:
    """TC4: unrecognized log format still gets a reduced-context summary."""

    def test_unrecognized_format_still_produces_summary(self) -> None:
        reduced_lines = [f"random unstructured line {i}" for i in range(10)]

        summary, degraded = generate_summary(reduced_lines, severity="low")

        assert degraded is False
        assert len(summary) > 0

    def test_high_severity_hint(self) -> None:
        reduced_lines = [
            "[5x] timeout to postgres — e.g. 'Error: timeout to postgres'",
        ]
        summary, _ = generate_summary(reduced_lines, severity="high")
        assert "worth investigating" in summary.lower()

    def test_low_severity_hint(self) -> None:
        reduced_lines = [
            "[1x] minor warning — e.g. 'Warning: deprecated API call'",
        ]
        summary, _ = generate_summary(reduced_lines, severity="low")
        assert "monitor for recurrence" in summary.lower()
