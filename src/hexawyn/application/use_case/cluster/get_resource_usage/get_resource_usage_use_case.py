from __future__ import annotations

from collections import defaultdict

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.pod_metrics_port import (
    PodMetricSnapshot,
    PodMetricsPort,
)
from hexawyn.application.use_case.cluster.get_resource_usage.command import (
    GetResourceUsageCommand,
)
from hexawyn.application.use_case.cluster.get_resource_usage.response import (
    GetResourceUsageResponse,
)
from hexawyn.domain.errors import MetricsUnavailableError
from hexawyn.domain.models.resource_usage import (
    NamespaceResourceUsageSummary,
    PodResourceUsage,
)

_MILLICORE_TO_CORE: float = 1.0 / 1000.0
_MIB_TO_GB: float = 1.0 / 1024.0
_SENTINEL_NO_REQUEST: float = -1.0


class GetResourceUsageUseCase:
    """Compare actual resource usage (metrics-server) against requested resources (K8s spec)."""

    def __init__(self, k8s_port: K8sPort, metrics_port: PodMetricsPort) -> None:
        self._k8s = k8s_port
        self._metrics = metrics_port

    def execute(self, command: GetResourceUsageCommand) -> GetResourceUsageResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        resource_filter = command.resource if command.resource in ("cpu", "memory") else "both"

        try:
            metrics = self._metrics.get_pod_metrics(namespace=command.namespace)
            metrics_available = True
            source = "metrics-server"
        except MetricsUnavailableError:
            metrics = []
            metrics_available = False
            source = ""

        metric_by_name: dict[str, PodMetricSnapshot] = {m["name"]: m for m in metrics}

        pod_usages = [
            self._build_pod_usage(
                pod, metric_by_name.get(pod.get("name", "")), resource_filter, metrics_available
            )
            for pod in pods
            if pod.get("namespace")
        ]

        summaries = self._build_namespace_summaries(pod_usages, metrics_available)

        return GetResourceUsageResponse(
            pods=pod_usages,
            namespace_summary=summaries,
            metrics_server_available=metrics_available,
            source=source,
        )

    def _build_pod_usage(
        self,
        pod: PodInfo,
        metric: PodMetricSnapshot | None,
        resource_filter: str,
        metrics_available: bool,
    ) -> PodResourceUsage:
        include_cpu = resource_filter in ("cpu", "both")
        include_memory = resource_filter in ("memory", "both")

        cpu_request_millicores = pod.get("cpu_request_millicores") or 0
        memory_request_mib = pod.get("memory_request_mib") or 0
        cpu_used = metric["cpu_cores"] if metric else 0.0
        memory_used = metric["memory_gb"] if metric else 0.0

        cpu_req_cores = cpu_request_millicores * _MILLICORE_TO_CORE
        mem_req_gb = memory_request_mib * _MIB_TO_GB

        pod_usage: PodResourceUsage = {
            "name": pod.get("name", "unknown"),
            "namespace": pod.get("namespace", "unknown"),
            "cpu_requested_cores": round(cpu_req_cores, 2) if include_cpu else 0.0,
            "cpu_used_cores": round(cpu_used, 2) if include_cpu else 0.0,
            "cpu_utilization_pct": round(
                self._utilization_pct(cpu_used, cpu_req_cores, metrics_available), 1
            )
            if include_cpu
            else 0.0,
            "memory_requested_gb": round(mem_req_gb, 2) if include_memory else 0.0,
            "memory_used_gb": round(memory_used, 2) if include_memory else 0.0,
            "memory_utilization_pct": round(
                self._utilization_pct(memory_used, mem_req_gb, metrics_available), 1
            )
            if include_memory
            else 0.0,
        }
        return pod_usage

    def _build_namespace_summaries(
        self, pod_usages: list[PodResourceUsage], metrics_available: bool
    ) -> list[NamespaceResourceUsageSummary]:
        ns_pod_count: dict[str, int] = defaultdict(int)
        ns_cpu_req: dict[str, float] = defaultdict(float)
        ns_cpu_used: dict[str, float] = defaultdict(float)
        ns_mem_req: dict[str, float] = defaultdict(float)
        ns_mem_used: dict[str, float] = defaultdict(float)

        for p in pod_usages:
            ns = p["namespace"]
            ns_pod_count[ns] += 1
            ns_cpu_req[ns] += p["cpu_requested_cores"]
            ns_cpu_used[ns] += p["cpu_used_cores"]
            ns_mem_req[ns] += p["memory_requested_gb"]
            ns_mem_used[ns] += p["memory_used_gb"]

        summaries: list[NamespaceResourceUsageSummary] = []
        for ns in ns_pod_count:
            summaries.append(
                NamespaceResourceUsageSummary(
                    namespace=ns,
                    pod_count=ns_pod_count[ns],
                    total_cpu_requested_cores=round(ns_cpu_req[ns], 2),
                    total_cpu_used_cores=round(ns_cpu_used[ns], 2),
                    total_cpu_utilization_pct=round(
                        self._utilization_pct(ns_cpu_used[ns], ns_cpu_req[ns], metrics_available), 1
                    ),
                    total_memory_requested_gb=round(ns_mem_req[ns], 2),
                    total_memory_used_gb=round(ns_mem_used[ns], 2),
                    total_memory_utilization_pct=round(
                        self._utilization_pct(ns_mem_used[ns], ns_mem_req[ns], metrics_available), 1
                    ),
                )
            )

        summaries.sort(key=lambda s: s["total_cpu_requested_cores"], reverse=True)
        return summaries

    @staticmethod
    def _utilization_pct(used: float, requested: float, metrics_available: bool = True) -> float:
        if not metrics_available:
            return _SENTINEL_NO_REQUEST
        if requested <= 0:
            return _SENTINEL_NO_REQUEST
        return (used / requested) * 100.0
