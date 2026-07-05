from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestConfigurationDriftDetectionTool:
    def test_returns_drift_report(self) -> None:
        from hexawyn.mcp.tools.configuration_drift_detection import (
            configuration_drift_detection,
        )

        with (
            patch("hexawyn.mcp.server.build_live_resource_adapter") as build_live,
            patch("hexawyn.mcp.server.build_helm_drift_adapter") as build_helm,
            patch("hexawyn.mcp.server.build_kustomize_drift_adapter") as build_kustomize,
        ):
            live_port = MagicMock()
            live_port.list_live_resources.return_value = []
            build_live.return_value = live_port

            helm_port = MagicMock()
            build_helm.return_value = helm_port

            kustomize_port = MagicMock()
            build_kustomize.return_value = kustomize_port

            result = configuration_drift_detection(namespace="production")

        assert result["error"] is None
        assert result["drifted_resources"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.configuration_drift_detection import (
            configuration_drift_detection,
        )

        with patch(
            "hexawyn.mcp.server.build_live_resource_adapter",
            side_effect=RuntimeError("cluster unreachable"),
        ):
            result = configuration_drift_detection(namespace="production")

        assert "cluster unreachable" in result["error"]


class TestConfigurationDriftAdapterFactories:
    def test_build_helm_drift_adapter_returns_drift_detection_port(self) -> None:
        from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
        from hexawyn.mcp.server import build_helm_drift_adapter

        result = build_helm_drift_adapter()

        assert isinstance(result, DriftDetectionPort)

    def test_build_kustomize_drift_adapter_returns_drift_detection_port(self) -> None:
        from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
        from hexawyn.mcp.server import build_kustomize_drift_adapter

        result = build_kustomize_drift_adapter()

        assert isinstance(result, DriftDetectionPort)

    def test_build_live_resource_adapter_returns_live_resource_port(self) -> None:
        from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort
        from hexawyn.mcp.server import build_live_resource_adapter

        result = build_live_resource_adapter()

        assert isinstance(result, LiveResourcePort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.configuration_drift_detection")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
