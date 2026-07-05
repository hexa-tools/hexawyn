from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestScanContainerVulnerabilitiesTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.scan_container_vulnerabilities import (
            scan_container_vulnerabilities,
        )

        with (
            patch("hexawyn.mcp.server.build_image_inventory_adapter") as build_inventory,
            patch("hexawyn.mcp.server.build_image_vulnerability_scan_adapter") as build_scanner,
        ):
            inventory_port = MagicMock()
            inventory_port.list_running_images.return_value = []
            build_inventory.return_value = inventory_port
            build_scanner.return_value = MagicMock()

            result = scan_container_vulnerabilities()

        assert result["error"] is None
        assert result["findings"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.scan_container_vulnerabilities import (
            scan_container_vulnerabilities,
        )

        with patch(
            "hexawyn.mcp.server.build_image_inventory_adapter",
            side_effect=RuntimeError("cluster unreachable"),
        ):
            result = scan_container_vulnerabilities()

        assert "cluster unreachable" in result["error"]


class TestBuildAdapterFactories:
    def test_build_image_inventory_adapter_returns_image_inventory_port(self) -> None:
        from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort
        from hexawyn.mcp.server import build_image_inventory_adapter

        result = build_image_inventory_adapter()

        assert isinstance(result, ImageInventoryPort)

    def test_build_image_vulnerability_scan_adapter_returns_scan_port(self) -> None:
        from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
            ImageVulnerabilityScanPort,
        )
        from hexawyn.mcp.server import build_image_vulnerability_scan_adapter

        result = build_image_vulnerability_scan_adapter()

        assert isinstance(result, ImageVulnerabilityScanPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.scan_container_vulnerabilities")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
