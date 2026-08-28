from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.get_cilium_status.command import (
    GetCiliumStatusCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_status.response import (
    CiliumStatusNodeOutput,
    GetCiliumStatusResponse,
)
from hexawyn.domain.models.cilium import CiliumAgentHealth


class GetCiliumStatusUseCase:
    def __init__(self, port: CiliumPort) -> None:
        self._port = port

    def execute(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    @staticmethod
    def _to_node(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }
