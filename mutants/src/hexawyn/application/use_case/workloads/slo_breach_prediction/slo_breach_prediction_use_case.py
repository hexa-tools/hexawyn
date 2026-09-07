from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.slo_breach_prediction_port import SLOBreachPredictionPort
from hexawyn.application.use_case.workloads.slo_breach_prediction.command import (
    SLOBreachPredictionCommand,
)
from hexawyn.application.use_case.workloads.slo_breach_prediction.response import (
    SLOBreachPredictionResponse,
)
from hexawyn.domain.models.slo_breach_prediction import (
    SLOBreachPredictionRequest,
    SLOBreachPredictionResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSLOBreachPredictionUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class SLOBreachPredictionUseCase:
    @_mutmut_mutated(mutants_xǁSLOBreachPredictionUseCaseǁ__init____mutmut)
    def __init__(self, port: SLOBreachPredictionPort) -> None:
        self._port = port
    def xǁSLOBreachPredictionUseCaseǁ__init____mutmut_orig(self, port: SLOBreachPredictionPort) -> None:
        self._port = port
    def xǁSLOBreachPredictionUseCaseǁ__init____mutmut_1(self, port: SLOBreachPredictionPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut)
    def execute(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_orig(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_1(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = None
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_2(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=None  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_3(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = None
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_4(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(None)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_5(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = None
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_6(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=None, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_7(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=None)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_8(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_9(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, )
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_10(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=None, safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_11(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=None
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_12(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            safe_count=r.safe_count
        )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_13(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], )

    def xǁSLOBreachPredictionUseCaseǁexecute__mutmut_14(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes  # type: ignore
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(None) for a in r.at_risk], safe_count=r.safe_count
        )

mutants_xǁSLOBreachPredictionUseCaseǁ__init____mutmut['_mutmut_orig'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁ__init____mutmut['xǁSLOBreachPredictionUseCaseǁ__init____mutmut_1'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['_mutmut_orig'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_1'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_2'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_3'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_4'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_5'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_6'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_7'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_8'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_9'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_10'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_11'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_12'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_13'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSLOBreachPredictionUseCaseǁexecute__mutmut['xǁSLOBreachPredictionUseCaseǁexecute__mutmut_14'] = SLOBreachPredictionUseCase.xǁSLOBreachPredictionUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
