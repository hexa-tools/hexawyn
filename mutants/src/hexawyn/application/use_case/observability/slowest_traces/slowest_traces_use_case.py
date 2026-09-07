from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.application.use_case.observability.slowest_traces.command import (
    SlowestTracesCommand,
)
from hexawyn.application.use_case.observability.slowest_traces.response import (
    SlowestTracesResponse,
)
from hexawyn.domain.models.slowest_traces import SlowestTracesRequest, SlowestTracesResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSlowestTracesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class SlowestTracesUseCase:
    @_mutmut_mutated(mutants_xǁSlowestTracesUseCaseǁ__init____mutmut)
    def __init__(self, port: SlowTraceSearchPort) -> None:
        self._port = port
    def xǁSlowestTracesUseCaseǁ__init____mutmut_orig(self, port: SlowTraceSearchPort) -> None:
        self._port = port
    def xǁSlowestTracesUseCaseǁ__init____mutmut_1(self, port: SlowTraceSearchPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁSlowestTracesUseCaseǁexecute__mutmut)
    def execute(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_orig(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_1(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = None
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_2(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=None,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_3(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=None,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_4(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=None,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_5(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_6(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_7(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_8(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = None
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_9(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(None)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_10(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = None
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_11(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=None, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_12(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=None)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_13(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_14(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, )
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_15(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=None,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_16(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=None,  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_17(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=None,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_18(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=None,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_19(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_20(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_21(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            note=r.note,
        )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_22(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            )

    def xǁSlowestTracesUseCaseǁexecute__mutmut_23(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(None) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )

mutants_xǁSlowestTracesUseCaseǁ__init____mutmut['_mutmut_orig'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁ__init____mutmut['xǁSlowestTracesUseCaseǁ__init____mutmut_1'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['_mutmut_orig'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_1'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_2'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_3'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_4'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_5'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_6'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_7'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_8'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_9'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_10'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_11'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_12'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_13'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_14'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_15'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_16'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_17'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_18'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_19'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_20'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_21'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_22'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSlowestTracesUseCaseǁexecute__mutmut['xǁSlowestTracesUseCaseǁexecute__mutmut_23'] = SlowestTracesUseCase.xǁSlowestTracesUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
