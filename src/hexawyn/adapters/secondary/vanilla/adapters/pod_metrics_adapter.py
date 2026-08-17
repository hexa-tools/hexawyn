# mypy: ignore-errors
"""Adapter for per-pod CPU/memory usage from Kubernetes metrics-server."""

from __future__ import annotations

from hexawyn.adapters.secondary.vanilla.adapters._helpers import (
    cpu_to_cores,
    mapping_from,
    memory_to_bytes,
    metric_items,
)
from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesMetricsApi,
)
from hexawyn.application.ports.driven.pod_metrics_port import (
    PodMetricSnapshot,
    PodMetricsPort,
)
from hexawyn.domain.errors import MetricsUnavailableError


class VanillaPodMetricsAdapter(PodMetricsPort):
    """Queries the Kubernetes metrics-server for per-pod CPU/memory usage."""

    def __init__(self, metrics_api: KubernetesMetricsApi | None, cluster_name: str) -> None:
        self._metrics_api = metrics_api
        self._cluster_name = cluster_name

    def get_pod_metrics(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group="metrics.k8s.io",
                    version="v1beta1",
                    namespace=namespace,
                    plural="pods",
                )
            else:
                raw = self._metrics_api.list_cluster_custom_object(
                    group="metrics.k8s.io",
                    version="v1beta1",
                    plural="pods",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def _parse_pod_metrics(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "unknown"
            )

            containers = item.get("containers", []) if isinstance(item, dict) else []
            if not isinstance(containers, list):
                containers = []

            cpu_cores = 0.0
            memory_gb = 0.0

            for container in containers:
                if not isinstance(container, dict):
                    continue
                usage = mapping_from(container.get("usage"))
                if usage is not None:
                    cpu_str = usage.get("cpu", "")
                    mem_str = usage.get("memory", "")
                    if isinstance(cpu_str, str):
                        cpu_cores += cpu_to_cores(cpu_str)
                    if isinstance(mem_str, str):
                        memory_gb += memory_to_bytes(mem_str) / (1024.0**3)

            snapshots.append(
                PodMetricSnapshot(
                    name=name,
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots
