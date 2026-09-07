from __future__ import annotations

from collections.abc import Mapping
from time import monotonic
from typing import cast

from kubernetes import client

from hexawyn.application.ports.driven.ingress_port import IngressInfo, IngressPort
from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterMetrics,
    K8sPort,
    NamespaceInfo,
    PodInfo,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters._helpers import (
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
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCoreApi,
    KubernetesMetricsApi,
)
from hexawyn.infrastructure.config.kubeconfig_reader import load_kubeconfig

_POD_CACHE_TTL_SECONDS = 5.0
_FORBIDDEN_STATUS = 403


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁVanillaK8sAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁlist_namespaces__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_context_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_pod_age__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_node_items__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_memory_capacity__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut: MutantDict = {}  # type: ignore


class VanillaK8sAdapter(K8sPort, IngressPort):
    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ__init____mutmut)
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
    def xǁVanillaK8sAdapterǁ__init____mutmut_orig(
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
    def xǁVanillaK8sAdapterǁ__init____mutmut_1(
        self,
        api: KubernetesCoreApi | None,
        metrics_api: KubernetesMetricsApi | None,
        cluster_name: str,
        prometheus_url: str = "XXXX",
    ) -> None:
        self._cluster_name = cluster_name
        self._api = api
        self._metrics_api = metrics_api
        self._prometheus_url = prometheus_url
        self._pod_cache: list[PodInfo] | None = None
        self._pod_cache_updated_at = 0.0
    def xǁVanillaK8sAdapterǁ__init____mutmut_2(
        self,
        api: KubernetesCoreApi | None,
        metrics_api: KubernetesMetricsApi | None,
        cluster_name: str,
        prometheus_url: str = "",
    ) -> None:
        self._cluster_name = None
        self._api = api
        self._metrics_api = metrics_api
        self._prometheus_url = prometheus_url
        self._pod_cache: list[PodInfo] | None = None
        self._pod_cache_updated_at = 0.0
    def xǁVanillaK8sAdapterǁ__init____mutmut_3(
        self,
        api: KubernetesCoreApi | None,
        metrics_api: KubernetesMetricsApi | None,
        cluster_name: str,
        prometheus_url: str = "",
    ) -> None:
        self._cluster_name = cluster_name
        self._api = None
        self._metrics_api = metrics_api
        self._prometheus_url = prometheus_url
        self._pod_cache: list[PodInfo] | None = None
        self._pod_cache_updated_at = 0.0
    def xǁVanillaK8sAdapterǁ__init____mutmut_4(
        self,
        api: KubernetesCoreApi | None,
        metrics_api: KubernetesMetricsApi | None,
        cluster_name: str,
        prometheus_url: str = "",
    ) -> None:
        self._cluster_name = cluster_name
        self._api = api
        self._metrics_api = None
        self._prometheus_url = prometheus_url
        self._pod_cache: list[PodInfo] | None = None
        self._pod_cache_updated_at = 0.0
    def xǁVanillaK8sAdapterǁ__init____mutmut_5(
        self,
        api: KubernetesCoreApi | None,
        metrics_api: KubernetesMetricsApi | None,
        cluster_name: str,
        prometheus_url: str = "",
    ) -> None:
        self._cluster_name = cluster_name
        self._api = api
        self._metrics_api = metrics_api
        self._prometheus_url = None
        self._pod_cache: list[PodInfo] | None = None
        self._pod_cache_updated_at = 0.0
    def xǁVanillaK8sAdapterǁ__init____mutmut_6(
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
        self._pod_cache: list[PodInfo] | None = ""
        self._pod_cache_updated_at = 0.0
    def xǁVanillaK8sAdapterǁ__init____mutmut_7(
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
        self._pod_cache_updated_at = None
    def xǁVanillaK8sAdapterǁ__init____mutmut_8(
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
        self._pod_cache_updated_at = 1.0

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut)
    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_orig(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_1(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None or self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_2(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is not None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_3(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(None)
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_4(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache and [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_5(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = None
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_6(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(None)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_7(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = None
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_8(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(None) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_9(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(None)]
        if namespace is None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_10(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is not None:
            self._refresh_pod_cache(pods)
        return pods

    def xǁVanillaK8sAdapterǁlist_pods__mutmut_11(self, namespace: str | None = None) -> list[PodInfo]:
        if namespace is None and self._pod_cache_is_fresh():
            return list(self._pod_cache or [])
        pod_list = self._list_kubernetes_pods(namespace)
        pods = [self._to_pod_info(pod) for pod in items_from(pod_list)]
        if namespace is None:
            self._refresh_pod_cache(None)
        return pods

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut)
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

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_orig(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_1(self) -> ClusterMetrics:
        nodes = None
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_2(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = None
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_3(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(None)
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_4(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = None
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_5(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "XXcpu_usage_pctXX": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_6(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "CPU_USAGE_PCT": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_7(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(None, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_8(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, None),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_9(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_10(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, ),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_11(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(None)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_12(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "XXmemory_usage_pctXX": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_13(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "MEMORY_USAGE_PCT": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_14(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(None, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_15(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, None),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_16(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_17(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, ),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_18(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(None)),
            "node_count": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_19(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "XXnode_countXX": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_20(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "NODE_COUNT": len(nodes),
            "pod_count": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_21(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "XXpod_countXX": len(pods),
        }

    def xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_22(self) -> ClusterMetrics:
        nodes = self._node_items()
        pods = items_from(self._list_kubernetes_pods(namespace=None))
        cpu_usage, memory_usage = self._node_metrics_usage()
        return {
            "cpu_usage_pct": percentage(cpu_usage, self._cpu_capacity(nodes)),
            "memory_usage_pct": percentage(memory_usage, self._memory_capacity(nodes)),
            "node_count": len(nodes),
            "POD_COUNT": len(pods),
        }

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut)
    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_orig(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_1(self) -> ClusterContext:
        return {
            "XXnameXX": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_2(self) -> ClusterContext:
        return {
            "NAME": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_3(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "XXclusterXX": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_4(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "CLUSTER": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_5(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "XXproviderXX": self._provider_name(),
            "namespace": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_6(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "PROVIDER": self._provider_name(),
            "namespace": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_7(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "XXnamespaceXX": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_8(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "NAMESPACE": "default",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_9(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "XXdefaultXX",
        }

    def xǁVanillaK8sAdapterǁget_cluster_context__mutmut_10(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": self._provider_name(),
            "namespace": "DEFAULT",
        }

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁlist_namespaces__mutmut)
    def list_namespaces(self) -> list[NamespaceInfo]:
        try:
            ns_list = self._api_client().list_namespace(timeout_seconds=5)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc
        return [self._to_namespace_info(ns) for ns in items_from(ns_list)]

    def xǁVanillaK8sAdapterǁlist_namespaces__mutmut_orig(self) -> list[NamespaceInfo]:
        try:
            ns_list = self._api_client().list_namespace(timeout_seconds=5)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc
        return [self._to_namespace_info(ns) for ns in items_from(ns_list)]

    def xǁVanillaK8sAdapterǁlist_namespaces__mutmut_1(self) -> list[NamespaceInfo]:
        try:
            ns_list = None
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc
        return [self._to_namespace_info(ns) for ns in items_from(ns_list)]

    def xǁVanillaK8sAdapterǁlist_namespaces__mutmut_2(self) -> list[NamespaceInfo]:
        try:
            ns_list = self._api_client().list_namespace(timeout_seconds=None)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc
        return [self._to_namespace_info(ns) for ns in items_from(ns_list)]

    def xǁVanillaK8sAdapterǁlist_namespaces__mutmut_3(self) -> list[NamespaceInfo]:
        try:
            ns_list = self._api_client().list_namespace(timeout_seconds=6)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc
        return [self._to_namespace_info(ns) for ns in items_from(ns_list)]

    def xǁVanillaK8sAdapterǁlist_namespaces__mutmut_4(self) -> list[NamespaceInfo]:
        try:
            ns_list = self._api_client().list_namespace(timeout_seconds=5)
        except Exception as exc:
            raise ClusterUnreachableError(None) from exc
        return [self._to_namespace_info(ns) for ns in items_from(ns_list)]

    def xǁVanillaK8sAdapterǁlist_namespaces__mutmut_5(self) -> list[NamespaceInfo]:
        try:
            ns_list = self._api_client().list_namespace(timeout_seconds=5)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc
        return [self._to_namespace_info(None) for ns in items_from(ns_list)]

    def xǁVanillaK8sAdapterǁlist_namespaces__mutmut_6(self) -> list[NamespaceInfo]:
        try:
            ns_list = self._api_client().list_namespace(timeout_seconds=5)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list namespaces: {exc}") from exc
        return [self._to_namespace_info(ns) for ns in items_from(None)]

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut)
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

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_orig(self, namespace: str) -> list[IngressInfo]:
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

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_1(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = None
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

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_2(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(None, self._api_client())
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

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_3(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, None)
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

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_4(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(self._api_client())
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

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_5(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, )
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

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_6(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = None
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_7(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=None)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_8(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = None
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_9(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=None, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_10(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=None
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_11(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_12(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_13(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=6
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_14(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(None, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_15(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, None) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_16(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_17(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, ) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_18(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = None
        for ingress in items_from(ingress_list):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_19(self, namespace: str) -> list[IngressInfo]:
        try:
            core_api = cast(client.CoreV1Api, self._api_client())
            networking_api = client.NetworkingV1Api(api_client=core_api.api_client)
            ingress_list = networking_api.list_namespaced_ingress(
                namespace=namespace, timeout_seconds=5
            )
        except Exception as exc:
            raise _translate_ingress_error(namespace, exc) from exc
        entries: list[IngressInfo] = []
        for ingress in items_from(None):
            entries.extend(_to_ingress_info(ingress, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_20(self, namespace: str) -> list[IngressInfo]:
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
            entries.extend(None)
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_21(self, namespace: str) -> list[IngressInfo]:
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
            entries.extend(_to_ingress_info(None, namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_22(self, namespace: str) -> list[IngressInfo]:
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
            entries.extend(_to_ingress_info(ingress, None))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_23(self, namespace: str) -> list[IngressInfo]:
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
            entries.extend(_to_ingress_info(namespace))
        return entries

    def xǁVanillaK8sAdapterǁlist_ingresses__mutmut_24(self, namespace: str) -> list[IngressInfo]:
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
            entries.extend(_to_ingress_info(ingress, ))
        return entries

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut)
    def _api_client(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(KubernetesCoreApi, load_kubeconfig(context=self._context_name()))
        return self._api

    def xǁVanillaK8sAdapterǁ_api_client__mutmut_orig(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(KubernetesCoreApi, load_kubeconfig(context=self._context_name()))
        return self._api

    def xǁVanillaK8sAdapterǁ_api_client__mutmut_1(self) -> KubernetesCoreApi:
        if self._api is not None:
            self._api = cast(KubernetesCoreApi, load_kubeconfig(context=self._context_name()))
        return self._api

    def xǁVanillaK8sAdapterǁ_api_client__mutmut_2(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = None
        return self._api

    def xǁVanillaK8sAdapterǁ_api_client__mutmut_3(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(None, load_kubeconfig(context=self._context_name()))
        return self._api

    def xǁVanillaK8sAdapterǁ_api_client__mutmut_4(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(KubernetesCoreApi, None)
        return self._api

    def xǁVanillaK8sAdapterǁ_api_client__mutmut_5(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(load_kubeconfig(context=self._context_name()))
        return self._api

    def xǁVanillaK8sAdapterǁ_api_client__mutmut_6(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(KubernetesCoreApi, )
        return self._api

    def xǁVanillaK8sAdapterǁ_api_client__mutmut_7(self) -> KubernetesCoreApi:
        if self._api is None:
            self._api = cast(KubernetesCoreApi, load_kubeconfig(context=None))
        return self._api

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut)
    def _metrics_api_client(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_orig(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_1(self) -> KubernetesMetricsApi:
        if self._metrics_api is not None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_2(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = None
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_3(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(None, self._api_client())
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_4(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, None)
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_5(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(self._api_client())
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_6(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, )
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_7(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = None
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_8(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = cast(
                None, client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_9(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = cast(
                KubernetesMetricsApi, None
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_10(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = cast(
                client.CustomObjectsApi(api_client=core_api.api_client)
            )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_11(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = cast(
                KubernetesMetricsApi, )
        return self._metrics_api

    def xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_12(self) -> KubernetesMetricsApi:
        if self._metrics_api is None:
            core_api = cast(client.CoreV1Api, self._api_client())
            self._metrics_api = cast(
                KubernetesMetricsApi, client.CustomObjectsApi(api_client=None)
            )
        return self._metrics_api

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_context_name__mutmut)
    def _context_name(self) -> str | None:
        return None if self._cluster_name == "unknown" else self._cluster_name

    def xǁVanillaK8sAdapterǁ_context_name__mutmut_orig(self) -> str | None:
        return None if self._cluster_name == "unknown" else self._cluster_name

    def xǁVanillaK8sAdapterǁ_context_name__mutmut_1(self) -> str | None:
        return None if self._cluster_name != "unknown" else self._cluster_name

    def xǁVanillaK8sAdapterǁ_context_name__mutmut_2(self) -> str | None:
        return None if self._cluster_name == "XXunknownXX" else self._cluster_name

    def xǁVanillaK8sAdapterǁ_context_name__mutmut_3(self) -> str | None:
        return None if self._cluster_name == "UNKNOWN" else self._cluster_name

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut)
    def _provider_name(self) -> str:
        if self._cluster_name.startswith("kind-"):
            return "kind"
        return "vanilla"

    def xǁVanillaK8sAdapterǁ_provider_name__mutmut_orig(self) -> str:
        if self._cluster_name.startswith("kind-"):
            return "kind"
        return "vanilla"

    def xǁVanillaK8sAdapterǁ_provider_name__mutmut_1(self) -> str:
        if self._cluster_name.startswith(None):
            return "kind"
        return "vanilla"

    def xǁVanillaK8sAdapterǁ_provider_name__mutmut_2(self) -> str:
        if self._cluster_name.startswith("XXkind-XX"):
            return "kind"
        return "vanilla"

    def xǁVanillaK8sAdapterǁ_provider_name__mutmut_3(self) -> str:
        if self._cluster_name.startswith("KIND-"):
            return "kind"
        return "vanilla"

    def xǁVanillaK8sAdapterǁ_provider_name__mutmut_4(self) -> str:
        if self._cluster_name.startswith("kind-"):
            return "XXkindXX"
        return "vanilla"

    def xǁVanillaK8sAdapterǁ_provider_name__mutmut_5(self) -> str:
        if self._cluster_name.startswith("kind-"):
            return "KIND"
        return "vanilla"

    def xǁVanillaK8sAdapterǁ_provider_name__mutmut_6(self) -> str:
        if self._cluster_name.startswith("kind-"):
            return "kind"
        return "XXvanillaXX"

    def xǁVanillaK8sAdapterǁ_provider_name__mutmut_7(self) -> str:
        if self._cluster_name.startswith("kind-"):
            return "kind"
        return "VANILLA"

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut)
    def _pod_cache_is_fresh(self) -> bool:
        cache_age_seconds = monotonic() - self._pod_cache_updated_at
        return self._pod_cache is not None and cache_age_seconds <= _POD_CACHE_TTL_SECONDS

    def xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_orig(self) -> bool:
        cache_age_seconds = monotonic() - self._pod_cache_updated_at
        return self._pod_cache is not None and cache_age_seconds <= _POD_CACHE_TTL_SECONDS

    def xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_1(self) -> bool:
        cache_age_seconds = None
        return self._pod_cache is not None and cache_age_seconds <= _POD_CACHE_TTL_SECONDS

    def xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_2(self) -> bool:
        cache_age_seconds = monotonic() + self._pod_cache_updated_at
        return self._pod_cache is not None and cache_age_seconds <= _POD_CACHE_TTL_SECONDS

    def xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_3(self) -> bool:
        cache_age_seconds = monotonic() - self._pod_cache_updated_at
        return self._pod_cache is not None or cache_age_seconds <= _POD_CACHE_TTL_SECONDS

    def xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_4(self) -> bool:
        cache_age_seconds = monotonic() - self._pod_cache_updated_at
        return self._pod_cache is None and cache_age_seconds <= _POD_CACHE_TTL_SECONDS

    def xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_5(self) -> bool:
        cache_age_seconds = monotonic() - self._pod_cache_updated_at
        return self._pod_cache is not None and cache_age_seconds < _POD_CACHE_TTL_SECONDS

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut)
    def _refresh_pod_cache(self, pods: list[PodInfo]) -> None:
        self._pod_cache = list(pods)
        self._pod_cache_updated_at = monotonic()

    def xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_orig(self, pods: list[PodInfo]) -> None:
        self._pod_cache = list(pods)
        self._pod_cache_updated_at = monotonic()

    def xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_1(self, pods: list[PodInfo]) -> None:
        self._pod_cache = None
        self._pod_cache_updated_at = monotonic()

    def xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_2(self, pods: list[PodInfo]) -> None:
        self._pod_cache = list(None)
        self._pod_cache_updated_at = monotonic()

    def xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_3(self, pods: list[PodInfo]) -> None:
        self._pod_cache = list(pods)
        self._pod_cache_updated_at = None

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut)
    def _list_kubernetes_pods(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_orig(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_1(self, namespace: str | None) -> object:
        api = None
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_2(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=None, timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_3(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=None)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_4(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_5(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, )
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_6(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=6)
        return api.list_pod_for_all_namespaces(timeout_seconds=5)

    def xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_7(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=None)

    def xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_8(self, namespace: str | None) -> object:
        api = self._api_client()
        if namespace:
            return api.list_namespaced_pod(namespace=namespace, timeout_seconds=5)
        return api.list_pod_for_all_namespaces(timeout_seconds=6)

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_orig(self, pod: object) -> PodInfo:
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_1(self, pod: object) -> PodInfo:
        metadata = None
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_2(self, pod: object) -> PodInfo:
        metadata = getattr(None, "metadata", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_3(self, pod: object) -> PodInfo:
        metadata = getattr(pod, None, None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_4(self, pod: object) -> PodInfo:
        metadata = getattr("metadata", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_5(self, pod: object) -> PodInfo:
        metadata = getattr(pod, None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_6(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", )
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_7(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "XXmetadataXX", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_8(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "METADATA", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_9(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = None
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_10(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(None, "spec", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_11(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, None, None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_12(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr("spec", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_13(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_14(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", )
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_15(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "XXspecXX", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_16(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "SPEC", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_17(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = None
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_18(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(None, "status", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_19(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, None, None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_20(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr("status", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_21(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_22(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", )
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_23(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "XXstatusXX", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_24(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "STATUS", None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_25(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = None
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_26(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(None)
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

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_27(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "XXnameXX": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_28(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "NAME": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_29(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(None, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_30(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, None, "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_31(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", None),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_32(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr("name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_33(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_34(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", ),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_35(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "XXnameXX", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_36(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "NAME", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_37(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "XXunknownXX"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_38(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "UNKNOWN"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_39(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "XXnamespaceXX": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_40(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "NAMESPACE": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_41(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(None, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_42(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, None, "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_43(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", None),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_44(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr("namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_45(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_46(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", ),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_47(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "XXnamespaceXX", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_48(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "NAMESPACE", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_49(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "XXdefaultXX"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_50(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "DEFAULT"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_51(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "XXstatusXX": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_52(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "STATUS": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_53(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(None),
            "restarts": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_54(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "XXrestartsXX": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_55(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "RESTARTS": restart_count(status),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_56(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(None),
            "age": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_57(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "XXageXX": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_58(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "AGE": self._pod_age(metadata),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_59(self, pod: object) -> PodInfo:
        metadata = getattr(pod, "metadata", None)
        spec = getattr(pod, "spec", None)
        status = getattr(pod, "status", None)
        cpu_req, mem_req = self._resource_requests(spec)
        return {
            "name": text_attr(metadata, "name", "unknown"),
            "namespace": text_attr(metadata, "namespace", "default"),
            "status": self._pod_status(status),
            "restarts": restart_count(status),
            "age": self._pod_age(None),
            "node": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_60(self, pod: object) -> PodInfo:
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
            "XXnodeXX": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_61(self, pod: object) -> PodInfo:
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
            "NODE": text_attr(spec, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_62(self, pod: object) -> PodInfo:
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
            "node": text_attr(None, "node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_63(self, pod: object) -> PodInfo:
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
            "node": text_attr(spec, None, "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_64(self, pod: object) -> PodInfo:
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
            "node": text_attr(spec, "node_name", None),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_65(self, pod: object) -> PodInfo:
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
            "node": text_attr("node_name", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_66(self, pod: object) -> PodInfo:
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
            "node": text_attr(spec, "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_67(self, pod: object) -> PodInfo:
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
            "node": text_attr(spec, "node_name", ),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_68(self, pod: object) -> PodInfo:
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
            "node": text_attr(spec, "XXnode_nameXX", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_69(self, pod: object) -> PodInfo:
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
            "node": text_attr(spec, "NODE_NAME", "unknown"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_70(self, pod: object) -> PodInfo:
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
            "node": text_attr(spec, "node_name", "XXunknownXX"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_71(self, pod: object) -> PodInfo:
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
            "node": text_attr(spec, "node_name", "UNKNOWN"),
            "cpu_request_millicores": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_72(self, pod: object) -> PodInfo:
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
            "XXcpu_request_millicoresXX": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_73(self, pod: object) -> PodInfo:
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
            "CPU_REQUEST_MILLICORES": cpu_req,
            "memory_request_mib": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_74(self, pod: object) -> PodInfo:
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
            "XXmemory_request_mibXX": mem_req,
        }

    def xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_75(self, pod: object) -> PodInfo:
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
            "MEMORY_REQUEST_MIB": mem_req,
        }

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut)
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_orig(self, spec: object) -> tuple[int, int]:
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_1(self, spec: object) -> tuple[int, int]:
        cpu = None
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_2(self, spec: object) -> tuple[int, int]:
        cpu = 1
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_3(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = None
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_4(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 1
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_5(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = None
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_6(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) and []
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_7(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(None, "containers", []) or []
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_8(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, None, []) or []
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_9(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", None) or []
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_10(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr("containers", []) or []
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_11(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, []) or []
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_12(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", ) or []
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_13(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "XXcontainersXX", []) or []
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_14(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "CONTAINERS", []) or []
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_15(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = None
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_16(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(None, "resources", None)
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_17(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, None, None)
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_18(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr("resources", None)
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_19(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, None)
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_20(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", )
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_21(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "XXresourcesXX", None)
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_22(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "RESOURCES", None)
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

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_23(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is not None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_24(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    break
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_25(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = None
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_26(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) and {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_27(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(None, "requests", None) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_28(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, None, None) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_29(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr("requests", None) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_30(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, None) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_31(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", ) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_32(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "XXrequestsXX", None) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_33(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "REQUESTS", None) or {}
                cpu_str = requests.get("cpu", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_34(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = None
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_35(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get(None, "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_36(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get("cpu", None)
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_37(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get("0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_38(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get("cpu", )
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_39(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get("XXcpuXX", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_40(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get("CPU", "0")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_41(self, spec: object) -> tuple[int, int]:
        cpu = 0
        mem = 0
        try:
            containers = getattr(spec, "containers", []) or []
            for container in containers:
                resources = getattr(container, "resources", None)
                if resources is None:
                    continue
                requests = getattr(resources, "requests", None) or {}
                cpu_str = requests.get("cpu", "XX0XX")
                mem_str = requests.get("memory", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_42(self, spec: object) -> tuple[int, int]:
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
                mem_str = None
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_43(self, spec: object) -> tuple[int, int]:
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
                mem_str = requests.get(None, "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_44(self, spec: object) -> tuple[int, int]:
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
                mem_str = requests.get("memory", None)
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_45(self, spec: object) -> tuple[int, int]:
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
                mem_str = requests.get("0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_46(self, spec: object) -> tuple[int, int]:
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
                mem_str = requests.get("memory", )
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_47(self, spec: object) -> tuple[int, int]:
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
                mem_str = requests.get("XXmemoryXX", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_48(self, spec: object) -> tuple[int, int]:
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
                mem_str = requests.get("MEMORY", "0")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_49(self, spec: object) -> tuple[int, int]:
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
                mem_str = requests.get("memory", "XX0XX")
                cpu += parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_50(self, spec: object) -> tuple[int, int]:
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
                cpu = parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_51(self, spec: object) -> tuple[int, int]:
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
                cpu -= parse_cpu(cpu_str)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_52(self, spec: object) -> tuple[int, int]:
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
                cpu += parse_cpu(None)
                mem += parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_53(self, spec: object) -> tuple[int, int]:
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
                mem = parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_54(self, spec: object) -> tuple[int, int]:
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
                mem -= parse_memory(mem_str)
        except Exception:
            pass
        return cpu, mem

    def xǁVanillaK8sAdapterǁ_resource_requests__mutmut_55(self, spec: object) -> tuple[int, int]:
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
                mem += parse_memory(None)
        except Exception:
            pass
        return cpu, mem

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut)
    def _pod_status(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "phase", "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_orig(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "phase", "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_1(self, status: object) -> str:
        reason = None
        if reason:
            return reason
        return text_attr(status, "phase", "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_2(self, status: object) -> str:
        reason = waiting_reason(None)
        if reason:
            return reason
        return text_attr(status, "phase", "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_3(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(None, "phase", "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_4(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, None, "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_5(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "phase", None)

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_6(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr("phase", "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_7(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_8(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "phase", )

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_9(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "XXphaseXX", "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_10(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "PHASE", "Unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_11(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "phase", "XXUnknownXX")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_12(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "phase", "unknown")

    def xǁVanillaK8sAdapterǁ_pod_status__mutmut_13(self, status: object) -> str:
        reason = waiting_reason(status)
        if reason:
            return reason
        return text_attr(status, "phase", "UNKNOWN")

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_pod_age__mutmut)
    def _pod_age(self, metadata: object) -> str:
        return namespace_age(metadata)

    def xǁVanillaK8sAdapterǁ_pod_age__mutmut_orig(self, metadata: object) -> str:
        return namespace_age(metadata)

    def xǁVanillaK8sAdapterǁ_pod_age__mutmut_1(self, metadata: object) -> str:
        return namespace_age(None)

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut)
    def _to_namespace_info(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_orig(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_1(self, ns: object) -> NamespaceInfo:
        metadata = None
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_2(self, ns: object) -> NamespaceInfo:
        metadata = getattr(None, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_3(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, None, None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_4(self, ns: object) -> NamespaceInfo:
        metadata = getattr("metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_5(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_6(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", )
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_7(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "XXmetadataXX", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_8(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "METADATA", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_9(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = None
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_10(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(None, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_11(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, None, "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_12(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", None)
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_13(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr("name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_14(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_15(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", )
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_16(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "XXnameXX", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_17(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "NAME", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_18(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "XXunknownXX")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_19(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "UNKNOWN")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_20(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = None
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_21(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(None, "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_22(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), None, "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_23(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", None)
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_24(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr("phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_25(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_26(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", )
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_27(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(None, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_28(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, None, None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_29(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr("status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_30(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_31(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", ), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_32(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "XXstatusXX", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_33(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "STATUS", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_34(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "XXphaseXX", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_35(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "PHASE", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_36(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "XXActiveXX")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_37(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_38(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "ACTIVE")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_39(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = None
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_40(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(None)
        return {"name": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_41(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"XXnameXX": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_42(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"NAME": name, "status": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_43(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "XXstatusXX": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_44(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "STATUS": status, "age": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_45(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "XXageXX": age}

    def xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_46(self, ns: object) -> NamespaceInfo:
        metadata = getattr(ns, "metadata", None)
        name = text_attr(metadata, "name", "unknown")
        status = text_attr(getattr(ns, "status", None), "phase", "Active")
        age = namespace_age(metadata)
        return {"name": name, "status": status, "AGE": age}

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_node_items__mutmut)
    def _node_items(self) -> list[object]:
        return items_from(self._api_client().list_node(timeout_seconds=5))

    def xǁVanillaK8sAdapterǁ_node_items__mutmut_orig(self) -> list[object]:
        return items_from(self._api_client().list_node(timeout_seconds=5))

    def xǁVanillaK8sAdapterǁ_node_items__mutmut_1(self) -> list[object]:
        return items_from(None)

    def xǁVanillaK8sAdapterǁ_node_items__mutmut_2(self) -> list[object]:
        return items_from(self._api_client().list_node(timeout_seconds=None))

    def xǁVanillaK8sAdapterǁ_node_items__mutmut_3(self) -> list[object]:
        return items_from(self._api_client().list_node(timeout_seconds=6))

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut)
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

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_orig(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_1(self) -> tuple[float, float]:
        try:
            metrics = None
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_2(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group=None,
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_3(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version=None,
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_4(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural=None,
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_5(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_6(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_7(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_8(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="XXmetrics.k8s.ioXX",
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_9(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="METRICS.K8S.IO",
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_10(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="XXv1beta1XX",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_11(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="V1BETA1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_12(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="XXnodesXX",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_13(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="NODES",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_14(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 1.0, 0.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_15(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 1.0
        return self._sum_node_metrics(metrics)

    def xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_16(self) -> tuple[float, float]:
        try:
            metrics = self._metrics_api_client().list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="nodes",
            )
        except Exception:
            return 0.0, 0.0
        return self._sum_node_metrics(None)

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut)
    def _sum_node_metrics(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_orig(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_1(self, metrics: object) -> tuple[float, float]:
        cpu_usage = None
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_2(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 1.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_3(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = None
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_4(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 1.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_5(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(None):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_6(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = None
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_7(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(None)
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_8(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get(None))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_9(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("XXusageXX"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_10(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("USAGE"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_11(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_12(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage = cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_13(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage -= cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_14(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(None)
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_15(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(None, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_16(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, None))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_17(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text("cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_18(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, ))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_19(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "XXcpuXX"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_20(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "CPU"))
                memory_usage += memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_21(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage = memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_22(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage -= memory_to_bytes(mapping_text(usage, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_23(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(None)
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_24(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(None, "memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_25(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, None))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_26(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text("memory"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_27(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, ))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_28(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "XXmemoryXX"))
        return cpu_usage, memory_usage

    def xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_29(self, metrics: object) -> tuple[float, float]:
        cpu_usage = 0.0
        memory_usage = 0.0
        for metric in metric_items(metrics):
            usage = mapping_from(metric.get("usage"))
            if usage is not None:
                cpu_usage += cpu_to_cores(mapping_text(usage, "cpu"))
                memory_usage += memory_to_bytes(mapping_text(usage, "MEMORY"))
        return cpu_usage, memory_usage

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut)
    def _cpu_capacity(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_cpu(node) for node in nodes)

    def xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut_orig(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_cpu(node) for node in nodes)

    def xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut_1(self, nodes: list[object]) -> float:
        return sum(None)

    def xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut_2(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_cpu(None) for node in nodes)

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_memory_capacity__mutmut)
    def _memory_capacity(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_memory(node) for node in nodes)

    def xǁVanillaK8sAdapterǁ_memory_capacity__mutmut_orig(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_memory(node) for node in nodes)

    def xǁVanillaK8sAdapterǁ_memory_capacity__mutmut_1(self, nodes: list[object]) -> float:
        return sum(None)

    def xǁVanillaK8sAdapterǁ_memory_capacity__mutmut_2(self, nodes: list[object]) -> float:
        return sum(self._node_allocatable_memory(None) for node in nodes)

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut)
    def _node_allocatable_cpu(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(mapping_text(alloc, "cpu"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_orig(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(mapping_text(alloc, "cpu"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_1(self, node: object) -> float:
        alloc = None
        return cpu_to_cores(mapping_text(alloc, "cpu"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_2(self, node: object) -> float:
        alloc = self._node_allocatable(None)
        return cpu_to_cores(mapping_text(alloc, "cpu"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_3(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(None)

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_4(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(mapping_text(None, "cpu"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_5(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(mapping_text(alloc, None))

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_6(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(mapping_text("cpu"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_7(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(mapping_text(alloc, ))

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_8(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(mapping_text(alloc, "XXcpuXX"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_9(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return cpu_to_cores(mapping_text(alloc, "CPU"))

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut)
    def _node_allocatable_memory(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(mapping_text(alloc, "memory"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_orig(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(mapping_text(alloc, "memory"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_1(self, node: object) -> float:
        alloc = None
        return memory_to_bytes(mapping_text(alloc, "memory"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_2(self, node: object) -> float:
        alloc = self._node_allocatable(None)
        return memory_to_bytes(mapping_text(alloc, "memory"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_3(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(None)

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_4(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(mapping_text(None, "memory"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_5(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(mapping_text(alloc, None))

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_6(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(mapping_text("memory"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_7(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(mapping_text(alloc, ))

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_8(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(mapping_text(alloc, "XXmemoryXX"))

    def xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_9(self, node: object) -> float:
        alloc = self._node_allocatable(node)
        return memory_to_bytes(mapping_text(alloc, "MEMORY"))

    @_mutmut_mutated(mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut)
    def _node_allocatable(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_orig(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_1(self, node: object) -> Mapping[object, object]:
        node_status = None
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_2(self, node: object) -> Mapping[object, object]:
        node_status = getattr(None, "status", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_3(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, None, None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_4(self, node: object) -> Mapping[object, object]:
        node_status = getattr("status", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_5(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_6(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", )
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_7(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "XXstatusXX", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_8(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "STATUS", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_9(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = None
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_10(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(None, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_11(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, None, {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_12(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", None)
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_13(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr("allocatable", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_14(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_15(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", )
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_16(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "XXallocatableXX", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_17(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "ALLOCATABLE", {})
        m = mapping_from(allocatable)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_18(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = None
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_19(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(None)
        return m if m is not None else {}

    def xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_20(self, node: object) -> Mapping[object, object]:
        node_status = getattr(node, "status", None)
        allocatable = getattr(node_status, "allocatable", {})
        m = mapping_from(allocatable)
        return m if m is None else {}

mutants_xǁVanillaK8sAdapterǁ__init____mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ__init____mutmut['xǁVanillaK8sAdapterǁ__init____mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ__init____mutmut['xǁVanillaK8sAdapterǁ__init____mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ__init____mutmut['xǁVanillaK8sAdapterǁ__init____mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ__init____mutmut['xǁVanillaK8sAdapterǁ__init____mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ__init____mutmut['xǁVanillaK8sAdapterǁ__init____mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ__init____mutmut['xǁVanillaK8sAdapterǁ__init____mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ__init____mutmut['xǁVanillaK8sAdapterǁ__init____mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ__init____mutmut['xǁVanillaK8sAdapterǁ__init____mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_pods__mutmut['xǁVanillaK8sAdapterǁlist_pods__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_pods__mutmut_11 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_13'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_14'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_15'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_16'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_17'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_18'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_19'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_20'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_21'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut['xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_22'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_metrics__mutmut_22 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁget_cluster_context__mutmut['xǁVanillaK8sAdapterǁget_cluster_context__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁget_cluster_context__mutmut_10 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁlist_namespaces__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_namespaces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_namespaces__mutmut['xǁVanillaK8sAdapterǁlist_namespaces__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_namespaces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_namespaces__mutmut['xǁVanillaK8sAdapterǁlist_namespaces__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_namespaces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_namespaces__mutmut['xǁVanillaK8sAdapterǁlist_namespaces__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_namespaces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_namespaces__mutmut['xǁVanillaK8sAdapterǁlist_namespaces__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_namespaces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_namespaces__mutmut['xǁVanillaK8sAdapterǁlist_namespaces__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_namespaces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_namespaces__mutmut['xǁVanillaK8sAdapterǁlist_namespaces__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_namespaces__mutmut_6 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_13'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_14'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_15'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_16'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_17'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_18'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_19'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_20'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_21'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_22'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_23'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁlist_ingresses__mutmut['xǁVanillaK8sAdapterǁlist_ingresses__mutmut_24'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁlist_ingresses__mutmut_24 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut['xǁVanillaK8sAdapterǁ_api_client__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut['xǁVanillaK8sAdapterǁ_api_client__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut['xǁVanillaK8sAdapterǁ_api_client__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut['xǁVanillaK8sAdapterǁ_api_client__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut['xǁVanillaK8sAdapterǁ_api_client__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut['xǁVanillaK8sAdapterǁ_api_client__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_api_client__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_api_client__mutmut['xǁVanillaK8sAdapterǁ_api_client__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_api_client__mutmut_7 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut['xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_metrics_api_client__mutmut_12 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_context_name__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_context_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_context_name__mutmut['xǁVanillaK8sAdapterǁ_context_name__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_context_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_context_name__mutmut['xǁVanillaK8sAdapterǁ_context_name__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_context_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_context_name__mutmut['xǁVanillaK8sAdapterǁ_context_name__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_context_name__mutmut_3 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_provider_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut['xǁVanillaK8sAdapterǁ_provider_name__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_provider_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut['xǁVanillaK8sAdapterǁ_provider_name__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_provider_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut['xǁVanillaK8sAdapterǁ_provider_name__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_provider_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut['xǁVanillaK8sAdapterǁ_provider_name__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_provider_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut['xǁVanillaK8sAdapterǁ_provider_name__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_provider_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut['xǁVanillaK8sAdapterǁ_provider_name__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_provider_name__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_provider_name__mutmut['xǁVanillaK8sAdapterǁ_provider_name__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_provider_name__mutmut_7 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut['xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut['xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut['xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut['xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut['xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_cache_is_fresh__mutmut_5 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut['xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut['xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut['xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_refresh_pod_cache__mutmut_3 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut['xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut['xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut['xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut['xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut['xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut['xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut['xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut['xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_list_kubernetes_pods__mutmut_8 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_13'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_14'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_15'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_16'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_17'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_18'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_19'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_20'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_21'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_22'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_23'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_24'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_25'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_26'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_27'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_28'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_29'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_30'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_31'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_32'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_33'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_34'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_35'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_36'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_37'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_38'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_39'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_40'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_41'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_42'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_43'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_44'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_45'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_46'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_47'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_48'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_49'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_50'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_51'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_52'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_53'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_54'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_55'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_56'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_57'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_58'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_59'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_60'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_61'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_62'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_63'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_64'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_65'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_66'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_67'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_68'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_69'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_70'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_71'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_72'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_73'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_74'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_pod_info__mutmut['xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_75'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_pod_info__mutmut_75 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_13'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_14'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_15'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_16'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_17'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_18'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_19'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_20'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_21'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_22'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_23'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_24'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_25'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_26'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_27'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_28'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_29'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_30'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_31'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_32'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_33'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_34'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_35'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_36'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_37'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_38'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_39'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_40'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_41'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_42'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_43'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_44'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_45'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_46'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_47'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_48'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_49'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_50'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_51'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_52'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_53'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_54'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_resource_requests__mutmut['xǁVanillaK8sAdapterǁ_resource_requests__mutmut_55'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_resource_requests__mutmut_55 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_status__mutmut['xǁVanillaK8sAdapterǁ_pod_status__mutmut_13'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_status__mutmut_13 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_pod_age__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_age__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_pod_age__mutmut['xǁVanillaK8sAdapterǁ_pod_age__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_pod_age__mutmut_1 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_13'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_14'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_15'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_16'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_17'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_18'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_19'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_20'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_21'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_22'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_23'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_24'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_25'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_26'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_27'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_28'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_29'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_30'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_31'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_32'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_33'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_34'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_35'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_36'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_37'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_38'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_39'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_40'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_41'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_42'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_43'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_44'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_45'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut['xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_46'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_to_namespace_info__mutmut_46 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_node_items__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_items__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_items__mutmut['xǁVanillaK8sAdapterǁ_node_items__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_items__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_items__mutmut['xǁVanillaK8sAdapterǁ_node_items__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_items__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_items__mutmut['xǁVanillaK8sAdapterǁ_node_items__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_items__mutmut_3 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_13'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_14'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_15'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut['xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_16'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_metrics_usage__mutmut_16 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_13'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_14'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_15'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_16'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_17'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_18'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_19'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_20'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_21'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_22'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_23'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_24'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_25'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_26'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_27'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_28'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut['xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_29'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_sum_node_metrics__mutmut_29 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut['xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut['xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_cpu_capacity__mutmut_2 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_memory_capacity__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_memory_capacity__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_memory_capacity__mutmut['xǁVanillaK8sAdapterǁ_memory_capacity__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_memory_capacity__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_memory_capacity__mutmut['xǁVanillaK8sAdapterǁ_memory_capacity__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_memory_capacity__mutmut_2 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_cpu__mutmut_9 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable_memory__mutmut_9 # type: ignore # mutmut generated

mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['_mutmut_orig'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_1'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_2'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_3'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_4'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_5'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_6'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_7'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_8'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_9'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_10'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_11'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_12'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_13'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_14'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_15'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_16'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_17'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_18'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_19'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaK8sAdapterǁ_node_allocatable__mutmut['xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_20'] = VanillaK8sAdapter.xǁVanillaK8sAdapterǁ_node_allocatable__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_ingress_error__mutmut)
def _translate_ingress_error(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_orig(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_1(namespace: str, exc: Exception) -> Exception:
    if getattr(None, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_2(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, None, None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_3(namespace: str, exc: Exception) -> Exception:
    if getattr("status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_4(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_5(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", ) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_6(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "XXstatusXX", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_7(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "STATUS", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_8(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) != _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_9(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            None,
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_10(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context=None,
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_11(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_12(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_13(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"XXnamespaceXX": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_14(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"NAMESPACE": namespace},
        )
    return ClusterUnreachableError(f"Cannot list ingresses in namespace {namespace}: {exc}")


def x__translate_ingress_error__mutmut_15(namespace: str, exc: Exception) -> Exception:
    if getattr(exc, "status", None) == _FORBIDDEN_STATUS:
        return InsufficientPermissionsError(
            f"RBAC denied access to ingresses in namespace {namespace!r}",
            context={"namespace": namespace},
        )
    return ClusterUnreachableError(None)

mutants_x__translate_ingress_error__mutmut['_mutmut_orig'] = x__translate_ingress_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_1'] = x__translate_ingress_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_2'] = x__translate_ingress_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_3'] = x__translate_ingress_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_4'] = x__translate_ingress_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_5'] = x__translate_ingress_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_6'] = x__translate_ingress_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_7'] = x__translate_ingress_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_8'] = x__translate_ingress_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_9'] = x__translate_ingress_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_10'] = x__translate_ingress_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_11'] = x__translate_ingress_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_12'] = x__translate_ingress_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_13'] = x__translate_ingress_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_14'] = x__translate_ingress_error__mutmut_14 # type: ignore # mutmut generated
mutants_x__translate_ingress_error__mutmut['x__translate_ingress_error__mutmut_15'] = x__translate_ingress_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_ingress_info__mutmut)
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


def x__to_ingress_info__mutmut_orig(ingress: object, namespace: str) -> list[IngressInfo]:
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


def x__to_ingress_info__mutmut_1(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = None
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


def x__to_ingress_info__mutmut_2(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(None, "metadata", None)
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


def x__to_ingress_info__mutmut_3(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, None, None)
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


def x__to_ingress_info__mutmut_4(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr("metadata", None)
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


def x__to_ingress_info__mutmut_5(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, None)
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


def x__to_ingress_info__mutmut_6(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", )
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


def x__to_ingress_info__mutmut_7(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "XXmetadataXX", None)
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


def x__to_ingress_info__mutmut_8(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "METADATA", None)
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


def x__to_ingress_info__mutmut_9(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = None
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


def x__to_ingress_info__mutmut_10(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(None, "name", "unknown")
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


def x__to_ingress_info__mutmut_11(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, None, "unknown")
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


def x__to_ingress_info__mutmut_12(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", None)
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


def x__to_ingress_info__mutmut_13(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr("name", "unknown")
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


def x__to_ingress_info__mutmut_14(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "unknown")
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


def x__to_ingress_info__mutmut_15(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", )
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


def x__to_ingress_info__mutmut_16(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "XXnameXX", "unknown")
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


def x__to_ingress_info__mutmut_17(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "NAME", "unknown")
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


def x__to_ingress_info__mutmut_18(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "XXunknownXX")
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


def x__to_ingress_info__mutmut_19(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "UNKNOWN")
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


def x__to_ingress_info__mutmut_20(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = None
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


def x__to_ingress_info__mutmut_21(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(None, "namespace", namespace)
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


def x__to_ingress_info__mutmut_22(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, None, namespace)
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


def x__to_ingress_info__mutmut_23(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", None)
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


def x__to_ingress_info__mutmut_24(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr("namespace", namespace)
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


def x__to_ingress_info__mutmut_25(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, namespace)
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


def x__to_ingress_info__mutmut_26(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", )
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


def x__to_ingress_info__mutmut_27(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "XXnamespaceXX", namespace)
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


def x__to_ingress_info__mutmut_28(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "NAMESPACE", namespace)
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


def x__to_ingress_info__mutmut_29(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = None
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


def x__to_ingress_info__mutmut_30(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(None, "spec", None)
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


def x__to_ingress_info__mutmut_31(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, None, None)
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


def x__to_ingress_info__mutmut_32(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr("spec", None)
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


def x__to_ingress_info__mutmut_33(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, None)
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


def x__to_ingress_info__mutmut_34(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", )
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


def x__to_ingress_info__mutmut_35(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "XXspecXX", None)
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


def x__to_ingress_info__mutmut_36(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "SPEC", None)
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


def x__to_ingress_info__mutmut_37(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = None
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


def x__to_ingress_info__mutmut_38(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(None)
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


def x__to_ingress_info__mutmut_39(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(None, "tls", None))
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


def x__to_ingress_info__mutmut_40(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, None, None))
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


def x__to_ingress_info__mutmut_41(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr("tls", None))
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


def x__to_ingress_info__mutmut_42(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, None))
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


def x__to_ingress_info__mutmut_43(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", ))
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


def x__to_ingress_info__mutmut_44(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "XXtlsXX", None))
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


def x__to_ingress_info__mutmut_45(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "TLS", None))
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


def x__to_ingress_info__mutmut_46(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = None
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


def x__to_ingress_info__mutmut_47(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) and []
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


def x__to_ingress_info__mutmut_48(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(None, "rules", None) or []
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


def x__to_ingress_info__mutmut_49(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, None, None) or []
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


def x__to_ingress_info__mutmut_50(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr("rules", None) or []
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


def x__to_ingress_info__mutmut_51(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, None) or []
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


def x__to_ingress_info__mutmut_52(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", ) or []
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


def x__to_ingress_info__mutmut_53(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "XXrulesXX", None) or []
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


def x__to_ingress_info__mutmut_54(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "RULES", None) or []
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


def x__to_ingress_info__mutmut_55(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = None
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


def x__to_ingress_info__mutmut_56(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = None
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


def x__to_ingress_info__mutmut_57(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(None)
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


def x__to_ingress_info__mutmut_58(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") and "")
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


def x__to_ingress_info__mutmut_59(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(None, "host", "") or "")
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


def x__to_ingress_info__mutmut_60(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, None, "") or "")
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


def x__to_ingress_info__mutmut_61(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", None) or "")
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


def x__to_ingress_info__mutmut_62(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr("host", "") or "")
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


def x__to_ingress_info__mutmut_63(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "") or "")
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


def x__to_ingress_info__mutmut_64(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", ) or "")
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


def x__to_ingress_info__mutmut_65(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "XXhostXX", "") or "")
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


def x__to_ingress_info__mutmut_66(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "HOST", "") or "")
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


def x__to_ingress_info__mutmut_67(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "XXXX") or "")
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


def x__to_ingress_info__mutmut_68(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "XXXX")
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


def x__to_ingress_info__mutmut_69(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "")
        http = None
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


def x__to_ingress_info__mutmut_70(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "")
        http = getattr(None, "http", None)
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


def x__to_ingress_info__mutmut_71(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "")
        http = getattr(rule, None, None)
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


def x__to_ingress_info__mutmut_72(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "")
        http = getattr("http", None)
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


def x__to_ingress_info__mutmut_73(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "")
        http = getattr(rule, None)
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


def x__to_ingress_info__mutmut_74(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "")
        http = getattr(rule, "http", )
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


def x__to_ingress_info__mutmut_75(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "")
        http = getattr(rule, "XXhttpXX", None)
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


def x__to_ingress_info__mutmut_76(ingress: object, namespace: str) -> list[IngressInfo]:
    metadata = getattr(ingress, "metadata", None)
    name = text_attr(metadata, "name", "unknown")
    ns = text_attr(metadata, "namespace", namespace)
    spec = getattr(ingress, "spec", None)
    tls_enabled = bool(getattr(spec, "tls", None))
    rules = getattr(spec, "rules", None) or []
    entries: list[IngressInfo] = []
    for rule in rules:
        host = str(getattr(rule, "host", "") or "")
        http = getattr(rule, "HTTP", None)
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


def x__to_ingress_info__mutmut_77(ingress: object, namespace: str) -> list[IngressInfo]:
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
        paths = None
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


def x__to_ingress_info__mutmut_78(ingress: object, namespace: str) -> list[IngressInfo]:
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
        paths = getattr(http, "paths", None) and []
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


def x__to_ingress_info__mutmut_79(ingress: object, namespace: str) -> list[IngressInfo]:
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
        paths = getattr(None, "paths", None) or []
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


def x__to_ingress_info__mutmut_80(ingress: object, namespace: str) -> list[IngressInfo]:
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
        paths = getattr(http, None, None) or []
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


def x__to_ingress_info__mutmut_81(ingress: object, namespace: str) -> list[IngressInfo]:
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
        paths = getattr("paths", None) or []
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


def x__to_ingress_info__mutmut_82(ingress: object, namespace: str) -> list[IngressInfo]:
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
        paths = getattr(http, None) or []
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


def x__to_ingress_info__mutmut_83(ingress: object, namespace: str) -> list[IngressInfo]:
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
        paths = getattr(http, "paths", ) or []
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


def x__to_ingress_info__mutmut_84(ingress: object, namespace: str) -> list[IngressInfo]:
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
        paths = getattr(http, "XXpathsXX", None) or []
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


def x__to_ingress_info__mutmut_85(ingress: object, namespace: str) -> list[IngressInfo]:
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
        paths = getattr(http, "PATHS", None) or []
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


def x__to_ingress_info__mutmut_86(ingress: object, namespace: str) -> list[IngressInfo]:
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
        if paths:
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


def x__to_ingress_info__mutmut_87(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(None)
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


def x__to_ingress_info__mutmut_88(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(None, ns, host, "", tls_enabled))
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


def x__to_ingress_info__mutmut_89(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(name, None, host, "", tls_enabled))
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


def x__to_ingress_info__mutmut_90(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(name, ns, None, "", tls_enabled))
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


def x__to_ingress_info__mutmut_91(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(name, ns, host, None, tls_enabled))
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


def x__to_ingress_info__mutmut_92(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(name, ns, host, "", None))
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


def x__to_ingress_info__mutmut_93(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(ns, host, "", tls_enabled))
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


def x__to_ingress_info__mutmut_94(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(name, host, "", tls_enabled))
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


def x__to_ingress_info__mutmut_95(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(name, ns, "", tls_enabled))
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


def x__to_ingress_info__mutmut_96(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(name, ns, host, tls_enabled))
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


def x__to_ingress_info__mutmut_97(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(name, ns, host, "", ))
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


def x__to_ingress_info__mutmut_98(ingress: object, namespace: str) -> list[IngressInfo]:
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
            entries.append(_ingress_entry(name, ns, host, "XXXX", tls_enabled))
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


def x__to_ingress_info__mutmut_99(ingress: object, namespace: str) -> list[IngressInfo]:
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
            break
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


def x__to_ingress_info__mutmut_100(ingress: object, namespace: str) -> list[IngressInfo]:
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
            backend = None
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


def x__to_ingress_info__mutmut_101(ingress: object, namespace: str) -> list[IngressInfo]:
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
            backend = getattr(None, "backend", None)
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


def x__to_ingress_info__mutmut_102(ingress: object, namespace: str) -> list[IngressInfo]:
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
            backend = getattr(path, None, None)
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


def x__to_ingress_info__mutmut_103(ingress: object, namespace: str) -> list[IngressInfo]:
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
            backend = getattr("backend", None)
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


def x__to_ingress_info__mutmut_104(ingress: object, namespace: str) -> list[IngressInfo]:
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
            backend = getattr(path, None)
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


def x__to_ingress_info__mutmut_105(ingress: object, namespace: str) -> list[IngressInfo]:
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
            backend = getattr(path, "backend", )
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


def x__to_ingress_info__mutmut_106(ingress: object, namespace: str) -> list[IngressInfo]:
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
            backend = getattr(path, "XXbackendXX", None)
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


def x__to_ingress_info__mutmut_107(ingress: object, namespace: str) -> list[IngressInfo]:
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
            backend = getattr(path, "BACKEND", None)
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


def x__to_ingress_info__mutmut_108(ingress: object, namespace: str) -> list[IngressInfo]:
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
            service = None
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


def x__to_ingress_info__mutmut_109(ingress: object, namespace: str) -> list[IngressInfo]:
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
            service = getattr(None, "service", None)
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


def x__to_ingress_info__mutmut_110(ingress: object, namespace: str) -> list[IngressInfo]:
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
            service = getattr(backend, None, None)
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


def x__to_ingress_info__mutmut_111(ingress: object, namespace: str) -> list[IngressInfo]:
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
            service = getattr("service", None)
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


def x__to_ingress_info__mutmut_112(ingress: object, namespace: str) -> list[IngressInfo]:
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
            service = getattr(backend, None)
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


def x__to_ingress_info__mutmut_113(ingress: object, namespace: str) -> list[IngressInfo]:
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
            service = getattr(backend, "service", )
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


def x__to_ingress_info__mutmut_114(ingress: object, namespace: str) -> list[IngressInfo]:
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
            service = getattr(backend, "XXserviceXX", None)
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


def x__to_ingress_info__mutmut_115(ingress: object, namespace: str) -> list[IngressInfo]:
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
            service = getattr(backend, "SERVICE", None)
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


def x__to_ingress_info__mutmut_116(ingress: object, namespace: str) -> list[IngressInfo]:
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
                None
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_117(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    None,
                    ns,
                    host,
                    str(getattr(service, "name", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_118(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    None,
                    host,
                    str(getattr(service, "name", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_119(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    None,
                    str(getattr(service, "name", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_120(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    None,
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_121(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    None,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_122(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    ns,
                    host,
                    str(getattr(service, "name", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_123(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    host,
                    str(getattr(service, "name", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_124(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, "name", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_125(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_126(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_127(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(None),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_128(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, "name", "") and ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_129(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(None, "name", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_130(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, None, "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_131(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, "name", None) or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_132(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr("name", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_133(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_134(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, "name", ) or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_135(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, "XXnameXX", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_136(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, "NAME", "") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_137(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, "name", "XXXX") or ""),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_138(ingress: object, namespace: str) -> list[IngressInfo]:
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
                    str(getattr(service, "name", "") or "XXXX"),
                    tls_enabled,
                )
            )
    if not rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_139(ingress: object, namespace: str) -> list[IngressInfo]:
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
    if rules:
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_140(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(None)
    return entries


def x__to_ingress_info__mutmut_141(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(None, ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_142(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, None, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_143(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, ns, None, _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_144(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, ns, "", None, tls_enabled))
    return entries


def x__to_ingress_info__mutmut_145(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), None))
    return entries


def x__to_ingress_info__mutmut_146(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(ns, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_147(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, "", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_148(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, ns, _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_149(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, ns, "", tls_enabled))
    return entries


def x__to_ingress_info__mutmut_150(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(spec), ))
    return entries


def x__to_ingress_info__mutmut_151(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, ns, "XXXX", _default_backend_service(spec), tls_enabled))
    return entries


def x__to_ingress_info__mutmut_152(ingress: object, namespace: str) -> list[IngressInfo]:
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
        entries.append(_ingress_entry(name, ns, "", _default_backend_service(None), tls_enabled))
    return entries

mutants_x__to_ingress_info__mutmut['_mutmut_orig'] = x__to_ingress_info__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_1'] = x__to_ingress_info__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_2'] = x__to_ingress_info__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_3'] = x__to_ingress_info__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_4'] = x__to_ingress_info__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_5'] = x__to_ingress_info__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_6'] = x__to_ingress_info__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_7'] = x__to_ingress_info__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_8'] = x__to_ingress_info__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_9'] = x__to_ingress_info__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_10'] = x__to_ingress_info__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_11'] = x__to_ingress_info__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_12'] = x__to_ingress_info__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_13'] = x__to_ingress_info__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_14'] = x__to_ingress_info__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_15'] = x__to_ingress_info__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_16'] = x__to_ingress_info__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_17'] = x__to_ingress_info__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_18'] = x__to_ingress_info__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_19'] = x__to_ingress_info__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_20'] = x__to_ingress_info__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_21'] = x__to_ingress_info__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_22'] = x__to_ingress_info__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_23'] = x__to_ingress_info__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_24'] = x__to_ingress_info__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_25'] = x__to_ingress_info__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_26'] = x__to_ingress_info__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_27'] = x__to_ingress_info__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_28'] = x__to_ingress_info__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_29'] = x__to_ingress_info__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_30'] = x__to_ingress_info__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_31'] = x__to_ingress_info__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_32'] = x__to_ingress_info__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_33'] = x__to_ingress_info__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_34'] = x__to_ingress_info__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_35'] = x__to_ingress_info__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_36'] = x__to_ingress_info__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_37'] = x__to_ingress_info__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_38'] = x__to_ingress_info__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_39'] = x__to_ingress_info__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_40'] = x__to_ingress_info__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_41'] = x__to_ingress_info__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_42'] = x__to_ingress_info__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_43'] = x__to_ingress_info__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_44'] = x__to_ingress_info__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_45'] = x__to_ingress_info__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_46'] = x__to_ingress_info__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_47'] = x__to_ingress_info__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_48'] = x__to_ingress_info__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_49'] = x__to_ingress_info__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_50'] = x__to_ingress_info__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_51'] = x__to_ingress_info__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_52'] = x__to_ingress_info__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_53'] = x__to_ingress_info__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_54'] = x__to_ingress_info__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_55'] = x__to_ingress_info__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_56'] = x__to_ingress_info__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_57'] = x__to_ingress_info__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_58'] = x__to_ingress_info__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_59'] = x__to_ingress_info__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_60'] = x__to_ingress_info__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_61'] = x__to_ingress_info__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_62'] = x__to_ingress_info__mutmut_62 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_63'] = x__to_ingress_info__mutmut_63 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_64'] = x__to_ingress_info__mutmut_64 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_65'] = x__to_ingress_info__mutmut_65 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_66'] = x__to_ingress_info__mutmut_66 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_67'] = x__to_ingress_info__mutmut_67 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_68'] = x__to_ingress_info__mutmut_68 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_69'] = x__to_ingress_info__mutmut_69 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_70'] = x__to_ingress_info__mutmut_70 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_71'] = x__to_ingress_info__mutmut_71 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_72'] = x__to_ingress_info__mutmut_72 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_73'] = x__to_ingress_info__mutmut_73 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_74'] = x__to_ingress_info__mutmut_74 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_75'] = x__to_ingress_info__mutmut_75 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_76'] = x__to_ingress_info__mutmut_76 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_77'] = x__to_ingress_info__mutmut_77 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_78'] = x__to_ingress_info__mutmut_78 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_79'] = x__to_ingress_info__mutmut_79 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_80'] = x__to_ingress_info__mutmut_80 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_81'] = x__to_ingress_info__mutmut_81 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_82'] = x__to_ingress_info__mutmut_82 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_83'] = x__to_ingress_info__mutmut_83 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_84'] = x__to_ingress_info__mutmut_84 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_85'] = x__to_ingress_info__mutmut_85 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_86'] = x__to_ingress_info__mutmut_86 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_87'] = x__to_ingress_info__mutmut_87 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_88'] = x__to_ingress_info__mutmut_88 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_89'] = x__to_ingress_info__mutmut_89 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_90'] = x__to_ingress_info__mutmut_90 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_91'] = x__to_ingress_info__mutmut_91 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_92'] = x__to_ingress_info__mutmut_92 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_93'] = x__to_ingress_info__mutmut_93 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_94'] = x__to_ingress_info__mutmut_94 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_95'] = x__to_ingress_info__mutmut_95 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_96'] = x__to_ingress_info__mutmut_96 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_97'] = x__to_ingress_info__mutmut_97 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_98'] = x__to_ingress_info__mutmut_98 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_99'] = x__to_ingress_info__mutmut_99 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_100'] = x__to_ingress_info__mutmut_100 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_101'] = x__to_ingress_info__mutmut_101 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_102'] = x__to_ingress_info__mutmut_102 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_103'] = x__to_ingress_info__mutmut_103 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_104'] = x__to_ingress_info__mutmut_104 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_105'] = x__to_ingress_info__mutmut_105 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_106'] = x__to_ingress_info__mutmut_106 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_107'] = x__to_ingress_info__mutmut_107 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_108'] = x__to_ingress_info__mutmut_108 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_109'] = x__to_ingress_info__mutmut_109 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_110'] = x__to_ingress_info__mutmut_110 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_111'] = x__to_ingress_info__mutmut_111 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_112'] = x__to_ingress_info__mutmut_112 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_113'] = x__to_ingress_info__mutmut_113 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_114'] = x__to_ingress_info__mutmut_114 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_115'] = x__to_ingress_info__mutmut_115 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_116'] = x__to_ingress_info__mutmut_116 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_117'] = x__to_ingress_info__mutmut_117 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_118'] = x__to_ingress_info__mutmut_118 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_119'] = x__to_ingress_info__mutmut_119 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_120'] = x__to_ingress_info__mutmut_120 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_121'] = x__to_ingress_info__mutmut_121 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_122'] = x__to_ingress_info__mutmut_122 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_123'] = x__to_ingress_info__mutmut_123 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_124'] = x__to_ingress_info__mutmut_124 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_125'] = x__to_ingress_info__mutmut_125 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_126'] = x__to_ingress_info__mutmut_126 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_127'] = x__to_ingress_info__mutmut_127 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_128'] = x__to_ingress_info__mutmut_128 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_129'] = x__to_ingress_info__mutmut_129 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_130'] = x__to_ingress_info__mutmut_130 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_131'] = x__to_ingress_info__mutmut_131 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_132'] = x__to_ingress_info__mutmut_132 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_133'] = x__to_ingress_info__mutmut_133 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_134'] = x__to_ingress_info__mutmut_134 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_135'] = x__to_ingress_info__mutmut_135 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_136'] = x__to_ingress_info__mutmut_136 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_137'] = x__to_ingress_info__mutmut_137 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_138'] = x__to_ingress_info__mutmut_138 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_139'] = x__to_ingress_info__mutmut_139 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_140'] = x__to_ingress_info__mutmut_140 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_141'] = x__to_ingress_info__mutmut_141 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_142'] = x__to_ingress_info__mutmut_142 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_143'] = x__to_ingress_info__mutmut_143 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_144'] = x__to_ingress_info__mutmut_144 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_145'] = x__to_ingress_info__mutmut_145 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_146'] = x__to_ingress_info__mutmut_146 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_147'] = x__to_ingress_info__mutmut_147 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_148'] = x__to_ingress_info__mutmut_148 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_149'] = x__to_ingress_info__mutmut_149 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_150'] = x__to_ingress_info__mutmut_150 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_151'] = x__to_ingress_info__mutmut_151 # type: ignore # mutmut generated
mutants_x__to_ingress_info__mutmut['x__to_ingress_info__mutmut_152'] = x__to_ingress_info__mutmut_152 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__default_backend_service__mutmut)
def _default_backend_service(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_orig(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_1(spec: object) -> str:
    default_backend = None
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_2(spec: object) -> str:
    default_backend = getattr(None, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_3(spec: object) -> str:
    default_backend = getattr(spec, None, None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_4(spec: object) -> str:
    default_backend = getattr("default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_5(spec: object) -> str:
    default_backend = getattr(spec, None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_6(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", )
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_7(spec: object) -> str:
    default_backend = getattr(spec, "XXdefault_backendXX", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_8(spec: object) -> str:
    default_backend = getattr(spec, "DEFAULT_BACKEND", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_9(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is not None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_10(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return "XXXX"
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_11(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = None
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_12(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(None, "service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_13(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, None, None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_14(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr("service", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_15(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_16(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", )
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_17(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "XXserviceXX", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_18(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "SERVICE", None)
    return str(getattr(service, "name", "") or "")


def x__default_backend_service__mutmut_19(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(None)


def x__default_backend_service__mutmut_20(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") and "")


def x__default_backend_service__mutmut_21(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(None, "name", "") or "")


def x__default_backend_service__mutmut_22(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, None, "") or "")


def x__default_backend_service__mutmut_23(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", None) or "")


def x__default_backend_service__mutmut_24(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr("name", "") or "")


def x__default_backend_service__mutmut_25(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "") or "")


def x__default_backend_service__mutmut_26(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", ) or "")


def x__default_backend_service__mutmut_27(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "XXnameXX", "") or "")


def x__default_backend_service__mutmut_28(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "NAME", "") or "")


def x__default_backend_service__mutmut_29(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "XXXX") or "")


def x__default_backend_service__mutmut_30(spec: object) -> str:
    default_backend = getattr(spec, "default_backend", None)
    if default_backend is None:
        return ""
    service = getattr(default_backend, "service", None)
    return str(getattr(service, "name", "") or "XXXX")

mutants_x__default_backend_service__mutmut['_mutmut_orig'] = x__default_backend_service__mutmut_orig # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_1'] = x__default_backend_service__mutmut_1 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_2'] = x__default_backend_service__mutmut_2 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_3'] = x__default_backend_service__mutmut_3 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_4'] = x__default_backend_service__mutmut_4 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_5'] = x__default_backend_service__mutmut_5 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_6'] = x__default_backend_service__mutmut_6 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_7'] = x__default_backend_service__mutmut_7 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_8'] = x__default_backend_service__mutmut_8 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_9'] = x__default_backend_service__mutmut_9 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_10'] = x__default_backend_service__mutmut_10 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_11'] = x__default_backend_service__mutmut_11 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_12'] = x__default_backend_service__mutmut_12 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_13'] = x__default_backend_service__mutmut_13 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_14'] = x__default_backend_service__mutmut_14 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_15'] = x__default_backend_service__mutmut_15 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_16'] = x__default_backend_service__mutmut_16 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_17'] = x__default_backend_service__mutmut_17 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_18'] = x__default_backend_service__mutmut_18 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_19'] = x__default_backend_service__mutmut_19 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_20'] = x__default_backend_service__mutmut_20 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_21'] = x__default_backend_service__mutmut_21 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_22'] = x__default_backend_service__mutmut_22 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_23'] = x__default_backend_service__mutmut_23 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_24'] = x__default_backend_service__mutmut_24 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_25'] = x__default_backend_service__mutmut_25 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_26'] = x__default_backend_service__mutmut_26 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_27'] = x__default_backend_service__mutmut_27 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_28'] = x__default_backend_service__mutmut_28 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_29'] = x__default_backend_service__mutmut_29 # type: ignore # mutmut generated
mutants_x__default_backend_service__mutmut['x__default_backend_service__mutmut_30'] = x__default_backend_service__mutmut_30 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__ingress_entry__mutmut)
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


def x__ingress_entry__mutmut_orig(
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


def x__ingress_entry__mutmut_1(
    name: str,
    namespace: str,
    host: str,
    target_service: str,
    tls_enabled: bool,
) -> IngressInfo:
    return IngressInfo(
        name=None,
        namespace=namespace,
        host=host,
        target_service=target_service,
        tls_enabled=tls_enabled,
    )


def x__ingress_entry__mutmut_2(
    name: str,
    namespace: str,
    host: str,
    target_service: str,
    tls_enabled: bool,
) -> IngressInfo:
    return IngressInfo(
        name=name,
        namespace=None,
        host=host,
        target_service=target_service,
        tls_enabled=tls_enabled,
    )


def x__ingress_entry__mutmut_3(
    name: str,
    namespace: str,
    host: str,
    target_service: str,
    tls_enabled: bool,
) -> IngressInfo:
    return IngressInfo(
        name=name,
        namespace=namespace,
        host=None,
        target_service=target_service,
        tls_enabled=tls_enabled,
    )


def x__ingress_entry__mutmut_4(
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
        target_service=None,
        tls_enabled=tls_enabled,
    )


def x__ingress_entry__mutmut_5(
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
        tls_enabled=None,
    )


def x__ingress_entry__mutmut_6(
    name: str,
    namespace: str,
    host: str,
    target_service: str,
    tls_enabled: bool,
) -> IngressInfo:
    return IngressInfo(
        namespace=namespace,
        host=host,
        target_service=target_service,
        tls_enabled=tls_enabled,
    )


def x__ingress_entry__mutmut_7(
    name: str,
    namespace: str,
    host: str,
    target_service: str,
    tls_enabled: bool,
) -> IngressInfo:
    return IngressInfo(
        name=name,
        host=host,
        target_service=target_service,
        tls_enabled=tls_enabled,
    )


def x__ingress_entry__mutmut_8(
    name: str,
    namespace: str,
    host: str,
    target_service: str,
    tls_enabled: bool,
) -> IngressInfo:
    return IngressInfo(
        name=name,
        namespace=namespace,
        target_service=target_service,
        tls_enabled=tls_enabled,
    )


def x__ingress_entry__mutmut_9(
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
        tls_enabled=tls_enabled,
    )


def x__ingress_entry__mutmut_10(
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
        )

mutants_x__ingress_entry__mutmut['_mutmut_orig'] = x__ingress_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_1'] = x__ingress_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_2'] = x__ingress_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_3'] = x__ingress_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_4'] = x__ingress_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_5'] = x__ingress_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_6'] = x__ingress_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_7'] = x__ingress_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_8'] = x__ingress_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_9'] = x__ingress_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x__ingress_entry__mutmut['x__ingress_entry__mutmut_10'] = x__ingress_entry__mutmut_10 # type: ignore # mutmut generated
