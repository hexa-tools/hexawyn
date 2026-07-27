from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.live_topology_mapper.command import (
    LiveTopologyMapperCommand,
)
from hexawyn.application.use_case.cluster.live_topology_mapper.live_topology_mapper_use_case import (  # noqa: E501
    LiveTopologyMapperUseCase,
)
from hexawyn.application.use_case.cluster.live_topology_mapper.response import (
    LiveTopologyMapperResponse,
)


class TestLiveTopologyMapperUseCase:
    def test_execute_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_services.return_value = []
        istio = MagicMock()
        istio.get_virtual_service_edges.return_value = []

        use_case = LiveTopologyMapperUseCase(
            kubernetes_topology_port=k8s,
            istio_topology_port=istio,
        )
        result = use_case.execute(LiveTopologyMapperCommand())

        assert isinstance(result, LiveTopologyMapperResponse)
        assert result.nodes == []

    def test_execute_falls_back_to_network_policies(self) -> None:
        k8s = MagicMock()
        k8s.list_services.return_value = []
        k8s.get_network_policy_edges.return_value = []
        istio = MagicMock()
        istio.get_virtual_service_edges.return_value = None

        use_case = LiveTopologyMapperUseCase(
            kubernetes_topology_port=k8s,
            istio_topology_port=istio,
        )
        result = use_case.execute(LiveTopologyMapperCommand())

        assert isinstance(result, LiveTopologyMapperResponse)
