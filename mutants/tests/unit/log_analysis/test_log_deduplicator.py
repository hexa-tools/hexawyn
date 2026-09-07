"""Unit tests for deduplicate_lines — collapses repeated lines with counts."""

from __future__ import annotations

from hexawyn.domain.services.log_analysis.log_deduplicator import deduplicate_lines


class TestDeduplicateLines:
    def test_groups_identical_lines_with_count(self) -> None:
        logs = ["GET /health HTTP/1.1 200" for _ in range(1750)]

        deduped = deduplicate_lines(logs)

        assert len(deduped) == 1
        assert deduped[0].line == "GET /health HTTP/1.1 200"
        assert deduped[0].count == 1750  # noqa: PLR2004

    def test_line_repeated_10000_times_shows_once_with_count(self) -> None:
        """Edge case: log line repeated 10000 times -> shown once with count=10000."""
        logs = ["Error: connection refused" for _ in range(10000)]

        deduped = deduplicate_lines(logs)

        assert len(deduped) == 1
        assert deduped[0].count == 10000  # noqa: PLR2004

    def test_preserves_first_seen_order(self) -> None:
        logs = ["b", "a", "b", "c", "a"]

        deduped = deduplicate_lines(logs)

        assert [d.line for d in deduped] == ["b", "a", "c"]
        assert [d.count for d in deduped] == [2, 2, 1]

    def test_all_unique_lines_returns_all_with_count_one(self) -> None:
        logs = [f"event-{i}" for i in range(2000)]

        deduped = deduplicate_lines(logs)

        assert len(deduped) == 2000  # noqa: PLR2004
        assert all(d.count == 1 for d in deduped)

    def test_empty_input_returns_empty(self) -> None:
        assert deduplicate_lines([]) == []
