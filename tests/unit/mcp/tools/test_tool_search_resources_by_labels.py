"""Unit tests for MCP tool: search_resources_by_labels."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSearchResourcesByLabelsTool:
    def test_search_resources_by_labels_returns_dict(self) -> None:
        from hexawyn.mcp.tools.search_resources_by_labels import search_resources_by_labels

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_resource_search_adapter", return_value=MagicMock()),
        ):
            result = search_resources_by_labels(label_selector="test")

        assert isinstance(result, dict)

    def test_search_resources_by_labels_handles_error(self) -> None:
        from hexawyn.mcp.tools.search_resources_by_labels import search_resources_by_labels

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch(
                "hexawyn.mcp.server.build_resource_search_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = search_resources_by_labels(label_selector="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.search_resources_by_labels")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
