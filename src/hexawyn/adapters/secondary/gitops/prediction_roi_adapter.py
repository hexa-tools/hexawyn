from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
    PredictionRoiPort,
)


class PredictionRoiSource(Protocol):
    def fetch_prediction_roi_data(self, period: str) -> PredictionRoiData: ...


class PredictionRoiAdapter(PredictionRoiPort):
    def __init__(self, source: PredictionRoiSource) -> None:
        self._source = source

    def get_prediction_roi_data(self, period: str) -> PredictionRoiData:
        return self._source.fetch_prediction_roi_data(period)
