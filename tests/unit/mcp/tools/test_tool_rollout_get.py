"""Unit tests for MCP tool: rollout_get."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRolloutGetTool:
    def test_rollout_get_returns_dict(self) -> None:
        from hexawyn.mcp.tools.rollout_get import rollout_get

        mock_response = MagicMock()
        mock_response.name = "test-rollout"
        mock_response.namespace = "test-ns"
        mock_response.strategy = "canary"
        mock_response.phase = "Progressing"
        mock_response.desired_replicas = 2
        mock_response.ready_replicas = 1
        mock_response.canary_replicas = 1
        mock_response.stable_replicas = 1
        mock_response.current_image = "img:v1"
        mock_response.stable_image = "img:v0"
        mock_response.step_index = 1
        mock_response.total_steps = 3
        mock_response.current_step_type = "pause"
        mock_response.canary_weight = 30
        mock_response.paused_at = None
        mock_response.pause_reason = None
        mock_response.message = ""
        mock_response.analysis_run_name = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_rollouts_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.rollout_get.RolloutGetUseCase",
                return_value=mock_uc,
            ),
        ):
            result = rollout_get("test-rollout", "test-ns")

        assert isinstance(result, dict)
        assert result["name"] == "test-rollout"

    def test_rollout_get_handles_error(self) -> None:
        from hexawyn.mcp.tools.rollout_get import rollout_get

        with patch(
            "hexawyn.mcp.server.build_rollouts_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = rollout_get("test-rollout", "test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.rollout_get")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
