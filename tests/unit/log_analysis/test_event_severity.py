"""Unit tests for classify_event_severity and the severity ordering used to rank events."""

from __future__ import annotations

from hexawyn.domain.services.log_analysis.event_severity import (
    SEVERITY_ORDER,
    classify_event_severity,
)


class TestClassifyEventSeverityCritical:
    def test_panic_is_critical(self) -> None:
        assert classify_event_severity("panic: runtime error") == "critical"

    def test_fatal_is_critical(self) -> None:
        assert classify_event_severity("fatal error occurred") == "critical"

    def test_oomkilled_is_critical(self) -> None:
        assert classify_event_severity("OOMKilled: memory limit exceeded") == "critical"

    def test_segfault_is_critical(self) -> None:
        assert classify_event_severity("segmentation fault (core dumped)") == "critical"


class TestClassifyEventSeverityHigh:
    def test_error_is_high(self) -> None:
        assert classify_event_severity("Error: connection refused") == "high"


class TestClassifyEventSeverityMedium:
    def test_warning_is_medium(self) -> None:
        assert classify_event_severity("Warning: eviction threshold reached") == "medium"

    def test_warn_is_medium(self) -> None:
        assert classify_event_severity("WARN: disk usage high") == "medium"


class TestClassifyEventSeverityInfo:
    def test_default_is_info(self) -> None:
        assert classify_event_severity("POST /api/orders HTTP/1.1 201") == "info"

    def test_case_insensitive(self) -> None:
        assert classify_event_severity("PANIC: nil pointer") == "critical"


class TestSeverityOrder:
    def test_critical_ranks_above_high(self) -> None:
        assert SEVERITY_ORDER["critical"] > SEVERITY_ORDER["high"]

    def test_high_ranks_above_medium(self) -> None:
        assert SEVERITY_ORDER["high"] > SEVERITY_ORDER["medium"]

    def test_medium_ranks_above_info(self) -> None:
        assert SEVERITY_ORDER["medium"] > SEVERITY_ORDER["info"]
