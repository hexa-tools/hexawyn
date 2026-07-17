"""Unit tests for MCP tool: detect_outdated_helm_releases."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectOutdatedHelmReleasesTool:
    def test_detect_outdated_helm_releases_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_outdated_helm_releases import detect_outdated_helm_releases

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_helm_release_version_adapter", return_value=MagicMock()
            ),
        ):
            result = detect_outdated_helm_releases()

        assert isinstance(result, dict)

    def test_detect_outdated_helm_releases_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_outdated_helm_releases import detect_outdated_helm_releases

        with (
            patch(
                "hexawyn.mcp.server.build_helm_release_version_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_outdated_helm_releases()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_outdated_helm_releases")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
