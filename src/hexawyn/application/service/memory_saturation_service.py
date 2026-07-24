from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.application.use_case.memory_saturation.command import (
    MemorySaturationCommand,
)
from hexawyn.application.use_case.memory_saturation.response import (
    MemorySaturationResponse,
)
from hexawyn.application.ports.driving.memory_saturation.memory_saturation_service_port import (
    MemorySaturationServicePort,
)
from hexawyn.domain.models.memory_saturation import MemorySaturationRequest, MemorySaturationResult


class MemorySaturationService(MemorySaturationServicePort):
    def __init__(self, port: MemorySaturationPort) -> None:
        self._port = port

    def predict(self, command: MemorySaturationCommand) -> MemorySaturationResponse:
        req = MemorySaturationRequest(prediction_window_minutes=command.prediction_window_minutes)
        raw = self._port.fetch_memory_metrics(req)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw)
        for p in result.critical_pods:
            cause = self._port.correlate_with_otel(p.pod_name, p.namespace)
            if cause:
                object.__setattr__(p, "otel_root_cause", cause)
        return MemorySaturationResponse(
            prediction_window_minutes=result.prediction_window_minutes,
            critical_pods=[asdict(p) for p in result.critical_pods],
            safe_pod_count=result.safe_pod_count,
        )
