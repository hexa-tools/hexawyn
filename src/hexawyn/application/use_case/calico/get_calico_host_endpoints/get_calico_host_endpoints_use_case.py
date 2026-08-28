"""GetCalicoHostEndpointsUseCase — lists Calico HostEndpoints cluster-wide."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.get_calico_host_endpoints.command import (
    GetCalicoHostEndpointsCommand,
)
from hexawyn.application.use_case.calico.get_calico_host_endpoints.response import (
    GetCalicoHostEndpointsResponse,
)


class GetCalicoHostEndpointsUseCase:
    """Orchestrates Calico HostEndpoint listing — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )
