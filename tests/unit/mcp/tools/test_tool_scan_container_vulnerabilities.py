"""Unit tests for MCP tool: scan_container_vulnerabilities."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestScanContainerVulnerabilitiesTool:
    def test_scan_container_vulnerabilities_returns_dict(self) -> None:
        from hexawyn.mcp.tools.scan_container_vulnerabilities import (
            scan_container_vulnerabilities,
        )

        with patch(
            "hexawyn.mcp.server.build_image_inventory_adapter",
            return_value=MagicMock(),
        ):
            result = scan_container_vulnerabilities()

        assert isinstance(result, dict)
        assert "error" in result

    def test_scan_container_vulnerabilities_handles_error(self) -> None:
        from hexawyn.mcp.tools.scan_container_vulnerabilities import (
            scan_container_vulnerabilities,
        )

        with patch(
            "hexawyn.mcp.server.build_image_inventory_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = scan_container_vulnerabilities()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_scan_container_vulnerabilities_success_path(self) -> None:
        from hexawyn.mcp.tools.scan_container_vulnerabilities import (
            scan_container_vulnerabilities,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_image_inventory_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.scan_container_vulnerabilities.ScanContainerVulnerabilitiesUseCase"
            ) as mock_uc,
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = scan_container_vulnerabilities()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.scan_container_vulnerabilities")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
