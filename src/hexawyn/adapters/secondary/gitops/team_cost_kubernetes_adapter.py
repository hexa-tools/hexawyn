from __future__ import annotations

from hexawyn.application.ports.driven.team_cost_port import (
    NamespaceResourceData,
    TeamCostPort,
)
from kubernetes import client, config


class TeamCostKubernetesAdapter(TeamCostPort):
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


def _parse_cpu(cpu_str: str) -> int:
    if cpu_str.endswith("m"):
        return int(cpu_str[:-1])
    try:
        return int(float(cpu_str) * 1000)
    except ValueError:
        return 0


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
