from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda.keda_scaledobject_status.command import (
    KedaScaledobjectStatusCommand,
)
from hexawyn.application.use_case.keda.keda_scaledobject_status.response import (
    KedaScaledobjectStatusResponse,
)


class KedaScaledobjectStatusUseCase:
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def execute(self, command: KedaScaledobjectStatusCommand) -> KedaScaledobjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledobjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,  # type: ignore
        )
