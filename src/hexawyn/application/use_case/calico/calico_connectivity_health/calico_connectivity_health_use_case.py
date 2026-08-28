"""CalicoConnectivityHealthUseCase — Calico dataplane end-to-end health."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_connectivity_health.command import (
    CalicoConnectivityHealthCommand,
)
from hexawyn.application.use_case.calico.calico_connectivity_health.response import (
    CalicoConnectivityHealthResponse,
)
from hexawyn.domain.models.calico import DataplaneMode
from hexawyn.domain.services.calico.connectivity_health_service import (
    build_calico_connectivity_health,
)


class CalicoConnectivityHealthUseCase:
    """Orchestrates the connectivity verdict — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )
