"""CalicoDetectUseCase — reports whether Calico is the active CNI and its health."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_detect.command import CalicoDetectCommand
from hexawyn.application.use_case.calico.calico_detect.response import CalicoDetectResponse
from hexawyn.domain.models.calico import CalicoDetectionStatus


class CalicoDetectUseCase:
    """Orchestrates Calico detection — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )
