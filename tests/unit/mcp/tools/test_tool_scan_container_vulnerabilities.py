"""Unit tests for MCP tool: scan_container_vulnerabilities."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestScanContainerVulnerabilitiesTool:
    def test_scan_container_vulnerabilities_returns_dict(self) -> None:
        from hexawyn.mcp.tools.scan_container_vulnerabilities import scan_container_vulnerabilities

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_image_inventory_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_image_vulnerability_scan_adapter",
                return_value=MagicMock(),
            ),
        ):
            result = scan_container_vulnerabilities()

        assert isinstance(result, dict)

    def test_scan_container_vulnerabilities_handles_error(self) -> None:
        from hexawyn.mcp.tools.scan_container_vulnerabilities import scan_container_vulnerabilities

        with (
            patch(
                "hexawyn.mcp.server.build_image_inventory_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_image_vulnerability_scan_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = scan_container_vulnerabilities()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.scan_container_vulnerabilities")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
