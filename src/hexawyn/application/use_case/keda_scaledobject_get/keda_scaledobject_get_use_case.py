from __future__ import annotations

from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.use_case.keda_scaledobject_get.command import KedaScaledobjectGetCommand
from hexawyn.application.use_case.keda_scaledobject_get.response import KedaScaledobjectGetResponse


class KedaScaledobjectGetUseCase:
    def __init__(self, port: KedaPort) -> None:
        self._port = port

    def execute(self, command: KedaScaledobjectGetCommand) -> KedaScaledobjectGetResponse:
        scaled_object = self._port.get_scaledobject(command.name, command.namespace)
        triggers: list[dict[str, object]] = []
        for t in scaled_object.triggers:
            triggers.append(
                {
                    "type": t.type,
                    "metadata": dict(t.metadata) if t.metadata else {},
                    "metric_type": t.metric_type,
                }
            )
        return KedaScaledobjectGetResponse(
            name=scaled_object.name,
            namespace=scaled_object.namespace,
            triggers=triggers,
            min_replicas=scaled_object.min_replicas,
            max_replicas=scaled_object.max_replicas,
            cooldown_period=scaled_object.cooldown_period,
            polling_interval=scaled_object.polling_interval,
            status=scaled_object.status,
        )
