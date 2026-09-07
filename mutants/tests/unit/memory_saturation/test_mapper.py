from __future__ import annotations

from hexawyn.application.use_case.troubleshooting.memory_saturation.mapper import (
    attach_otel_root_cause,
    predictions_to_dicts,
)
from hexawyn.domain.models.memory_saturation import (
    MemoryPrediction,
    PredictionRisk,
)


class TestMapper:
    def test_predictions_to_dicts_converts_empty_list(self) -> None:
        result = predictions_to_dicts([])
        assert result == []

    def test_predictions_to_dicts_converts_critical_pods(self) -> None:
        pred = MemoryPrediction(
            pod_name="leaky-app",
            namespace="production",
            current_memory_mb=5000.0,
            limit_mb=5120.0,
            growth_rate_mb_per_min=10.0,
            saturation_in_minutes=12.0,
            otel_root_cause=None,
            risk=PredictionRisk.CRITICAL,
        )

        result = predictions_to_dicts([pred])

        assert len(result) == 1
        assert result[0]["pod_name"] == "leaky-app"
        assert result[0]["risk"] == PredictionRisk.CRITICAL

    def test_attach_otel_root_cause_preserves_fields(self) -> None:
        pred = MemoryPrediction(
            pod_name="leaky-app",
            namespace="production",
            current_memory_mb=5000.0,
            limit_mb=5120.0,
            growth_rate_mb_per_min=10.0,
            saturation_in_minutes=12.0,
            otel_root_cause=None,
            risk=PredictionRisk.CRITICAL,
        )

        updated = attach_otel_root_cause(pred, "memory_leak")

        assert updated.otel_root_cause == "memory_leak"
        assert updated.pod_name == "leaky-app"
        assert updated.current_memory_mb == 5000.0  # noqa: PLR2004
