from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
from hexawyn.application.ports.driven.kubernetes_topology_port import KubernetesTopologyPort
from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort


class TestMCPToolLiveTopologyMapper:
    def test_tool_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.live_topology_mapper import live_topology_mapper

        with patch(
            "hexawyn.mcp.server.build_kubernetes_topology_adapter",
            side_effect=RuntimeError("cluster down"),
        ):
            result = live_topology_mapper(namespace="production")

        assert result["error"] is not None
        assert "cluster down" in str(result["error"])
        assert result["nodes"] == []

    def test_tool_returns_structured_result(self) -> None:
        from hexawyn.mcp.tools.live_topology_mapper import live_topology_mapper

        k8s_adapter = MagicMock(spec=KubernetesTopologyPort)
        k8s_adapter.list_services.return_value = [
            {
                "name": "api-gateway",
                "namespace": "production",
                "replicas": 3,
                "is_external": False,
            },
            {
                "name": "auth-service",
                "namespace": "production",
                "replicas": 1,
                "is_external": False,
            },
        ]
        k8s_adapter.get_network_policy_edges.return_value = [
            {"caller": "api-gateway", "callee": "auth-service"}
        ]
        istio_adapter = MagicMock(spec=IstioTopologyPort)
        istio_adapter.get_virtual_service_edges.return_value = None
        snapshot_adapter = MagicMock(spec=TopologySnapshotPort)

        with (
            patch(
                "hexawyn.mcp.server.build_kubernetes_topology_adapter",
                return_value=k8s_adapter,
            ),
            patch(
                "hexawyn.mcp.server.build_istio_topology_adapter",
                return_value=istio_adapter,
            ),
            patch(
                "hexawyn.mcp.server.build_topology_snapshot_adapter",
                return_value=snapshot_adapter,
            ),
        ):
            result = live_topology_mapper(namespace="production")

        assert result["error"] is None
        assert result["single_points_of_failure"] == ["auth-service"]
        assert result["inference_source"] == "NETWORK_POLICY"
        assert str(result["mermaid_diagram"]).startswith("graph TD")
        snapshot_adapter.save_snapshot.assert_called_once()

    def test_snapshot_adapter_failure_does_not_break_tool(self) -> None:
        from hexawyn.mcp.tools.live_topology_mapper import live_topology_mapper

        k8s_adapter = MagicMock(spec=KubernetesTopologyPort)
        k8s_adapter.list_services.return_value = []
        k8s_adapter.get_network_policy_edges.return_value = []
        istio_adapter = MagicMock(spec=IstioTopologyPort)
        istio_adapter.get_virtual_service_edges.return_value = None

        with (
            patch(
                "hexawyn.mcp.server.build_kubernetes_topology_adapter",
                return_value=k8s_adapter,
            ),
            patch(
                "hexawyn.mcp.server.build_istio_topology_adapter",
                return_value=istio_adapter,
            ),
            patch(
                "hexawyn.mcp.server.build_topology_snapshot_adapter",
                side_effect=RuntimeError("duckdb unavailable"),
            ),
        ):
            result = live_topology_mapper(namespace=None)

        assert result["error"] is None

    def test_register_adds_tool(self) -> None:
        from hexawyn.mcp.tools.live_topology_mapper import register

        mock_mcp = MagicMock()
        decorator = MagicMock()
        mock_mcp.tool.return_value = decorator

        register(mock_mcp)

        mock_mcp.tool.assert_called_once()
        decorator.assert_called_once()
