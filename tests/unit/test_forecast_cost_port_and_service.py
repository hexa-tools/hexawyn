"""RED → GREEN — Layers 3-5: port, driving ports, application service, use case."""

from datetime import date
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort, DailyCostData
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_command import (
    ForecastCostCommand,
)
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_response import (
    ForecastCostResponse,
)
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_service_port import (
    ForecastCostServicePort,
)
from hexawyn.application.service.forecast_cost_service import ForecastCostService
from hexawyn.application.use_case.forecast_cost.forecast_cost_use_case import ForecastCostUseCase
from hexawyn.domain.models.cost_forecast import CostForecast


def _make_forecast() -> CostForecast:
    return CostForecast(
        cluster_name="prod",
        month="2026-06",
        days_elapsed=22,
        days_remaining=8,
        current_spend_usd=1100.0,
        projected_total_usd=1500.0,
        previous_month_usd=None,
        month_over_month_delta=0.0,
        trend_factor=1.0,
        forecast_confidence="low",
        historical_days_used=1,
        data_source="estimated",
    )


def _daily(date_str: str, total: float) -> DailyCostData:
    return DailyCostData(date=date_str, total_usd=total, namespace_costs=[])


class TestCostForecastPort:
    def test_is_abstract(self) -> None:
        import inspect

        assert inspect.isabstract(CostForecastPort)

    def test_concrete_impl_must_implement_get_daily_costs(self) -> None:
        class BadAdapter(CostForecastPort):
            pass

        with pytest.raises(TypeError):
            BadAdapter()  # type: ignore[abstract]

    def test_concrete_impl_accepted(self) -> None:
        class GoodAdapter(CostForecastPort):
            def get_daily_costs(self, days: int) -> list[DailyCostData]:
                return []

        adapter = GoodAdapter()
        assert adapter.get_daily_costs(7) == []


class TestForecastCostCommand:
    def test_default_historical_days_is_7(self) -> None:
        cmd = ForecastCostCommand()
        assert cmd.historical_days == 7

    def test_default_top_n_drivers_is_3(self) -> None:
        cmd = ForecastCostCommand()
        assert cmd.top_n_drivers == 3

    def test_custom_values(self) -> None:
        cmd = ForecastCostCommand(historical_days=30, top_n_drivers=5)
        assert cmd.historical_days == 30
        assert cmd.top_n_drivers == 5

    def test_is_frozen(self) -> None:
        cmd = ForecastCostCommand()
        with pytest.raises(Exception):
            cmd.historical_days = 99  # type: ignore[misc]


class TestForecastCostResponse:
    def test_holds_forecast(self) -> None:
        forecast = _make_forecast()
        response = ForecastCostResponse(forecast=forecast)
        assert response.forecast is forecast


class TestForecastCostService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=CostForecastPort)
        port.get_daily_costs.return_value = [_daily("2026-06-22", 50.0)]
        return port

    def test_calls_port_with_historical_days(self) -> None:
        port = self._mock_port()
        service = ForecastCostService(cost_forecast_port=port, cluster_name="prod")

        service.forecast_cost(ForecastCostCommand(historical_days=7))

        port.get_daily_costs.assert_called_once_with(7)

    def test_returns_forecast_cost_response(self) -> None:
        port = self._mock_port()
        service = ForecastCostService(cost_forecast_port=port, cluster_name="prod")

        result = service.forecast_cost(ForecastCostCommand())

        assert isinstance(result, ForecastCostResponse)
        assert isinstance(result.forecast, CostForecast)

    def test_forecast_uses_current_month_context(self) -> None:
        port = self._mock_port()
        service = ForecastCostService(cost_forecast_port=port, cluster_name="prod")
        today = date.today()

        result = service.forecast_cost(ForecastCostCommand())

        assert result.forecast.month == today.strftime("%Y-%m")
        assert result.forecast.days_elapsed == today.day

    def test_forecast_cluster_name_from_service(self) -> None:
        port = self._mock_port()
        service = ForecastCostService(cost_forecast_port=port, cluster_name="my-cluster")

        result = service.forecast_cost(ForecastCostCommand())

        assert result.forecast.cluster_name == "my-cluster"

    def test_data_source_is_estimated_for_vanilla(self) -> None:
        port = self._mock_port()
        service = ForecastCostService(cost_forecast_port=port, cluster_name="prod")

        result = service.forecast_cost(ForecastCostCommand())

        assert result.forecast.data_source == "estimated"
        assert result.forecast.forecast_confidence == "low"


class TestForecastCostUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=ForecastCostServicePort)
        forecast = _make_forecast()
        service.forecast_cost.return_value = ForecastCostResponse(forecast=forecast)
        use_case = ForecastCostUseCase(service=service)

        result = use_case.execute(ForecastCostCommand())

        service.forecast_cost.assert_called_once()
        assert result.forecast is forecast

    def test_passes_command_through(self) -> None:
        service = MagicMock(spec=ForecastCostServicePort)
        service.forecast_cost.return_value = ForecastCostResponse(forecast=_make_forecast())
        use_case = ForecastCostUseCase(service=service)
        cmd = ForecastCostCommand(historical_days=30, top_n_drivers=5)

        use_case.execute(cmd)

        service.forecast_cost.assert_called_once_with(cmd)
