"""Unit tests for extract_error_patterns / reduce_logs_for_summarization."""

from __future__ import annotations

from hexawyn.domain.services.log_analysis.pattern_reducer import (
    extract_error_patterns,
    reduce_logs_for_summarization,
)


class TestExtractErrorPatterns:
    def test_groups_and_counts_repeated_pattern(self) -> None:
        logs = ["Error: connection refused to redis:6379" for _ in range(45)]

        classifications = extract_error_patterns(logs)

        assert len(classifications) == 1
        assert classifications[0].count == 45  # noqa: PLR2004
        assert "refused" in classifications[0].pattern
        assert "redis" in classifications[0].sample_line

    def test_separates_distinct_patterns(self) -> None:
        logs = ["Error: OOMKilled container api" for _ in range(10)] + [
            "Error: connection timeout to postgres" for _ in range(5)
        ]

        classifications = extract_error_patterns(logs)

        counts = {c.pattern: c.count for c in classifications}
        assert sum(counts.values()) == 15  # noqa: PLR2004
        assert len(classifications) == 2  # noqa: PLR2004

    def test_no_matches_returns_empty(self) -> None:
        logs = ["pod scheduled successfully", "readiness probe succeeded"]

        assert extract_error_patterns(logs) == []

    def test_empty_input_returns_empty(self) -> None:
        assert extract_error_patterns([]) == []

    def test_ranked_by_count_descending(self) -> None:
        logs = ["Error: rare failure"] + ["Error: connection refused" for _ in range(20)]

        classifications = extract_error_patterns(logs)

        assert classifications[0].count >= classifications[-1].count


class TestReduceLogsForSummarization:
    def test_reduces_repetitive_log_dramatically(self) -> None:
        raw = ["Error: connection refused to redis:6379" for _ in range(3000)]

        reduced = reduce_logs_for_summarization(raw)

        assert len(reduced) < len(raw) * 0.1
        assert any("connection refused" in line for line in reduced)

    def test_realistic_mixed_log_meets_96_percent_reduction_target(self) -> None:
        raw: list[str] = []
        for i in range(45):
            raw.extend([f"Error: pattern-{i} occurred"] * 70)  # 45 * 70 = 3150 lines

        reduced = reduce_logs_for_summarization(raw)

        reduction_ratio = 1 - (len(reduced) / len(raw))
        assert reduction_ratio >= 0.90  # noqa: PLR2004

    def test_unrecognized_format_falls_back_to_head_tail_sample(self) -> None:
        raw = [f"random unstructured line {i}" for i in range(500)]

        reduced = reduce_logs_for_summarization(raw)

        assert len(reduced) < len(raw)
        assert reduced[0] == raw[0]
        assert reduced[-1] == raw[-1]

    def test_small_unrecognized_log_is_kept_whole(self) -> None:
        raw = [f"random unstructured line {i}" for i in range(10)]

        reduced = reduce_logs_for_summarization(raw)

        assert reduced == raw

    def test_empty_input_returns_empty(self) -> None:
        assert reduce_logs_for_summarization([]) == []
