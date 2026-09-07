from __future__ import annotations

import calendar
from datetime import date

from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort
from hexawyn.application.use_case.finops.forecast_cost.command import (
    ForecastCostCommand,
)
from hexawyn.application.use_case.finops.forecast_cost.response import (
    ForecastCostResponse,
)
from hexawyn.domain.services.cost_forecast.cost_forecast_engine import CostForecastEngine


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁForecastCostUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁForecastCostUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ForecastCostUseCase:
    @_mutmut_mutated(mutants_xǁForecastCostUseCaseǁ__init____mutmut)
    def __init__(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_orig(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_1(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "XXdefaultXX",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_2(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "DEFAULT",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_3(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "XXestimatedXX",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_4(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "ESTIMATED",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_5(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "XXlowXX",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_6(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "LOW",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_7(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = None
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_8(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = None
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_9(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = None
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_10(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = None
        self._engine = CostForecastEngine()
    def xǁForecastCostUseCaseǁ__init____mutmut_11(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = None

    @_mutmut_mutated(mutants_xǁForecastCostUseCaseǁexecute__mutmut)
    def execute(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_orig(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_1(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = None
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_2(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(None)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_3(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = None
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_4(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = None
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_5(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = None
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_6(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(None, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_7(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, None)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_8(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_9(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, )[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_10(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[2]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_11(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = None

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_12(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime(None)

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_13(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("XX%Y-%mXX")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_14(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_15(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%M")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_16(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = None
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_17(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=None,
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_18(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=None,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_19(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=None,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_20(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=None,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_21(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=None,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_22(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=None,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_23(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=None,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_24(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=None,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_25(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_26(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_27(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_28(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_29(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_30(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_31(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_32(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_33(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(None) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)  # type: ignore

    def xǁForecastCostUseCaseǁexecute__mutmut_34(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=None)  # type: ignore

mutants_xǁForecastCostUseCaseǁ__init____mutmut['_mutmut_orig'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_1'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_2'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_3'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_4'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_5'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_6'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_7'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_8'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_9'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_10'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁ__init____mutmut['xǁForecastCostUseCaseǁ__init____mutmut_11'] = ForecastCostUseCase.xǁForecastCostUseCaseǁ__init____mutmut_11 # type: ignore # mutmut generated

mutants_xǁForecastCostUseCaseǁexecute__mutmut['_mutmut_orig'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_1'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_2'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_3'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_4'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_5'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_6'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_7'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_8'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_9'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_10'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_11'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_12'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_13'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_14'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_15'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_16'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_17'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_18'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_19'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_20'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_21'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_22'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_23'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_24'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_25'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_26'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_27'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_28'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_29'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_30'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_31'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_32'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_33'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁForecastCostUseCaseǁexecute__mutmut['xǁForecastCostUseCaseǁexecute__mutmut_34'] = ForecastCostUseCase.xǁForecastCostUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
