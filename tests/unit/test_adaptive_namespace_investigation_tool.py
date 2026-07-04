from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAdaptiveNamespaceInvestigationTool:
    def test_returns_investigation(self) -> None:
        from hexawyn.mcp.tools.adaptive_namespace_investigation import (
            adaptive_namespace_investigation,
        )

        with (
            patch("hexawyn.mcp.server.build_namespace_overview_adapter") as build_overview,
            patch("hexawyn.mcp.server.build_k8s_adapter") as build_k8s,
            patch("hexawyn.mcp.server.build_adaptive_investigation_adapter") as build_investigation,
        ):
            overview_port = MagicMock()
            overview_port.get_namespace_overview_data.return_value = {
                "namespace_status": "Active",
                "pods": [],
                "deployments": [],
                "services_count": 1,
                "hpas": [],
            }
            build_overview.return_value = overview_port

            k8s_adapter = MagicMock()
            k8s_adapter.list_namespaces.return_value = [
                {"name": "production", "status": "Active", "age": "10d"}
            ]
            k8s_adapter.list_pods.return_value = []
            build_k8s.return_value = k8s_adapter

            build_investigation.return_value = MagicMock()

            result = adaptive_namespace_investigation(namespace="production")

        assert result["error"] is None
        assert result["namespace"] == "production"
        assert result["investigated_resources"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.adaptive_namespace_investigation import (
            adaptive_namespace_investigation,
        )

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("Namespace 'ghost' not found"),
        ):
            result = adaptive_namespace_investigation(namespace="ghost")

        assert "Namespace 'ghost' not found" in result["error"]


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.adaptive_namespace_investigation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
