from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
)
from hexawyn.infrastructure.config.config_manager import load_config


class ConfigPredictionRoiSource:
    def fetch_prediction_roi_data(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )


def _as_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None
