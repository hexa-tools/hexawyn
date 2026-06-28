from collections.abc import Mapping, Sequence
from time import monotonic
from typing import Protocol, cast

from kubernetes import client

from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterHealthPort,
    ClusterMetrics,
    Finding,
    K8sPort,
    PodInfo,
)
from hexawyn.infrastructure.config.kubeconfig_reader import load_kubeconfig

_HEALTHY_POD_STATUSES = {"Running", "Succeeded"}
_POD_CACHE_TTL_SECONDS = 5.0


class KubernetesCoreApi(Protocol):
    def list_pod_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List pods across all namespaces."""

    def list_namespaced_pod(self, namespace: str, timeout_seconds: int) -> object:
        """List pods in a namespace."""

    def list_node(self, timeout_seconds: int) -> object:
        """List cluster nodes."""


class KubernetesMetricsApi(Protocol):
    def list_cluster_custom_object(self, group: str, version: str, plural: str) -> object:
        """List cluster-scoped custom objects."""


class VanillaAdapter(K8sPort, ClusterHealthPort):
    """Minimal adapter for vanilla Kubernetes with no cloud provider dependencies."""

    def __init__(
        self,
        cluster_name: str,
        api: KubernetesCoreApi | None = None,
        metrics_api: KubernetesMetricsApi | None = None,
    ) -> None:
        self._cluster_name = cluster_name
        self._api = api
        self._metrics_api = metrics_api
        self._pod_cache: list[PodInfo] | None = None
        self._pod_cache_updated_at = 0.0

    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])

        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in self._items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def get_cluster_metrics(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = self._items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": self._percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": self._percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def get_findings(self) -> list[Finding]:
        return [*self._pod_findings(), *self._node_findings()]

    def get_health_score(self) -> int:
        findings = self.get_findings()
        critical_count = self._severity_count(findings, "critical")
        warning_count = self._severity_count(findings, "warning")
        return max(0, 100 - critical_count * 30 - warning_count * 10)

    def get_health_status(self) -> str:
        findings = self.get_findings()
        if self._severity_count(findings, "critical") > 0:
            return "critical"
        if self._severity_count(findings, "warning") > 0:
            return "degraded"
        return "healthy"

    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "default",
        }

    def _provider_name(self) -> str:
        if self._cluster_name.startswith("kind-"):
            return "kind"
        return "vanilla"

    def _list_kubernetes_pods(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def _api_client(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(KubernetesCoreApi, load_kubeconfig(context=self._context_name()))
        return self._api

    def _context_name(self) -> str | None:
        return None if self._cluster_name == "unknown" else self._cluster_name

    def _pod_cache_is_fresh(self) -> bool:
        cache_age_seconds = monotonic() - self._pod_cache_updated_at
        return self._pod_cache is not None and cache_age_seconds <= _POD_CACHE_TTL_SECONDS

    def _refresh_pod_cache(self, pods: list[PodInfo]) -> None:
        self._pod_cache = list(pods)
        self._pod_cache_updated_at = monotonic()

    def _metrics_api_client(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            self._api_client()
            self._metrics_api = cast(KubernetesMetricsApi, client.CustomObjectsApi())
        return self._metrics_api

    def _to_pod_info(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        status = getattr(pod, "status", None)
        return {
            "name": self._text_attr(metadata, "name", "unknown"),
            "namespace": self._text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": self._restart_count(status),
        }

    def _pod_status(self, status: object) -> str:
        waiting_reason = self._waiting_reason(status)
        if waiting_reason:
            return waiting_reason
        return self._text_attr(status, "phase", "Unknown")

    def _pod_findings(self) -> list[Finding]:
        findings: list[Finding] = []
        for pod in self.list_pods():
            if pod["status"] not in _HEALTHY_POD_STATUSES:
                findings.append(self._unhealthy_pod_finding(pod))
            elif pod["restarts"] > 0:
                findings.append(self._restarted_pod_finding(pod))
        return findings

    def _node_findings(self) -> list[Finding]:
        findings: list[Finding] = []
        for node in self._node_items():
            if not self._node_is_ready(node):
                findings.append(self._not_ready_node_finding(node))
        return findings

    def _unhealthy_pod_finding(self, pod: PodInfo) -> Finding:
        return {
            "severity": "critical" if pod["status"] == "CrashLoop" else "warning",
            "message": f"Pod {pod['namespace']}/{pod['name']} is {pod['status']}",
            "remediation": self._pod_remediation(pod["status"]),
        }

    def _restarted_pod_finding(self, pod: PodInfo) -> Finding:
        return {
            "severity": "warning",
            "message": f"Pod {pod['namespace']}/{pod['name']} restarted {pod['restarts']} times",
            "remediation": "Inspect recent logs and events for this pod.",
        }

    def _not_ready_node_finding(self, node: object) -> Finding:
        node_name = self._text_attr(getattr(node, "metadata", None), "name", "unknown")
        return {
            "severity": "critical",
            "message": f"Node {node_name} is NotReady",
            "remediation": "Inspect node conditions, kubelet status, and recent node events.",
        }

    def _pod_remediation(self, status: str) -> str:
        if status == "CrashLoop":
            return "Inspect container logs, probes, image pull errors, and recent rollout changes."
        if status == "Pending":
            return "Check scheduling events, resource requests, and node capacity."
        return "Inspect pod events and container state for the reported status."

    def _node_is_ready(self, node: object) -> bool:
        node_status = getattr(node, "status", None)
        for condition in self._conditions(node_status):
            if self._text_attr(condition, "type", "") == "Ready":
                return self._text_attr(condition, "status", "False") == "True"
        return False

    def _node_items(self) -> list[object]:
        return self._items_from(self._api_client().list_node(timeout_seconds=5))

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
        for metric in self._metric_items(metrics):
            usage = self._mapping(metric.get("usage"))
            if usage is not None:
                cpu_usage += self._cpu_to_cores(self._mapping_text(usage, "cpu"))
                memory_usage += self._memory_to_bytes(self._mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def _cpu_capacity(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_cpu(node) for node in nodes)

    def _memory_capacity(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_memory(node) for node in nodes)

    def _node_allocatable_cpu(self, node: object) -> float:
        allocatable = self._node_allocatable(node)
        return self._cpu_to_cores(self._mapping_text(allocatable, "cpu"))

    def _node_allocatable_memory(self, node: object) -> float:
        allocatable = self._node_allocatable(node)
        return self._memory_to_bytes(self._mapping_text(allocatable, "memory"))

    def _node_allocatable(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", {})
        mapping = self._mapping(allocatable)
        return mapping if mapping is not None else {}

    def _waiting_reason(self, status: object) -> str | None:
        for container_status in self._container_statuses(status):
            state = getattr(container_status, "state", None)
            waiting = getattr(state, "waiting", None)
            reason = self._optional_text_attr(waiting, "reason")
            if reason:
                return "CrashLoop" if reason == "CrashLoopBackOff" else reason
        return None

    def _restart_count(self, status: object) -> int:
        return sum(
            self._integer_attr(container_status, "restart_count")
            for container_status in self._container_statuses(status)
        )

    def _conditions(self, status: object) -> list[object]:
        conditions = getattr(status, "conditions", [])
        return self._object_sequence(conditions)

    def _container_statuses(self, status: object) -> list[object]:
        container_statuses = getattr(status, "container_statuses", [])
        return self._object_sequence(container_statuses)

    def _items_from(self, item_list: object) -> list[object]:
        items = getattr(item_list, "items", [])
        return self._object_sequence(items)

    def _metric_items(self, metrics: object) -> list[Mapping[object, object]]:
        mapping = self._mapping(metrics)
        if mapping is None:
            return []
        items = mapping.get("items", [])
        return [item for item in self._object_sequence(items) if isinstance(item, Mapping)]

    def _object_sequence(self, value: object) -> list[object]:
        if isinstance(value, Sequence) and not isinstance(value, str | bytes):
            return list(cast(Sequence[object], value))
        return []

    def _mapping(self, value: object) -> Mapping[object, object] | None:
        return value if isinstance(value, Mapping) else None

    def _mapping_text(self, mapping: Mapping[object, object], key: str) -> str:
        value = mapping.get(key, "")
        return value if isinstance(value, str) else ""

    def _text_attr(self, source: object, attr_name: str, default: str) -> str:
        value = self._optional_text_attr(source, attr_name)
        return value if value is not None else default

    def _optional_text_attr(self, source: object, attr_name: str) -> str | None:
        value = getattr(source, attr_name, None)
        if isinstance(value, str) and value:
            return value
        return None

    def _integer_attr(self, source: object, attr_name: str) -> int:
        value = getattr(source, attr_name, 0)
        return value if isinstance(value, int) else 0

    def _cpu_to_cores(self, value: str) -> float:
        if value.endswith("n"):
            return self._float_prefix(value, "n") / 1_000_000_000
        if value.endswith("u"):
            return self._float_prefix(value, "u") / 1_000_000
        if value.endswith("m"):
            return self._float_prefix(value, "m") / 1_000
        return self._safe_float(value)

    def _memory_to_bytes(self, value: str) -> float:
        multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
        for suffix, multiplier in multipliers.items():
            if value.endswith(suffix):
                return self._float_prefix(value, suffix) * multiplier
        return self._safe_float(value)

    def _float_prefix(self, value: str, suffix: str) -> float:
        return self._safe_float(value[: -len(suffix)])

    def _safe_float(self, value: str) -> float:
        try:
            return float(value)
        except ValueError:
            return 0.0

    def _percentage(self, used: float, capacity: float) -> float:
        if capacity <= 0:
            return 0.0
        return round((used / capacity) * 100, 2)

    def _severity_count(self, findings: list[Finding], severity: str) -> int:
        return sum(1 for finding in findings if finding["severity"] == severity)
