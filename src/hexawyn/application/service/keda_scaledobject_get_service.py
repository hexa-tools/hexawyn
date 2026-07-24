from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda_scaledobject_get.command import (
    KedaScaledObjectGetCommand,
)
from hexawyn.application.use_case.keda_scaledobject_get.response import (
    KedaScaledObjectGetResponse,
)
from hexawyn.application.ports.driving.keda_scaledobject_get.keda_scaledobject_get_service_port import (
    KedaScaledObjectGetServicePort,
)


class KedaScaledObjectGetService(KedaScaledObjectGetServicePort):
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def get_object(self, command: KedaScaledObjectGetCommand) -> KedaScaledObjectGetResponse:
        so = self._port.get_scaledobject(name=command.name, namespace=command.namespace)
        return KedaScaledObjectGetResponse(
            name=so.name,
            namespace=so.namespace,
            phase=so.phase.value,
            min_replicas=so.min_replicas,
            max_replicas=so.max_replicas,
            current_replicas=so.current_replicas,
            hpa_target_replicas=so.hpa_target_replicas,
            hpa_name=so.hpa_name,
            hpa_status=so.hpa_status.value,
            cooldown_period_seconds=so.cooldown_period_seconds,
            last_scale_time=so.last_scale_time,
            idle_replicas=so.idle_replicas,
            fallback_replicas=so.fallback_replicas,
            workload_kind=so.workload_kind,
            workload_name=so.workload_name,
            ready=so.ready,
            message=so.message,
        )
