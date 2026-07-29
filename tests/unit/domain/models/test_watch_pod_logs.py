"""Unit tests for watch_pod_logs domain models (pure dataclasses)."""

from __future__ import annotations

import dataclasses

from hexawyn.domain.models.analyze_pod_logs import LogPatternMatch
from hexawyn.domain.models.watch_pod_logs import (
    CriticalMatch,
    WatchPodLogsRequest,
    WatchPodLogsResult,
)


class TestCriticalMatch:
    def test_fields(self) -> None:
        match = CriticalMatch(
            category="oom",
            pattern="oomkilled",
            log_line="OOMKilled: memory limit exceeded",
            timestamp="2024-01-01T00:00:00Z",
            pod_name="payment-service-7f9b",
        )
        assert match.category == "oom"
        assert match.pod_name == "payment-service-7f9b"

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(CriticalMatch)


class TestWatchPodLogsRequest:
    def test_defaults(self) -> None:
        req = WatchPodLogsRequest(pod_name="payment-service-7f9b", namespace="prod")
        assert req.timeout_seconds == 300  # noqa: PLR2004
        assert req.max_reconnect_attempts == 3  # noqa: PLR2004
        assert req.sample_rate == 100  # noqa: PLR2004

    def test_explicit_values(self) -> None:
        req = WatchPodLogsRequest(
            pod_name="p",
            namespace="ns",
            timeout_seconds=10,
            max_reconnect_attempts=1,
            sample_rate=5,
        )
        assert req.timeout_seconds == 10  # noqa: PLR2004
        assert req.max_reconnect_attempts == 1
        assert req.sample_rate == 5  # noqa: PLR2004


class TestWatchPodLogsResult:
    def test_fields(self) -> None:
        result = WatchPodLogsResult(
            pod_name="payment-service-7f9b",
            namespace="prod",
            stop_reason="timeout",
            alerts=[
                CriticalMatch(
                    category="oom",
                    pattern="oomkilled",
                    log_line="OOMKilled: memory limit exceeded",
                    timestamp="T1",
                    pod_name="payment-service-7f9b",
                )
            ],
            lines_observed=501,
            lines_sampled=6,
            reconnect_count=0,
            summary="1 critical alert detected",
            patterns=[LogPatternMatch(pattern="oomkilled", count=1, confidence=0.9)],
            confidence=0.9,
        )
        assert result.stop_reason == "timeout"
        assert len(result.alerts) == 1
        assert result.lines_observed == 501  # noqa: PLR2004

    def test_defaults(self) -> None:
        result = WatchPodLogsResult(
            pod_name="p",
            namespace="ns",
            stop_reason="session_ended",
            lines_observed=0,
            lines_sampled=0,
            reconnect_count=0,
        )
        assert result.alerts == []
        assert result.patterns == []
        assert result.confidence == 0.0
        assert result.summary == ""

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(WatchPodLogsResult)
