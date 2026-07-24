from __future__ import annotations

from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
from hexawyn.application.ports.driven.kubernetes_topology_port import KubernetesTopologyPort
from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
from hexawyn.application.use_case.live_topology_mapper.command import LiveTopologyMapperCommand
from hexawyn.application.use_case.live_topology_mapper.response import LiveTopologyMapperResponse


def _build_mermaid(nodes: list[dict[str, object]], edges: list[dict[str, object]]) -> str:
    lines = ["graph TD"]
    for node in nodes:
        name = str(node.get("name", ""))
        lines.append(f'    {name}["{name}"]')
    count = 0
    for edge in edges:
        if count >= 30:
            break
        lines.append(f"    {edge['caller']} --> {edge['callee']}")
        count += 1
    return "\n".join(lines)


class LiveTopologyMapperUseCase:
    def __init__(
        self,
        kubernetes_topology_port: KubernetesTopologyPort,
        istio_topology_port: IstioTopologyPort,
        snapshot_port: TopologySnapshotPort | None,
        cluster_name: str,
    ) -> None:
        self._k8s_port = kubernetes_topology_port
        self._istio_port = istio_topology_port
        self._snapshot_port = snapshot_port
        self._cluster_name = cluster_name

    def execute(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        namespace = command.namespace

        services = self._k8s_port.list_services(namespace)

        istio_edges = self._istio_port.get_virtual_service_edges(namespace)
        if istio_edges is not None:
            edges = istio_edges
            source = "istio"
        else:
            edges = self._k8s_port.get_network_policy_edges(namespace)
            source = "network_policy"

        nodes: list[dict[str, object]] = [
            {
                "name": svc["name"],
                "namespace": svc["namespace"],
                "replicas": svc["replicas"],
                "is_external": svc["is_external"],
            }
            for svc in services
        ]

        edge_list: list[dict[str, object]] = [
            {"caller": e["caller"], "callee": e["callee"]} for e in edges
        ]

        callee_counts: dict[str, int] = {}
        for e in edges:
            callee_counts[e["callee"]] = callee_counts.get(e["callee"], 0) + 1
        spof: list[dict[str, object]] = []
        for svc in services:
            if (
                not svc["is_external"]
                and callee_counts.get(svc["name"], 0) == 0
                and svc["replicas"] <= 1
            ):
                spof.append(
                    {
                        "name": svc["name"],
                        "namespace": svc["namespace"],
                        "replicas": svc["replicas"],
                    }
                )

        has_caller: set[str] = set()
        has_callee: set[str] = set()
        for e in edges:
            has_caller.add(e["caller"])
            has_callee.add(e["callee"])
        all_svc_names = {svc["name"] for svc in services}
        orphans = all_svc_names - has_caller - has_callee
        orphan_list: list[dict[str, object]] = [{"name": o} for o in orphans]

        mermaid = _build_mermaid(nodes, edge_list)

        if self._snapshot_port is not None:
            try:
                from hexawyn.domain.services.topology.exporter import (
                    DependencyEdgeExport,
                    DependencyGraphExport,
                    ServiceNodeExport,
                )

                snapshot_nodes: list[ServiceNodeExport] = [
                    ServiceNodeExport(
                        name=str(svc["name"]),
                        namespace=str(svc["namespace"]),
                        replicas=int(svc["replicas"]),
                        type="external" if svc["is_external"] else "internal",
                        is_spof=any(sp["name"] == svc["name"] for sp in spof),
                    )
                    for svc in services
                ]
                snapshot_edges: list[DependencyEdgeExport] = [
                    DependencyEdgeExport(caller=str(e["caller"]), callee=str(e["callee"]))
                    for e in edges
                ]
                snapshot: DependencyGraphExport = DependencyGraphExport(
                    nodes=snapshot_nodes,
                    edges=snapshot_edges,
                    single_points_of_failure=[str(sp["name"]) for sp in spof],
                    orphan_nodes=list(orphans),
                    cycles=[],
                    inference_source=source,
                    truncated=len(services) > 50,
                    namespace_scope=namespace,
                )
                self._snapshot_port.save_snapshot(self._cluster_name, snapshot)
            except Exception:
                pass

        return LiveTopologyMapperResponse(
            nodes=nodes,
            edges=edge_list,
            single_points_of_failure=spof,
            orphan_nodes=orphan_list,
            cycles=[],
            inference_source=source,
            truncated=len(services) > 50,
            namespace_scope=namespace,
            mermaid_diagram=mermaid,
        )
