from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSemanticLogSearchTool:
    def test_returns_grouped_results(self) -> None:
        from hexawyn.mcp.tools.semantic_log_search import semantic_log_search

        with (
            patch("hexawyn.mcp.server.build_log_search_adapter") as build_log_search,
            patch("hexawyn.mcp.server.build_k8s_adapter") as build_k8s,
        ):
            port = MagicMock()
            port.fetch_pod_container_logs.return_value = [
                {
                    "container": "app",
                    "lines": ["2024-01-01T10:32:15Z connection refused to postgres"],
                    "truncated": False,
                }
            ]
            build_log_search.return_value = port

            k8s_adapter = MagicMock()
            k8s_adapter.list_namespaces.return_value = [
                {"name": "production", "status": "Active", "age": "10d"}
            ]
            k8s_adapter.list_pods.return_value = [
                {
                    "name": "checkout-pod-abc12",
                    "namespace": "production",
                    "status": "Running",
                    "restarts": 0,
                    "age": "1d",
                    "node": "n1",
                }
            ]
            build_k8s.return_value = k8s_adapter

            result = semantic_log_search(pattern="connection refused to postgres")

        assert result["error"] is None
        assert result["pods_affected"] == 1
        assert len(result["groups"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.semantic_log_search import semantic_log_search

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("Namespace 'ghost' not found"),
        ):
            result = semantic_log_search(pattern="connection refused", namespace="ghost")

        assert "Namespace 'ghost' not found" in result["error"]


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.semantic_log_search")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
