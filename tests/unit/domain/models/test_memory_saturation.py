from __future__ import annotations

from hexawyn.domain.models.memory_saturation import (
    MemoryPrediction,
    MemorySaturationRequest,
    MemorySaturationResult,
    PredictionRisk,
)


class TestMemoryPrediction:
    def test_critical(self) -> None:
        p = MemoryPrediction(
            pod_name="checkout-pod-abc",
            namespace="production",
            current_memory_mb=850.0,
            limit_mb=1024.0,
            growth_rate_mb_per_min=8.5,
            saturation_in_minutes=20.0,
            otel_root_cause="DB query returning 15MB on each /checkout",
            risk=PredictionRisk.CRITICAL,
        )
        assert p.saturation_in_minutes == 20.0
        assert p.risk == PredictionRisk.CRITICAL

    def test_stable(self) -> None:
        p = MemoryPrediction(
            pod_name="auth-pod-xyz",
            namespace="production",
            current_memory_mb=300.0,
            limit_mb=1024.0,
            growth_rate_mb_per_min=0.0,
            saturation_in_minutes=None,
            otel_root_cause=None,
            risk=PredictionRisk.STABLE,
        )
        assert p.risk == PredictionRisk.STABLE
        assert p.saturation_in_minutes is None


class TestMemorySaturationResult:
    def test_compute_critical(self) -> None:
        raw_pods = [
            {
                "name": "checkout-pod-abc",
                "namespace": "production",
                "current_mb": 850.0,
                "limit_mb": 1024.0,
                "growth_rate_mb_per_min": 8.5,
            },
            {
                "name": "auth-pod",
                "namespace": "production",
                "current_mb": 300.0,
                "limit_mb": 1024.0,
                "growth_rate_mb_per_min": 0.0,
            },
        ]
        req = MemorySaturationRequest(prediction_window_minutes=30, critical_threshold_minutes=30)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw_pods)
        assert len(result.critical_pods) == 1
        assert result.critical_pods[0].pod_name == "checkout-pod-abc"
        assert result.critical_pods[0].risk == PredictionRisk.AT_RISK

    def test_no_risk(self) -> None:
        raw_pods = [
            {
                "name": "stable-pod",
                "namespace": "default",
                "current_mb": 100.0,
                "limit_mb": 1024.0,
                "growth_rate_mb_per_min": 0.1,
            },
        ]
        req = MemorySaturationRequest(prediction_window_minutes=30, critical_threshold_minutes=30)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw_pods)
        assert len(result.critical_pods) == 0
        assert result.safe_pod_count == 1

    def test_no_limit_uses_default(self) -> None:
        raw_pods = [
            {
                "name": "no-limit-pod",
                "namespace": "default",
                "current_mb": 15000.0,
                "limit_mb": None,
                "growth_rate_mb_per_min": 2000.0,
            },
        ]
        req = MemorySaturationRequest(prediction_window_minutes=30, critical_threshold_minutes=30)
        result = MemorySaturationResult.compute(request=req, raw_pods=raw_pods)
        assert result.critical_pods[0].limit_mb is None
        assert result.critical_pods[0].risk == PredictionRisk.CRITICAL
