from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda_scaledjobs_list.command import (
    KedaScaledJobsListCommand,
)
from hexawyn.application.use_case.keda_scaledjobs_list.response import (
    KedaScaledJobsListResponse,
)
from hexawyn.application.ports.driving.keda_scaledjobs_list.keda_scaledjobs_list_service_port import (
    KedaScaledJobsListServicePort,
)


class KedaScaledJobsListService(KedaScaledJobsListServicePort):
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def list_jobs(self, command: KedaScaledJobsListCommand) -> KedaScaledJobsListResponse:
        jobs = self._port.list_scaledjobs(namespace=command.namespace)
        return KedaScaledJobsListResponse(scaled_jobs=[asdict(j) for j in jobs])
