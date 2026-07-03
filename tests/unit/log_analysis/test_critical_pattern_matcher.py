"""Unit tests for match_critical_pattern — deterministic OOM/DB/panic classifier."""

from __future__ import annotations

from hexawyn.domain.services.log_analysis.critical_pattern_matcher import (
    match_critical_pattern,
)


class TestMatchCriticalPatternOOM:
    def test_oomkilled_matches(self) -> None:
        match = match_critical_pattern(
            "OOMKilled: memory limit exceeded", pod_name="payment-service-7f9b"
        )
        assert match is not None
        assert match.category == "oom"
        assert match.pod_name == "payment-service-7f9b"
        assert match.log_line == "OOMKilled: memory limit exceeded"

    def test_out_of_memory_matches(self) -> None:
        match = match_critical_pattern("Error: out of memory", pod_name="p")
        assert match is not None
        assert match.category == "oom"


class TestMatchCriticalPatternDbConnection:
    def test_connection_refused_matches(self) -> None:
        match = match_critical_pattern(
            "dial tcp 10.0.0.5:5432: connect: connection refused", pod_name="p"
        )
        assert match is not None
        assert match.category == "db_connection_error"

    def test_could_not_connect_matches(self) -> None:
        match = match_critical_pattern("could not connect to postgres server", pod_name="p")
        assert match is not None
        assert match.category == "db_connection_error"


class TestMatchCriticalPatternPanic:
    def test_panic_matches(self) -> None:
        match = match_critical_pattern("panic: runtime error: invalid memory address", pod_name="p")
        assert match is not None
        assert match.category == "panic"

    def test_traceback_matches(self) -> None:
        match = match_critical_pattern("Traceback (most recent call last):", pod_name="p")
        assert match is not None
        assert match.category == "panic"

    def test_segfault_matches(self) -> None:
        match = match_critical_pattern("Segmentation fault (core dumped)", pod_name="p")
        assert match is not None
        assert match.category == "panic"


class TestMatchCriticalPatternNoMatch:
    def test_healthy_line_does_not_match(self) -> None:
        assert match_critical_pattern("pod scheduled successfully", pod_name="p") is None

    def test_case_insensitive(self) -> None:
        match = match_critical_pattern("error: OUT OF MEMORY detected", pod_name="p")
        assert match is not None
        assert match.category == "oom"

    def test_timestamp_defaults_to_empty_string(self) -> None:
        match = match_critical_pattern("OOMKilled", pod_name="p")
        assert match is not None
        assert match.timestamp == ""

    def test_explicit_timestamp_passed_through(self) -> None:
        match = match_critical_pattern("OOMKilled", pod_name="p", timestamp="T1")
        assert match is not None
        assert match.timestamp == "T1"
