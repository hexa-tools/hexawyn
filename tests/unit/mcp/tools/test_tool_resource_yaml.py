"""Unit tests for MCP tool: resource_yaml."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestResourceYamlTool:
    def test_resource_yaml_returns_dict(self) -> None:
        from hexawyn.mcp.tools.resource_yaml import resource_yaml

        mock_response = MagicMock()
        mock_response.resource_name = "test-pod"
        mock_response.namespace = "test-ns"
        mock_response.kind = "Pod"
        mock_response.resource_found = True
        mock_response.yaml_data = "---"
        mock_response.image_tags = []
        mock_response.resource_limits = {}
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_resource_yaml_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.resource_yaml.ResourceYAMLUseCase",
                return_value=mock_uc,
            ),
        ):
            result = resource_yaml("test-pod", "test-ns", "Pod")

        assert isinstance(result, dict)
        assert result["resource_name"] == "test-pod"

    def test_resource_yaml_handles_error(self) -> None:
        from hexawyn.mcp.tools.resource_yaml import resource_yaml

        with patch(
            "hexawyn.mcp.server.build_resource_yaml_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = resource_yaml("test-pod", "test-ns", "Pod")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.resource_yaml")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
