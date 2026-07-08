from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.ports.driving.keda_scaledobject_status.keda_scaledobject_status_command import (
    KedaScaledObjectStatusCommand,
)
from hexawyn.application.ports.driving.keda_scaledobject_status.keda_scaledobject_status_response import (
    KedaScaledObjectStatusResponse,
)
from hexawyn.application.ports.driving.keda_scaledobject_status.keda_scaledobject_status_service_port import (
    KedaScaledObjectStatusServicePort,
)


class KedaScaledObjectStatusService(KedaScaledObjectStatusServicePort):
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def get_status(self, command: KedaScaledObjectStatusCommand) -> KedaScaledObjectStatusResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledObjectStatusResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            last_scale_time=so.last_scale_time,
            cooldown_period_seconds=so.cooldown_period_seconds,
            message=so.message,
        )
