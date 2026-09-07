from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)
from hexawyn.application.use_case.observability.redundant_calls.command import (
    RedundantCallsCommand,
)
from hexawyn.application.use_case.observability.redundant_calls.response import (
    RedundantCallsResponse,
)
from hexawyn.domain.models.redundant_calls import RedundantCallRequest, RedundantCallResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRedundantCallsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class RedundantCallsUseCase:
    @_mutmut_mutated(mutants_xǁRedundantCallsUseCaseǁ__init____mutmut)
    def __init__(self, port: RedundantCallDetectionPort) -> None:
        self._port = port
    def xǁRedundantCallsUseCaseǁ__init____mutmut_orig(self, port: RedundantCallDetectionPort) -> None:
        self._port = port
    def xǁRedundantCallsUseCaseǁ__init____mutmut_1(self, port: RedundantCallDetectionPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁRedundantCallsUseCaseǁexecute__mutmut)
    def execute(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_orig(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_1(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = None
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_2(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=None, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_3(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=None)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_4(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_5(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, )
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_6(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = None
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_7(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(None)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_8(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = None
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_9(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=None, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_10(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=None)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_11(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_12(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, )
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_13(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=None,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_14(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=None,  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_15(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=None,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_16(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=None,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_17(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_18(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_19(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_20(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            )

    def xǁRedundantCallsUseCaseǁexecute__mutmut_21(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(None) for p in r.patterns],  # type: ignore
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,  # type: ignore
        )

mutants_xǁRedundantCallsUseCaseǁ__init____mutmut['_mutmut_orig'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁ__init____mutmut['xǁRedundantCallsUseCaseǁ__init____mutmut_1'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['_mutmut_orig'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_1'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_2'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_3'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_4'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_5'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_6'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_7'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_8'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_9'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_10'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_11'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_12'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_13'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_14'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_15'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_16'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_17'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_18'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_19'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_20'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRedundantCallsUseCaseǁexecute__mutmut['xǁRedundantCallsUseCaseǁexecute__mutmut_21'] = RedundantCallsUseCase.xǁRedundantCallsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
