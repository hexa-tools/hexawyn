from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort
from hexawyn.application.use_case.observability.error_attribution.command import (
    ErrorAttributionCommand,
)
from hexawyn.application.use_case.observability.error_attribution.response import (
    ErrorAttributionResponse,
)
from hexawyn.domain.models.error_attribution import ErrorAttributionRequest, ErrorAttributionResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁErrorAttributionUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ErrorAttributionUseCase:
    @_mutmut_mutated(mutants_xǁErrorAttributionUseCaseǁ__init____mutmut)
    def __init__(self, port: ErrorAttributionPort) -> None:
        self._port = port
    def xǁErrorAttributionUseCaseǁ__init____mutmut_orig(self, port: ErrorAttributionPort) -> None:
        self._port = port
    def xǁErrorAttributionUseCaseǁ__init____mutmut_1(self, port: ErrorAttributionPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁErrorAttributionUseCaseǁexecute__mutmut)
    def execute(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_orig(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_1(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = None
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_2(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=None,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_3(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=None,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_4(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_5(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_6(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = None
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_7(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(None)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_8(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = None
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_9(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=None, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_10(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=None)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_11(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_12(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, )
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_13(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=None,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_14(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=None,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_15(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=None,  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_16(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=None,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_17(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_18(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_19(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_20(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],  # type: ignore
            )

    def xǁErrorAttributionUseCaseǁexecute__mutmut_21(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(None) for a in r.attribution],  # type: ignore
            pareto_culprit=r.pareto_culprit,  # type: ignore
        )

mutants_xǁErrorAttributionUseCaseǁ__init____mutmut['_mutmut_orig'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁ__init____mutmut['xǁErrorAttributionUseCaseǁ__init____mutmut_1'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['_mutmut_orig'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_1'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_2'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_3'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_4'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_5'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_6'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_7'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_8'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_9'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_10'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_11'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_12'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_13'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_14'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_15'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_16'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_17'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_18'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_19'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_20'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁErrorAttributionUseCaseǁexecute__mutmut['xǁErrorAttributionUseCaseǁexecute__mutmut_21'] = ErrorAttributionUseCase.xǁErrorAttributionUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
