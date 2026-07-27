from dataclasses import dataclass


@dataclass(frozen=True)
class SLOBreachPredictionCommand:
    prediction_window_minutes: str = ""
