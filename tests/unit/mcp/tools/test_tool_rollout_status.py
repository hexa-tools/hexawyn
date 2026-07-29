"""Unit tests for MCP tool: rollout_status."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRolloutStatusTool:
    def test_rollout_status_returns_dict(self) -> None:
        from hexawyn.mcp.tools.rollout_status import rollout_status

        with patch("hexawyn.mcp.server.build_rollouts_adapter", return_value=MagicMock()):
            result = rollout_status()

        assert isinstance(result, dict)
        assert "error" in result

    def test_rollout_status_handles_error(self) -> None:
        from hexawyn.mcp.tools.rollout_status import rollout_status

        with patch(
            "hexawyn.mcp.server.build_rollouts_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = rollout_status()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_rollout_status_success_path(self) -> None:
        from hexawyn.mcp.tools.rollout_status import rollout_status

        with (
            patch(
                "hexawyn.mcp.server.build_rollouts_adapter",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.tools.rollout_status.RolloutStatusUseCase"),
            patch("hexawyn.mcp.tools.rollout_status.RolloutStatusCommand"),
        ):
            result = rollout_status()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.rollout_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
