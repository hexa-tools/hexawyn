"""RED → GREEN — Layer 6: MCP tool + VanillaAdapter CostForecastPort."""

import asyncio
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort, DailyCostData
from hexawyn.domain.errors import ClusterUnreachableError


def _fake_apps_api(deployments: list) -> MagicMock:
    api = MagicMock()
    dep_list = MagicMock()
    dep_list.items = deployments
    api.list_deployment_for_all_namespaces.return_value = dep_list
    sts_list = MagicMock()
    sts_list.items = []
    api.list_stateful_set_for_all_namespaces.return_value = sts_list
    return api


def _fake_deployment(
    name: str, namespace: str, cpu: str = "2000m", memory: str = "4Gi"
) -> MagicMock:
    dep = MagicMock()
    dep.metadata.name = name
    dep.metadata.namespace = namespace
    dep.spec.replicas = 1
    container = MagicMock()
    container.resources.requests = {"cpu": cpu, "memory": memory}
    dep.spec.template.spec.containers = [container]
    return dep


class TestVanillaAdapterCostForecastPort:
    def test_implements_cost_forecast_port(self) -> None:
        assert isinstance(VanillaAdapter("test"), CostForecastPort)

    def test_get_daily_costs_returns_list(self) -> None:
        dep = _fake_deployment("svc", "ns")
        adapter = VanillaAdapter("test", apps_api=_fake_apps_api([dep]))

        result = adapter.get_daily_costs(days=7)

        assert isinstance(result, list)

    def test_returns_n_data_points(self) -> None:
        dep = _fake_deployment("svc", "ns")
        adapter = VanillaAdapter("test", apps_api=_fake_apps_api([dep]))

        result = adapter.get_daily_costs(days=7)

        assert len(result) == 7

    def test_data_points_have_correct_keys(self) -> None:
        dep = _fake_deployment("svc", "ns")
        adapter = VanillaAdapter("test", apps_api=_fake_apps_api([dep]))

        result = adapter.get_daily_costs(days=1)

        assert "date" in result[0]
        assert "total_usd" in result[0]
        assert "namespace_costs" in result[0]

    def test_daily_cost_positive_for_workload_with_requests(self) -> None:
        # 2 cores × $21.6/core/month / 30 days = $1.44/day
        dep = _fake_deployment("svc", "ns", cpu="2000m", memory="0")
        adapter = VanillaAdapter("test", apps_api=_fake_apps_api([dep]))

        result = adapter.get_daily_costs(days=1)

        assert result[0]["total_usd"] > 0.0

    def test_namespace_costs_listed(self) -> None:
        dep = _fake_deployment("svc", "production", cpu="1000m", memory="2Gi")
        adapter = VanillaAdapter("test", apps_api=_fake_apps_api([dep]))

        result = adapter.get_daily_costs(days=1)

        ns_names = [ns["name"] for ns in result[0]["namespace_costs"]]
        assert "production" in ns_names

    def test_dates_are_consecutive_ending_today(self) -> None:
        from datetime import date, timedelta

        dep = _fake_deployment("svc", "ns")
        adapter = VanillaAdapter("test", apps_api=_fake_apps_api([dep]))

        result = adapter.get_daily_costs(days=3)

        today = date.today()
        assert result[-1]["date"] == today.strftime("%Y-%m-%d")
        assert result[-2]["date"] == (today - timedelta(days=1)).strftime("%Y-%m-%d")
        assert result[0]["date"] == (today - timedelta(days=2)).strftime("%Y-%m-%d")

    def test_cluster_unreachable_raises(self) -> None:
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.side_effect = Exception("forbidden")
        adapter = VanillaAdapter("test", apps_api=apps_api)

        with pytest.raises(ClusterUnreachableError):
            adapter.get_daily_costs(days=7)


class TestMCPForecastCostTool:
    def test_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        assert "forecast_cost" in {t.name for t in tools}

    def test_returns_forecast_fields(self) -> None:
        mock_port = MagicMock(spec=CostForecastPort)
        mock_port.get_daily_costs.return_value = [
            DailyCostData(
                date="2026-06-22",
                total_usd=50.0,
                namespace_costs=[{"name": "prod", "cost_usd": 50.0}],
            )
        ]

        with patch("hexawyn.mcp.server.build_cost_forecast_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.forecast_cost import forecast_cost

            result = forecast_cost()

        assert result["error"] is None
        assert result["projected_total_usd"] > 0
        assert result["forecast_confidence"] in ("low", "medium")
        assert result["data_source"] == "estimated"

    def test_cluster_error_captured_in_error_field(self) -> None:
        mock_port = MagicMock(spec=CostForecastPort)
        mock_port.get_daily_costs.side_effect = ClusterUnreachableError("down")

        with patch("hexawyn.mcp.server.build_cost_forecast_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.forecast_cost import forecast_cost

            result = forecast_cost()

        assert result["error"] is not None
        assert result["projected_total_usd"] == 0.0
