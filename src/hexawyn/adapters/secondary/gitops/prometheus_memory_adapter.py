from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import query_prometheus_instant
from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.domain.models.memory_saturation import MemorySaturationRequest


class PrometheusMemoryAdapter(MemorySaturationPort):
    def fetch_memory_metrics(self, request: MemorySaturationRequest) -> list[dict[str, object]]:
        try:
            pod_filter = ""
            if request.pod_name:  # type: ignore
                pod_filter = f'pod="{request.pod_name}",'  # type: ignore
            query = (
                f"container_memory_working_set_bytes{{{pod_filter}"
                f'namespace="{request.namespace}"}}'  # type: ignore
            )
            metrics = query_prometheus_instant(query)
            result: list[dict[str, object]] = []
            for m in metrics:
                result.append(
                    {
                        "pod": m["labels"].get("pod", ""),
                        "namespace": m["labels"].get("namespace", ""),
                        "memory_bytes": m["value"],
                        "memory_mib": round(m["value"] / (1024 * 1024), 2),
                    }
                )
            return result
        except Exception:
            return []

    def correlate_with_otel(self, pod_name: str, namespace: str) -> str | None:
        return None
