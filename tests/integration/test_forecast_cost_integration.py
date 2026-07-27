# mypy: ignore-errors
"""Integration tests: ForecastCostUseCase → service → VanillaAdapter.

Uses a real VanillaAdapter wired with fake K8s clients — no cluster needed.
"""

from datetime import date
from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.service.forecast_cost_service import ForecastCostService
from hexawyn.application.use_case.finops.forecast_cost.command import (
    ForecastCostCommand,
)
from hexawyn.application.use_case.finops.forecast_cost.forecast_cost_use_case import (
    ForecastCostUseCase,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _deployment(name: str, namespace: str, cpu: str = "2000m", memory: str = "4Gi") -> MagicMock:
    dep = MagicMock()
    dep.metadata.name = name
    dep.metadata.namespace = namespace
    dep.spec.replicas = 1
    container = MagicMock()
    container.resources.requests = {"cpu": cpu, "memory": memory}
    dep.spec.template.spec.containers = [container]
    return dep


def _fake_apps_api(deployments: list[MagicMock]) -> MagicMock:
    api = MagicMock()
    dep_list = MagicMock()
    dep_list.items = deployments
    api.list_deployment_for_all_namespaces.return_value = dep_list
    sts_list = MagicMock()
    sts_list.items = []
    api.list_stateful_set_for_all_namespaces.return_value = sts_list
    return api


def _build_use_case(deployments: list[MagicMock]) -> ForecastCostUseCase:
    adapter = VanillaAdapter("test-cluster", apps_api=_fake_apps_api(deployments))
    service = ForecastCostService(cost_forecast_port=adapter, cluster_name="test-cluster")
    return ForecastCostUseCase(service=service)


class TestForecastCostIntegration:
    def test_tc1_returns_positive_projected_total(self) -> None:
        use_case = _build_use_case([_deployment("api", "production")])

        response = use_case.execute(ForecastCostCommand())

        assert response.forecast.projected_total_usd > 0.0

    def test_tc2_month_matches_current_month(self) -> None:
        use_case = _build_use_case([_deployment("api", "production")])

        response = use_case.execute(ForecastCostCommand())

        assert response.forecast.month == date.today().strftime("%Y-%m")

    def test_tc3_days_elapsed_matches_today(self) -> None:
        use_case = _build_use_case([_deployment("api", "production")])

        response = use_case.execute(ForecastCostCommand())

        assert response.forecast.days_elapsed == date.today().day

    def test_tc4_confidence_is_low_for_vanilla(self) -> None:
        use_case = _build_use_case([_deployment("api", "production")])

        response = use_case.execute(ForecastCostCommand())

        assert response.forecast.forecast_confidence == "low"
        assert response.forecast.data_source == "estimated"

    def test_tc5_historical_days_used_matches_command(self) -> None:
        use_case = _build_use_case([_deployment("api", "production")])

        response = use_case.execute(ForecastCostCommand(historical_days=7))

        assert response.forecast.historical_days_used == 7  # noqa: PLR2004

    def test_tc6_trend_factor_is_one_for_uniform_estimate(self) -> None:
        # Vanilla adapter returns same rate every day → no acceleration
        use_case = _build_use_case([_deployment("api", "production")])

        response = use_case.execute(ForecastCostCommand(historical_days=7))

        assert response.forecast.trend_factor == pytest.approx(1.0, abs=0.001)

    def test_tc7_top_cost_drivers_contains_namespace(self) -> None:
        use_case = _build_use_case(
            [_deployment("api", "production"), _deployment("worker", "staging")]
        )

        response = use_case.execute(ForecastCostCommand(top_n_drivers=3))

        driver_names = {d.name for d in response.forecast.top_cost_drivers}
        assert "production" in driver_names
        assert "staging" in driver_names

    def test_tc8_cluster_unreachable_raises(self) -> None:
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.side_effect = Exception("timeout")
        adapter = VanillaAdapter("test", apps_api=apps_api)
        service = ForecastCostService(cost_forecast_port=adapter, cluster_name="test")
        use_case = ForecastCostUseCase(service=service)

        with pytest.raises(ClusterUnreachableError):
            use_case.execute(ForecastCostCommand())

    def test_tc9_no_deployments_returns_zero_projected(self) -> None:
        use_case = _build_use_case([])

        response = use_case.execute(ForecastCostCommand())

        assert response.forecast.projected_total_usd == 0.0
