"""Unit tests for MCP tool: search_resources_by_labels."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSearchResourcesByLabelsTool:
    def test_search_resources_by_labels_returns_dict(self) -> None:
        from hexawyn.mcp.tools.search_resources_by_labels import search_resources_by_labels

        with patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()):
            result = search_resources_by_labels()

        assert isinstance(result, dict)
        assert "error" in result

    def test_search_resources_by_labels_handles_error(self) -> None:
        from hexawyn.mcp.tools.search_resources_by_labels import search_resources_by_labels

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = search_resources_by_labels()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_search_resources_by_labels_success_path(self) -> None:
        from hexawyn.mcp.tools.search_resources_by_labels import search_resources_by_labels

        with (
            patch(
                "hexawyn.mcp.server.build_k8s_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.search_resources_by_labels.SearchResourcesByLabelsUseCase"
            ) as mock_uc,
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = search_resources_by_labels()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.search_resources_by_labels")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
