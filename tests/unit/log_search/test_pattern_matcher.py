"""Unit tests for compile_pattern / similarity_score — pure pattern-matching logic."""

from __future__ import annotations

import re

import pytest
from hexawyn.domain.errors import LogPatternError
from hexawyn.domain.services.log_search.pattern_matcher import (
    compile_pattern,
    similarity_score,
)


class TestCompilePatternLiteral:
    def test_literal_substring_matches(self) -> None:
        pattern = compile_pattern("connection refused to postgres", is_regex=False)
        assert pattern.search("ERROR: connection refused to postgres at 10:32:15")

    def test_special_characters_escaped(self) -> None:
        """Edge case: pattern is a literal string with regex special chars."""
        pattern = compile_pattern("version=1.2.3", is_regex=False)
        assert pattern.search("app version=1.2.3 started")
        assert pattern.search("app version=1X2Y3 started") is None

    def test_parentheses_escaped(self) -> None:
        pattern = compile_pattern("connection refused (postgres)", is_regex=False)
        assert pattern.search("connection refused (postgres) at retry 3")
        assert pattern.search("connection refused Xpostgres at retry 3") is None


class TestCompilePatternRegex:
    def test_regex_mode_compiles_as_is(self) -> None:
        pattern = compile_pattern(r"connection refused.*postgres", is_regex=True)
        assert pattern.search("connection refused: cannot reach postgres")

    def test_invalid_regex_raises(self) -> None:
        with pytest.raises(LogPatternError):
            compile_pattern("foo(", is_regex=True)


class TestSimilarityScore:
    def test_identical_strings_score_one(self) -> None:
        assert similarity_score("connection refused", "connection refused") == 1.0

    def test_similar_strings_score_high(self) -> None:
        score = similarity_score(
            "connection refused to postgres", "connection reset by postgres peer"
        )
        assert 0.4 < score < 1.0  # noqa: PLR2004

    def test_unrelated_strings_score_low(self) -> None:
        score = similarity_score("connection refused to postgres", "heartbeat ok seq=42")
        assert score < 0.3  # noqa: PLR2004


def test_compile_pattern_returns_real_pattern_object() -> None:
    assert isinstance(compile_pattern("foo", is_regex=False), re.Pattern)
