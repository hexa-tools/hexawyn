from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.optimization_roi_port import (
    OptimizationRoiPort,
    SprintRoiData,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SprintRoiSource(Protocol):
    """Assembles a sprint's ROI inputs from the cost, right-sizing and
    reliability sources into a single SprintRoiData record."""

    def fetch_sprint_roi_data(self, sprint_id: str) -> SprintRoiData: ...
mutants_xǁOptimizationRoiAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOptimizationRoiAdapterǁget_sprint_roi_data__mutmut: MutantDict = {}  # type: ignore


class OptimizationRoiAdapter(OptimizationRoiPort):
    """Facade over the cost / right-sizing / reliability sources.

    Delegates to an injected source that normalizes the heterogeneous audit
    outputs into the uniform SprintRoiData contract, keeping the domain free of
    any knowledge of the individual sources.
    """

    @_mutmut_mutated(mutants_xǁOptimizationRoiAdapterǁ__init____mutmut)
    def __init__(self, source: SprintRoiSource) -> None:
        self._source = source

    def xǁOptimizationRoiAdapterǁ__init____mutmut_orig(self, source: SprintRoiSource) -> None:
        self._source = source

    def xǁOptimizationRoiAdapterǁ__init____mutmut_1(self, source: SprintRoiSource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁOptimizationRoiAdapterǁget_sprint_roi_data__mutmut)
    def get_sprint_roi_data(self, sprint_id: str) -> SprintRoiData:
        return self._source.fetch_sprint_roi_data(sprint_id)

    def xǁOptimizationRoiAdapterǁget_sprint_roi_data__mutmut_orig(self, sprint_id: str) -> SprintRoiData:
        return self._source.fetch_sprint_roi_data(sprint_id)

    def xǁOptimizationRoiAdapterǁget_sprint_roi_data__mutmut_1(self, sprint_id: str) -> SprintRoiData:
        return self._source.fetch_sprint_roi_data(None)

mutants_xǁOptimizationRoiAdapterǁ__init____mutmut['_mutmut_orig'] = OptimizationRoiAdapter.xǁOptimizationRoiAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOptimizationRoiAdapterǁ__init____mutmut['xǁOptimizationRoiAdapterǁ__init____mutmut_1'] = OptimizationRoiAdapter.xǁOptimizationRoiAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁOptimizationRoiAdapterǁget_sprint_roi_data__mutmut['_mutmut_orig'] = OptimizationRoiAdapter.xǁOptimizationRoiAdapterǁget_sprint_roi_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOptimizationRoiAdapterǁget_sprint_roi_data__mutmut['xǁOptimizationRoiAdapterǁget_sprint_roi_data__mutmut_1'] = OptimizationRoiAdapter.xǁOptimizationRoiAdapterǁget_sprint_roi_data__mutmut_1 # type: ignore # mutmut generated
