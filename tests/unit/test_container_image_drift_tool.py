from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestContainerImageDriftDetectionTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.container_image_drift_detection import (
            detect_container_image_drift,
        )

        with (
            patch("hexawyn.mcp.server.build_live_resource_adapter") as build_live,
            patch("hexawyn.mcp.server.build_helm_drift_adapter") as build_helm,
            patch("hexawyn.mcp.server.build_kustomize_drift_adapter") as build_kustomize,
            patch("hexawyn.mcp.server.build_image_drift_adapter") as build_image,
        ):
            live_port = MagicMock()
            live_port.list_live_resources.return_value = []
            build_live.return_value = live_port

            build_helm.return_value = MagicMock()
            build_kustomize.return_value = MagicMock()

            image_port = MagicMock()
            image_port.list_resolved_container_images.return_value = []
            build_image.return_value = image_port

            result = detect_container_image_drift(namespace="production")

        assert result["error"] is None
        assert result["out_of_sync"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.container_image_drift_detection import (
            detect_container_image_drift,
        )

        with patch(
            "hexawyn.mcp.server.build_live_resource_adapter",
            side_effect=RuntimeError("cluster unreachable"),
        ):
            result = detect_container_image_drift(namespace="production")

        assert "cluster unreachable" in result["error"]


class TestBuildImageDriftAdapterFactory:
    def test_build_image_drift_adapter_returns_image_drift_port(self) -> None:
        from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort
        from hexawyn.mcp.server import build_image_drift_adapter

        result = build_image_drift_adapter()

        assert isinstance(result, ImageDriftPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.container_image_drift_detection")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
