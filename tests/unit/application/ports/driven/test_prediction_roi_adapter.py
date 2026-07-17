from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
    PredictionRoiPort,
)


class _FakeSource:
    def __init__(self, data: PredictionRoiData) -> None:
        self._data = data

    def fetch_prediction_roi_data(self, period: str) -> PredictionRoiData:
        return self._data


def _data() -> PredictionRoiData:
    return PredictionRoiData(detections=[], infrastructure_cost_eur=0.0, revenue_per_minute=None)


class TestPortImplementation:
    def test_is_a_prediction_roi_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.prediction_roi_adapter import (
            PredictionRoiAdapter,
        )

        assert isinstance(PredictionRoiAdapter(source=_FakeSource(_data())), PredictionRoiPort)


class TestDelegation:
    def test_get_prediction_roi_data_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.prediction_roi_adapter import (
            PredictionRoiAdapter,
        )

        adapter = PredictionRoiAdapter(source=_FakeSource(_data()))

        result = adapter.get_prediction_roi_data("2026-06")

        assert result["revenue_per_minute"] is None
