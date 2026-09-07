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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut: MutantDict = {}  # type: ignore


class GetNamespaceResourceAllocationUseCase:
    """Aggregates pod resource requests per namespace, ranked by CPU."""

    @_mutmut_mutated(mutants_xǁGetNamespaceResourceAllocationUseCaseǁ__init____mutmut)
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def xǁGetNamespaceResourceAllocationUseCaseǁ__init____mutmut_orig(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def xǁGetNamespaceResourceAllocationUseCaseǁ__init____mutmut_1(self, k8s_port: K8sPort) -> None:
        self._k8s = None

    @_mutmut_mutated(mutants_xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut)
    def execute(
        self, command: GetNamespaceResourceAllocationCommand
    ) -> GetNamespaceResourceAllocationResponse:
        pods = self._k8s.list_pods()
        return GetNamespaceResourceAllocationResponse(allocations=self._aggregate_and_rank(pods))

    def xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_orig(
        self, command: GetNamespaceResourceAllocationCommand
    ) -> GetNamespaceResourceAllocationResponse:
        pods = self._k8s.list_pods()
        return GetNamespaceResourceAllocationResponse(allocations=self._aggregate_and_rank(pods))

    def xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_1(
        self, command: GetNamespaceResourceAllocationCommand
    ) -> GetNamespaceResourceAllocationResponse:
        pods = None
        return GetNamespaceResourceAllocationResponse(allocations=self._aggregate_and_rank(pods))

    def xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_2(
        self, command: GetNamespaceResourceAllocationCommand
    ) -> GetNamespaceResourceAllocationResponse:
        pods = self._k8s.list_pods()
        return GetNamespaceResourceAllocationResponse(allocations=None)

    def xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_3(
        self, command: GetNamespaceResourceAllocationCommand
    ) -> GetNamespaceResourceAllocationResponse:
        pods = self._k8s.list_pods()
        return GetNamespaceResourceAllocationResponse(allocations=self._aggregate_and_rank(None))

    @_mutmut_mutated(mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut)
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_orig(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_1(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = None
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_2(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(None)
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_3(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = None
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_4(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(None)
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_5(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = None

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_6(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(None)

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_7(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = None
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_8(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get(None)
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_9(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("XXnamespaceXX")
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_10(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("NAMESPACE")
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_11(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if namespace:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_12(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                break

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_13(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = None
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_14(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get(None)
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_15(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("XXcpu_request_millicoresXX")
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_16(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("CPU_REQUEST_MILLICORES")
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_17(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("cpu_request_millicores")
            memory_mib = None

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_18(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("cpu_request_millicores")
            memory_mib = pod.get(None)

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_19(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("cpu_request_millicores")
            memory_mib = pod.get("XXmemory_request_mibXX")

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_20(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("cpu_request_millicores")
            memory_mib = pod.get("MEMORY_REQUEST_MIB")

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_21(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("cpu_request_millicores")
            memory_mib = pod.get("memory_request_mib")

            if cpu_millicores is not None or cpu_millicores > 0:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_22(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("cpu_request_millicores")
            memory_mib = pod.get("memory_request_mib")

            if cpu_millicores is None and cpu_millicores > 0:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_23(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("cpu_request_millicores")
            memory_mib = pod.get("memory_request_mib")

            if cpu_millicores is not None and cpu_millicores >= 0:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_24(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
        namespace_cpu: dict[str, float] = defaultdict(float)
        namespace_memory: dict[str, float] = defaultdict(float)
        namespace_pod_count: dict[str, int] = defaultdict(int)

        for pod in pods:
            namespace = pod.get("namespace")
            if not namespace:
                continue

            cpu_millicores = pod.get("cpu_request_millicores")
            memory_mib = pod.get("memory_request_mib")

            if cpu_millicores is not None and cpu_millicores > 1:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_25(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                namespace_cpu[namespace] = cpu_millicores * _MILLICORE_TO_CORE
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_26(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                namespace_cpu[namespace] -= cpu_millicores * _MILLICORE_TO_CORE
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_27(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                namespace_cpu[namespace] += cpu_millicores / _MILLICORE_TO_CORE
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_28(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
            if memory_mib is not None or memory_mib > 0:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_29(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
            if memory_mib is None and memory_mib > 0:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_30(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
            if memory_mib is not None and memory_mib >= 0:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_31(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
            if memory_mib is not None and memory_mib > 1:
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_32(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                namespace_memory[namespace] = memory_mib * _MIB_TO_GB

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_33(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                namespace_memory[namespace] -= memory_mib * _MIB_TO_GB

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_34(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                namespace_memory[namespace] += memory_mib / _MIB_TO_GB

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_35(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

            namespace_pod_count[namespace] = 1

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_36(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

            namespace_pod_count[namespace] -= 1

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_37(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

            namespace_pod_count[namespace] += 2

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_38(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        all_namespaces = None

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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_39(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
            | set(namespace_memory.keys()) & set(namespace_pod_count.keys())
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_40(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
            set(namespace_cpu.keys()) & set(namespace_memory.keys())
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_41(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
            set(None)
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_42(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
            | set(None)
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_43(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
            | set(None)
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

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_44(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        allocations: list[NamespaceResourceAllocation] = None

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_45(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                namespace=None,
                total_cpu_cores=round(namespace_cpu[ns], 2),
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_46(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_cpu_cores=None,
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_47(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_memory_gb=None,
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_48(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                pod_count=None,
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_49(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_cpu_cores=round(namespace_cpu[ns], 2),
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_50(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_51(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_52(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_53(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_cpu_cores=round(None, 2),
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_54(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_cpu_cores=round(namespace_cpu[ns], None),
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_55(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_cpu_cores=round(2),
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_56(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_cpu_cores=round(namespace_cpu[ns], ),
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_57(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_cpu_cores=round(namespace_cpu[ns], 3),
                total_memory_gb=round(namespace_memory[ns], 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_58(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_memory_gb=round(None, 2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_59(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_memory_gb=round(namespace_memory[ns], None),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_60(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_memory_gb=round(2),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_61(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_memory_gb=round(namespace_memory[ns], ),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_62(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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
                total_memory_gb=round(namespace_memory[ns], 3),
                pod_count=namespace_pod_count[ns],
            )
            for ns in all_namespaces
        ]

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_63(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        allocations.sort(key=None, reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_64(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=None)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_65(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        allocations.sort(reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_66(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        allocations.sort(key=lambda a: a["total_cpu_cores"], )
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_67(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        allocations.sort(key=lambda a: None, reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_68(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        allocations.sort(key=lambda a: a["XXtotal_cpu_coresXX"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_69(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        allocations.sort(key=lambda a: a["TOTAL_CPU_CORES"], reverse=True)
        return allocations

    def xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_70(self, pods: list[PodInfo]) -> list[NamespaceResourceAllocation]:
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

        allocations.sort(key=lambda a: a["total_cpu_cores"], reverse=False)
        return allocations

mutants_xǁGetNamespaceResourceAllocationUseCaseǁ__init____mutmut['_mutmut_orig'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ__init____mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ__init____mutmut_1'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut['_mutmut_orig'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_1'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_2'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_3'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated

mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['_mutmut_orig'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_1'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_2'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_3'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_4'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_5'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_6'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_7'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_8'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_9'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_10'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_11'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_12'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_13'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_14'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_15'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_16'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_17'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_18'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_19'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_20'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_21'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_22'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_23'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_24'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_25'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_26'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_27'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_28'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_29'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_30'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_31'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_32'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_33'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_34'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_35'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_36'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_37'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_38'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_39'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_40'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_41'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_42'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_43'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_44'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_45'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_46'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_47'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_48'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_49'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_50'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_51'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_52'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_53'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_54'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_55'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_56'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_57'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_58'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_58 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_59'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_59 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_60'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_60 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_61'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_61 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_62'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_62 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_63'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_63 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_64'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_64 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_65'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_65 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_66'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_66 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_67'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_67 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_68'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_68 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_69'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_69 # type: ignore # mutmut generated
mutants_xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut['xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_70'] = GetNamespaceResourceAllocationUseCase.xǁGetNamespaceResourceAllocationUseCaseǁ_aggregate_and_rank__mutmut_70 # type: ignore # mutmut generated
