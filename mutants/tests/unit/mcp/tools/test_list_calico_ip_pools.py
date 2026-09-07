"""Unit tests for MCP tool: list_calico_ip_pools."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListCalicoIpPoolsTool:
    def test_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_calico_ip_pools import list_calico_ip_pools

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.total = 1
        mock_response.pools = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_calico_ip_pools.ListCalicoIpPoolsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_calico_ip_pools()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["total"] == 1  # noqa: PLR2004
        assert result["error"] is None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_calico_ip_pools import list_calico_ip_pools

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = list_calico_ip_pools()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_calico_ip_pools")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_pool_dict(self) -> None:
        from hexawyn.domain.models.calico import CalicoIPPool
        from hexawyn.mcp.tools.list_calico_ip_pools import _pool_dict

        pool = CalicoIPPool(
            name="pool-1",
            cidr="10.1.0.0/16",
            ipip_mode="Always",
            vxlan_mode="Never",
            disabled=True,
            nat_outgoing=True,
            node_selector="all()",
        )
        result = _pool_dict(pool)

        assert result["name"] == "pool-1"
        assert result["cidr"] == "10.1.0.0/16"
        assert result["disabled"] is True
        assert result["nat_outgoing"] is True
        assert result["node_selector"] == "all()"
