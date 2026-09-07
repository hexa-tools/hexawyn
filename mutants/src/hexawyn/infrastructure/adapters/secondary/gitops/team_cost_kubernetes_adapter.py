from __future__ import annotations

from hexawyn.application.ports.driven.team_cost_port import (
    NamespaceResourceData,
    TeamCostPort,
)
from kubernetes import client, config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut: MutantDict = {}  # type: ignore


class TeamCostKubernetesAdapter(TeamCostPort):
    @_mutmut_mutated(mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut)
    def fetch_namespace_resources(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_orig(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_1(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = None

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_2(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = None
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_3(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = None

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_4(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_5(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    break
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_6(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = None
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_7(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name and ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_8(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or "XXXX"
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_9(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = None

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_10(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=None)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_11(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = None
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_12(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 1
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_13(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = None
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_14(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 1
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_15(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = None

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_16(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 1

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_17(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count = 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_18(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count -= 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_19(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 2
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_20(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = None
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_21(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests and {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_22(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores = _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_23(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores -= _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_24(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(None)
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_25(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(None))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_26(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get(None, "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_27(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", None)))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_28(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_29(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", )))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_30(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("XXcpuXX", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_31(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("CPU", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_32(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "XX0XX")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_33(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib = _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_34(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib -= _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_35(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(None)

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_36(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(None))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_37(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get(None, "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_38(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", None)))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_39(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_40(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", )))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_41(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("XXmemoryXX", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_42(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("MEMORY", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_43(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "XX0XX")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_44(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count >= 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_45(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 1:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_46(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        None
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_47(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=None,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_48(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=None,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_49(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=None,
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_50(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=None,
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_51(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_52(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_53(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_54(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_55(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(None, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_56(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, None),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_57(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_58(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, ),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_59(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores * 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_60(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1001.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_61(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 3),
                            memory_gib=round(mem_total_mib / 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_62(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(None, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_63(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, None),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_64(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_65(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, ),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_66(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib * 1024.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_67(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1025.0, 2),
                        )
                    )
            return result
        except Exception:
            return []
    def xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_68(self, month: str) -> list[NamespaceResourceData]:
        try:
            config.load_kube_config()
            v1 = client.CoreV1Api()

            namespaces = v1.list_namespace()
            result: list[NamespaceResourceData] = []

            for ns in namespaces.items:
                if not ns.metadata:
                    continue
                ns_name = ns.metadata.name or ""
                pods = v1.list_namespaced_pod(namespace=ns_name)

                cpu_total_millicores = 0
                mem_total_mib = 0
                pod_count = 0

                for pod in pods.items:
                    pod_count += 1
                    for container in pod.spec.containers:
                        requests = container.resources.requests or {}
                        cpu_total_millicores += _parse_cpu(str(requests.get("cpu", "0")))
                        mem_total_mib += _parse_memory(str(requests.get("memory", "0")))

                if pod_count > 0:
                    result.append(
                        NamespaceResourceData(  # type: ignore
                            namespace=ns_name,
                            pod_count=pod_count,
                            cpu_cores=round(cpu_total_millicores / 1000.0, 2),
                            memory_gib=round(mem_total_mib / 1024.0, 3),
                        )
                    )
            return result
        except Exception:
            return []

mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['_mutmut_orig'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_1'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_2'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_3'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_4'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_5'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_6'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_7'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_8'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_9'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_10'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_11'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_12'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_13'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_14'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_15'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_16'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_17'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_18'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_19'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_20'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_21'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_22'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_23'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_24'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_25'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_26'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_27'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_28'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_29'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_30'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_31'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_32'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_33'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_34'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_35'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_36'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_37'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_38'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_38 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_39'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_39 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_40'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_40 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_41'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_41 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_42'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_42 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_43'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_43 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_44'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_44 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_45'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_45 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_46'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_46 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_47'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_47 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_48'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_48 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_49'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_49 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_50'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_50 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_51'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_51 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_52'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_52 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_53'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_53 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_54'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_54 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_55'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_55 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_56'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_56 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_57'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_57 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_58'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_58 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_59'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_59 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_60'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_60 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_61'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_61 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_62'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_62 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_63'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_63 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_64'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_64 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_65'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_65 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_66'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_66 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_67'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_67 # type: ignore # mutmut generated
mutants_xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut['xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_68'] = TeamCostKubernetesAdapter.xǁTeamCostKubernetesAdapterǁfetch_namespace_resources__mutmut_68 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_cpu__mutmut)
def _parse_cpu(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:-1])
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_orig(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:-1])
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_1(cpu_str: str) -> int:
    if cpu_str.endswith(None):
        return int(cpu_str[:-1])
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_2(cpu_str: str) -> int:
    if cpu_str.endswith("XXmXX"):
        return int(cpu_str[:-1])
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_3(cpu_str: str) -> int:
    if cpu_str.endswith("M"):
        return int(cpu_str[:-1])
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_4(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(None)
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_5(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:+1])
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_6(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:-2])
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_7(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:-1])
    try:
        return int(None)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_8(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:-1])
    try:
        return int(float(cpu_str) / 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_9(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:-1])
    try:
        return int(float(None) * 1000)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_10(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:-1])
    try:
        return int(float(cpu_str) * 1001)
    except ValueError:
        return 0


def x__parse_cpu__mutmut_11(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:-1])
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 1

mutants_x__parse_cpu__mutmut['_mutmut_orig'] = x__parse_cpu__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_1'] = x__parse_cpu__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_2'] = x__parse_cpu__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_3'] = x__parse_cpu__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_4'] = x__parse_cpu__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_5'] = x__parse_cpu__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_6'] = x__parse_cpu__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_7'] = x__parse_cpu__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_8'] = x__parse_cpu__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_9'] = x__parse_cpu__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_10'] = x__parse_cpu__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_cpu__mutmut['x__parse_cpu__mutmut_11'] = x__parse_cpu__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_memory__mutmut)
def _parse_memory(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_orig(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_1(mem_str: str) -> int:
    mem_str = None
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_2(mem_str: str) -> int:
    mem_str = mem_str.lower()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_3(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith(None):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_4(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("XXMIXX"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_5(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("mi"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_6(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(None)
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_7(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:+2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_8(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-3])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_9(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith(None):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_10(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("XXGIXX"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_11(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("gi"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_12(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) / 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_13(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(None) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_14(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:+2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_15(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-3]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_16(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1025
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_17(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith(None):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_18(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("XXKIXX"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_19(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("ki"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_20(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) / 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_21(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(None) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_22(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:+2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_23(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-3]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_24(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1025
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_25(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) / (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_26(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(None) // (1024 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_27(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 / 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_28(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1025 * 1024)
    except ValueError:
        return 0


def x__parse_memory__mutmut_29(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1025)
    except ValueError:
        return 0


def x__parse_memory__mutmut_30(mem_str: str) -> int:
    mem_str = mem_str.upper()
    if mem_str.endswith("MI"):
        return int(mem_str[:-2])
    if mem_str.endswith("GI"):
        return int(mem_str[:-2]) * 1024
    if mem_str.endswith("KI"):
        return int(mem_str[:-2]) // 1024
    try:
        return int(mem_str) // (1024 * 1024)
    except ValueError:
        return 1

mutants_x__parse_memory__mutmut['_mutmut_orig'] = x__parse_memory__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_1'] = x__parse_memory__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_2'] = x__parse_memory__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_3'] = x__parse_memory__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_4'] = x__parse_memory__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_5'] = x__parse_memory__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_6'] = x__parse_memory__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_7'] = x__parse_memory__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_8'] = x__parse_memory__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_9'] = x__parse_memory__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_10'] = x__parse_memory__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_11'] = x__parse_memory__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_12'] = x__parse_memory__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_13'] = x__parse_memory__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_14'] = x__parse_memory__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_15'] = x__parse_memory__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_16'] = x__parse_memory__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_17'] = x__parse_memory__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_18'] = x__parse_memory__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_19'] = x__parse_memory__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_20'] = x__parse_memory__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_21'] = x__parse_memory__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_22'] = x__parse_memory__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_23'] = x__parse_memory__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_24'] = x__parse_memory__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_25'] = x__parse_memory__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_26'] = x__parse_memory__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_27'] = x__parse_memory__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_28'] = x__parse_memory__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_29'] = x__parse_memory__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_memory__mutmut['x__parse_memory__mutmut_30'] = x__parse_memory__mutmut_30 # type: ignore # mutmut generated
