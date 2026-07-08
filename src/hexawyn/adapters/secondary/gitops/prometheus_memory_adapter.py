from __future__ import annotations

from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.domain.models.memory_saturation import MemorySaturationRequest


class PrometheusMemoryAdapter(MemorySaturationPort):
    def fetch_memory_metrics(self, request: MemorySaturationRequest) -> list[dict[str, object]]:
        return []

    def correlate_with_otel(self, pod_name: str, namespace: str) -> str | None:
        return None
