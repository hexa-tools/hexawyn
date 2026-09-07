from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from kubernetes import client

from hexawyn.application.ports.driven.cost_saving_estimation_port import (
    CostSavingEstimationPort,
    PodResourceData,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCoreApi,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.resource_parsers import (
    _deployment_key_from_pod,
    _parse_prometheus_pod_vector,
    _pod_requests_and_limits,
)

_K8S_TIMEOUT = 10
_PROMETHEUS_QUERY_TIMEOUT = 15.0
_POD_CPU_P95_QUERY = (
    "quantile_over_time(0.95,"
    " sum by (pod, namespace) (rate(container_cpu_usage_seconds_total{container!=''}[5m]))"
    "[7d:1h])"
)
_POD_MEM_P95_QUERY = (
    "quantile_over_time(0.95,"
    " sum by (pod, namespace) (container_memory_working_set_bytes{container!=''})"
    "[7d:1h]) / (1024 * 1024)"
)
_POD_CPU_MAX_QUERY = (
    "max_over_time("
    " sum by (pod, namespace) (rate(container_cpu_usage_seconds_total{container!=''}[5m]))"
    "[7d:1h])"
)


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
mutants_xǁVanillaCostSavingAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut: MutantDict = {}  # type: ignore


class VanillaCostSavingAdapter(CostSavingEstimationPort):
    @_mutmut_mutated(mutants_xǁVanillaCostSavingAdapterǁ__init____mutmut)
    def __init__(self, api: KubernetesCoreApi, prometheus_url: str = "") -> None:
        self._api = api
        self._prometheus_url = prometheus_url
    def xǁVanillaCostSavingAdapterǁ__init____mutmut_orig(self, api: KubernetesCoreApi, prometheus_url: str = "") -> None:
        self._api = api
        self._prometheus_url = prometheus_url
    def xǁVanillaCostSavingAdapterǁ__init____mutmut_1(self, api: KubernetesCoreApi, prometheus_url: str = "XXXX") -> None:
        self._api = api
        self._prometheus_url = prometheus_url
    def xǁVanillaCostSavingAdapterǁ__init____mutmut_2(self, api: KubernetesCoreApi, prometheus_url: str = "") -> None:
        self._api = None
        self._prometheus_url = prometheus_url
    def xǁVanillaCostSavingAdapterǁ__init____mutmut_3(self, api: KubernetesCoreApi, prometheus_url: str = "") -> None:
        self._api = api
        self._prometheus_url = None

    @_mutmut_mutated(mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut)
    def get_pod_resource_data(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_orig(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_1(self) -> list[PodResourceData]:
        try:
            raw = None
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_2(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=None)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_3(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(None) from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_4(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = None
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_5(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = None
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_6(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(None)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_7(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = None
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_8(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(None)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_9(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = None
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_10(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(None)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_11(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = None
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_12(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(None):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_13(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = None
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_14(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(None, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_15(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, None, None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_16(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr("metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_17(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_18(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", )
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_19(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "XXmetadataXX", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_20(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "METADATA", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_21(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = None
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_22(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(None)
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_23(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(None, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_24(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, None, ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_25(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", None))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_26(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr("name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_27(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_28(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_29(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "XXnameXX", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_30(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "NAME", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_31(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "XXXX"))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_32(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = None
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_33(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(None)
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_34(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(None, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_35(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, None, ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_36(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", None))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_37(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr("namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_38(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_39(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_40(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "XXnamespaceXX", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_41(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "NAMESPACE", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_42(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", "XXXX"))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_43(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = None
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_44(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(None, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_45(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, None, None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_46(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr("spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_47(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_48(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", )
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_49(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "XXspecXX", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_50(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "SPEC", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_51(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = None
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_52(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(None) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_53(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) and []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_54(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(None, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_55(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, None, None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_56(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr("containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_57(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_58(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", ) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_59(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "XXcontainersXX", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_60(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "CONTAINERS", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_61(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = None
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_62(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(None)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_63(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = None
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_64(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = None
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_65(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(None, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_66(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, None)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_67(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_68(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, )
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_69(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_70(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(None) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_71(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                None
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_72(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=None,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_73(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=None,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_74(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=None,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_75(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=None,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_76(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=None,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_77(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=None,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_78(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=None,
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_79(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=None,
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_80(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=None,
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_81(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_82(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=None,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_83(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_84(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_85(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_86(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_87(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_88(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_89(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_90(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_91(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_92(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_93(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_94(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(None),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_95(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(None),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_96(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(None),
                    hpa_enabled=hpa_info is not None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    def xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_97(self) -> list[PodResourceData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for cost saving: {exc}") from exc
        hpa_map = self._fetch_hpa_map()
        cpu_p95_map = self._fetch_pod_prometheus_map(_POD_CPU_P95_QUERY)
        mem_p95_map = self._fetch_pod_prometheus_map(_POD_MEM_P95_QUERY)
        cpu_max_map = self._fetch_pod_prometheus_map(_POD_CPU_MAX_QUERY)
        result: list[PodResourceData] = []
        for pod in _items_from(raw):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            spec = getattr(pod, "spec", None)
            containers_list = list(getattr(spec, "containers", None) or []) if spec else []
            cpu_req, mem_req_mi, cpu_lim, mem_lim_mi = _pod_requests_and_limits(containers_list)
            pod_key = f"{namespace}/{pod_name}"
            deployment_key = _deployment_key_from_pod(pod_name, namespace)
            hpa_info = hpa_map.get(deployment_key) if deployment_key else None
            result.append(
                PodResourceData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_request_cores=cpu_req,
                    memory_request_mi=mem_req_mi,
                    cpu_limit_cores=cpu_lim,
                    memory_limit_mi=mem_lim_mi,
                    cpu_p95_cores=cpu_p95_map.get(pod_key),
                    memory_p95_mi=mem_p95_map.get(pod_key),
                    cpu_max_cores=cpu_max_map.get(pod_key),
                    hpa_enabled=hpa_info is None,
                    hpa_min_replicas=hpa_info,
                )
            )
        return result

    @_mutmut_mutated(mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut)
    def _fetch_hpa_map(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_orig(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_1(self) -> dict[str, int]:
        try:
            auto_api = None
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_2(self) -> dict[str, int]:
        try:
            auto_api = cast(None, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_3(self) -> dict[str, int]:
        try:
            auto_api = cast(object, None)
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_4(self) -> dict[str, int]:
        try:
            auto_api = cast(client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_5(self) -> dict[str, int]:
        try:
            auto_api = cast(object, )
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_6(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = None
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_7(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=None
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_8(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(None, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_9(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, None)(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_10(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr("list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_11(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, )(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_12(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "XXlist_horizontal_pod_autoscaler_for_all_namespacesXX")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_13(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "LIST_HORIZONTAL_POD_AUTOSCALER_FOR_ALL_NAMESPACES")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_14(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = None
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_15(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(None):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_16(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = None
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_17(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(None, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_18(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, None, None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_19(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr("metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_20(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_21(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", )
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_22(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "XXmetadataXX", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_23(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "METADATA", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_24(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = None
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_25(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(None)
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_26(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(None, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_27(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, None, ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_28(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", None))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_29(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr("namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_30(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_31(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_32(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "XXnamespaceXX", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_33(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "NAMESPACE", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_34(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", "XXXX"))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_35(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = None
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_36(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(None, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_37(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, None, None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_38(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr("spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_39(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_40(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", )
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_41(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "XXspecXX", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_42(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "SPEC", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_43(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_44(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(None, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_45(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, None, None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_46(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr("scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_47(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_48(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", ) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_49(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "XXscale_target_refXX", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_50(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "SCALE_TARGET_REF", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_51(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = None
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_52(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(None) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_53(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(None, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_54(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, None, "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_55(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", None)) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_56(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr("name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_57(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_58(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", )) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_59(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "XXnameXX", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_60(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "NAME", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_61(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "XXXX")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_62(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else "XXXX"
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_63(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = None
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_64(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(None)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_65(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) and 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_66(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(None, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_67(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, None, 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_68(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", None) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_69(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr("min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_70(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_71(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", ) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_72(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "XXmin_replicasXX", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_73(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "MIN_REPLICAS", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_74(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 2) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_75(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 2)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_76(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns or target_name:
                    hpa_map[f"{ns}/{target_name}"] = min_rep
            return hpa_map
        except Exception:
            return {}

    def xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_77(self) -> dict[str, int]:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_horizontal_pod_autoscaler_for_all_namespaces")(
                timeout_seconds=_K8S_TIMEOUT
            )
            hpa_map: dict[str, int] = {}
            for item in _items_from(raw):
                meta = getattr(item, "metadata", None)
                ns = str(getattr(meta, "namespace", ""))
                spec = getattr(item, "spec", None)
                ref = getattr(spec, "scale_target_ref", None) if spec else None
                target_name = str(getattr(ref, "name", "")) if ref else ""
                min_rep = int(getattr(spec, "min_replicas", 1) or 1)
                if ns and target_name:
                    hpa_map[f"{ns}/{target_name}"] = None
            return hpa_map
        except Exception:
            return {}

    @_mutmut_mutated(mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut)
    def _fetch_pod_prometheus_map(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_orig(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_1(self, query: str) -> dict[str, float]:
        if self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_2(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = None
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_3(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                None,
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_4(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params=None,
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_5(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=None,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_6(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_7(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_8(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_9(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"XXqueryXX": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_10(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"QUERY": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(resp.json())

    def xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_11(self, query: str) -> dict[str, float]:
        if not self._prometheus_url:
            return {}
        import httpx

        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
        except Exception:
            return {}
        return _parse_prometheus_pod_vector(None)

    @_mutmut_mutated(mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut)
    def get_previous_total_saving(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_orig(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_1(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = None
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_2(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = None
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_3(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                None
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_4(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "XXSELECT savings_right_sizing FROM cost_audits XX"
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_5(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "select savings_right_sizing from cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_6(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT SAVINGS_RIGHT_SIZING FROM COST_AUDITS "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_7(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "XXWHERE namespace = '__cost_saving__' XX"
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_8(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "where namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_9(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE NAMESPACE = '__COST_SAVING__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_10(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "XXORDER BY timestamp DESC LIMIT 1XX"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_11(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "order by timestamp desc limit 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_12(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY TIMESTAMP DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_13(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(None) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_14(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[1]) if row and row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_15(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row or row[0] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_16(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[1] is not None else None
        except Exception:
            return None

    def xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_17(self) -> float | None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            row = conn.execute(
                "SELECT savings_right_sizing FROM cost_audits "
                "WHERE namespace = '__cost_saving__' "
                "ORDER BY timestamp DESC LIMIT 1"
            ).fetchone()
            return float(row[0]) if row and row[0] is None else None
        except Exception:
            return None

    @_mutmut_mutated(mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut)
    def store_total_saving(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "INSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) "
                "VALUES ('__cost_saving__', ?, ?)",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_orig(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "INSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) "
                "VALUES ('__cost_saving__', ?, ?)",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_1(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = None
            conn.execute(
                "INSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) "
                "VALUES ('__cost_saving__', ?, ?)",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_2(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                None,
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_3(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "INSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) "
                "VALUES ('__cost_saving__', ?, ?)",
                None,
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_4(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_5(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "INSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) "
                "VALUES ('__cost_saving__', ?, ?)",
                )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_6(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "XXINSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) XX"
                "VALUES ('__cost_saving__', ?, ?)",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_7(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "insert into cost_audits (namespace, savings_right_sizing, savings_total) "
                "VALUES ('__cost_saving__', ?, ?)",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_8(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "INSERT INTO COST_AUDITS (NAMESPACE, SAVINGS_RIGHT_SIZING, SAVINGS_TOTAL) "
                "VALUES ('__cost_saving__', ?, ?)",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_9(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "INSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) "
                "XXVALUES ('__cost_saving__', ?, ?)XX",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_10(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "INSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) "
                "values ('__cost_saving__', ?, ?)",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

    def xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_11(self, total_saving_usd: float) -> None:
        try:
            from hexawyn.infrastructure.memory.duckdb_client import get_connection

            conn = get_connection()
            conn.execute(
                "INSERT INTO cost_audits (namespace, savings_right_sizing, savings_total) "
                "VALUES ('__COST_SAVING__', ?, ?)",
                [total_saving_usd, total_saving_usd],
            )
        except Exception:
            pass

mutants_xǁVanillaCostSavingAdapterǁ__init____mutmut['_mutmut_orig'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ__init____mutmut['xǁVanillaCostSavingAdapterǁ__init____mutmut_1'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ__init____mutmut['xǁVanillaCostSavingAdapterǁ__init____mutmut_2'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ__init____mutmut['xǁVanillaCostSavingAdapterǁ__init____mutmut_3'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['_mutmut_orig'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_1'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_2'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_3'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_4'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_5'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_6'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_7'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_8'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_9'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_10'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_11'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_12'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_13'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_14'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_15'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_16'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_17'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_18'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_19'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_20'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_21'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_22'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_23'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_24'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_25'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_26'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_27'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_28'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_29'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_30'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_31'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_32'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_33'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_34'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_35'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_36'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_37'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_38'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_39'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_40'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_41'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_42'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_43'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_44'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_45'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_46'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_47'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_48'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_49'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_50'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_51'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_52'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_53'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_54'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_55'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_56'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_57'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_58'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_59'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_60'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_61'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_62'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_63'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_64'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_65'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_66'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_67'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_68'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_69'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_70'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_71'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_72'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_73'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_74'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_75'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_75 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_76'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_76 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_77'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_77 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_78'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_78 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_79'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_79 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_80'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_80 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_81'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_81 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_82'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_82 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_83'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_83 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_84'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_84 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_85'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_85 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_86'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_86 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_87'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_87 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_88'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_88 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_89'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_89 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_90'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_90 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_91'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_91 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_92'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_92 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_93'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_93 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_94'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_94 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_95'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_95 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_96'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_96 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut['xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_97'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_pod_resource_data__mutmut_97 # type: ignore # mutmut generated

mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['_mutmut_orig'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_1'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_2'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_3'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_4'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_5'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_6'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_7'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_8'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_9'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_10'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_11'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_12'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_13'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_14'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_15'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_16'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_17'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_18'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_19'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_20'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_21'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_22'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_23'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_24'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_25'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_26'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_27'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_28'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_29'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_30'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_31'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_32'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_33'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_34'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_35'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_36'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_37'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_38'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_39'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_40'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_41'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_42'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_43'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_44'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_45'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_46'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_47'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_48'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_49'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_50'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_51'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_52'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_53'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_54'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_55'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_56'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_57'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_58'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_59'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_60'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_61'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_62'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_63'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_64'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_65'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_66'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_67'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_68'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_69'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_70'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_71'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_72'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_73'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_74'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_75'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_75 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_76'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_76 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_77'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_hpa_map__mutmut_77 # type: ignore # mutmut generated

mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['_mutmut_orig'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_1'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_2'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_3'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_4'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_5'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_6'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_7'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_8'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_9'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_10'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut['xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_11'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁ_fetch_pod_prometheus_map__mutmut_11 # type: ignore # mutmut generated

mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['_mutmut_orig'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_1'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_2'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_3'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_4'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_5'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_6'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_7'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_8'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_9'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_10'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_11'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_12'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_13'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_14'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_15'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_16'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut['xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_17'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁget_previous_total_saving__mutmut_17 # type: ignore # mutmut generated

mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['_mutmut_orig'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_1'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_2'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_3'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_4'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_5'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_6'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_7'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_8'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_9'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_10'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut['xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_11'] = VanillaCostSavingAdapter.xǁVanillaCostSavingAdapterǁstore_total_saving__mutmut_11 # type: ignore # mutmut generated
