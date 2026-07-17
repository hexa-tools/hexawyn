"""Unit tests for MCP tool: rollout_status."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRolloutStatusTool:
    def test_rollout_status_returns_dict(self) -> None:
        from hexawyn.mcp.tools.rollout_status import rollout_status

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_rollouts_adapter", return_value=MagicMock()),
        ):
            result = rollout_status(name="test-name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_rollout_status_handles_error(self) -> None:
        from hexawyn.mcp.tools.rollout_status import rollout_status

        with (
            patch(
                "hexawyn.mcp.server.build_rollouts_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = rollout_status(name="test-name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.rollout_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
