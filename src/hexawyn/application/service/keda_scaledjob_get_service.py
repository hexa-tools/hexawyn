from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_command import (
    KedaScaledJobGetCommand,
)
from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_response import (
    KedaScaledJobGetResponse,
)
from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_service_port import (
    KedaScaledJobGetServicePort,
)


class KedaScaledJobGetService(KedaScaledJobGetServicePort):
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def get_job(self, command: KedaScaledJobGetCommand) -> KedaScaledJobGetResponse:
        j = self._port.get_scaledjob(name=command.name, namespace=command.namespace)
        return KedaScaledJobGetResponse(
            name=j.name,
            namespace=j.namespace,
            phase=j.phase.value,
            successful_jobs=j.successful_jobs,
            failed_jobs=j.failed_jobs,
            last_execution_time=j.last_execution_time,
            job_target_ref=j.job_target_ref,
            cooldown_period_seconds=j.cooldown_period_seconds,
            max_replica_count=j.max_replica_count,
            message=j.message,
        )
