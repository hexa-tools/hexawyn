from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestConservativeNamespaceOverviewTool:
    def test_returns_overview(self) -> None:
        from hexawyn.mcp.tools.conservative_namespace_overview import (
            conservative_namespace_overview,
        )

        with (
            patch("hexawyn.mcp.server.build_namespace_overview_adapter") as build_overview,
            patch("hexawyn.mcp.server.build_k8s_adapter") as build_k8s,
        ):
            port = MagicMock()
            port.get_namespace_overview_data.return_value = {
                "namespace_status": "Active",
                "pods": [{"name": "pod-a", "status": "Running"}],
                "deployments": [],
                "services_count": 1,
                "hpas": [],
            }
            build_overview.return_value = port

            k8s_adapter = MagicMock()
            k8s_adapter.list_namespaces.return_value = [
                {"name": "staging", "status": "Active", "age": "10d"}
            ]
            build_k8s.return_value = k8s_adapter

            result = conservative_namespace_overview(namespace="staging")

        assert result["error"] is None
        assert result["health_status"] == "Healthy"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.conservative_namespace_overview import (
            conservative_namespace_overview,
        )

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("Namespace 'ghost' not found"),
        ):
            result = conservative_namespace_overview(namespace="ghost")

        assert "Namespace 'ghost' not found" in result["error"]


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.conservative_namespace_overview")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
