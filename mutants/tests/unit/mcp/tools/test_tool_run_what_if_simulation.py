"""Unit tests for MCP tool: run_what_if_simulation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRunWhatIfSimulationTool:
    def test_run_what_if_simulation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.run_what_if_simulation import run_what_if_simulation

        mock_response = MagicMock()
        mock_response.target_service = "test-svc"
        mock_response.namespace = "test-ns"
        mock_response.current_replicas = 2
        mock_response.proposed_replicas = 3
        mock_response.risk = "low"
        mock_response.risk_level = 1
        mock_response.affected_services = []
        mock_response.estimated_latency_increase_percent = 5.0
        mock_response.error_risk = "none"
        mock_response.pdb_violation = False
        mock_response.hpa_detected = False
        mock_response.circular_dependency = False
        mock_response.recommendation = "safe"
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_what_if_simulation_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.run_what_if_simulation.RunWhatIfSimulationUseCase",
                return_value=mock_uc,
            ),
        ):
            result = run_what_if_simulation("test-svc", "test-ns")

        assert isinstance(result, dict)
        assert result["target_service"] == "test-svc"

    def test_run_what_if_simulation_handles_error(self) -> None:
        from hexawyn.mcp.tools.run_what_if_simulation import run_what_if_simulation

        with patch(
            "hexawyn.mcp.server.build_what_if_simulation_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = run_what_if_simulation("test-svc", "test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.run_what_if_simulation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
