from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from hexawyn.application.ports.driven.rightsizing_port import (
    RightsizingPort,
    WorkloadRawData,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesAppsApi,
    KubernetesMetricsApi,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.resource_parsers import (
    _sum_container_metrics,
    _workload_key_from_pod_name,
    _workload_resource_requests,
)

_K8S_TIMEOUT = 10
_METRICS_GROUP = "metrics.k8s.io"
_METRICS_VERSION = "v1beta1"
_METRICS_PODS_PLURAL = "pods"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__items_from__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__items_from__mutmut)
def _items_from(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def x__items_from__mutmut_orig(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def x__items_from__mutmut_1(item_list: object) -> list[object]:
    items = None
    return _object_sequence(items)


def x__items_from__mutmut_2(item_list: object) -> list[object]:
    items = getattr(None, "items", [])
    return _object_sequence(items)


def x__items_from__mutmut_3(item_list: object) -> list[object]:
    items = getattr(item_list, None, [])
    return _object_sequence(items)


def x__items_from__mutmut_4(item_list: object) -> list[object]:
    items = getattr(item_list, "items", None)
    return _object_sequence(items)


def x__items_from__mutmut_5(item_list: object) -> list[object]:
    items = getattr("items", [])
    return _object_sequence(items)


def x__items_from__mutmut_6(item_list: object) -> list[object]:
    items = getattr(item_list, [])
    return _object_sequence(items)


def x__items_from__mutmut_7(item_list: object) -> list[object]:
    items = getattr(item_list, "items", )
    return _object_sequence(items)


def x__items_from__mutmut_8(item_list: object) -> list[object]:
    items = getattr(item_list, "XXitemsXX", [])
    return _object_sequence(items)


def x__items_from__mutmut_9(item_list: object) -> list[object]:
    items = getattr(item_list, "ITEMS", [])
    return _object_sequence(items)


def x__items_from__mutmut_10(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(None)

mutants_x__items_from__mutmut['_mutmut_orig'] = x__items_from__mutmut_orig # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_1'] = x__items_from__mutmut_1 # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_2'] = x__items_from__mutmut_2 # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_3'] = x__items_from__mutmut_3 # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_4'] = x__items_from__mutmut_4 # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_5'] = x__items_from__mutmut_5 # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_6'] = x__items_from__mutmut_6 # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_7'] = x__items_from__mutmut_7 # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_8'] = x__items_from__mutmut_8 # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_9'] = x__items_from__mutmut_9 # type: ignore # mutmut generated
mutants_x__items_from__mutmut['x__items_from__mutmut_10'] = x__items_from__mutmut_10 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__object_sequence__mutmut)
def _object_sequence(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


def x__object_sequence__mutmut_orig(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


def x__object_sequence__mutmut_1(value: object) -> list[object]:
    if isinstance(value, Sequence) or not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


def x__object_sequence__mutmut_2(value: object) -> list[object]:
    if isinstance(value, Sequence) and isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


def x__object_sequence__mutmut_3(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(None)
    return []


def x__object_sequence__mutmut_4(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(None, value))
    return []


def x__object_sequence__mutmut_5(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], None))
    return []


def x__object_sequence__mutmut_6(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(value))
    return []


def x__object_sequence__mutmut_7(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], ))
    return []

mutants_x__object_sequence__mutmut['_mutmut_orig'] = x__object_sequence__mutmut_orig # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_1'] = x__object_sequence__mutmut_1 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_2'] = x__object_sequence__mutmut_2 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_3'] = x__object_sequence__mutmut_3 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_4'] = x__object_sequence__mutmut_4 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_5'] = x__object_sequence__mutmut_5 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_6'] = x__object_sequence__mutmut_6 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_7'] = x__object_sequence__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut: MutantDict = {}  # type: ignore


class VanillaRightsizingAdapter(RightsizingPort):
    @_mutmut_mutated(mutants_xǁVanillaRightsizingAdapterǁ__init____mutmut)
    def __init__(
        self,
        apps_api: KubernetesAppsApi,
        metrics_api: KubernetesMetricsApi,
    ) -> None:
        self._apps_api = apps_api
        self._metrics_api = metrics_api
    def xǁVanillaRightsizingAdapterǁ__init____mutmut_orig(
        self,
        apps_api: KubernetesAppsApi,
        metrics_api: KubernetesMetricsApi,
    ) -> None:
        self._apps_api = apps_api
        self._metrics_api = metrics_api
    def xǁVanillaRightsizingAdapterǁ__init____mutmut_1(
        self,
        apps_api: KubernetesAppsApi,
        metrics_api: KubernetesMetricsApi,
    ) -> None:
        self._apps_api = None
        self._metrics_api = metrics_api
    def xǁVanillaRightsizingAdapterǁ__init____mutmut_2(
        self,
        apps_api: KubernetesAppsApi,
        metrics_api: KubernetesMetricsApi,
    ) -> None:
        self._apps_api = apps_api
        self._metrics_api = None

    @_mutmut_mutated(mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut)
    def get_workload_rightsizing_data(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "Deployment", pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_orig(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "Deployment", pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_1(self) -> list[WorkloadRawData]:
        deployments = None
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "Deployment", pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_2(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = None
        return [
            self._build_workload_raw_data(dep, "Deployment", pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_3(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(None, "Deployment", pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_4(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, None, pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_5(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "Deployment", None) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_6(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data("Deployment", pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_7(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_8(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "Deployment", ) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_9(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "XXDeploymentXX", pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_10(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "deployment", pod_metrics) for dep in deployments
        ]

    def xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_11(self) -> list[WorkloadRawData]:
        deployments = self._fetch_deployments()
        pod_metrics = self._fetch_pod_metrics_by_workload()
        return [
            self._build_workload_raw_data(dep, "DEPLOYMENT", pod_metrics) for dep in deployments
        ]

    @_mutmut_mutated(mutants_xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut)
    def _fetch_deployments(self) -> list[object]:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list deployments: {exc}") from exc
        return list(_items_from(raw))

    def xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_orig(self) -> list[object]:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list deployments: {exc}") from exc
        return list(_items_from(raw))

    def xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_1(self) -> list[object]:
        try:
            raw = None
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list deployments: {exc}") from exc
        return list(_items_from(raw))

    def xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_2(self) -> list[object]:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=None)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list deployments: {exc}") from exc
        return list(_items_from(raw))

    def xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_3(self) -> list[object]:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(None) from exc
        return list(_items_from(raw))

    def xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_4(self) -> list[object]:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list deployments: {exc}") from exc
        return list(None)

    def xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_5(self) -> list[object]:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list deployments: {exc}") from exc
        return list(_items_from(None))

    @_mutmut_mutated(mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut)
    def _fetch_pod_metrics_by_workload(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_orig(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_1(self) -> dict[str, dict[str, float]]:
        try:
            raw = None
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_2(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=None,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_3(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=None,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_4(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=None,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_5(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_6(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_7(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_8(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = None
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_9(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = None
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_10(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get(None, []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_11(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", None) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_12(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get([]) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_13(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", ) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_14(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("XXitemsXX", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_15(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("ITEMS", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_16(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_17(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                break
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_18(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = None
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_19(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get(None, {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_20(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", None)
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_21(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get({})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_22(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", )
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_23(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("XXmetadataXX", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_24(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("METADATA", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_25(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_26(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                break
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_27(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = None
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_28(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(None)
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_29(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get(None, ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_30(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", None))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_31(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get(""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_32(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_33(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("XXnameXX", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_34(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("NAME", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_35(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", "XXXX"))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_36(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = None
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_37(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(None)
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_38(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get(None, ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_39(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", None))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_40(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get(""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_41(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_42(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("XXnamespaceXX", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_43(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("NAMESPACE", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_44(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", "XXXX"))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_45(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = None
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_46(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(None)
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_47(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get(None, []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_48(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", None))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_49(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get([]))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_50(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", ))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_51(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("XXcontainersXX", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_52(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("CONTAINERS", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_53(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = None
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_54(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(None, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_55(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, None)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_56(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_57(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, )
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_58(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = None
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_59(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(None)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_60(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is not None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_61(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = None
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_62(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"XXcpuXX": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_63(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"CPU": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_64(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "XXmem_miXX": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_65(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "MEM_MI": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_66(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "XXcountXX": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_67(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "COUNT": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_68(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 2.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_69(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] = cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_70(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] -= cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_71(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["XXcpuXX"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_72(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["CPU"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_73(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] = mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_74(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] -= mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_75(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["XXmem_miXX"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_76(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["MEM_MI"] += mem_mi
                    existing["count"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_77(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] = 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_78(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] -= 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_79(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["XXcountXX"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_80(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["COUNT"] += 1.0
        return result

    def xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_81(self) -> dict[str, dict[str, float]]:
        try:
            raw = self._metrics_api.list_cluster_custom_object(
                group=_METRICS_GROUP,
                version=_METRICS_VERSION,
                plural=_METRICS_PODS_PLURAL,
            )
        except Exception:
            return {}
        result: dict[str, dict[str, float]] = {}
        items = raw.get("items", []) if isinstance(raw, dict) else []
        for item in items:
            if not isinstance(item, dict):
                continue
            meta = item.get("metadata", {})
            if not isinstance(meta, dict):
                continue
            pod_name: str = str(meta.get("name", ""))
            namespace: str = str(meta.get("namespace", ""))
            cpu, mem_mi = _sum_container_metrics(item.get("containers", []))
            workload_key = _workload_key_from_pod_name(pod_name, namespace)
            if workload_key:
                existing = result.get(workload_key)
                if existing is None:
                    result[workload_key] = {"cpu": cpu, "mem_mi": mem_mi, "count": 1.0}
                else:
                    existing["cpu"] += cpu
                    existing["mem_mi"] += mem_mi
                    existing["count"] += 2.0
        return result

    @_mutmut_mutated(mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut)
    def _build_workload_raw_data(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_orig(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_1(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = None
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_2(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(None, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_3(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, None, None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_4(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr("metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_5(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_6(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", )
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_7(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "XXmetadataXX", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_8(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "METADATA", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_9(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = None
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_10(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(None)
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_11(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") and "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_12(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(None, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_13(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, None, "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_14(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", None) or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_15(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr("name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_16(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_17(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", ) or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_18(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "XXnameXX", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_19(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "NAME", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_20(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "XXXX") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_21(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "XXXX")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_22(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = None
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_23(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(None)
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_24(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") and "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_25(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(None, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_26(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, None, "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_27(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", None) or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_28(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr("namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_29(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_30(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", ) or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_31(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "XXnamespaceXX", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_32(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "NAMESPACE", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_33(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "XXXX") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_34(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "XXXX")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_35(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = None
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_36(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(None)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_37(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = None
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_38(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = None
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_39(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(None)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_40(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = ""
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_41(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = ""
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_42(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_43(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = None
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_44(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] and 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_45(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["XXcountXX"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_46(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["COUNT"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_47(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 2.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_48(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = None
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_49(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] * count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_50(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["XXcpuXX"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_51(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["CPU"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_52(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = None
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_53(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] * count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_54(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["XXmem_miXX"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_55(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["MEM_MI"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_56(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "XXresource_nameXX": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_57(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "RESOURCE_NAME": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_58(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "XXnamespaceXX": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_59(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "NAMESPACE": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_60(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "XXkindXX": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_61(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "KIND": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_62(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "XXcpu_requested_coresXX": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_63(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "CPU_REQUESTED_CORES": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_64(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "XXmemory_requested_miXX": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_65(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "MEMORY_REQUESTED_MI": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_66(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "XXcpu_actual_coresXX": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_67(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "CPU_ACTUAL_CORES": cpu_actual,
            "memory_actual_mi": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_68(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "XXmemory_actual_miXX": mem_actual_mi,
        }

    def xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_69(
        self,
        workload: object,
        kind: str,
        pod_metrics: dict[str, dict[str, float]],
    ) -> WorkloadRawData:
        meta = getattr(workload, "metadata", None)
        name = str(getattr(meta, "name", "") or "")
        namespace = str(getattr(meta, "namespace", "") or "")
        cpu_req, mem_req_mi = _workload_resource_requests(workload)
        key = f"{namespace}/{name}"
        metrics = pod_metrics.get(key)
        cpu_actual: float | None = None
        mem_actual_mi: float | None = None
        if metrics is not None:
            count = metrics["count"] or 1.0
            cpu_actual = metrics["cpu"] / count
            mem_actual_mi = metrics["mem_mi"] / count
        return {
            "resource_name": name,
            "namespace": namespace,
            "kind": kind,
            "cpu_requested_cores": cpu_req,
            "memory_requested_mi": mem_req_mi,
            "cpu_actual_cores": cpu_actual,
            "MEMORY_ACTUAL_MI": mem_actual_mi,
        }

mutants_xǁVanillaRightsizingAdapterǁ__init____mutmut['_mutmut_orig'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ__init____mutmut['xǁVanillaRightsizingAdapterǁ__init____mutmut_1'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ__init____mutmut['xǁVanillaRightsizingAdapterǁ__init____mutmut_2'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['_mutmut_orig'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_1'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_2'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_3'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_4'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_5'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_6'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_7'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_8'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_9'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_10'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut['xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_11'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁget_workload_rightsizing_data__mutmut_11 # type: ignore # mutmut generated

mutants_xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut['_mutmut_orig'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_1'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_2'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_3'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_4'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_5'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_deployments__mutmut_5 # type: ignore # mutmut generated

mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['_mutmut_orig'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_1'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_2'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_3'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_4'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_5'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_6'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_7'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_8'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_9'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_10'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_11'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_12'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_13'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_14'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_15'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_16'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_17'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_18'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_19'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_20'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_21'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_22'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_23'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_24'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_25'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_26'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_27'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_28'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_29'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_30'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_31'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_32'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_33'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_34'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_35'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_36'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_37'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_38'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_39'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_40'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_41'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_42'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_43'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_44'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_45'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_46'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_47'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_48'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_49'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_50'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_51'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_52'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_53'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_54'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_55'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_56'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_57'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_58'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_59'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_60'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_61'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_62'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_63'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_64'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_65'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_66'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_67'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_68'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_69'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_70'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_71'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_72'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_73'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_74'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_75'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_75 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_76'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_76 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_77'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_77 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_78'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_78 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_79'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_79 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_80'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_80 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut['xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_81'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_fetch_pod_metrics_by_workload__mutmut_81 # type: ignore # mutmut generated

mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['_mutmut_orig'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_1'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_2'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_3'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_4'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_5'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_6'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_7'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_8'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_9'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_10'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_11'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_12'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_13'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_14'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_15'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_16'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_17'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_18'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_19'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_20'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_21'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_22'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_23'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_24'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_25'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_26'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_27'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_28'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_29'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_30'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_31'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_32'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_33'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_34'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_35'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_36'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_37'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_38'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_39'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_40'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_41'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_42'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_43'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_44'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_45'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_46'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_47'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_48'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_49'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_50'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_51'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_52'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_53'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_54'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_55'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_56'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_57'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_58'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_59'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_60'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_61'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_62'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_63'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_64'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_65'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_66'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_67'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_68'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut['xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_69'] = VanillaRightsizingAdapter.xǁVanillaRightsizingAdapterǁ_build_workload_raw_data__mutmut_69 # type: ignore # mutmut generated
