"""Unit tests for MCP tool: detect_zombies."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectZombiesTool:
    def test_detect_zombies_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_zombies import detect_zombies

        mock_candidate = MagicMock()
        mock_candidate.pod_name = "zombie-pod"
        mock_candidate.namespace = "test-ns"
        mock_candidate.age_days = 30.0
        mock_candidate.traffic_rps = 0.0
        mock_candidate.cpu_cores = 0.5
        mock_candidate.memory_gb = 1.0
        mock_candidate.risk = "high"
        mock_candidate.reason = "idle"

        mock_result = MagicMock()
        mock_result.analysis_window_hours = 24
        mock_result.zombie_candidates = [mock_candidate]
        mock_result.total_wasted_cores = 0.5
        mock_result.total_wasted_gb = 1.0
        mock_result.prometheus_available = True
        mock_result.data_source = "prometheus"

        mock_response = MagicMock()
        mock_response.result = mock_result
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_zombie_detection_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.detect_zombies.DetectZombiesUseCase",
                return_value=mock_uc,
            ),
        ):
            result = detect_zombies()

        assert isinstance(result, dict)
        assert result["zombie_count"] == 1

    def test_detect_zombies_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_zombies import detect_zombies

        with patch(
            "hexawyn.mcp.server.build_zombie_detection_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = detect_zombies()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_zombies")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
