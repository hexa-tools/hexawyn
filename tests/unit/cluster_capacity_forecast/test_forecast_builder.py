"""Unit tests for build_cluster_capacity_forecast — pure orchestration of
growth-rate + saturation-prediction per resource type into one report."""

from __future__ import annotations

from datetime import date

from hexawyn.domain.models.cluster_capacity_forecast import (
    ClusterCapacityForecastRequest,
    ClusterCapacityRawData,
)
from hexawyn.domain.services.cluster_capacity_forecast.forecast_builder import (
    build_cluster_capacity_forecast,
)

_OBSERVED_AT = date(2026, 6, 17)


def _cpu_series_matching_ticket() -> list[float]:
    return [67.2 - 1.92 * (13 - i) for i in range(14)]


def _memory_series_matching_ticket() -> list[float]:
    return [307.2 - 1.92 * (13 - i) for i in range(14)]


class TestCriticalResourceSelection:
    def test_cpu_saturates_sooner_is_critical(self) -> None:
        """TC3: CPU (15d) sooner than Memory (40d) → CPU is critical."""
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=_cpu_series_matching_ticket(),
            memory_daily_usage_gb=_memory_series_matching_ticket(),
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.days_to_saturation == 15
        assert report.memory.days_to_saturation == 40
        assert report.critical_resource == "CPU"

    def test_memory_saturates_sooner_is_critical(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=_memory_series_matching_ticket(),
            memory_daily_usage_gb=_cpu_series_matching_ticket(),
            total_allocatable_cpu_cores=384.0,
            total_allocatable_memory_gb=96.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.critical_resource == "Memory"

    def test_only_memory_saturating_is_critical(self) -> None:
        flat = [50.0] * 14
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=flat,
            memory_daily_usage_gb=_memory_series_matching_ticket(),
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.days_to_saturation is None
        assert report.critical_resource == "Memory"

    def test_only_cpu_saturating_is_critical(self) -> None:
        flat = [50.0] * 14
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=_cpu_series_matching_ticket(),
            memory_daily_usage_gb=flat,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.memory.days_to_saturation is None
        assert report.critical_resource == "CPU"


class TestNoRiskFraming:
    def test_declining_usage_is_no_risk(self) -> None:
        """TC4: cluster usage declining → no saturation risk."""
        declining = [80.0 - 1.0 * i for i in range(14)]
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=declining,
            memory_daily_usage_gb=declining,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.days_to_saturation is None
        assert report.critical_resource == "None"

    def test_flat_usage_is_stable_no_prediction(self) -> None:
        """TC5: usage flat for 14 days → no saturation predicted."""
        flat = [50.0] * 14
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=flat,
            memory_daily_usage_gb=flat,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.days_to_saturation is None
        assert report.critical_resource == "None"


class TestConfidenceTiers:
    def test_full_window_is_high_confidence(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=[50.0] * 14,
            memory_daily_usage_gb=[50.0] * 14,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.confidence == "high"
        assert report.window_days_used == 14

    def test_medium_window_is_medium_confidence(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=[50.0] * 10,
            memory_daily_usage_gb=[50.0] * 10,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.confidence == "medium"

    def test_short_window_is_low_confidence(self) -> None:
        """Edge case: less than 7 days of history → lower confidence, not a hard failure."""
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=[50.0] * 5,
            memory_daily_usage_gb=[50.0] * 5,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.confidence == "low"
        assert report.window_days_used == 5


class TestAutoscalerPassthrough:
    def test_autoscaler_flag_passed_through(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=[50.0] * 14,
            memory_daily_usage_gb=[50.0] * 14,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
            autoscaler_enabled=True,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.autoscaler_enabled is True


class TestRecommendation:
    def test_near_term_critical_resource_mentioned_in_recommendation(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=_cpu_series_matching_ticket(),
            memory_daily_usage_gb=_memory_series_matching_ticket(),
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert "CPU" in report.recommendation

    def test_capped_horizon_never_becomes_the_critical_resource(self) -> None:
        """Checker edge case: negligible growth must never produce an absurd
        far-future date — a capped-horizon resource is treated as no-risk,
        same as a flat/declining one, never picked as `critical_resource`."""
        tiny_growth = [10.0 + 0.1 * i for i in range(14)]
        flat = [50.0] * 14
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=tiny_growth,
            memory_daily_usage_gb=flat,
            total_allocatable_cpu_cores=1000.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.capped_horizon is True
        assert report.critical_resource == "None"
        assert "no saturation risk" in report.recommendation.lower()

    def test_far_out_but_uncapped_critical_resource_recommendation(self) -> None:
        far_out = [10.0 + 1.0 * i for i in range(14)]
        flat = [50.0] * 14
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=far_out,
            memory_daily_usage_gb=flat,
            total_allocatable_cpu_cores=123.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.capped_horizon is False
        assert report.cpu.days_to_saturation is not None
        assert report.cpu.days_to_saturation > 30
        assert "monitor and plan ahead" in report.recommendation.lower()

    def test_no_risk_recommendation_is_reassuring(self) -> None:
        flat = [50.0] * 14
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=flat,
            memory_daily_usage_gb=flat,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.recommendation != ""
        assert "no saturation risk" in report.recommendation.lower()


class TestCurrentUtilization:
    def test_utilization_percent_computed(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=_cpu_series_matching_ticket(),
            memory_daily_usage_gb=_memory_series_matching_ticket(),
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.current_utilization_percent == 70.0
        assert report.memory.current_utilization_percent == 80.0
