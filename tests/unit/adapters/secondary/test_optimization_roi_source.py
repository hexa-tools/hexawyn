from __future__ import annotations


class TestEmptySprintRoiSource:
    def test_returns_no_baseline_by_default(self) -> None:
        from hexawyn.adapters.secondary.gitops.optimization_roi_source import (
            EmptySprintRoiSource,
        )

        data = EmptySprintRoiSource().fetch_sprint_roi_data("sprint-1")

        assert data["has_baseline"] is False
        assert data["optimizations"] == []
        assert data["performance_metrics"] == []
