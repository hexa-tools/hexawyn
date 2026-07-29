from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import query_prometheus_instant
from hexawyn.application.ports.driven.service_cost_port import (
    PodResourceSnapshotData,
    ServiceCostPort,
)


class ServiceCostPrometheusAdapter(ServiceCostPort):
    def fetch_pod_resources(self, service_name: str, month: str) -> list[PodResourceSnapshotData]:
        try:
            cpu_query = (
                f"sum(rate(container_cpu_usage_seconds_total{{"
                f'service="{service_name}"}}[30d])) by (pod, namespace)'
            )
            mem_query = (
                f"avg(container_memory_working_set_bytes{{"
                f'service="{service_name}"}}) by (pod, namespace)'
            )
            cpu_metrics = query_prometheus_instant(cpu_query)
            mem_metrics = query_prometheus_instant(mem_query)

            mem_by_pod: dict[str, float] = {}
            for m in mem_metrics:
                key = f"{m['labels'].get('namespace', '')}/{m['labels'].get('pod', '')}"
                mem_by_pod[key] = m["value"]

            result: list[PodResourceSnapshotData] = []
            for m in cpu_metrics:
                ns = m["labels"].get("namespace", "")
                pod = m["labels"].get("pod", "")
                key = f"{ns}/{pod}"
                result.append(
                    PodResourceSnapshotData(  # type: ignore
                        namespace=ns,
                        pod_name=pod,
                        cpu_cores=m["value"],
                        memory_mib=round(mem_by_pod.get(key, 0) / (1024 * 1024), 2),
                    )
                )
            return result
        except Exception:
            return []
