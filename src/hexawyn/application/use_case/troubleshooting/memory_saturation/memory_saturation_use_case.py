from __future__ import annotations

from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.application.use_case.troubleshooting.memory_saturation.command import (
    MemorySaturationCommand,
)
from hexawyn.application.use_case.troubleshooting.memory_saturation.mapper import (
    attach_otel_root_cause,
    predictions_to_dicts,
)
from hexawyn.application.use_case.troubleshooting.memory_saturation.response import (
    MemorySaturationResponse,
)
from hexawyn.domain.models.memory_saturation import (
    MemorySaturationRequest,
    MemorySaturationResult,
)


class MemorySaturationUseCase:
    def __init__(self, port: MemorySaturationPort) -> None:
        self._port = port

    def execute(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(
            prediction_window_minutes=command.prediction_window_minutes,
        )
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)

        enriched_pods = result.critical_pods[:]
        for idx, pod in enumerate(enriched_pods):
            cause = self._port.correlate_with_otel(pod.pod_name, pod.namespace)
            if cause:
                enriched_pods[idx] = attach_otel_root_cause(pod, cause)

        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=predictions_to_dicts(enriched_pods),
            safe_pod_count=result.safe_pod_count,
        )
