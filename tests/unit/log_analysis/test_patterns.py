"""Unit tests for categorize_connection_issues (connection timeout/refused extraction)."""

from __future__ import annotations

from hexawyn.domain.models.analyze_pod_logs import PodLogLine
from hexawyn.domain.services.log_analysis.patterns import categorize_connection_issues


def _line(message: str) -> PodLogLine:
    return PodLogLine(timestamp="T1", level="ERROR", message=message, run_index=0, is_json=False)


class TestCategorizeConnectionIssues:
    def test_extracts_connection_timeouts(self) -> None:
        lines = [_line("connection timeout to postgres:5432") for _ in range(15)]
        timeouts, refused = categorize_connection_issues(lines)
        assert len(timeouts) == 1
        assert timeouts[0].category == "connection_timeout"
        assert timeouts[0].count == 15
        assert refused == []

    def test_extracts_connection_refused(self) -> None:
        lines = [_line("upstream connect error") for _ in range(3)]
        timeouts, refused = categorize_connection_issues(lines)
        assert timeouts == []
        assert len(refused) == 1
        assert refused[0].category == "connection_refused"
        assert refused[0].count == 3

    def test_separates_timeouts_and_refused(self) -> None:
        lines = [_line("connection timeout to postgres:5432") for _ in range(15)] + [
            _line("upstream connect error") for _ in range(3)
        ]
        timeouts, refused = categorize_connection_issues(lines)
        assert timeouts[0].count == 15
        assert refused[0].count == 3

    def test_ignores_unrelated_lines(self) -> None:
        lines = [_line("pod scheduled successfully"), _line("readiness probe succeeded")]
        timeouts, refused = categorize_connection_issues(lines)
        assert timeouts == []
        assert refused == []

    def test_empty_input_returns_empty_lists(self) -> None:
        timeouts, refused = categorize_connection_issues([])
        assert timeouts == []
        assert refused == []

    def test_confidence_increases_with_count(self) -> None:
        few = [_line("connection refused") for _ in range(1)]
        many = [_line("connection refused") for _ in range(20)]
        _, refused_few = categorize_connection_issues(few)
        _, refused_many = categorize_connection_issues(many)
        assert refused_many[0].confidence > refused_few[0].confidence

    def test_confidence_capped_at_one(self) -> None:
        lines = [_line("connection refused") for _ in range(100)]
        _, refused = categorize_connection_issues(lines)
        assert refused[0].confidence == 1.0

    def test_dial_tcp_refused_variant_categorized(self) -> None:
        lines = [_line("dial tcp 10.0.0.5:5432: connect: connection refused")]
        _, refused = categorize_connection_issues(lines)
        assert len(refused) == 1

    def test_case_insensitive_matching(self) -> None:
        lines = [_line("Connection Timeout to postgres:5432")]
        timeouts, _ = categorize_connection_issues(lines)
        assert len(timeouts) == 1
