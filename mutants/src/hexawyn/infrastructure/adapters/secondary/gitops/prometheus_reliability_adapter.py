from __future__ import annotations

from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    IncidentRawData,
    ServiceReliabilityRawData,
    WeeklyReliabilityReportPort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPrometheusReliabilityAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut: MutantDict = {}  # type: ignore


class PrometheusReliabilityAdapter(WeeklyReliabilityReportPort):
    @_mutmut_mutated(mutants_xǁPrometheusReliabilityAdapterǁ__init____mutmut)
    def __init__(self, metrics_query_port: MetricsQueryPort) -> None:
        self._metrics = metrics_query_port
    def xǁPrometheusReliabilityAdapterǁ__init____mutmut_orig(self, metrics_query_port: MetricsQueryPort) -> None:
        self._metrics = metrics_query_port
    def xǁPrometheusReliabilityAdapterǁ__init____mutmut_1(self, metrics_query_port: MetricsQueryPort) -> None:
        self._metrics = None

    @_mutmut_mutated(mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut)
    def fetch_service_reliability(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_orig(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_1(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = None
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_2(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 / 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_3(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 / 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_4(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days / 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_5(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 25 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_6(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 61 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_7(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 61
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_8(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = None
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_9(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(None)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_10(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = None
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_11(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(None, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_12(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=None)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_13(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_14(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, )
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_15(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=16.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_16(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = None
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_17(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = None
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_18(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get(None, {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_19(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", None)
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_20(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get({})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_21(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", )
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_22(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("XXmetricXX", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_23(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("METRIC", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_24(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = None
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_25(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(None)
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_26(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get(None, ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_27(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", None))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_28(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get(""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_29(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_30(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("XXserviceXX", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_31(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("SERVICE", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_32(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", "XXXX"))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_33(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_34(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = None

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_35(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(None)

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_36(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get(None, ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_37(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", None))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_38(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get(""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_39(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_40(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("XXexported_serviceXX", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_41(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("EXPORTED_SERVICE", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_42(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", "XXXX"))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_43(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = None
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_44(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(None)
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_45(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get(None, 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_46(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", None))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_47(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get(1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_48(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", ))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_49(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("XXvalueXX", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_50(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("VALUE", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_51(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 2.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_52(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = None
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_53(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(None, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_54(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, None)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_55(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_56(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, )
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_57(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate / 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_58(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 101.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_59(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 3)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_60(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = None

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_61(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(None, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_62(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, None)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_63(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_64(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, )

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_65(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 + uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_66(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(101.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_67(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 3)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_68(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                None
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_69(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=None,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_70(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=None,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_71(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=None,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_72(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=None,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_73(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=None,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_74(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=None,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_75(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=None,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_76(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=None,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_77(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_78(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_79(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_80(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_81(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_82(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_83(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_84(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_85(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=1.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_86(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=100.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_87(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=1,
                    data_gap_minutes=0,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_88(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=1,
                    created_mid_week=False,
                )
            )
        return result

    def xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_89(self, window_days: int) -> list[ServiceReliabilityRawData]:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_uptime_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)
        except Exception:
            return []

        result: list[ServiceReliabilityRawData] = []
        for sample in samples:
            metric = sample.get("metric", {})
            service_name = str(metric.get("service", ""))
            if not service_name:
                service_name = str(metric.get("exported_service", ""))

            success_rate = float(sample.get("value", 1.0))
            uptime_pct = round(success_rate * 100.0, 2)
            error_rate = round(100.0 - uptime_pct, 2)

            result.append(
                ServiceReliabilityRawData(
                    service_name=service_name,
                    uptime_pct=uptime_pct,
                    error_rate=error_rate,
                    p99_latency_ms=0.0,
                    slo_target=99.9,
                    downtime_minutes=0,
                    data_gap_minutes=0,
                    created_mid_week=True,
                )
            )
        return result

    @_mutmut_mutated(mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut)
    def fetch_incidents(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_orig(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_1(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = None
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_2(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = None

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_3(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=None)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_4(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=51)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_5(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = None
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_6(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" or event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_7(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type != "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_8(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "XXWarningXX" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_9(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_10(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "WARNING" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_11(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        None
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_12(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=None,
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_13(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=None,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_14(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=None,
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_15(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=None,
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_16(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=None,
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_17(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_18(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_19(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_20(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_21(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_22(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason and "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_23(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "XXXX",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_24(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count and 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_25(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 2,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_26(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace and "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_27(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "XXXX",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_28(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(None) if event.first_timestamp else ""
                            ),
                        )
                    )
            return result
        except Exception:
            return []

    def xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_29(self, window_days: int) -> list[IncidentRawData]:
        try:
            from kubernetes import client, config

            config.load_kube_config()
            v1 = client.CoreV1Api()
            events = v1.list_event_for_all_namespaces(limit=50)

            result: list[IncidentRawData] = []
            for event in events.items:
                if event.type == "Warning" and event.involved_object:
                    result.append(
                        IncidentRawData(  # type: ignore
                            reason=event.reason or "",
                            count=event.count or 1,
                            resource=(f"{event.involved_object.kind}/{event.involved_object.name}"),
                            namespace=event.involved_object.namespace or "",
                            first_seen=(
                                str(event.first_timestamp) if event.first_timestamp else "XXXX"
                            ),
                        )
                    )
            return result
        except Exception:
            return []

mutants_xǁPrometheusReliabilityAdapterǁ__init____mutmut['_mutmut_orig'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁ__init____mutmut['xǁPrometheusReliabilityAdapterǁ__init____mutmut_1'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['_mutmut_orig'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_1'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_2'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_3'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_4'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_5'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_6'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_7'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_8'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_9'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_10'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_11'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_12'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_13'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_14'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_15'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_16'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_17'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_18'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_19'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_20'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_21'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_22'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_23'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_24'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_25'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_26'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_27'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_28'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_29'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_30'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_31'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_32'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_33'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_34'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_35'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_36'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_37'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_38'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_39'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_40'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_41'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_42'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_43'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_44'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_45'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_46'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_47'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_48'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_49'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_49 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_50'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_50 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_51'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_51 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_52'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_52 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_53'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_53 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_54'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_54 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_55'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_55 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_56'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_56 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_57'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_57 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_58'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_58 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_59'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_59 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_60'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_60 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_61'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_61 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_62'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_62 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_63'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_63 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_64'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_64 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_65'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_65 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_66'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_66 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_67'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_67 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_68'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_68 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_69'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_69 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_70'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_70 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_71'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_71 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_72'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_72 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_73'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_73 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_74'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_74 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_75'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_75 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_76'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_76 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_77'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_77 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_78'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_78 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_79'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_79 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_80'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_80 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_81'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_81 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_82'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_82 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_83'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_83 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_84'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_84 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_85'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_85 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_86'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_86 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_87'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_87 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_88'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_88 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut['xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_89'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_service_reliability__mutmut_89 # type: ignore # mutmut generated

mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['_mutmut_orig'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_1'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_2'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_3'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_4'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_5'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_6'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_7'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_8'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_9'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_10'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_11'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_12'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_13'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_14'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_15'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_16'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_17'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_18'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_19'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_20'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_21'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_22'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_23'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_24'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_25'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_26'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_27'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_28'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut['xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_29'] = PrometheusReliabilityAdapter.xǁPrometheusReliabilityAdapterǁfetch_incidents__mutmut_29 # type: ignore # mutmut generated


def _build_uptime_query(window_seconds: int) -> str:
    return (
        f'avg(rate(http_requests_total{{code!~"5.."}}[{window_seconds}s]))'
        f" / "
        f"avg(rate(http_requests_total[{window_seconds}s]))"
    )
