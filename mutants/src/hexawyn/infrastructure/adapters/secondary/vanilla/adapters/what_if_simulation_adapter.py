from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from kubernetes import client

from hexawyn.application.ports.driven.probe_audit_port import (
    ProbeAuditPort,
    ProbeContainerRawData,
    ProbeDeploymentRawData,
)
from hexawyn.application.ports.driven.what_if_simulation_port import (
    DependentServiceData,
    HPAData,
    PDBData,
    WhatIfSimulationPort,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesAppsApi,
    KubernetesCoreApi,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.resource_parsers import (
    _deployment_key_from_pod,
    _extract_container_data,
    _extract_init_container_data,
    _get_workload_type,
)

_K8S_TIMEOUT = 10
_PROMETHEUS_QUERY_TIMEOUT = 15.0


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
mutants_xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut: MutantDict = {}  # type: ignore


class VanillaWhatIfSimulationAdapter(WhatIfSimulationPort, ProbeAuditPort):
    @_mutmut_mutated(mutants_xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut)
    def __init__(
        self,
        api: KubernetesCoreApi,
        apps_api: KubernetesAppsApi,
        prometheus_url: str = "",
    ) -> None:
        self._api = api
        self._apps_api = apps_api
        self._prometheus_url = prometheus_url
    def xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_orig(
        self,
        api: KubernetesCoreApi,
        apps_api: KubernetesAppsApi,
        prometheus_url: str = "",
    ) -> None:
        self._api = api
        self._apps_api = apps_api
        self._prometheus_url = prometheus_url
    def xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_1(
        self,
        api: KubernetesCoreApi,
        apps_api: KubernetesAppsApi,
        prometheus_url: str = "XXXX",
    ) -> None:
        self._api = api
        self._apps_api = apps_api
        self._prometheus_url = prometheus_url
    def xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_2(
        self,
        api: KubernetesCoreApi,
        apps_api: KubernetesAppsApi,
        prometheus_url: str = "",
    ) -> None:
        self._api = None
        self._apps_api = apps_api
        self._prometheus_url = prometheus_url
    def xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_3(
        self,
        api: KubernetesCoreApi,
        apps_api: KubernetesAppsApi,
        prometheus_url: str = "",
    ) -> None:
        self._api = api
        self._apps_api = None
        self._prometheus_url = prometheus_url
    def xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_4(
        self,
        api: KubernetesCoreApi,
        apps_api: KubernetesAppsApi,
        prometheus_url: str = "",
    ) -> None:
        self._api = api
        self._apps_api = apps_api
        self._prometheus_url = None

    @_mutmut_mutated(mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut)
    def get_current_replicas(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_orig(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_1(self, namespace: str, service_name: str) -> int:
        try:
            raw = None
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_2(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=None)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_3(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 1
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_4(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(None):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_5(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = None
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_6(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(None, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_7(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, None, None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_8(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr("metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_9(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_10(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", )
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_11(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "XXmetadataXX", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_12(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "METADATA", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_13(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = None
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_14(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(None)
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_15(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(None, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_16(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, None, ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_17(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", None))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_18(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr("namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_19(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_20(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_21(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "XXnamespaceXX", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_22(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "NAMESPACE", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_23(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", "XXXX"))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_24(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = None
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_25(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(None)
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_26(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(None, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_27(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, None, ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_28(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", None))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_29(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr("name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_30(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_31(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_32(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "XXnameXX", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_33(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "NAME", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_34(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", "XXXX"))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_35(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace or name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_36(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns != namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_37(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name != service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_38(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = None
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_39(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(None, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_40(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, None, None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_41(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr("spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_42(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_43(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", )
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_44(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "XXspecXX", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_45(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "SPEC", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_46(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(None)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_47(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) and 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_48(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(None, "replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_49(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, None, 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_50(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", None) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_51(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr("replicas", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_52(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_53(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", ) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_54(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "XXreplicasXX", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_55(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "REPLICAS", 0) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_56(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 1) or 0)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_57(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 1)
        return 0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_58(self, namespace: str, service_name: str) -> int:
        try:
            raw = self._apps_api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return 0
        for dep in _items_from(raw):
            meta = getattr(dep, "metadata", None)
            ns = str(getattr(meta, "namespace", ""))
            name = str(getattr(meta, "name", ""))
            if ns == namespace and name == service_name:
                spec = getattr(dep, "spec", None)
                return int(getattr(spec, "replicas", 0) or 0)
        return 1

    @_mutmut_mutated(mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut)
    def get_current_cpu_utilization(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_orig(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_1(self, namespace: str, service_name: str) -> float:
        if self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_2(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 1.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_3(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = None
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_4(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = None
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_5(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                None,
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_6(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params=None,
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_7(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=None,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_8(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_9(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_10(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_11(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"XXqueryXX": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_12(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"QUERY": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_13(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = None
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_14(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = None
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_15(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get(None, [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_16(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", None)
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_17(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get([])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_18(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", )
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_19(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get(None, {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_20(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", None).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_21(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get({}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_22(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", ).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_23(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("XXdataXX", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_24(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("DATA", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_25(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("XXresultXX", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_26(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("RESULT", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_27(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results or isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_28(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = None
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_29(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get(None, [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_30(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", None)
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_31(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get([None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_32(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", )
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_33(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[1].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_34(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("XXvalueXX", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_35(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("VALUE", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_36(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "XX0XX"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_37(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) > 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_38(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 3:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_39(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(None)
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_40(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[2])
        except Exception:
            pass
        return 0.0

    def xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_41(self, namespace: str, service_name: str) -> float:
        if not self._prometheus_url:
            return 0.0
        import httpx

        query = (
            f'sum(rate(container_cpu_usage_seconds_total{{namespace="{namespace}",'
            f'pod=~"{service_name}-.*"}}[5m])) / '
            f'sum(kube_pod_container_resource_requests{{resource="cpu",'
            f'namespace="{namespace}",pod=~"{service_name}-.*"}}) * 100'
        )
        try:
            resp = httpx.get(
                f"{self._prometheus_url}/api/v1/query",
                params={"query": query},
                timeout=_PROMETHEUS_QUERY_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("data", {}).get("result", [])
            if results and isinstance(results, list):
                value = results[0].get("value", [None, "0"])
                if len(value) >= 2:  # noqa: PLR2004
                    return float(value[1])
        except Exception:
            pass
        return 1.0

    @_mutmut_mutated(mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut)
    def get_pdb_info(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_orig(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_1(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = None
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_2(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(None, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_3(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, None, None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_4(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr("list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_5(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_6(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", )
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_7(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "XXlist_namespaced_pod_disruption_budgetXX", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_8(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "LIST_NAMESPACED_POD_DISRUPTION_BUDGET", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_9(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is not None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_10(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = None
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_11(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(None, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_12(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=None)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_13(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_14(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, )
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_15(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(None):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_16(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = None
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_17(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(None, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_18(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, None, None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_19(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr("metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_20(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_21(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", )
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_22(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "XXmetadataXX", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_23(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "METADATA", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_24(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = None
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_25(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(None)
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_26(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(None, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_27(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, None, ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_28(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", None))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_29(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr("name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_30(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_31(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_32(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "XXnameXX", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_33(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "NAME", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_34(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", "XXXX"))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_35(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name not in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_36(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = None
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_37(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(None, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_38(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, None, None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_39(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr("spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_40(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_41(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", )
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_42(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "XXspecXX", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_43(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "SPEC", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_44(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_45(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(None, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_46(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, None, None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_47(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr("min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_48(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_49(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", ) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_50(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "XXmin_availableXX", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_51(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "MIN_AVAILABLE", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_52(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "XXmin_availableXX": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_53(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "MIN_AVAILABLE": int(min_available)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_54(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(None)
                    if isinstance(min_available, int | str) and str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_55(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) or str(min_available).isdigit()
                    else None
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_56(self, namespace: str, service_name: str) -> PDBData | None:
        try:
            raw = getattr(self._api, "list_namespaced_pod_disruption_budget", None)
            if raw is None:
                return None
            item_list = raw(namespace, timeout_seconds=_K8S_TIMEOUT)
        except Exception:
            return None
        for item in _items_from(item_list):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                min_available = getattr(spec, "min_available", None) if spec else None
                return {
                    "min_available": int(min_available)
                    if isinstance(min_available, int | str) and str(None).isdigit()
                    else None
                }
        return None

    @_mutmut_mutated(mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut)
    def get_hpa_info(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_orig(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_1(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = None
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_2(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(None, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_3(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, None)
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_4(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_5(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, )
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_6(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = None
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_7(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                None, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_8(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=None
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_9(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_10(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_11(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(None, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_12(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, None)(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_13(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr("list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_14(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, )(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_15(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "XXlist_namespaced_horizontal_pod_autoscalerXX")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_16(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "LIST_NAMESPACED_HORIZONTAL_POD_AUTOSCALER")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_17(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(None):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_18(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = None
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_19(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(None, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_20(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, None, None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_21(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr("metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_22(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_23(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", )
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_24(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "XXmetadataXX", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_25(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "METADATA", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_26(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = None
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_27(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(None)
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_28(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(None, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_29(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, None, ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_30(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", None))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_31(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr("name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_32(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_33(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_34(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "XXnameXX", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_35(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "NAME", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_36(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", "XXXX"))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_37(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name not in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_38(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = None
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_39(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(None, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_40(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, None, None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_41(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr("spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_42(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_43(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", )
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_44(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "XXspecXX", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_45(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "SPEC", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_46(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = None
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_47(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(None, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_48(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, None, None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_49(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr("status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_50(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_51(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", )
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_52(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "XXstatusXX", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_53(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "STATUS", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_54(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "XXmin_replicasXX": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_55(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "MIN_REPLICAS": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_56(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(None),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_57(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) and 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_58(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(None, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_59(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, None, 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_60(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", None) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_61(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr("min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_62(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_63(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", ) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_64(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "XXmin_replicasXX", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_65(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "MIN_REPLICAS", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_66(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 2) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_67(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 2),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_68(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "XXmax_replicasXX": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_69(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "MAX_REPLICAS": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_70(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(None),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_71(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) and 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_72(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(None, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_73(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, None, 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_74(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", None) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_75(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr("max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_76(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_77(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", ) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_78(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "XXmax_replicasXX", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_79(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "MAX_REPLICAS", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_80(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 2) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_81(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 2),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_82(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "XXcurrent_replicasXX": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_83(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "CURRENT_REPLICAS": int(getattr(status, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_84(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(None),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_85(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) and 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_86(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(None, "current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_87(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, None, 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_88(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", None) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_89(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr("current_replicas", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_90(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_91(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", ) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_92(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "XXcurrent_replicasXX", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_93(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "CURRENT_REPLICAS", 0) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_94(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 1) or 0),
                }
        return None

    def xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_95(self, namespace: str, service_name: str) -> HPAData | None:
        try:
            auto_api = cast(object, client.AutoscalingV2Api())
            raw = getattr(auto_api, "list_namespaced_horizontal_pod_autoscaler")(
                namespace, timeout_seconds=_K8S_TIMEOUT
            )
        except Exception:
            return None
        for item in _items_from(raw):
            meta = getattr(item, "metadata", None)
            name = str(getattr(meta, "name", ""))
            if service_name in name:
                spec = getattr(item, "spec", None)
                status = getattr(item, "status", None)
                return {
                    "min_replicas": int(getattr(spec, "min_replicas", 1) or 1),
                    "max_replicas": int(getattr(spec, "max_replicas", 1) or 1),
                    "current_replicas": int(getattr(status, "current_replicas", 0) or 1),
                }
        return None

    @_mutmut_mutated(mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut)
    def get_service_topology(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_orig(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_1(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = None  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_2(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=None)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_3(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = None
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_4(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_5(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    break
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_6(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = None
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_7(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name and ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_8(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or "XXXX"
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_9(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = None
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_10(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector and {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_11(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = None
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_12(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=None,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_13(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=None,
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_14(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_15(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_16(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(None),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_17(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector="XX,XX".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_18(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = None
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_19(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            None
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_20(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=None,
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_21(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=None,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_22(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=None,
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_23(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_24(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_25(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_26(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name and "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_27(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "XXXX",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_28(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase and "Unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_29(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "XXUnknownXX",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_30(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "unknown",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_31(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "UNKNOWN",
                            )
                        )
                result[svc_name] = deps
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_32(
        self, namespace: str, service_name: str
    ) -> dict[str, list[DependentServiceData]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[DependentServiceData]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                deps: list[DependentServiceData] = []
                for pod in pods.items:  # type: ignore
                    if pod.metadata:
                        deps.append(
                            DependentServiceData(  # type: ignore
                                name=pod.metadata.name or "",
                                namespace=namespace,
                                status=pod.status.phase or "Unknown",
                            )
                        )
                result[svc_name] = None
            return result
        except Exception:
            return {}

    @_mutmut_mutated(mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut)
    def get_dependency_graph(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_orig(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_1(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = None  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_2(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=None)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_3(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = None
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_4(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_5(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    break
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_6(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = None
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_7(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name and ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_8(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or "XXXX"
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_9(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = None
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_10(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector and {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_11(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = None
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_12(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=None,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_13(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=None,
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_14(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_15(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_16(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(None),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_17(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector="XX,XX".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_18(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = None
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_19(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(None):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_20(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = None
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_21(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(None, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_22(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, None, None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_23(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr("metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_24(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_25(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", )
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_26(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "XXmetadataXX", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_27(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "METADATA", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_28(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_29(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(None, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_30(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, None, None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_31(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr("name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_32(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_33(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", ) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_34(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "XXnameXX", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_35(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "NAME", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_36(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(None)
                result[svc_name] = pod_names
            return result
        except Exception:
            return {}

    def xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_37(self, namespace: str) -> dict[str, list[str]]:
        try:
            services = self._api.list_namespaced_service(namespace=namespace)  # type: ignore
            result: dict[str, list[str]] = {}
            for svc in services.items:
                if not svc.metadata:
                    continue
                svc_name = svc.metadata.name or ""
                selectors = svc.spec.selector or {}
                pods = self._api.list_namespaced_pod(  # type: ignore
                    namespace=namespace,
                    label_selector=",".join(f"{k}={v}" for k, v in selectors.items()),
                )
                pod_names = []
                for p in _items_from(pods):
                    meta = getattr(p, "metadata", None)
                    name = getattr(meta, "name", None) if meta else None
                    if name:
                        pod_names.append(name)
                result[svc_name] = None
            return result
        except Exception:
            return {}

    @_mutmut_mutated(mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut)
    def get_probe_audit_data(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_orig(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_1(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = None
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_2(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=None)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_3(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(None) from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_4(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = None
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_5(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = None
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_6(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(None):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_7(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = None
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_8(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(None, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_9(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, None, None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_10(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr("metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_11(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_12(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", )
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_13(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "XXmetadataXX", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_14(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "METADATA", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_15(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = None
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_16(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(None) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_17(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(None, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_18(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, None, "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_19(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", None)) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_20(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr("name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_21(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_22(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", )) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_23(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "XXnameXX", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_24(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "NAME", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_25(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "XXXX")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_26(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else "XXXX"
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_27(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = None
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_28(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(None) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_29(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(None, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_30(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, None, "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_31(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", None)) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_32(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr("namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_33(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_34(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", )) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_35(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "XXnamespaceXX", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_36(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "NAMESPACE", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_37(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "XXXX")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_38(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else "XXXX"
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_39(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None or namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_40(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_41(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name == namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_42(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                break
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_43(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = None
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_44(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(None, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_45(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, None)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_46(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_47(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, )
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_48(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is not None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_49(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                break
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_50(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key not in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_51(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                break
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_52(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(None)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_53(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = None
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_54(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit(None, 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_55(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", None)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_56(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit(2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_57(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", )[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_58(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.split("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_59(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("XX-XX", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_60(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 3)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_61(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[1] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_62(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "XX-XX" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_63(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" not in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_64(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_65(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(None, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_66(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, None, None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_67(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr("owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_68(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_69(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", ) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_70(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "XXowner_referencesXX", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_71(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "OWNER_REFERENCES", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_72(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = None
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_73(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(None)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_74(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = None
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_75(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(None, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_76(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, None, None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_77(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr("spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_78(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_79(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", )
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_80(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "XXspecXX", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_81(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "SPEC", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_82(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = None
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_83(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(None, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_84(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, None, []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_85(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", None) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_86(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr("containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_87(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_88(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", ) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_89(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "XXcontainersXX", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_90(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "CONTAINERS", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_91(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = None
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_92(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(None, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_93(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, None, []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_94(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", None) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_95(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr("init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_96(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_97(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", ) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_98(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "XXinit_containersXX", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_99(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "INIT_CONTAINERS", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_100(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = None
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_101(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(None)
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_102(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(None))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_103(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(None)
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_104(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(None))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_105(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                None
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_106(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=None,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_107(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=None,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_108(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=None,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_109(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=None,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_110(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=None,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_111(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=None,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_112(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_113(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_114(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_115(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    has_service=False,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_116(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_117(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_118(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=True,
                    is_exposed_externally=False,
                )
            )
        return result

    def xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_119(self, namespace: str | None = None) -> list[ProbeDeploymentRawData]:
        try:
            pod_list = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for probe audit: {exc}") from exc
        result: list[ProbeDeploymentRawData] = []
        seen_deployments: set[str] = set()
        for pod in _items_from(pod_list):
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "")) if meta else ""
            namespace_name = str(getattr(meta, "namespace", "")) if meta else ""
            if namespace is not None and namespace_name != namespace:
                continue
            deployment_key = _deployment_key_from_pod(pod_name, namespace_name)
            if deployment_key is None:
                continue
            if deployment_key in seen_deployments:
                continue
            seen_deployments.add(deployment_key)
            deployment_name = pod_name.rsplit("-", 2)[0] if "-" in pod_name else pod_name
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            workload_type = _get_workload_type(owner_refs)
            spec = getattr(pod, "spec", None)
            containers_raw = getattr(spec, "containers", []) if spec else []
            init_containers_raw = getattr(spec, "init_containers", []) if spec else []
            containers: list[ProbeContainerRawData] = []
            for container in init_containers_raw:
                containers.append(_extract_init_container_data(container))
            for container in containers_raw:
                containers.append(_extract_container_data(container))
            result.append(
                ProbeDeploymentRawData(
                    deployment_name=deployment_name,
                    namespace=namespace_name,
                    workload_type=workload_type,
                    containers=containers,
                    has_service=False,
                    is_exposed_externally=True,
                )
            )
        return result

mutants_xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut['_mutmut_orig'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut['xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_1'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut['xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_2'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut['xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_3'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut['xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_4'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['_mutmut_orig'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_1'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_2'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_3'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_4'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_5'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_6'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_7'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_8'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_9'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_10'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_11'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_12'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_13'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_14'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_15'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_16'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_17'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_18'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_19'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_20'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_21'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_22'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_23'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_24'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_25'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_26'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_27'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_28'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_29'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_30'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_31'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_32'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_33'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_34'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_35'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_36'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_37'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_38'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_39'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_40'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_41'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_42'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_43'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_44'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_45'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_46'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_47'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_48'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_49'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_50'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_51'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_52'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_53'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_54'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_55'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_56'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_57'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_58'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_replicas__mutmut_58 # type: ignore # mutmut generated

mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['_mutmut_orig'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_1'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_2'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_3'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_4'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_5'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_6'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_7'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_8'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_9'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_10'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_11'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_12'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_13'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_14'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_15'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_16'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_17'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_18'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_19'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_20'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_21'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_22'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_23'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_24'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_25'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_26'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_27'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_28'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_29'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_30'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_31'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_32'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_33'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_34'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_35'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_36'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_37'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_38'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_39'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_40'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_41'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_current_cpu_utilization__mutmut_41 # type: ignore # mutmut generated

mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['_mutmut_orig'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_1'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_2'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_3'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_4'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_5'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_6'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_7'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_8'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_9'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_10'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_11'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_12'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_13'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_14'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_15'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_16'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_17'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_18'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_19'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_20'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_21'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_22'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_23'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_24'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_25'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_26'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_27'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_28'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_29'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_30'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_31'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_32'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_33'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_34'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_35'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_36'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_37'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_38'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_39'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_40'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_41'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_42'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_43'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_44'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_45'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_46'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_47'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_48'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_49'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_50'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_51'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_52'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_53'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_54'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_55'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_56'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_pdb_info__mutmut_56 # type: ignore # mutmut generated

mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['_mutmut_orig'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_1'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_2'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_3'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_4'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_5'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_6'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_7'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_8'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_9'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_10'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_11'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_12'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_13'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_14'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_15'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_16'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_17'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_18'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_19'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_20'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_21'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_22'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_23'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_24'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_25'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_26'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_27'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_28'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_29'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_30'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_31'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_32'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_33'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_34'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_35'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_36'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_37'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_38'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_39'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_40'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_41'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_42'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_43'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_44'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_45'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_46'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_47'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_48'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_49'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_50'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_51'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_52'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_53'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_54'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_55'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_56'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_57'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_58'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_59'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_60'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_61'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_62'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_63'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_64'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_65'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_66'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_67'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_68'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_69'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_70'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_71'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_72'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_73'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_74'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_75'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_75 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_76'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_76 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_77'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_77 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_78'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_78 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_79'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_79 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_80'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_80 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_81'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_81 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_82'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_82 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_83'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_83 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_84'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_84 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_85'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_85 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_86'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_86 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_87'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_87 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_88'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_88 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_89'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_89 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_90'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_90 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_91'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_91 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_92'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_92 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_93'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_93 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_94'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_94 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_95'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_hpa_info__mutmut_95 # type: ignore # mutmut generated

mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['_mutmut_orig'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_1'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_2'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_3'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_4'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_5'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_6'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_7'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_8'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_9'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_10'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_11'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_12'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_13'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_14'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_15'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_16'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_17'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_18'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_19'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_20'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_21'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_22'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_23'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_24'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_25'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_26'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_27'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_28'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_29'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_30'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_31'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_32'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_service_topology__mutmut_32 # type: ignore # mutmut generated

mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['_mutmut_orig'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_1'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_2'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_3'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_4'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_5'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_6'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_7'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_8'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_9'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_10'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_11'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_12'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_13'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_14'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_15'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_16'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_17'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_18'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_19'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_20'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_21'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_22'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_23'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_24'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_25'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_26'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_27'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_28'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_29'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_30'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_31'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_32'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_33'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_34'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_35'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_36'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_37'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_dependency_graph__mutmut_37 # type: ignore # mutmut generated

mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['_mutmut_orig'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_1'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_2'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_3'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_4'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_5'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_6'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_7'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_8'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_9'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_10'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_11'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_12'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_13'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_14'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_15'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_16'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_17'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_18'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_19'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_20'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_21'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_22'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_23'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_24'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_25'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_26'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_27'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_28'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_29'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_30'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_31'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_32'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_33'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_34'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_35'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_36'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_37'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_38'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_39'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_40'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_41'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_42'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_43'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_44'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_45'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_46'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_47'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_48'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_49'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_50'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_51'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_52'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_53'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_54'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_55'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_56'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_57'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_58'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_59'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_60'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_61'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_62'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_63'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_64'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_65'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_66'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_67'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_68'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_69'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_70'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_71'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_72'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_73'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_74'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_75'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_75 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_76'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_76 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_77'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_77 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_78'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_78 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_79'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_79 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_80'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_80 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_81'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_81 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_82'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_82 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_83'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_83 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_84'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_84 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_85'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_85 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_86'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_86 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_87'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_87 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_88'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_88 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_89'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_89 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_90'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_90 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_91'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_91 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_92'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_92 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_93'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_93 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_94'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_94 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_95'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_95 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_96'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_96 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_97'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_97 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_98'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_98 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_99'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_99 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_100'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_100 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_101'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_101 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_102'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_102 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_103'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_103 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_104'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_104 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_105'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_105 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_106'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_106 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_107'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_107 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_108'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_108 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_109'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_109 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_110'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_110 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_111'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_111 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_112'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_112 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_113'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_113 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_114'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_114 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_115'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_115 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_116'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_116 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_117'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_117 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_118'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_118 # type: ignore # mutmut generated
mutants_xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut['xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_119'] = VanillaWhatIfSimulationAdapter.xǁVanillaWhatIfSimulationAdapterǁget_probe_audit_data__mutmut_119 # type: ignore # mutmut generated
