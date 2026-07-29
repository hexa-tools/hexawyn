from __future__ import annotations

from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
from hexawyn.application.ports.driven.kubernetes_topology_port import KubernetesTopologyPort
from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
from hexawyn.application.use_case.cluster.live_topology_mapper.command import (
    LiveTopologyMapperCommand,
)
from hexawyn.application.use_case.cluster.live_topology_mapper.response import (
    LiveTopologyMapperResponse,
)
from hexawyn.domain.models.dependency_graph import InferenceSource
from hexawyn.domain.services.topology.exporter import to_mermaid, to_structured_dict
from hexawyn.domain.services.topology.mapper import TopologyGraphBuilderService


class LiveTopologyMapperUseCase:
    def __init__(
        self,
        kubernetes_topology_port: KubernetesTopologyPort,
        istio_topology_port: IstioTopologyPort,
        snapshot_port: TopologySnapshotPort | None = None,
        cluster_name: str = "default",
    ) -> None:
        self._k8s_port = kubernetes_topology_port
        self._istio_port = istio_topology_port
        self._snapshot_port = snapshot_port
        self._cluster_name = cluster_name
        self._engine = TopologyGraphBuilderService()

    def execute(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is not None:
            edges = istio_edges
            inference_source = InferenceSource.ISTIO_VIRTUAL_SERVICE
        else:
            edges = self._k8s_port.get_network_policy_edges(command.namespace)
            inference_source = InferenceSource.NETWORK_POLICY

        graph = self._engine.build_graph(
            services=services,
            edges=edges,
            inference_source=inference_source,
            namespace_scope=command.namespace,
        )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))
