from __future__ import annotations

from hexawyn.application.ports.driving.keda_scaledjobs_list.keda_scaledjobs_list_command import (
    KedaScaledJobsListCommand,
)
from hexawyn.application.ports.driving.keda_scaledjobs_list.keda_scaledjobs_list_response import (
    KedaScaledJobsListResponse,
)
from hexawyn.application.ports.driving.keda_scaledjobs_list.keda_scaledjobs_list_service_port import (
    KedaScaledJobsListServicePort,
)


class KedaScaledJobsListUseCase:
    def __init__(self, service: KedaScaledJobsListServicePort) -> None:
        self._svc = service

    def execute(self, cmd: KedaScaledJobsListCommand) -> KedaScaledJobsListResponse:
        return self._svc.list_jobs(cmd)
