from __future__ import annotations

from collections.abc import Mapping
from time import monotonic
from typing import cast

from kubernetes import client

from hexawyn.adapters.secondary.vanilla.adapters._helpers import (
    cpu_to_cores,
    items_from,
    mapping_from,
    mapping_text,
    memory_to_bytes,
    metric_items,
    namespace_age,
    parse_cpu,
    parse_memory,
    percentage,
    restart_count,
    text_attr,
    waiting_reason,
)
from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCoreApi,
    KubernetesMetricsApi,
)
from hexawyn.application.ports.driven.ingress_port import IngressInfo, IngressPort
from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterMetrics,
    K8sPort,
    NamespaceInfo,
    PodInfo,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError
from hexawyn.infrastructure.config.kubeconfig_reader import load_kubeconfig

_POD_CACHE_TTL_SECONDS = 5.0
_FORBIDDEN_STATUS = 403


class VanillaK8sAdapter(K8sPort, IngressPort):
    def __init__(
        self,
        api: KubernetesCoreApi | None,
        metrics_api: KubernetesMetricsApi | None,
        cluster_name: str,
        prometheus_url: str = "",
    ) -> None:
        self._cluster_name = cluster_name
        self._api = api
        self._metrics_api = metrics_api
        self._prometheus_url = prometheus_url
        self._pod_cache: list[PodInfo] | None = None
        self._pod_cache_updated_at = 0.0

    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def get_cluster_metrics(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "default",
        }

    def list_namespaces(self) -> list[NamespaceInfo]:
        try:
            ns_list = self._api_client().list_namespace(timeout_seconds=5)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc
        return [self._to_namespace_info(ns) for ns in items_from(ns_list)]

    def list_ingresses(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def _api_client(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(KubernetesCoreApi, load_kubeconfig(context=self._context_name()))
        return self._api

    def _metrics_api_client(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def _context_name(self) -> str | None:
        return None if self._cluster_name == "unknown" else self._cluster_name

    def _provider_name(self) -> str:
        if self._cluster_name.startswith("kind-"):
            return "kind"
        return "vanilla"

    def _pod_cache_is_fresh(self) -> bool:
        cache_age_seconds = monotonic() - self._pod_cache_updated_at
        return self._pod_cache is not None and cache_age_seconds <= _POD_CACHE_TTL_SECONDS

    def _refresh_pod_cache(self, pods: list[PodInfo]) -> None:
        self._pod_cache = list(pods)
        self._pod_cache_updated_at = monotonic()

    def _list_kubernetes_pods(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def _to_pod_info(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def _resource_requests(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def _pod_status(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "phase", "Unknown")

    def _pod_age(self, metadata: object) -> str:
        return namespace_age(metadata)

    def _to_namespace_info(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def _node_items(self) -> list[object]:
        return items_from(self._api_client().list_node(timeout_seconds=5))

    def _node_metrics_usage(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def _sum_node_metrics(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def _cpu_capacity(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_cpu(node) for node in nodes)

    def _memory_capacity(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_memory(node) for node in nodes)

    def _node_allocatable_cpu(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(mapping_text(alloc, "cpu"))

    def _node_allocatable_memory(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(mapping_text(alloc, "memory"))

    def _node_allocatable(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}


def _translate_ingress_error(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def _to_ingress_info(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "")
        http = getattr(rule, "http", None)
        paths = getattr(http, "paths", None) or []
        if not paths:
            entries.append(_ingress_entry(name, ns, host, "", tls_enabled))
            continue
        for path in paths:
            backend = getattr(path, "backend", None)
            service = getattr(backend, "service", None)
            entries.append(
                _ingress_entry(
                    name,
                    ns,
                    host,
                    str(getattr(service, "name", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def _default_backend_service(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def _ingress_entry(
    name: str,
    namespace: str,
    host: str,
    target_service: str,
    tls_enabled: bool,
) -> IngressInfo:
    return IngressInfo(
        name=name,
        namespace=namespace,
        host=host,
        target_service=target_service,
        tls_enabled=tls_enabled,
    )
