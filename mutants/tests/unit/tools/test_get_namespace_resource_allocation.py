"""Unit tests for MCP tool: get_namespace_resource_allocation — guard mirror."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetNamespaceResourceAllocationTool:
    def test_get_namespace_resource_allocation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_namespace_resource_allocation import (
            get_namespace_resource_allocation,
        )

        mock_response = MagicMock()
        mock_response.allocations = []
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_namespace_resource_allocation.GetNamespaceResourceAllocationUseCase",
                return_value=mock_uc,
            ),
        ):
            result = get_namespace_resource_allocation()

        assert isinstance(result, dict)
        assert "allocations" in result

    def test_get_namespace_resource_allocation_handles_error(self) -> None:
        from hexawyn.mcp.tools.get_namespace_resource_allocation import (
            get_namespace_resource_allocation,
        )

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = get_namespace_resource_allocation()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_get_namespace_resource_allocation_success_path(self) -> None:
        from hexawyn.domain.models.namespace_resource_allocation import (
            NamespaceResourceAllocation,
        )
        from hexawyn.mcp.tools.get_namespace_resource_allocation import (
            get_namespace_resource_allocation,
        )

        mock_allocations: list[NamespaceResourceAllocation] = [
            {
                "namespace": "staging",
                "total_cpu_cores": 4.0,
                "total_memory_gb": 8.0,
                "pod_count": 6,
            },
            {
                "namespace": "production",
                "total_cpu_cores": 3.0,
                "total_memory_gb": 6.0,
                "pod_count": 4,
            },
        ]
        mock_response = MagicMock()
        mock_response.allocations = mock_allocations
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_namespace_resource_allocation.GetNamespaceResourceAllocationUseCase",
                return_value=mock_uc,
            ),
        ):
            result = get_namespace_resource_allocation()

        assert result.get("error") is None
        allocations = result.get("allocations")
        assert isinstance(allocations, list)
        assert len(allocations) == 2  # noqa: PLR2004
        assert allocations[0]["namespace"] == "staging"
        assert allocations[0]["total_cpu_cores"] == 4.0  # noqa: PLR2004

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_namespace_resource_allocation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
