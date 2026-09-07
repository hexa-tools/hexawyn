from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.optimization_roi_port import (
    OptimizationRoiPort,
    SprintRoiData,
)


class SprintRoiSource(Protocol):
    """Assembles a sprint's ROI inputs from the cost, right-sizing and
    reliability sources into a single SprintRoiData record."""

    def fetch_sprint_roi_data(self, sprint_id: str) -> SprintRoiData: ...


class OptimizationRoiAdapter(OptimizationRoiPort):
    """Facade over the cost / right-sizing / reliability sources.

    Delegates to an injected source that normalizes the heterogeneous audit
    outputs into the uniform SprintRoiData contract, keeping the domain free of
    any knowledge of the individual sources.
    """

    def __init__(self, source: SprintRoiSource) -> None:
        self._source = source

    def get_sprint_roi_data(self, sprint_id: str) -> SprintRoiData:
        return self._source.fetch_sprint_roi_data(sprint_id)
