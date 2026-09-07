"""Unit tests for MCP tool: etcd_logs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestEtcdLogsTool:
    def test_etcd_logs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.etcd_logs import etcd_logs

        mock_response = MagicMock()
        mock_response.etcd_accessible = True
        mock_response.total_log_lines = 10
        mock_response.error_count = 2
        mock_response.leader_election_count = 0
        mock_response.compaction_errors = 0
        mock_response.leader_instability = False
        mock_response.summary = "ok"
        mock_response.errors = []
        mock_response.error = None

        with (
            patch(
                "hexawyn.mcp.tools.etcd_logs.ETCDLogsUseCase",
                return_value=MagicMock(execute=MagicMock(return_value=mock_response)),
            ),
            patch("hexawyn.mcp.server.build_etcd_logs_adapter", return_value=MagicMock()),
        ):
            result = etcd_logs()

        assert isinstance(result, dict)
        assert result.get("etcd_accessible") is True
        assert result.get("error") is None

    def test_etcd_logs_handles_error(self) -> None:
        from hexawyn.mcp.tools.etcd_logs import etcd_logs

        with patch(
            "hexawyn.mcp.server.build_etcd_logs_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = etcd_logs()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.etcd_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
