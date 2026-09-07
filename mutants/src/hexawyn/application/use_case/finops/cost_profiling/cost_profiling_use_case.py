from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
from hexawyn.application.use_case.finops.cost_profiling.command import (
    CostProfilingCommand,
)
from hexawyn.application.use_case.finops.cost_profiling.response import (
    CostProfilingResponse,
)
from hexawyn.domain.models.cost_profiling import CostProfilingRequest, CostProfilingResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCostProfilingUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCostProfilingUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CostProfilingUseCase:
    @_mutmut_mutated(mutants_xǁCostProfilingUseCaseǁ__init____mutmut)
    def __init__(self, port: CostProfilingPort) -> None:
        self._port = port
    def xǁCostProfilingUseCaseǁ__init____mutmut_orig(self, port: CostProfilingPort) -> None:
        self._port = port
    def xǁCostProfilingUseCaseǁ__init____mutmut_1(self, port: CostProfilingPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCostProfilingUseCaseǁexecute__mutmut)
    def execute(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_orig(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_1(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = None
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_2(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=None, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_3(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=None
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_4(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_5(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_6(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = None
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_7(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(None)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_8(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = None
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_9(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=None, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_10(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=None)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_11(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_12(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, )
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_13(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=None,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_14(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=None,
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_15(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=None,
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_16(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_17(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_18(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            )

    def xǁCostProfilingUseCaseǁexecute__mutmut_19(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(None) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(c) for c in result.optimisation_candidates],
        )

    def xǁCostProfilingUseCaseǁexecute__mutmut_20(self, command: CostProfilingCommand) -> CostProfilingResponse:
        req = CostProfilingRequest(
            time_window_minutes=command.time_window_minutes, top_n=command.top_n
        )
        eps = self._port.fetch_endpoint_cpu_metrics(req)
        result = CostProfilingResult.compute(request=req, endpoints=eps)
        return CostProfilingResponse(
            time_window_minutes=result.time_window_minutes,
            ranked_endpoints=[asdict(e) for e in result.ranked_endpoints],
            optimisation_candidates=[asdict(None) for c in result.optimisation_candidates],
        )

mutants_xǁCostProfilingUseCaseǁ__init____mutmut['_mutmut_orig'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁ__init____mutmut['xǁCostProfilingUseCaseǁ__init____mutmut_1'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCostProfilingUseCaseǁexecute__mutmut['_mutmut_orig'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_1'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_2'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_3'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_4'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_5'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_6'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_7'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_8'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_9'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_10'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_11'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_12'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_13'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_14'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_15'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_16'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_17'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_18'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_19'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCostProfilingUseCaseǁexecute__mutmut['xǁCostProfilingUseCaseǁexecute__mutmut_20'] = CostProfilingUseCase.xǁCostProfilingUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
