from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_scaledjobs_list.command import (
    KedaScaledjobsListCommand,
)
from hexawyn.application.use_case.keda.keda_scaledjobs_list.response import (
    KedaScaledjobsListResponse,
)


class KedaScaledjobsListUseCase:
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def execute(self, command: KedaScaledjobsListCommand) -> KedaScaledjobsListResponse:
        jobs = self._port.list_scaledjobs(namespace=command.namespace)
        return KedaScaledjobsListResponse(scaled_jobs=[asdict(j) for j in jobs])
