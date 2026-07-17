from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import (
    OptimizationRoiPort,
    SprintRoiData,
)


class _FakeSource:
    def __init__(self, data: SprintRoiData) -> None:
        self._data = data

    def fetch_sprint_roi_data(self, sprint_id: str) -> SprintRoiData:
        return self._data


def _data(has_baseline: bool = True) -> SprintRoiData:
    return SprintRoiData(
        has_baseline=has_baseline,
        baseline_monthly_eur=500.0,
        current_monthly_eur=150.0,
        optimizations=[
            {
                "name": "right-size",
                "category": "right_sizing",
                "monthly_saving_eur": 350.0,
                "description": "",
            }
        ],
        performance_metrics=[{"metric": "p99_latency_ms", "before": 120.0, "after": 95.0}],
    )


class TestPortImplementation:
    def test_is_an_optimization_roi_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.optimization_roi_adapter import (
            OptimizationRoiAdapter,
        )

        assert isinstance(OptimizationRoiAdapter(source=_FakeSource(_data())), OptimizationRoiPort)


class TestGetSprintRoiData:
    def test_delegates_to_source(self) -> None:
        from hexawyn.adapters.secondary.gitops.optimization_roi_adapter import (
            OptimizationRoiAdapter,
        )

        adapter = OptimizationRoiAdapter(source=_FakeSource(_data()))

        result = adapter.get_sprint_roi_data("sprint-1")

        assert result["baseline_monthly_eur"] == 500.0
        assert result["optimizations"][0]["category"] == "right_sizing"

    def test_passes_no_baseline_through(self) -> None:
        from hexawyn.adapters.secondary.gitops.optimization_roi_adapter import (
            OptimizationRoiAdapter,
        )

        adapter = OptimizationRoiAdapter(source=_FakeSource(_data(has_baseline=False)))

        result = adapter.get_sprint_roi_data("sprint-1")

        assert result["has_baseline"] is False
