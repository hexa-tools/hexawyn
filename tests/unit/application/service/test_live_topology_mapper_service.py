from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_command import (
    LiveTopologyMapperCommand,
)
from hexawyn.application.service.live_topology_mapper_service import LiveTopologyMapperService


def _k8s_port(
    services: list[dict[str, object]], network_policy_edges: list[dict[str, str]] | None = None
) -> MagicMock:
    port = MagicMock()
    port.list_services.return_value = services
    port.get_network_policy_edges.return_value = network_policy_edges or []
    return port


def _istio_port(edges: list[dict[str, str]] | None) -> MagicMock:
    port = MagicMock()
    port.get_virtual_service_edges.return_value = edges
    return port


_SERVICES = [
    {"name": "api-gateway", "namespace": "production", "replicas": 3, "is_external": False},
    {"name": "auth-service", "namespace": "production", "replicas": 1, "is_external": False},
]


class TestLiveTopologyMapperService:
    def test_uses_istio_edges_when_available(self) -> None:
        k8s_port = _k8s_port(_SERVICES)
        istio_port = _istio_port([{"caller": "api-gateway", "callee": "auth-service"}])
        service = LiveTopologyMapperService(
            kubernetes_topology_port=k8s_port, istio_topology_port=istio_port
        )

        response = service.map_topology(LiveTopologyMapperCommand())

        assert response.inference_source == "ISTIO_VIRTUAL_SERVICE"
        k8s_port.get_network_policy_edges.assert_not_called()

    def test_falls_back_to_network_policy_when_istio_unavailable(self) -> None:
        k8s_port = _k8s_port(
            _SERVICES, network_policy_edges=[{"caller": "api-gateway", "callee": "auth-service"}]
        )
        istio_port = _istio_port(None)
        service = LiveTopologyMapperService(
            kubernetes_topology_port=k8s_port, istio_topology_port=istio_port
        )

        response = service.map_topology(LiveTopologyMapperCommand())

        assert response.inference_source == "NETWORK_POLICY"
        k8s_port.get_network_policy_edges.assert_called_once()

    def test_flags_single_point_of_failure(self) -> None:
        k8s_port = _k8s_port(
            _SERVICES, network_policy_edges=[{"caller": "api-gateway", "callee": "auth-service"}]
        )
        istio_port = _istio_port(None)
        service = LiveTopologyMapperService(
            kubernetes_topology_port=k8s_port, istio_topology_port=istio_port
        )

        response = service.map_topology(LiveTopologyMapperCommand())

        assert response.single_points_of_failure == ["auth-service"]

    def test_response_includes_mermaid_diagram(self) -> None:
        k8s_port = _k8s_port(_SERVICES)
        istio_port = _istio_port(None)
        service = LiveTopologyMapperService(
            kubernetes_topology_port=k8s_port, istio_topology_port=istio_port
        )

        response = service.map_topology(LiveTopologyMapperCommand())

        assert response.mermaid_diagram.startswith("graph TD")

    def test_passes_namespace_scope_through(self) -> None:
        k8s_port = _k8s_port(_SERVICES)
        istio_port = _istio_port(None)
        service = LiveTopologyMapperService(
            kubernetes_topology_port=k8s_port, istio_topology_port=istio_port
        )

        response = service.map_topology(LiveTopologyMapperCommand(namespace="production"))

        assert response.namespace_scope == "production"
        k8s_port.list_services.assert_called_once_with("production")

    def test_saves_snapshot_when_snapshot_port_provided(self) -> None:
        k8s_port = _k8s_port(_SERVICES)
        istio_port = _istio_port(None)
        snapshot_port = MagicMock()
        service = LiveTopologyMapperService(
            kubernetes_topology_port=k8s_port,
            istio_topology_port=istio_port,
            snapshot_port=snapshot_port,
            cluster_name="prod-cluster",
        )

        service.map_topology(LiveTopologyMapperCommand())

        snapshot_port.save_snapshot.assert_called_once()
        args, _ = snapshot_port.save_snapshot.call_args
        assert args[0] == "prod-cluster"

    def test_does_not_save_snapshot_when_snapshot_port_is_none(self) -> None:
        k8s_port = _k8s_port(_SERVICES)
        istio_port = _istio_port(None)
        service = LiveTopologyMapperService(
            kubernetes_topology_port=k8s_port, istio_topology_port=istio_port
        )

        # Should not raise even though no snapshot port is configured.
        service.map_topology(LiveTopologyMapperCommand())


class TestLiveTopologyMapperServiceEdgeCases:
    def test_k8s_port_failure_propagates(self) -> None:
        import pytest

        k8s_port = MagicMock()
        k8s_port.list_services.side_effect = RuntimeError("k8s API unavailable")
        istio_port = _istio_port(None)
        service = LiveTopologyMapperService(
            kubernetes_topology_port=k8s_port, istio_topology_port=istio_port
        )

        with pytest.raises(RuntimeError, match="k8s API unavailable"):
            service.map_topology(LiveTopologyMapperCommand())
