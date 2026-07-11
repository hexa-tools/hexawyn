from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import SprintRoiData


class EmptySprintRoiSource:
    """Default sprint ROI source used until a persistent sprint baseline store
    is wired in. Reports no baseline, so the domain asks the user to establish
    one rather than fabricating a misleading zero-ROI report."""

    def fetch_sprint_roi_data(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )
