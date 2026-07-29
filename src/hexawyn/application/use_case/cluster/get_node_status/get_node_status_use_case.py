from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.cluster.get_node_status.command import (
    GetNodeStatusCommand,
)
from hexawyn.application.use_case.cluster.get_node_status.response import (
    GetNodeStatusResponse,
)


class GetNodeStatusUseCase:
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(self, command: GetNodeStatusCommand) -> GetNodeStatusResponse:
        pods = self._k8s.list_pods()
        node_name = command.node_name or ""

        node_pods = [p for p in pods if node_name and p.get("node") == node_name]

        return GetNodeStatusResponse(
            node_name=node_name,
            status="Ready" if node_pods else "Unknown",
            pods=[
                {
                    "name": p.get("name", ""),
                    "namespace": p.get("namespace", ""),
                    "status": p.get("status", ""),
                    "restarts": p.get("restarts", 0),
                }
                for p in node_pods
            ],
            total_pods=len(node_pods),
        )
