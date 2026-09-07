"""Unit tests for build_cluster_capacity_forecast — pure orchestration of
growth-rate + saturation-prediction per resource type into one report."""

from __future__ import annotations

from datetime import date

from hexawyn.domain.models.cluster_capacity_forecast import (
    ClusterCapacityForecastReport,
    ClusterCapacityForecastRequest,
    ClusterCapacityRawData,
    ResourceForecast,
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

        assert report.cpu.days_to_saturation == 15  # noqa: PLR2004
        assert report.memory.days_to_saturation == 40  # noqa: PLR2004
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
        assert report.window_days_used == 14  # noqa: PLR2004

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
        assert report.window_days_used == 5  # noqa: PLR2004


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
        assert report.cpu.days_to_saturation > 30  # noqa: PLR2004
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

        assert report.cpu.current_utilization_percent == 70.0  # noqa: PLR2004
        assert report.memory.current_utilization_percent == 80.0  # noqa: PLR2004


class TestExactReportPayload:
    def test_report_matches_full_expected_payload(self) -> None:
        cpu = _cpu_series_matching_ticket()
        memory = _memory_series_matching_ticket()
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=cpu,
            memory_daily_usage_gb=memory,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report == ClusterCapacityForecastReport(
            cpu=ResourceForecast(
                resource_type="cpu",
                current_value=67.2,
                ceiling=96.0,
                current_utilization_percent=70.0,
                growth_rate_per_day=1.9199999999999997,
                days_to_saturation=15,
                saturation_date="2026-07-02",
                capacity_jump_detected=False,
                spike_caveat=False,
                capped_horizon=False,
            ),
            memory=ResourceForecast(
                resource_type="memory",
                current_value=307.2,
                ceiling=384.0,
                current_utilization_percent=80.0,
                growth_rate_per_day=1.9200000000000004,
                days_to_saturation=40,
                saturation_date="2026-07-27",
                capacity_jump_detected=False,
                spike_caveat=False,
                capped_horizon=False,
            ),
            critical_resource="CPU",
            autoscaler_enabled=False,
            recommendation=(
                "CPU projected to saturate in 15 days (around 2026-07-02) "
                "— plan capacity expansion soon."
            ),
            confidence="high",
            window_days_used=14,
        )

    def test_empty_history_uses_request_window_and_zero_current(self) -> None:
        raw = ClusterCapacityRawData()
        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(window_days=21), raw, observed_at=_OBSERVED_AT
        )

        assert report.window_days_used == 21  # noqa: PLR2004
        assert report.confidence == "high"
        assert report.cpu.current_value == 0.0
        assert report.cpu.ceiling == 0.0
        assert report.cpu.current_utilization_percent == 0.0
        assert report.cpu.days_to_saturation is None
        assert report.cpu.saturation_date is None
        assert report.cpu.capacity_jump_detected is False
        assert report.cpu.spike_caveat is False
        assert report.cpu.capped_horizon is False
        assert report.cpu.resource_type == "cpu"
        assert report.critical_resource == "None"
        assert report.recommendation == (
            "No saturation risk in the foreseeable future — cluster capacity is stable."
        )

    def test_cpu_ties_with_memory_picks_cpu(self) -> None:
        same_series = [float(value) for value in range(40, 54)]
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=same_series,
            memory_daily_usage_gb=same_series,
            total_allocatable_cpu_cores=100.0,
            total_allocatable_memory_gb=100.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.days_to_saturation == report.memory.days_to_saturation
        assert report.critical_resource == "CPU"

    def test_utilization_keeps_two_decimal_places(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=[3.0],
            memory_daily_usage_gb=[3.0],
            total_allocatable_cpu_cores=7.0,
            total_allocatable_memory_gb=7.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.current_utilization_percent == 42.86  # noqa: PLR2004
        assert report.memory.current_utilization_percent == 42.86  # noqa: PLR2004


class TestBoundaryConditions:
    def test_sub_one_ceiling_still_computes_utilization(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=[0.25] * 7,
            memory_daily_usage_gb=[0.25] * 7,
            total_allocatable_cpu_cores=0.5,
            total_allocatable_memory_gb=0.5,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.current_utilization_percent == 50.0  # noqa: PLR2004

    def test_exactly_seven_days_is_medium_confidence(self) -> None:
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=[50.0] * 7,
            memory_daily_usage_gb=[50.0] * 7,
            total_allocatable_cpu_cores=96.0,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.window_days_used == 7  # noqa: PLR2004
        assert report.confidence == "medium"

    def test_exactly_thirty_days_is_near_term(self) -> None:
        series = [50.0 + 1.0 * i for i in range(14)]
        ceiling = series[-1] + 30.0
        raw = ClusterCapacityRawData(
            cpu_daily_usage_cores=series,
            memory_daily_usage_gb=[50.0] * 14,
            total_allocatable_cpu_cores=ceiling,
            total_allocatable_memory_gb=384.0,
        )

        report = build_cluster_capacity_forecast(
            ClusterCapacityForecastRequest(), raw, observed_at=_OBSERVED_AT
        )

        assert report.cpu.days_to_saturation == 30  # noqa: PLR2004
        assert "plan capacity expansion soon" in report.recommendation
