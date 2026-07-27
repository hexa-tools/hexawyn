from __future__ import annotations

from hexawyn.domain.models.slo_breach_prediction import (
    RiskLevel,
    ServiceRisk,
    SLOBreachPredictionRequest,
    SLOBreachPredictionResult,
)


class TestServiceRisk:
    def test_high_risk(self) -> None:
        sr = ServiceRisk(
            service_name="auth-service",
            current_p99_ms=320.0,
            slo_threshold_ms=500.0,
            trend_slope_ms_per_min=8.2,
            projected_p99_ms=812.0,
            breach_in_minutes=22.0,
            risk=RiskLevel.HIGH,
        )
        assert sr.risk == RiskLevel.HIGH
        assert sr.breach_in_minutes == 22.0  # noqa: PLR2004


class TestSLOBreachPredictionResult:
    def test_ranked_risks(self) -> None:
        raw = [
            {"service": "auth-service", "current_p99": 320.0, "slo": 500.0, "slope": 8.2},
            {"service": "payment-service", "current_p99": 200.0, "slo": 500.0, "slope": 0.0},
            {"service": "checkout-service", "current_p99": 180.0, "slo": 300.0, "slope": 2.1},
        ]
        result = SLOBreachPredictionResult.compute(
            request=SLOBreachPredictionRequest(prediction_window_minutes=60),
            raw_metrics=raw,
        )
        assert len(result.at_risk) == 2  # noqa: PLR2004
        assert result.at_risk[0].service_name == "auth-service"
        assert result.safe_count == 1

    def test_no_risk(self) -> None:
        raw = [
            {"service": "stable-svc", "current_p99": 200.0, "slo": 500.0, "slope": 0.0},
        ]
        result = SLOBreachPredictionResult.compute(
            request=SLOBreachPredictionRequest(),
            raw_metrics=raw,
        )
        assert len(result.at_risk) == 0
        assert result.safe_count == 1

    def test_positive_slope_but_safe(self) -> None:
        raw = [
            {"service": "slow-growth", "current_p99": 50.0, "slo": 500.0, "slope": 1.0},
        ]
        result = SLOBreachPredictionResult.compute(
            request=SLOBreachPredictionRequest(prediction_window_minutes=60),
            raw_metrics=raw,
        )
        assert len(result.at_risk) == 1
        assert result.at_risk[0].risk == RiskLevel.LOW

    def test_low_risk(self) -> None:
        raw = [
            {"service": "distant-risk", "current_p99": 100.0, "slo": 500.0, "slope": 0.5},
        ]
        result = SLOBreachPredictionResult.compute(
            request=SLOBreachPredictionRequest(prediction_window_minutes=60),
            raw_metrics=raw,
        )
        assert len(result.at_risk) == 1
        assert result.at_risk[0].risk == RiskLevel.LOW
