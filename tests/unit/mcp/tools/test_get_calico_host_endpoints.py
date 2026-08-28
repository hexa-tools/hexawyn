"""Unit tests for MCP tool: get_calico_host_endpoints."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetCalicoHostEndpointsTool:
    def test_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_calico_host_endpoints import get_calico_host_endpoints

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.total = 1
        mock_response.endpoints = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_calico_host_endpoints.GetCalicoHostEndpointsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = get_calico_host_endpoints()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["total"] == 1  # noqa: PLR2004
        assert result["error"] is None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.get_calico_host_endpoints import get_calico_host_endpoints

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = get_calico_host_endpoints()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_calico_host_endpoints")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_endpoint_dict(self) -> None:
        from hexawyn.domain.models.calico import CalicoHostEndpoint
        from hexawyn.mcp.tools.get_calico_host_endpoints import _endpoint_dict

        endpoint = CalicoHostEndpoint(
            name="he",
            node="node-1",
            interface_name="eth0",
            expected_ip="10.0.0.1",
            expected_ips=("10.0.0.1",),
            labels=(("kubernetes.io/hostname", "node-1"),),
            applied_policies=("default.host-endpoints",),
        )
        result = _endpoint_dict(endpoint)

        assert result["name"] == "he"
        assert result["applied_policies"] == ["default.host-endpoints"]
        assert result["labels"] == [["kubernetes.io/hostname", "node-1"]]
        assert result["expected_ips"] == ["10.0.0.1"]
