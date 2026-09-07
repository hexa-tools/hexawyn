from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.response import (
    ClusterCapacityCeilingForecastResponse,
    ResourceForecastDict,
)
from hexawyn.domain.errors import InsufficientDataError
from hexawyn.domain.models.cluster_capacity_forecast import (
    ClusterCapacityForecastReport,
    ClusterCapacityForecastRequest,
    ClusterCapacityRawData,
    ResourceForecast,
)
from hexawyn.domain.services.cluster_capacity_forecast.forecast_builder import (
    build_cluster_capacity_forecast,
)

_QUERY_TIMEOUT_SECONDS = 15.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut: MutantDict = {}  # type: ignore


class ClusterCapacityCeilingForecastUseCase:
    @_mutmut_mutated(mutants_xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut)
    def __init__(
        self, metrics_port: ClusterResourceMetricsPort, capacity_port: CapacityForecastPort
    ) -> None:
        self._metrics_port = metrics_port
        self._capacity_port = capacity_port
    def xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut_orig(
        self, metrics_port: ClusterResourceMetricsPort, capacity_port: CapacityForecastPort
    ) -> None:
        self._metrics_port = metrics_port
        self._capacity_port = capacity_port
    def xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut_1(
        self, metrics_port: ClusterResourceMetricsPort, capacity_port: CapacityForecastPort
    ) -> None:
        self._metrics_port = None
        self._capacity_port = capacity_port
    def xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut_2(
        self, metrics_port: ClusterResourceMetricsPort, capacity_port: CapacityForecastPort
    ) -> None:
        self._metrics_port = metrics_port
        self._capacity_port = None

    @_mutmut_mutated(mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut)
    def forecast(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_orig(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_1(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = None
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_2(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(None)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_3(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = None

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_4(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end + timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_5(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=None)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_6(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = None
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_7(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            None, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_8(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, None, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_9(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=None
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_10(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_11(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_12(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_13(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = None
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_14(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["XXcpu_daily_coresXX"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_15(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["CPU_DAILY_CORES"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_16(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = None
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_17(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["XXmemory_daily_gbXX"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_18(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["MEMORY_DAILY_GB"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_19(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values or not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_20(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_21(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_22(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                None
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_23(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "XXNo Prometheus data available to compute a capacity forecast.XX"
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_24(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "no prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_25(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "NO PROMETHEUS DATA AVAILABLE TO COMPUTE A CAPACITY FORECAST."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_26(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = None
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_27(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = None

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_28(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=None,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_29(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=None,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_30(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=None,
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_31(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=None,
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_32(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=None,
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_33(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_34(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_35(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_36(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_37(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_38(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["XXtotal_allocatable_cpu_coresXX"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_39(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["TOTAL_ALLOCATABLE_CPU_CORES"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_40(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["XXtotal_allocatable_memory_gbXX"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_41(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["TOTAL_ALLOCATABLE_MEMORY_GB"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_42(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["XXautoscaler_enabledXX"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_43(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["AUTOSCALER_ENABLED"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_44(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = None
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_45(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=None,
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_46(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=None,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_47(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=None,
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_48(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_49(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_50(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_51(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=None),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(report)

    def xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_52(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        end = datetime.now(UTC)
        start = end - timedelta(days=command.window_days)

        daily_usage = self._metrics_port.get_daily_usage(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )
        cpu_values = daily_usage["cpu_daily_cores"]
        memory_values = daily_usage["memory_daily_gb"]
        if not cpu_values and not memory_values:
            raise InsufficientDataError(
                "No Prometheus data available to compute a capacity forecast."
            )

        capacity_info = self._capacity_port.get_cluster_capacity_info()
        raw_data = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu_values,
            memory_daily_usage_gb=memory_values,
            total_allocatable_cpu_cores=capacity_info["total_allocatable_cpu_cores"],
            total_allocatable_memory_gb=capacity_info["total_allocatable_memory_gb"],
            autoscaler_enabled=capacity_info["autoscaler_enabled"],
        )

        report = build_cluster_capacity_forecast(
            request=ClusterCapacityForecastRequest(window_days=command.window_days),
            raw_data=raw_data,
            observed_at=end.date(),
        )
        return _to_response(None)

mutants_xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut['_mutmut_orig'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut['xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut_1'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut['xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut_2'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['_mutmut_orig'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_1'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_2'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_3'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_4'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_4 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_5'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_5 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_6'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_6 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_7'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_7 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_8'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_8 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_9'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_9 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_10'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_10 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_11'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_11 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_12'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_12 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_13'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_13 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_14'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_14 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_15'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_15 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_16'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_16 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_17'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_17 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_18'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_18 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_19'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_19 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_20'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_20 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_21'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_21 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_22'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_22 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_23'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_23 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_24'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_24 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_25'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_25 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_26'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_26 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_27'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_27 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_28'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_28 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_29'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_29 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_30'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_30 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_31'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_31 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_32'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_32 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_33'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_33 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_34'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_34 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_35'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_35 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_36'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_36 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_37'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_37 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_38'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_38 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_39'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_39 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_40'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_40 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_41'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_41 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_42'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_42 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_43'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_43 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_44'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_44 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_45'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_45 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_46'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_46 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_47'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_47 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_48'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_48 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_49'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_49 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_50'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_50 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_51'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_51 # type: ignore # mutmut generated
mutants_xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut['xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_52'] = ClusterCapacityCeilingForecastUseCase.xǁClusterCapacityCeilingForecastUseCaseǁforecast__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_orig(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_1(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=None,
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_2(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=None,
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_3(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=None,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_4(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=None,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_5(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=None,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_6(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=None,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_7(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=None,
    )


def x__to_response__mutmut_8(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_9(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_10(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_11(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_12(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_13(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_14(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        )


def x__to_response__mutmut_15(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(None),
        memory=_to_resource_dict(report.memory),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )


def x__to_response__mutmut_16(
    report: ClusterCapacityForecastReport,
) -> ClusterCapacityCeilingForecastResponse:
    return ClusterCapacityCeilingForecastResponse(
        cpu=_to_resource_dict(report.cpu),
        memory=_to_resource_dict(None),
        critical_resource=report.critical_resource,
        autoscaler_enabled=report.autoscaler_enabled,
        recommendation=report.recommendation,
        confidence=report.confidence,
        window_days_used=report.window_days_used,
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_15'] = x__to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_16'] = x__to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_resource_dict__mutmut)
def _to_resource_dict(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_orig(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_1(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=None,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_2(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=None,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_3(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=None,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_4(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=None,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_5(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=None,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_6(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=None,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_7(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=None,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_8(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=None,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_9(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=None,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_10(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=None,
    )


def x__to_resource_dict__mutmut_11(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_12(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_13(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_14(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_15(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_16(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_17(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_18(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        spike_caveat=forecast.spike_caveat,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_19(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        capped_horizon=forecast.capped_horizon,
    )


def x__to_resource_dict__mutmut_20(forecast: ResourceForecast) -> ResourceForecastDict:
    return ResourceForecastDict(
        resource_type=forecast.resource_type,
        current_value=forecast.current_value,
        ceiling=forecast.ceiling,
        current_utilization_percent=forecast.current_utilization_percent,
        growth_rate_per_day=forecast.growth_rate_per_day,
        days_to_saturation=forecast.days_to_saturation,
        saturation_date=forecast.saturation_date,
        capacity_jump_detected=forecast.capacity_jump_detected,
        spike_caveat=forecast.spike_caveat,
        )

mutants_x__to_resource_dict__mutmut['_mutmut_orig'] = x__to_resource_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_1'] = x__to_resource_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_2'] = x__to_resource_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_3'] = x__to_resource_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_4'] = x__to_resource_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_5'] = x__to_resource_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_6'] = x__to_resource_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_7'] = x__to_resource_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_8'] = x__to_resource_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_9'] = x__to_resource_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_10'] = x__to_resource_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_11'] = x__to_resource_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_12'] = x__to_resource_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_13'] = x__to_resource_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_14'] = x__to_resource_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_15'] = x__to_resource_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_16'] = x__to_resource_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_17'] = x__to_resource_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_18'] = x__to_resource_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_19'] = x__to_resource_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_20'] = x__to_resource_dict__mutmut_20 # type: ignore # mutmut generated
