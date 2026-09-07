# mypy: ignore-errors
"""Adapter for per-pod CPU/memory usage from Kubernetes metrics-server."""

from __future__ import annotations

from hexawyn.application.ports.driven.pod_metrics_port import (
    PodMetricSnapshot,
    PodMetricsPort,
)
from hexawyn.domain.errors import MetricsUnavailableError
from hexawyn.infrastructure.adapters.secondary.vanilla.adapters._helpers import (
    cpu_to_cores,
    mapping_from,
    memory_to_bytes,
    metric_items,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesMetricsApi,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁVanillaPodMetricsAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut: MutantDict = {}  # type: ignore


class VanillaPodMetricsAdapter(PodMetricsPort):
    """Queries the Kubernetes metrics-server for per-pod CPU/memory usage."""

    @_mutmut_mutated(mutants_xǁVanillaPodMetricsAdapterǁ__init____mutmut)
    def __init__(self, metrics_api: KubernetesMetricsApi | None, cluster_name: str) -> None:
        self._metrics_api = metrics_api
        self._cluster_name = cluster_name

    def xǁVanillaPodMetricsAdapterǁ__init____mutmut_orig(self, metrics_api: KubernetesMetricsApi | None, cluster_name: str) -> None:
        self._metrics_api = metrics_api
        self._cluster_name = cluster_name

    def xǁVanillaPodMetricsAdapterǁ__init____mutmut_1(self, metrics_api: KubernetesMetricsApi | None, cluster_name: str) -> None:
        self._metrics_api = None
        self._cluster_name = cluster_name

    def xǁVanillaPodMetricsAdapterǁ__init____mutmut_2(self, metrics_api: KubernetesMetricsApi | None, cluster_name: str) -> None:
        self._metrics_api = metrics_api
        self._cluster_name = None

    @_mutmut_mutated(mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut)
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_orig(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_1(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is not None:
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_2(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                None
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_3(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = None
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_4(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group=None,
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_5(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group="metrics.k8s.io",
                    version=None,
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_6(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group="metrics.k8s.io",
                    version="v1beta1",
                    namespace=None,
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_7(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    plural=None,
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_8(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_9(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group="metrics.k8s.io",
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_10(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group="metrics.k8s.io",
                    version="v1beta1",
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_11(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_12(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group="XXmetrics.k8s.ioXX",
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_13(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group="METRICS.K8S.IO",
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_14(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group="metrics.k8s.io",
                    version="XXv1beta1XX",
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_15(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        if self._metrics_api is None:
            raise MetricsUnavailableError(
                f"Metrics-server client not initialized on cluster '{self._cluster_name}'"
            )
        try:
            if namespace:
                raw = self._metrics_api.list_namespaced_custom_object(
                    group="metrics.k8s.io",
                    version="V1BETA1",
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_16(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    plural="XXpodsXX",
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_17(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    plural="PODS",
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

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_18(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                raw = None
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_19(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    group=None,
                    version="v1beta1",
                    plural="pods",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_20(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    version=None,
                    plural="pods",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_21(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    plural=None,
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_22(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    version="v1beta1",
                    plural="pods",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_23(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    plural="pods",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_24(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_25(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    group="XXmetrics.k8s.ioXX",
                    version="v1beta1",
                    plural="pods",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_26(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    group="METRICS.K8S.IO",
                    version="v1beta1",
                    plural="pods",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_27(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    version="XXv1beta1XX",
                    plural="pods",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_28(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    version="V1BETA1",
                    plural="pods",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_29(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    plural="XXpodsXX",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_30(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                    plural="PODS",
                )
        except Exception as exc:
            raise MetricsUnavailableError(
                f"Metrics-server not available on cluster '{self._cluster_name}': {exc}"
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_31(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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
                None
            ) from exc

        return self._parse_pod_metrics(raw)

    def xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_32(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
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

        return self._parse_pod_metrics(None)

    @_mutmut_mutated(mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut)
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_orig(self, raw: object) -> list[PodMetricSnapshot]:
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_1(self, raw: object) -> list[PodMetricSnapshot]:
        items = None
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_2(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(None)
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_3(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = None

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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_4(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = None
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_5(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get(None, {}) if isinstance(item, dict) else {}
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_6(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", None) if isinstance(item, dict) else {}
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_7(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get({}) if isinstance(item, dict) else {}
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_8(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", ) if isinstance(item, dict) else {}
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_9(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("XXmetadataXX", {}) if isinstance(item, dict) else {}
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_10(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("METADATA", {}) if isinstance(item, dict) else {}
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_11(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = None
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_12(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get(None, "unknown") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_13(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", None) if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_14(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("unknown") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_15(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", ) if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_16(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("XXnameXX", "unknown") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_17(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("NAME", "unknown") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_18(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "XXunknownXX") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_19(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "UNKNOWN") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_20(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "XXunknownXX"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_21(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "UNKNOWN"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_22(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = None

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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_23(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get(None, "unknown") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_24(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", None) if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_25(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("unknown") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_26(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", ) if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_27(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("XXnamespaceXX", "unknown") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_28(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("NAMESPACE", "unknown") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_29(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "XXunknownXX") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_30(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "UNKNOWN") if isinstance(metadata, dict) else "unknown"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_31(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "XXunknownXX"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_32(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "UNKNOWN"
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_33(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "unknown"
            )

            containers = None
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_34(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "unknown"
            )

            containers = item.get(None, []) if isinstance(item, dict) else []
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_35(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "unknown"
            )

            containers = item.get("containers", None) if isinstance(item, dict) else []
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_36(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "unknown"
            )

            containers = item.get([]) if isinstance(item, dict) else []
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_37(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "unknown"
            )

            containers = item.get("containers", ) if isinstance(item, dict) else []
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_38(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "unknown"
            )

            containers = item.get("XXcontainersXX", []) if isinstance(item, dict) else []
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_39(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "unknown"
            )

            containers = item.get("CONTAINERS", []) if isinstance(item, dict) else []
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_40(self, raw: object) -> list[PodMetricSnapshot]:
        items = metric_items(raw)
        snapshots: list[PodMetricSnapshot] = []

        for item in items:
            metadata = item.get("metadata", {}) if isinstance(item, dict) else {}
            name = metadata.get("name", "unknown") if isinstance(metadata, dict) else "unknown"
            namespace = (
                metadata.get("namespace", "unknown") if isinstance(metadata, dict) else "unknown"
            )

            containers = item.get("containers", []) if isinstance(item, dict) else []
            if isinstance(containers, list):
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_41(self, raw: object) -> list[PodMetricSnapshot]:
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
                containers = None

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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_42(self, raw: object) -> list[PodMetricSnapshot]:
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

            cpu_cores = None
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_43(self, raw: object) -> list[PodMetricSnapshot]:
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

            cpu_cores = 1.0
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_44(self, raw: object) -> list[PodMetricSnapshot]:
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
            memory_gb = None

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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_45(self, raw: object) -> list[PodMetricSnapshot]:
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
            memory_gb = 1.0

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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_46(self, raw: object) -> list[PodMetricSnapshot]:
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
                if isinstance(container, dict):
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_47(self, raw: object) -> list[PodMetricSnapshot]:
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
                    break
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_48(self, raw: object) -> list[PodMetricSnapshot]:
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
                usage = None
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_49(self, raw: object) -> list[PodMetricSnapshot]:
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
                usage = mapping_from(None)
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_50(self, raw: object) -> list[PodMetricSnapshot]:
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
                usage = mapping_from(container.get(None))
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_51(self, raw: object) -> list[PodMetricSnapshot]:
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
                usage = mapping_from(container.get("XXusageXX"))
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_52(self, raw: object) -> list[PodMetricSnapshot]:
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
                usage = mapping_from(container.get("USAGE"))
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_53(self, raw: object) -> list[PodMetricSnapshot]:
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
                if usage is None:
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_54(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_str = None
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_55(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_str = usage.get(None, "")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_56(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_str = usage.get("cpu", None)
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_57(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_str = usage.get("")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_58(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_str = usage.get("cpu", )
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_59(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_str = usage.get("XXcpuXX", "")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_60(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_str = usage.get("CPU", "")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_61(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_str = usage.get("cpu", "XXXX")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_62(self, raw: object) -> list[PodMetricSnapshot]:
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
                    mem_str = None
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_63(self, raw: object) -> list[PodMetricSnapshot]:
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
                    mem_str = usage.get(None, "")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_64(self, raw: object) -> list[PodMetricSnapshot]:
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
                    mem_str = usage.get("memory", None)
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_65(self, raw: object) -> list[PodMetricSnapshot]:
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
                    mem_str = usage.get("")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_66(self, raw: object) -> list[PodMetricSnapshot]:
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
                    mem_str = usage.get("memory", )
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_67(self, raw: object) -> list[PodMetricSnapshot]:
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
                    mem_str = usage.get("XXmemoryXX", "")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_68(self, raw: object) -> list[PodMetricSnapshot]:
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
                    mem_str = usage.get("MEMORY", "")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_69(self, raw: object) -> list[PodMetricSnapshot]:
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
                    mem_str = usage.get("memory", "XXXX")
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_70(self, raw: object) -> list[PodMetricSnapshot]:
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
                        cpu_cores = cpu_to_cores(cpu_str)
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_71(self, raw: object) -> list[PodMetricSnapshot]:
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
                        cpu_cores -= cpu_to_cores(cpu_str)
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_72(self, raw: object) -> list[PodMetricSnapshot]:
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
                        cpu_cores += cpu_to_cores(None)
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

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_73(self, raw: object) -> list[PodMetricSnapshot]:
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
                        memory_gb = memory_to_bytes(mem_str) / (1024.0**3)

            snapshots.append(
                PodMetricSnapshot(
                    name=name,
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_74(self, raw: object) -> list[PodMetricSnapshot]:
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
                        memory_gb -= memory_to_bytes(mem_str) / (1024.0**3)

            snapshots.append(
                PodMetricSnapshot(
                    name=name,
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_75(self, raw: object) -> list[PodMetricSnapshot]:
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
                        memory_gb += memory_to_bytes(mem_str) * (1024.0**3)

            snapshots.append(
                PodMetricSnapshot(
                    name=name,
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_76(self, raw: object) -> list[PodMetricSnapshot]:
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
                        memory_gb += memory_to_bytes(None) / (1024.0**3)

            snapshots.append(
                PodMetricSnapshot(
                    name=name,
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_77(self, raw: object) -> list[PodMetricSnapshot]:
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
                        memory_gb += memory_to_bytes(mem_str) / (1024.0 * 3)

            snapshots.append(
                PodMetricSnapshot(
                    name=name,
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_78(self, raw: object) -> list[PodMetricSnapshot]:
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
                        memory_gb += memory_to_bytes(mem_str) / (1025.0**3)

            snapshots.append(
                PodMetricSnapshot(
                    name=name,
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_79(self, raw: object) -> list[PodMetricSnapshot]:
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
                        memory_gb += memory_to_bytes(mem_str) / (1024.0**4)

            snapshots.append(
                PodMetricSnapshot(
                    name=name,
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_80(self, raw: object) -> list[PodMetricSnapshot]:
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
                None
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_81(self, raw: object) -> list[PodMetricSnapshot]:
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
                    name=None,
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_82(self, raw: object) -> list[PodMetricSnapshot]:
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
                    namespace=None,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_83(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_cores=None,
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_84(self, raw: object) -> list[PodMetricSnapshot]:
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
                    memory_gb=None,
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_85(self, raw: object) -> list[PodMetricSnapshot]:
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
                    namespace=namespace,
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_86(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_cores=round(cpu_cores, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_87(self, raw: object) -> list[PodMetricSnapshot]:
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
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_88(self, raw: object) -> list[PodMetricSnapshot]:
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
                    )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_89(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_cores=round(None, 4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_90(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_cores=round(cpu_cores, None),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_91(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_cores=round(4),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_92(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_cores=round(cpu_cores, ),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_93(self, raw: object) -> list[PodMetricSnapshot]:
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
                    cpu_cores=round(cpu_cores, 5),
                    memory_gb=round(memory_gb, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_94(self, raw: object) -> list[PodMetricSnapshot]:
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
                    memory_gb=round(None, 4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_95(self, raw: object) -> list[PodMetricSnapshot]:
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
                    memory_gb=round(memory_gb, None),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_96(self, raw: object) -> list[PodMetricSnapshot]:
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
                    memory_gb=round(4),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_97(self, raw: object) -> list[PodMetricSnapshot]:
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
                    memory_gb=round(memory_gb, ),
                )
            )

        return snapshots

    def xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_98(self, raw: object) -> list[PodMetricSnapshot]:
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
                    memory_gb=round(memory_gb, 5),
                )
            )

        return snapshots

mutants_xǁVanillaPodMetricsAdapterǁ__init____mutmut['_mutmut_orig'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ__init____mutmut['xǁVanillaPodMetricsAdapterǁ__init____mutmut_1'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ__init____mutmut['xǁVanillaPodMetricsAdapterǁ__init____mutmut_2'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['_mutmut_orig'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_1'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_2'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_3'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_4'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_5'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_6'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_7'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_8'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_9'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_10'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_11'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_12'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_13'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_14'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_15'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_16'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_17'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_18'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_19'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_20'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_21'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_22'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_23'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_24'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_25'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_26'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_27'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_28'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_29'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_30'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_31'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_32'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁget_pod_metrics__mutmut_32 # type: ignore # mutmut generated

mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['_mutmut_orig'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_1'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_2'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_3'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_4'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_5'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_6'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_7'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_8'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_9'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_10'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_11'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_12'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_13'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_14'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_15'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_16'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_17'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_18'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_19'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_20'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_21'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_22'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_23'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_24'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_25'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_26'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_27'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_28'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_29'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_30'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_31'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_32'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_33'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_34'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_35'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_36'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_37'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_38'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_39'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_40'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_41'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_42'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_43'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_44'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_45'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_46'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_47'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_48'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_49'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_50'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_51'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_52'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_53'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_54'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_55'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_56'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_57'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_58'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_59'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_60'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_61'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_62'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_63'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_64'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_65'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_66'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_67'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_68'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_69'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_70'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_71'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_72'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_73'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_74'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_75'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_75 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_76'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_76 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_77'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_77 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_78'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_78 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_79'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_79 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_80'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_80 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_81'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_81 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_82'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_82 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_83'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_83 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_84'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_84 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_85'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_85 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_86'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_86 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_87'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_87 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_88'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_88 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_89'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_89 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_90'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_90 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_91'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_91 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_92'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_92 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_93'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_93 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_94'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_94 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_95'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_95 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_96'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_96 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_97'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_97 # type: ignore # mutmut generated
mutants_xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut['xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_98'] = VanillaPodMetricsAdapter.xǁVanillaPodMetricsAdapterǁ_parse_pod_metrics__mutmut_98 # type: ignore # mutmut generated
