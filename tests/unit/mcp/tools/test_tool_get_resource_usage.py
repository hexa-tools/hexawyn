"""Unit tests for MCP tool: get_resource_usage."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetResourceUsageTool:
    def test_get_resource_usage_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_resource_usage import get_resource_usage

        mock_response = MagicMock()
        mock_response.pods = []
        mock_response.namespace_summary = []
        mock_response.metrics_server_available = True
        mock_response.source = "metrics-server"
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pod_metrics_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_resource_usage.GetResourceUsageUseCase", return_value=mock_uc
            ),
        ):
            result = get_resource_usage()

        assert isinstance(result, dict)
        assert "pods" in result
        assert "namespace_summary" in result
        assert "metrics_server_available" in result

    def test_get_resource_usage_handles_error(self) -> None:
        from hexawyn.mcp.tools.get_resource_usage import get_resource_usage

        with patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")):
            result = get_resource_usage()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_get_resource_usage_with_namespace_filter(self) -> None:
        from hexawyn.mcp.tools.get_resource_usage import get_resource_usage

        mock_response = MagicMock()
        mock_response.pods = []
        mock_response.namespace_summary = []
        mock_response.metrics_server_available = True
        mock_response.source = "metrics-server"
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pod_metrics_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_resource_usage.GetResourceUsageUseCase", return_value=mock_uc
            ),
        ):
            result = get_resource_usage(namespace="dev")

        assert result.get("error") is None

    def test_get_resource_usage_with_resource_filter(self) -> None:
        from hexawyn.mcp.tools.get_resource_usage import get_resource_usage

        mock_response = MagicMock()
        mock_response.pods = []
        mock_response.namespace_summary = []
        mock_response.metrics_server_available = True
        mock_response.source = "metrics-server"
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pod_metrics_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_resource_usage.GetResourceUsageUseCase", return_value=mock_uc
            ),
        ):
            result = get_resource_usage(resource="cpu")

        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_resource_usage")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
