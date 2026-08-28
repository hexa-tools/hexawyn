from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_detect.command import (
    CiliumDetectCommand,
)
from hexawyn.application.use_case.cilium.cilium_detect.response import (
    CiliumAgentOutput,
    CiliumDetectResponse,
)
from hexawyn.domain.models.cilium import CiliumAgentHealth


class CiliumDetectUseCase:
    def __init__(self, port: CiliumPort) -> None:
        self._port = port

    def execute(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    @staticmethod
    def _to_output(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }
