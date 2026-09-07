from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
    PredictionRoiPort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PredictionRoiSource(Protocol):
    def fetch_prediction_roi_data(self, period: str) -> PredictionRoiData: ...
mutants_xǁPredictionRoiAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPredictionRoiAdapterǁget_prediction_roi_data__mutmut: MutantDict = {}  # type: ignore


class PredictionRoiAdapter(PredictionRoiPort):
    @_mutmut_mutated(mutants_xǁPredictionRoiAdapterǁ__init____mutmut)
    def __init__(self, source: PredictionRoiSource) -> None:
        self._source = source
    def xǁPredictionRoiAdapterǁ__init____mutmut_orig(self, source: PredictionRoiSource) -> None:
        self._source = source
    def xǁPredictionRoiAdapterǁ__init____mutmut_1(self, source: PredictionRoiSource) -> None:
        self._source = None

    @_mutmut_mutated(mutants_xǁPredictionRoiAdapterǁget_prediction_roi_data__mutmut)
    def get_prediction_roi_data(self, period: str) -> PredictionRoiData:
        return self._source.fetch_prediction_roi_data(period)

    def xǁPredictionRoiAdapterǁget_prediction_roi_data__mutmut_orig(self, period: str) -> PredictionRoiData:
        return self._source.fetch_prediction_roi_data(period)

    def xǁPredictionRoiAdapterǁget_prediction_roi_data__mutmut_1(self, period: str) -> PredictionRoiData:
        return self._source.fetch_prediction_roi_data(None)

mutants_xǁPredictionRoiAdapterǁ__init____mutmut['_mutmut_orig'] = PredictionRoiAdapter.xǁPredictionRoiAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPredictionRoiAdapterǁ__init____mutmut['xǁPredictionRoiAdapterǁ__init____mutmut_1'] = PredictionRoiAdapter.xǁPredictionRoiAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPredictionRoiAdapterǁget_prediction_roi_data__mutmut['_mutmut_orig'] = PredictionRoiAdapter.xǁPredictionRoiAdapterǁget_prediction_roi_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPredictionRoiAdapterǁget_prediction_roi_data__mutmut['xǁPredictionRoiAdapterǁget_prediction_roi_data__mutmut_1'] = PredictionRoiAdapter.xǁPredictionRoiAdapterǁget_prediction_roi_data__mutmut_1 # type: ignore # mutmut generated
