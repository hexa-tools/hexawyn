from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SLOBreachPredictionCommand:
    prediction_window_minutes: int = 60
