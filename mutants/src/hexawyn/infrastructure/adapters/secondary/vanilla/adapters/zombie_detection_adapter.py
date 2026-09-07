from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from hexawyn.application.ports.driven.zombie_detection_port import (
    ZombieDetectionPort,
    ZombiePodData,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCoreApi,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.resource_parsers import (
    _compute_pod_resources,
)

_K8S_TIMEOUT = 10


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
mutants_xǁVanillaZombieDetectionAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut: MutantDict = {}  # type: ignore


class VanillaZombieDetectionAdapter(ZombieDetectionPort):
    @_mutmut_mutated(mutants_xǁVanillaZombieDetectionAdapterǁ__init____mutmut)
    def __init__(
        self,
        api: KubernetesCoreApi,
        prometheus_url: str = "",
        pod_cache: list[object] | None = None,
    ) -> None:
        self._api = api
        self._prometheus_url = prometheus_url
        self._pod_cache = pod_cache or []
    def xǁVanillaZombieDetectionAdapterǁ__init____mutmut_orig(
        self,
        api: KubernetesCoreApi,
        prometheus_url: str = "",
        pod_cache: list[object] | None = None,
    ) -> None:
        self._api = api
        self._prometheus_url = prometheus_url
        self._pod_cache = pod_cache or []
    def xǁVanillaZombieDetectionAdapterǁ__init____mutmut_1(
        self,
        api: KubernetesCoreApi,
        prometheus_url: str = "XXXX",
        pod_cache: list[object] | None = None,
    ) -> None:
        self._api = api
        self._prometheus_url = prometheus_url
        self._pod_cache = pod_cache or []
    def xǁVanillaZombieDetectionAdapterǁ__init____mutmut_2(
        self,
        api: KubernetesCoreApi,
        prometheus_url: str = "",
        pod_cache: list[object] | None = None,
    ) -> None:
        self._api = None
        self._prometheus_url = prometheus_url
        self._pod_cache = pod_cache or []
    def xǁVanillaZombieDetectionAdapterǁ__init____mutmut_3(
        self,
        api: KubernetesCoreApi,
        prometheus_url: str = "",
        pod_cache: list[object] | None = None,
    ) -> None:
        self._api = api
        self._prometheus_url = None
        self._pod_cache = pod_cache or []
    def xǁVanillaZombieDetectionAdapterǁ__init____mutmut_4(
        self,
        api: KubernetesCoreApi,
        prometheus_url: str = "",
        pod_cache: list[object] | None = None,
    ) -> None:
        self._api = api
        self._prometheus_url = prometheus_url
        self._pod_cache = None
    def xǁVanillaZombieDetectionAdapterǁ__init____mutmut_5(
        self,
        api: KubernetesCoreApi,
        prometheus_url: str = "",
        pod_cache: list[object] | None = None,
    ) -> None:
        self._api = api
        self._prometheus_url = prometheus_url
        self._pod_cache = pod_cache and []

    @_mutmut_mutated(mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut)
    def get_zombie_workloads(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_orig(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_1(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = None
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_2(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=None)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_3(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(None) from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_4(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = None
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_5(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(None)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_6(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = None
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_7(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = None
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_8(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(None, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_9(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, None, None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_10(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr("metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_11(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_12(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", )
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_13(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "XXmetadataXX", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_14(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "METADATA", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_15(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = None
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_16(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(None)
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_17(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(None, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_18(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, None, ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_19(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", None))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_20(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr("name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_21(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_22(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_23(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "XXnameXX", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_24(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "NAME", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_25(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", "XXXX"))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_26(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = None
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_27(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(None)
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_28(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(None, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_29(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, None, ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_30(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", None))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_31(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr("namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_32(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_33(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_34(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "XXnamespaceXX", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_35(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "NAMESPACE", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_36(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", "XXXX"))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_37(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = None
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_38(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(None, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_39(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, None, None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_40(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr("status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_41(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_42(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", )
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_43(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "XXstatusXX", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_44(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "STATUS", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_45(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = None
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_46(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(None) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_47(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(None, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_48(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, None, "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_49(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", None)) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_50(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr("phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_51(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_52(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", )) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_53(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "XXphaseXX", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_54(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "PHASE", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_55(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "XXXX")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_56(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else "XXXX"
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_57(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = None
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_58(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase != "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_59(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "XXTerminatingXX"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_60(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_61(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "TERMINATING"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_62(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_63(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(None, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_64(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, None, None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_65(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr("owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_66(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_67(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", ) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_68(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "XXowner_referencesXX", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_69(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "OWNER_REFERENCES", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_70(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = None
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_71(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = True
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_72(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) or hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_73(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(None, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_74(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, None):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_75(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr("kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_76(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, ):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_77(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "XXkindXX"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_78(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "KIND"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_79(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(None, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_80(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, None) == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_81(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr("kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_82(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, ) == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_83(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "XXkindXX") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_84(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "KIND") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_85(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") != "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_86(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "XXCronJobXX":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_87(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "cronjob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_88(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CRONJOB":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_89(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = None
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_90(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = False
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_91(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            return
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_92(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = None
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_93(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(None, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_94(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, None, None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_95(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr("spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_96(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_97(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", )
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_98(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "XXspecXX", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_99(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "SPEC", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_100(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = None
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_101(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(None, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_102(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, None, []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_103(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", None) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_104(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr("containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_105(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_106(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", ) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_107(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "XXcontainersXX", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_108(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "CONTAINERS", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_109(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = None
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_110(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) >= 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_111(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 2
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_112(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = None
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_113(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(None)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_114(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                None
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_115(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=None,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_116(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=None,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_117(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=None,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_118(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=None,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_119(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=None,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_120(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=None,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_121(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=None,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_122(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=None,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_123(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=None,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_124(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=None,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_125(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=None,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_126(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=None,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_127(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_128(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_129(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_130(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_131(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_132(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_133(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_134(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_135(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_136(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_137(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_138(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_139(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=1.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_140(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=1,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_141(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=True,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_142(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=1.0,
                    seven_day_traffic_rps=0.0,
                )
            )
        return result

    def xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_143(self, window_hours: int) -> list[ZombiePodData]:
        try:
            raw = self._api.list_pod_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot list pods for zombie detection: {exc}") from exc
        pods_iter = _items_from(raw)
        result: list[ZombiePodData] = []
        for pod in pods_iter:
            meta = getattr(pod, "metadata", None)
            pod_name = str(getattr(meta, "name", ""))
            namespace = str(getattr(meta, "namespace", ""))
            status = getattr(pod, "status", None)
            pod_phase = str(getattr(status, "phase", "")) if status else ""
            is_terminating = pod_phase == "Terminating"
            owner_refs = getattr(meta, "owner_references", None) if meta else None
            is_cronjob = False
            if isinstance(owner_refs, list):
                for ref in owner_refs:
                    if isinstance(ref, object) and hasattr(ref, "kind"):
                        if getattr(ref, "kind") == "CronJob":
                            is_cronjob = True
                            break
            containers = getattr(pod, "spec", None)
            containers_list = getattr(containers, "containers", []) if containers else []
            has_sidecar = len(containers_list) > 1
            cpu_cores, memory_gb = _compute_pod_resources(containers_list)
            result.append(
                ZombiePodData(
                    pod_name=pod_name,
                    namespace=namespace,
                    traffic_rps=0.0,
                    cpu_cores=cpu_cores,
                    memory_gb=memory_gb,
                    age_days=0,
                    has_service=False,
                    is_cronjob=is_cronjob,
                    is_terminating=is_terminating,
                    has_sidecar=has_sidecar,
                    sidecar_traffic_rps=0.0,
                    seven_day_traffic_rps=1.0,
                )
            )
        return result

mutants_xǁVanillaZombieDetectionAdapterǁ__init____mutmut['_mutmut_orig'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁ__init____mutmut['xǁVanillaZombieDetectionAdapterǁ__init____mutmut_1'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁ__init____mutmut['xǁVanillaZombieDetectionAdapterǁ__init____mutmut_2'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁ__init____mutmut['xǁVanillaZombieDetectionAdapterǁ__init____mutmut_3'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁ__init____mutmut['xǁVanillaZombieDetectionAdapterǁ__init____mutmut_4'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁ__init____mutmut['xǁVanillaZombieDetectionAdapterǁ__init____mutmut_5'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated

mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['_mutmut_orig'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_1'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_2'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_3'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_4'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_5'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_6'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_7'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_8'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_9'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_10'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_11'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_12'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_13'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_14'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_15'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_16'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_16 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_17'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_17 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_18'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_18 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_19'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_19 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_20'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_20 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_21'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_21 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_22'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_22 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_23'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_23 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_24'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_24 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_25'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_25 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_26'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_26 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_27'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_27 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_28'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_28 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_29'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_29 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_30'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_30 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_31'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_31 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_32'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_32 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_33'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_33 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_34'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_34 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_35'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_35 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_36'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_36 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_37'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_37 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_38'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_38 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_39'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_39 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_40'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_40 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_41'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_41 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_42'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_42 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_43'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_43 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_44'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_44 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_45'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_45 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_46'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_46 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_47'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_47 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_48'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_48 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_49'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_49 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_50'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_50 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_51'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_51 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_52'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_52 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_53'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_53 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_54'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_54 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_55'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_55 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_56'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_56 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_57'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_57 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_58'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_58 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_59'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_59 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_60'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_60 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_61'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_61 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_62'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_62 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_63'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_63 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_64'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_64 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_65'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_65 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_66'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_66 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_67'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_67 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_68'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_68 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_69'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_69 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_70'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_70 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_71'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_71 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_72'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_72 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_73'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_73 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_74'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_74 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_75'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_75 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_76'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_76 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_77'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_77 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_78'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_78 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_79'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_79 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_80'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_80 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_81'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_81 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_82'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_82 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_83'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_83 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_84'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_84 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_85'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_85 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_86'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_86 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_87'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_87 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_88'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_88 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_89'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_89 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_90'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_90 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_91'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_91 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_92'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_92 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_93'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_93 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_94'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_94 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_95'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_95 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_96'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_96 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_97'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_97 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_98'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_98 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_99'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_99 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_100'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_100 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_101'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_101 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_102'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_102 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_103'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_103 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_104'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_104 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_105'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_105 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_106'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_106 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_107'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_107 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_108'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_108 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_109'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_109 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_110'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_110 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_111'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_111 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_112'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_112 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_113'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_113 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_114'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_114 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_115'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_115 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_116'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_116 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_117'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_117 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_118'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_118 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_119'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_119 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_120'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_120 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_121'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_121 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_122'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_122 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_123'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_123 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_124'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_124 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_125'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_125 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_126'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_126 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_127'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_127 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_128'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_128 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_129'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_129 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_130'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_130 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_131'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_131 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_132'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_132 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_133'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_133 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_134'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_134 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_135'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_135 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_136'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_136 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_137'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_137 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_138'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_138 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_139'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_139 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_140'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_140 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_141'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_141 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_142'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_142 # type: ignore # mutmut generated
mutants_xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut['xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_143'] = VanillaZombieDetectionAdapter.xǁVanillaZombieDetectionAdapterǁget_zombie_workloads__mutmut_143 # type: ignore # mutmut generated
