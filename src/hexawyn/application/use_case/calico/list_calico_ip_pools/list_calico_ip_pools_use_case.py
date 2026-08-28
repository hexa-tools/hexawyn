"""ListCalicoIpPoolsUseCase — lists Calico IPPools cluster-wide."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.list_calico_ip_pools.command import (
    ListCalicoIpPoolsCommand,
)
from hexawyn.application.use_case.calico.list_calico_ip_pools.response import (
    ListCalicoIpPoolsResponse,
)


class ListCalicoIpPoolsUseCase:
    """Orchestrates Calico IPPool listing — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )
