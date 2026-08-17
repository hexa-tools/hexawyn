from __future__ import annotations

from collections import defaultdict

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.command import (
    GetNamespaceResourceAllocationCommand,
)
from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.response import (
    GetNamespaceResourceAllocationResponse,
)
from hexawyn.domain.models.namespace_resource_allocation import (
    NamespaceResourceAllocation,
)

_MILLICORE_TO_CORE: float = 1.0 / 1000.0
_MIB_TO_GB: float = 1.0 / 1024.0


class GetNamespaceResourceAllocationUseCase:
    """Aggregates pod resource requests per namespace, ranked by CPU."""

    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(
        self, command: GetNamespaceResourceAllocationCommand
    ) -> GetNamespaceResourceAllocationResponse:
        pods = self._k8s.list_pods()
        return GetNamespaceResourceAllocationResponse(allocations=self._aggregate_and_rank(pods))

    def _aggregate_and_rank(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("cpu_request_millicores")
            memory_mib = pod.get("memory_request_mib")

            if cpu_millicores is not None and cpu_millicores > 0:
                namespace_cpu[namespace] += cpu_millicores * _MILLICORE_TO_CORE
            if memory_mib is not None and memory_mib > 0:
                namespace_memory[namespace] += memory_mib * _MIB_TO_GB

            namespace_pod_count[namespace] += 1

        all_namespaces = (
            set(namespace_cpu.keys())
            | set(namespace_memory.keys())
            | set(namespace_pod_count.keys())
        )

        allocations: list[NamespaceResourceAllocation] = [
            NamespaceResourceAllocation(
                namespace=ns,
                total_cpu_cores=round(namespace_cpu[ns], 2),
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations
