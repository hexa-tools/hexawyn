from __future__ import annotations

from unittest.mock import MagicMock, patch


def _raw(name: str, namespace: str = "production") -> dict:
    return {
        "name": name,
        "namespace": namespace,
        "kind": "pod",
        "node": "worker-1",
        "phase": "Running",
        "ready": True,
        "labels": {"app": "payment"},
    }


class TestSearchResourcesByLabelsTool:
    def test_returns_grouped_results(self) -> None:
        from hexawyn.mcp.tools.search_resources_by_labels import search_resources_by_labels

        with patch("hexawyn.mcp.server.build_resource_search_adapter") as build_resource_search:
            port = MagicMock()
            port.search_pods.return_value = [_raw("payment-pod-abc12")]
            port.search_deployments.return_value = []
            port.search_services.return_value = []
            port.search_configmaps.return_value = []
            build_resource_search.return_value = port

            result = search_resources_by_labels(label_selector="app=payment")

        assert result["error"] is None
        assert result["total_matched"] == 1
        assert len(result["groups"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.search_resources_by_labels import search_resources_by_labels

        with patch(
            "hexawyn.mcp.server.build_resource_search_adapter",
            side_effect=RuntimeError("Invalid label selector 'bad': missing '='"),
        ):
            result = search_resources_by_labels(label_selector="bad")

        assert "Invalid label selector" in result["error"]


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.search_resources_by_labels")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
