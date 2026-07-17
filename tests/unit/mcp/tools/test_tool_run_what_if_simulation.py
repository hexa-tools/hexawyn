"""Unit tests for MCP tool: run_what_if_simulation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRunWhatIfSimulationTool:
    def test_run_what_if_simulation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.run_what_if_simulation import run_what_if_simulation

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_what_if_simulation_adapter", return_value=MagicMock()),
        ):
            result = run_what_if_simulation(
                target_service="test-target_service", namespace="test-ns", proposed_replicas="test"
            )

        assert isinstance(result, dict)

    def test_run_what_if_simulation_handles_error(self) -> None:
        from hexawyn.mcp.tools.run_what_if_simulation import run_what_if_simulation

        with (
            patch(
                "hexawyn.mcp.server.build_what_if_simulation_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = run_what_if_simulation(
                target_service="test-target_service", namespace="test-ns", proposed_replicas="test"
            )

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.run_what_if_simulation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
