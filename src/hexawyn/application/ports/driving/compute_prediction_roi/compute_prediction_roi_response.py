from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.prediction_roi import PredictionRoiReport


@dataclass
class ComputePredictionRoiResponse:
    result: PredictionRoiReport
