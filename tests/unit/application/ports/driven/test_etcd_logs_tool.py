from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
from hexawyn.domain.models.etcd_logs import ETCDLogLine


class TestETCDLogsTool:
    def test_returns_anomalies(self) -> None:
        from hexawyn.mcp.tools.etcd_logs import etcd_logs

        with patch("hexawyn.mcp.server.build_etcd_logs_adapter") as m:
            a = MagicMock(spec=ETCDLogsPort)
            a.fetch_logs.return_value = [
                ETCDLogLine(level="INFO", message="leader election started", timestamp="T1"),
                ETCDLogLine(level="INFO", message="leader election started", timestamp="T2"),
                ETCDLogLine(level="ERROR", message="mvcc: database space exceeded", timestamp="T3"),
            ]
            m.return_value = a
            r = etcd_logs(time_window_minutes=60)
        assert r["error"] is None
        assert r["leader_election_count"] == 2
        assert r["compaction_errors"] == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.etcd_logs import etcd_logs

        with patch("hexawyn.mcp.server.build_etcd_logs_adapter", side_effect=RuntimeError("boom")):
            r = etcd_logs()
        assert r["error"] == "boom"


class TestBuildETCDLogsAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
        from hexawyn.mcp.server import build_etcd_logs_adapter

        assert isinstance(build_etcd_logs_adapter(), ETCDLogsPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.etcd_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
