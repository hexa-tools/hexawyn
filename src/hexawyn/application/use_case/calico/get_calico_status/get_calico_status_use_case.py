"""GetCalicoStatusUseCase — aggregated Calico datapath health & connectivity."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.get_calico_status.command import (
    GetCalicoStatusCommand,
)
from hexawyn.application.use_case.calico.get_calico_status.response import (
    GetCalicoStatusResponse,
)
from hexawyn.domain.models.calico import CalicoDetectionStatus
from hexawyn.domain.services.calico.get_calico_status_service import (
    build_calico_status_result,
)


class GetCalicoStatusUseCase:
    """Composes agent health, felix errors and the connectivity probe."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )
