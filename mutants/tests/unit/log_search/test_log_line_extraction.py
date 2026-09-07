"""Unit tests for extract_matching_lines — pure log-line extraction logic."""

from __future__ import annotations

from hexawyn.domain.services.log_search.log_line_extraction import extract_matching_lines
from hexawyn.domain.services.log_search.pattern_matcher import compile_pattern

_THRESHOLD = 0.5


class TestExactMatches:
    def test_matches_capped_at_max_lines(self) -> None:
        pattern = compile_pattern("ERROR", is_regex=False)
        raw_lines = [f"2024-01-01T10:00:0{i}Z ERROR line {i}" for i in range(10)]

        matches = extract_matching_lines(
            pattern, "ERROR", raw_lines, max_lines=5, semantic_threshold=_THRESHOLD
        )

        assert len(matches) == 5  # noqa: PLR2004
        assert all(match.match_type == "exact" for match in matches)

    def test_timestamp_split_from_k8s_prefix(self) -> None:
        pattern = compile_pattern("connection refused", is_regex=False)
        raw_lines = ["2024-01-01T10:32:15.123456789Z ERROR: connection refused to postgres"]

        matches = extract_matching_lines(
            pattern, "connection refused", raw_lines, max_lines=5, semantic_threshold=_THRESHOLD
        )

        assert matches[0].timestamp == "2024-01-01T10:32:15.123456789Z"
        assert matches[0].message == "ERROR: connection refused to postgres"

    def test_no_exact_match_returns_empty_without_lines(self) -> None:
        pattern = compile_pattern("connection refused", is_regex=False)
        raw_lines = ["2024-01-01T10:00:00Z heartbeat ok"]

        matches = extract_matching_lines(
            pattern, "connection refused", raw_lines, max_lines=5, semantic_threshold=0.99
        )

        assert matches == []


class TestSemanticFallback:
    def test_semantic_fallback_when_no_exact_match(self) -> None:
        pattern = compile_pattern("connection refused to postgres", is_regex=False)
        raw_lines = [
            "2024-01-01T10:00:00Z heartbeat ok seq=1",
            "2024-01-01T10:00:01Z connection reset by postgres peer",
        ]

        matches = extract_matching_lines(
            pattern,
            "connection refused to postgres",
            raw_lines,
            max_lines=5,
            semantic_threshold=0.3,
        )

        assert len(matches) == 1
        assert matches[0].match_type == "semantic"
        assert "postgres" in matches[0].message

    def test_no_semantic_fallback_below_threshold(self) -> None:
        pattern = compile_pattern("connection refused to postgres", is_regex=False)
        raw_lines = ["2024-01-01T10:00:00Z heartbeat ok seq=1"]

        matches = extract_matching_lines(
            pattern,
            "connection refused to postgres",
            raw_lines,
            max_lines=5,
            semantic_threshold=0.9,
        )

        assert matches == []

    def test_exact_match_takes_priority_over_semantic(self) -> None:
        pattern = compile_pattern("connection refused", is_regex=False)
        raw_lines = [
            "2024-01-01T10:00:00Z connection reset (similar)",
            "2024-01-01T10:00:01Z connection refused (exact)",
        ]

        matches = extract_matching_lines(
            pattern, "connection refused", raw_lines, max_lines=5, semantic_threshold=0.3
        )

        assert len(matches) == 1
        assert matches[0].match_type == "exact"
        assert "exact" in matches[0].message
