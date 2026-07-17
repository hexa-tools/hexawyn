from __future__ import annotations

from hexawyn.domain.models.p99_latency import (
    LatencyPercentileRequest,
    LatencyPercentiles,
    P99Result,
    SLOStatus,
)


class TestLatencyPercentiles:
    def test_create(self) -> None:
        lp = LatencyPercentiles(p50_ms=85.0, p95_ms=210.0, p99_ms=480.0, sample_count=14200)
        assert lp.p99_ms == 480.0
        assert lp.sample_count == 14200


class TestSLOStatus:
    def test_values(self) -> None:
        assert SLOStatus.PASS.value == "pass"
        assert SLOStatus.FAIL.value == "fail"
        assert SLOStatus.NO_DATA.value == "no_data"


class TestP99Result:
    def test_slo_pass(self) -> None:
        lp = LatencyPercentiles(p50_ms=85.0, p95_ms=210.0, p99_ms=320.0, sample_count=14200)
        result = P99Result.compute(
            request=LatencyPercentileRequest(
                endpoint="/v1/checkout", time_window_minutes=120, slo_threshold_ms=500.0
            ),
            percentiles=lp,
        )
        assert result.slo_status == SLOStatus.PASS
        assert result.p99_ms == 320.0

    def test_slo_fail(self) -> None:
        lp = LatencyPercentiles(p50_ms=350.0, p95_ms=600.0, p99_ms=820.0, sample_count=10000)
        result = P99Result.compute(
            request=LatencyPercentileRequest(
                endpoint="/v1/checkout", time_window_minutes=120, slo_threshold_ms=500.0
            ),
            percentiles=lp,
        )
        assert result.slo_status == SLOStatus.FAIL
        assert result.slo_delta_ms == 320.0

    def test_no_data(self) -> None:
        lp = LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
        result = P99Result.compute(
            request=LatencyPercentileRequest(
                endpoint="/v1/ghost", time_window_minutes=60, slo_threshold_ms=500.0
            ),
            percentiles=lp,
        )
        assert result.slo_status == SLOStatus.NO_DATA
