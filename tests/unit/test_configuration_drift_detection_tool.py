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


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.configuration_drift_detection")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
