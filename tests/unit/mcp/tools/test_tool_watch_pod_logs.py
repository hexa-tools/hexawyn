"""Unit tests for MCP tool: watch_pod_logs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestWatchPodLogsTool:
    def test_watch_pod_logs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.watch_pod_logs import watch_pod_logs

        with patch(
            "hexawyn.mcp.server.build_alert_notification_adapter",
            return_value=MagicMock(),
        ):
            result = watch_pod_logs()

        assert isinstance(result, dict)
        assert "error" in result

    def test_watch_pod_logs_handles_error(self) -> None:
        from hexawyn.mcp.tools.watch_pod_logs import watch_pod_logs

        with patch(
            "hexawyn.mcp.server.build_alert_notification_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = watch_pod_logs()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_watch_pod_logs_success_path(self) -> None:
        from hexawyn.mcp.tools.watch_pod_logs import watch_pod_logs

        with (
            patch(
                "hexawyn.mcp.server.build_alert_notification_adapter",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.tools.watch_pod_logs.WatchPodLogsUseCase") as mock_uc,
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = watch_pod_logs()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.watch_pod_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
