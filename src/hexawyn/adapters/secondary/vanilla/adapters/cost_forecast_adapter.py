from __future__ import annotations

from collections.abc import Sequence
from typing import cast

from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesAppsApi,
)
from hexawyn.adapters.secondary.vanilla.helpers.resource_parsers import (
    _build_daily_cost_entries,
    _compute_namespace_daily_costs,
)
from hexawyn.application.ports.driven.cost_forecast_port import (
    CostForecastPort,
    DailyCostData,
)
from hexawyn.domain.errors import ClusterUnreachableError

_K8S_TIMEOUT = 10


def _items_from(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def _object_sequence(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


class VanillaCostForecastAdapter(CostForecastPort):
    def __init__(self, api: KubernetesAppsApi, prometheus_url: str = "") -> None:
        self._api = api
        self._prometheus_url = prometheus_url

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
