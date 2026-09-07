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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class LiveTopologyMapperUseCase:
    @_mutmut_mutated(mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut)
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
    def xǁLiveTopologyMapperUseCaseǁ__init____mutmut_orig(
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
    def xǁLiveTopologyMapperUseCaseǁ__init____mutmut_1(
        self,
        kubernetes_topology_port: KubernetesTopologyPort,
        istio_topology_port: IstioTopologyPort,
        snapshot_port: TopologySnapshotPort | None = None,
        cluster_name: str = "XXdefaultXX",
    ) -> None:
        self._k8s_port = kubernetes_topology_port
        self._istio_port = istio_topology_port
        self._snapshot_port = snapshot_port
        self._cluster_name = cluster_name
        self._engine = TopologyGraphBuilderService()
    def xǁLiveTopologyMapperUseCaseǁ__init____mutmut_2(
        self,
        kubernetes_topology_port: KubernetesTopologyPort,
        istio_topology_port: IstioTopologyPort,
        snapshot_port: TopologySnapshotPort | None = None,
        cluster_name: str = "DEFAULT",
    ) -> None:
        self._k8s_port = kubernetes_topology_port
        self._istio_port = istio_topology_port
        self._snapshot_port = snapshot_port
        self._cluster_name = cluster_name
        self._engine = TopologyGraphBuilderService()
    def xǁLiveTopologyMapperUseCaseǁ__init____mutmut_3(
        self,
        kubernetes_topology_port: KubernetesTopologyPort,
        istio_topology_port: IstioTopologyPort,
        snapshot_port: TopologySnapshotPort | None = None,
        cluster_name: str = "default",
    ) -> None:
        self._k8s_port = None
        self._istio_port = istio_topology_port
        self._snapshot_port = snapshot_port
        self._cluster_name = cluster_name
        self._engine = TopologyGraphBuilderService()
    def xǁLiveTopologyMapperUseCaseǁ__init____mutmut_4(
        self,
        kubernetes_topology_port: KubernetesTopologyPort,
        istio_topology_port: IstioTopologyPort,
        snapshot_port: TopologySnapshotPort | None = None,
        cluster_name: str = "default",
    ) -> None:
        self._k8s_port = kubernetes_topology_port
        self._istio_port = None
        self._snapshot_port = snapshot_port
        self._cluster_name = cluster_name
        self._engine = TopologyGraphBuilderService()
    def xǁLiveTopologyMapperUseCaseǁ__init____mutmut_5(
        self,
        kubernetes_topology_port: KubernetesTopologyPort,
        istio_topology_port: IstioTopologyPort,
        snapshot_port: TopologySnapshotPort | None = None,
        cluster_name: str = "default",
    ) -> None:
        self._k8s_port = kubernetes_topology_port
        self._istio_port = istio_topology_port
        self._snapshot_port = None
        self._cluster_name = cluster_name
        self._engine = TopologyGraphBuilderService()
    def xǁLiveTopologyMapperUseCaseǁ__init____mutmut_6(
        self,
        kubernetes_topology_port: KubernetesTopologyPort,
        istio_topology_port: IstioTopologyPort,
        snapshot_port: TopologySnapshotPort | None = None,
        cluster_name: str = "default",
    ) -> None:
        self._k8s_port = kubernetes_topology_port
        self._istio_port = istio_topology_port
        self._snapshot_port = snapshot_port
        self._cluster_name = None
        self._engine = TopologyGraphBuilderService()
    def xǁLiveTopologyMapperUseCaseǁ__init____mutmut_7(
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
        self._engine = None

    @_mutmut_mutated(mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut)
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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_orig(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_1(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = None

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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_2(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(None)

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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_3(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = None
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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_4(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(None)
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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_5(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is None:
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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_6(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is not None:
            edges = None
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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_7(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is not None:
            edges = istio_edges
            inference_source = None
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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_8(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is not None:
            edges = istio_edges
            inference_source = InferenceSource.ISTIO_VIRTUAL_SERVICE
        else:
            edges = None
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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_9(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is not None:
            edges = istio_edges
            inference_source = InferenceSource.ISTIO_VIRTUAL_SERVICE
        else:
            edges = self._k8s_port.get_network_policy_edges(None)
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

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_10(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is not None:
            edges = istio_edges
            inference_source = InferenceSource.ISTIO_VIRTUAL_SERVICE
        else:
            edges = self._k8s_port.get_network_policy_edges(command.namespace)
            inference_source = None

        graph = self._engine.build_graph(
            services=services,
            edges=edges,
            inference_source=inference_source,
            namespace_scope=command.namespace,
        )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_11(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is not None:
            edges = istio_edges
            inference_source = InferenceSource.ISTIO_VIRTUAL_SERVICE
        else:
            edges = self._k8s_port.get_network_policy_edges(command.namespace)
            inference_source = InferenceSource.NETWORK_POLICY

        graph = None

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_12(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is not None:
            edges = istio_edges
            inference_source = InferenceSource.ISTIO_VIRTUAL_SERVICE
        else:
            edges = self._k8s_port.get_network_policy_edges(command.namespace)
            inference_source = InferenceSource.NETWORK_POLICY

        graph = self._engine.build_graph(
            services=None,
            edges=edges,
            inference_source=inference_source,
            namespace_scope=command.namespace,
        )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_13(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            edges=None,
            inference_source=inference_source,
            namespace_scope=command.namespace,
        )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_14(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            inference_source=None,
            namespace_scope=command.namespace,
        )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_15(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            namespace_scope=None,
        )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_16(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        services = self._k8s_port.list_services(command.namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(command.namespace)
        if istio_edges is not None:
            edges = istio_edges
            inference_source = InferenceSource.ISTIO_VIRTUAL_SERVICE
        else:
            edges = self._k8s_port.get_network_policy_edges(command.namespace)
            inference_source = InferenceSource.NETWORK_POLICY

        graph = self._engine.build_graph(
            edges=edges,
            inference_source=inference_source,
            namespace_scope=command.namespace,
        )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_17(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            inference_source=inference_source,
            namespace_scope=command.namespace,
        )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_18(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            namespace_scope=command.namespace,
        )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_19(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            )

        if self._snapshot_port is not None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_20(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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

        if self._snapshot_port is None:
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_21(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            self._snapshot_port.save_snapshot(None, to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_22(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            self._snapshot_port.save_snapshot(self._cluster_name, None)

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_23(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            self._snapshot_port.save_snapshot(to_structured_dict(graph))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_24(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            self._snapshot_port.save_snapshot(self._cluster_name, )

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_25(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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
            self._snapshot_port.save_snapshot(self._cluster_name, to_structured_dict(None))

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_26(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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

        return LiveTopologyMapperResponse.from_graph(None, mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_27(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=None)

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_28(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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

        return LiveTopologyMapperResponse.from_graph(mermaid_diagram=to_mermaid(graph))

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_29(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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

        return LiveTopologyMapperResponse.from_graph(graph, )

    def xǁLiveTopologyMapperUseCaseǁexecute__mutmut_30(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
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

        return LiveTopologyMapperResponse.from_graph(graph, mermaid_diagram=to_mermaid(None))

mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut['_mutmut_orig'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut['xǁLiveTopologyMapperUseCaseǁ__init____mutmut_1'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut['xǁLiveTopologyMapperUseCaseǁ__init____mutmut_2'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut['xǁLiveTopologyMapperUseCaseǁ__init____mutmut_3'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut['xǁLiveTopologyMapperUseCaseǁ__init____mutmut_4'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut['xǁLiveTopologyMapperUseCaseǁ__init____mutmut_5'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut['xǁLiveTopologyMapperUseCaseǁ__init____mutmut_6'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁ__init____mutmut['xǁLiveTopologyMapperUseCaseǁ__init____mutmut_7'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁ__init____mutmut_7 # type: ignore # mutmut generated

mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['_mutmut_orig'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_1'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_2'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_3'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_4'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_5'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_6'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_7'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_8'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_9'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_10'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_11'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_12'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_13'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_14'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_15'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_16'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_17'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_18'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_19'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_20'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_21'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_22'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_23'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_24'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_25'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_26'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_27'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_28'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_29'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁLiveTopologyMapperUseCaseǁexecute__mutmut['xǁLiveTopologyMapperUseCaseǁexecute__mutmut_30'] = LiveTopologyMapperUseCase.xǁLiveTopologyMapperUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
