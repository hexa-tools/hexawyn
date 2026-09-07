from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from hexawyn.application.ports.driven.cost_forecast_port import (
    CostForecastPort,
    DailyCostData,
)
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesAppsApi,
)
from hexawyn.infrastructure.adapters.secondary.vanilla.helpers.resource_parsers import (
    _build_daily_cost_entries,
    _compute_namespace_daily_costs,
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
mutants_xǁVanillaCostForecastAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut: MutantDict = {}  # type: ignore


class VanillaCostForecastAdapter(CostForecastPort):
    @_mutmut_mutated(mutants_xǁVanillaCostForecastAdapterǁ__init____mutmut)
    def __init__(self, api: KubernetesAppsApi, prometheus_url: str = "") -> None:
        self._api = api
        self._prometheus_url = prometheus_url
    def xǁVanillaCostForecastAdapterǁ__init____mutmut_orig(self, api: KubernetesAppsApi, prometheus_url: str = "") -> None:
        self._api = api
        self._prometheus_url = prometheus_url
    def xǁVanillaCostForecastAdapterǁ__init____mutmut_1(self, api: KubernetesAppsApi, prometheus_url: str = "XXXX") -> None:
        self._api = api
        self._prometheus_url = prometheus_url
    def xǁVanillaCostForecastAdapterǁ__init____mutmut_2(self, api: KubernetesAppsApi, prometheus_url: str = "") -> None:
        self._api = None
        self._prometheus_url = prometheus_url
    def xǁVanillaCostForecastAdapterǁ__init____mutmut_3(self, api: KubernetesAppsApi, prometheus_url: str = "") -> None:
        self._api = api
        self._prometheus_url = None

    @_mutmut_mutated(mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut)
    def get_daily_costs(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_orig(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_1(self, days: int) -> list[DailyCostData]:
        try:
            raw = None
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_2(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=None)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_3(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                None
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_4(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = None
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_5(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(None)
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_6(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(None))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_7(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = None
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_8(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(None)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_9(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = None
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_10(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(None)
        return _build_daily_cost_entries(ns_daily_costs, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_11(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(None, total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_12(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, None, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_13(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, None)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_14(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(total_daily, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_15(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, days)

    def xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_16(self, days: int) -> list[DailyCostData]:
        try:
            raw = self._api.list_deployment_for_all_namespaces(timeout_seconds=_K8S_TIMEOUT)
        except Exception as exc:
            raise ClusterUnreachableError(
                f"Cannot list deployments for cost forecast: {exc}"
            ) from exc
        deployments = list(_items_from(raw))
        ns_daily_costs = _compute_namespace_daily_costs(deployments)
        total_daily = sum(ns_daily_costs.values())
        return _build_daily_cost_entries(ns_daily_costs, total_daily, )

mutants_xǁVanillaCostForecastAdapterǁ__init____mutmut['_mutmut_orig'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁ__init____mutmut['xǁVanillaCostForecastAdapterǁ__init____mutmut_1'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁ__init____mutmut['xǁVanillaCostForecastAdapterǁ__init____mutmut_2'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁ__init____mutmut['xǁVanillaCostForecastAdapterǁ__init____mutmut_3'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['_mutmut_orig'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_1'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_2'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_3'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_4'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_5'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_6'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_7'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_8'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_9'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_10'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_11'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_12'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_13'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_14'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_15'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut['xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_16'] = VanillaCostForecastAdapter.xǁVanillaCostForecastAdapterǁget_daily_costs__mutmut_16 # type: ignore # mutmut generated
