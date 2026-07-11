from abc import ABC, abstractmethod
from typing import TypedDict


class OptimizationRaw(TypedDict):
    name: str
    category: str
    monthly_saving_eur: float
    description: str


class PerformanceMetricRaw(TypedDict):
    metric: str
    before: float
    after: float


class SprintRoiData(TypedDict):
    has_baseline: bool
    baseline_monthly_eur: float
    current_monthly_eur: float
    optimizations: list[OptimizationRaw]
    performance_metrics: list[PerformanceMetricRaw]


class OptimizationRoiPort(ABC):
    """Driven port — provides before/after cost, the individual optimizations
    applied, and before/after performance metrics for one optimization sprint.

    A secondary adapter fans out to the cost, right-sizing and reliability
    sources and normalizes them into this single contract; the domain never
    touches those sources directly.
    """

    @abstractmethod
    def get_sprint_roi_data(self, sprint_id: str) -> SprintRoiData:
        """Return the ROI inputs for *sprint_id*.

        ``has_baseline`` is False when no pre-sprint cost baseline was recorded,
        so the domain can ask the user to establish one instead of reporting a
        misleading zero.

        Raises ClusterUnreachableError on data-source failures.
        """
