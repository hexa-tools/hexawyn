from __future__ import annotations

from hexawyn.domain.models.etcd_logs import (
    ETCDLogLine,
    ETCDLogsRequest,
    ETCDLogsResult,
)


class TestETCDLogLine:
    def test_error(self) -> None:
        ll = ETCDLogLine(level="ERROR", message="mvcc: database space exceeded", timestamp="T1")
        assert ll.level == "ERROR"
        assert ll.is_error is True

    def test_info(self) -> None:
        ll = ETCDLogLine(level="INFO", message="compaction completed", timestamp="T2")
        assert ll.is_error is False


class TestETCDLogsResult:
    def test_leader_election_detected(self) -> None:
        lines = [
            ETCDLogLine(level="INFO", message="leader election started", timestamp="T1"),
            ETCDLogLine(level="INFO", message="leader election started", timestamp="T2"),
            ETCDLogLine(level="INFO", message="leader election started", timestamp="T3"),
            ETCDLogLine(level="ERROR", message="mvcc: database space exceeded", timestamp="T4"),
        ]
        result = ETCDLogsResult.compute(
            request=ETCDLogsRequest(time_window_minutes=60),
            log_lines=lines,
        )
        assert result.leader_election_count == 3
        assert result.compaction_errors > 0
        assert result.leader_instability is True

    def test_no_anomalies(self) -> None:
        lines = [
            ETCDLogLine(level="INFO", message="compaction completed", timestamp="T1"),
            ETCDLogLine(level="INFO", message="raft heartbeat", timestamp="T2"),
        ]
        result = ETCDLogsResult.compute(
            request=ETCDLogsRequest(time_window_minutes=60),
            log_lines=lines,
        )
        assert result.leader_election_count == 0
        assert result.leader_instability is False

    def test_etcd_not_accessible(self) -> None:
        result = ETCDLogsResult.compute(
            request=ETCDLogsRequest(time_window_minutes=60),
            log_lines=[],
        )
        assert result.etcd_accessible is False
