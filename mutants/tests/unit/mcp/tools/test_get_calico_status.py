"""Unit tests for MCP tool: get_calico_status."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetCalicoStatusTool:
    def test_get_calico_status_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_calico_status import get_calico_status

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.status = "installed"
        mock_response.ready_agents = 3
        mock_response.total_agents = 3
        mock_response.degraded_summary = None
        mock_response.agents = []
        mock_response.felix_errors = 0
        mock_response.felix_errors_available = True
        mock_response.connectivity_status = "healthy"
        mock_response.connectivity_available = True
        mock_response.connectivity_detail = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_calico_status.GetCalicoStatusUseCase",
                return_value=mock_uc,
            ),
        ):
            result = get_calico_status()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["status"] == "installed"
        assert result["ready_agents"] == 3  # noqa: PLR2004
        assert result["error"] is None

    def test_get_calico_status_handles_error(self) -> None:
        from hexawyn.mcp.tools.get_calico_status import get_calico_status

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = get_calico_status()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_calico_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_agent_dict_converts_phase(self) -> None:
        from hexawyn.domain.models.calico import CalicoAgentPhase, CalicoNodeAgent
        from hexawyn.mcp.tools.get_calico_status import _agent_dict

        agent = CalicoNodeAgent(
            node="n1",
            phase=CalicoAgentPhase.READY,
            ready=True,
            ready_replicas=1,
            desired_replicas=1,
            available_replicas=1,
        )
        result = _agent_dict(agent)

        assert result["node"] == "n1"
        assert result["phase"] == "ready"
        assert result["ready"] is True
