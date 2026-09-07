from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.application.use_case.observability.service_dependency_graph.command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.use_case.observability.service_dependency_graph.response import (
    ServiceDependencyGraphResponse,
)
from hexawyn.domain.models.service_dependency_graph import DependencyGraph, DependencyGraphRequest


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁUseCaseDependencyGraphUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class UseCaseDependencyGraphUseCase:
    @_mutmut_mutated(mutants_xǁUseCaseDependencyGraphUseCaseǁ__init____mutmut)
    def __init__(self, port: ServiceDependencyGraphPort) -> None:
        self._port = port
    def xǁUseCaseDependencyGraphUseCaseǁ__init____mutmut_orig(self, port: ServiceDependencyGraphPort) -> None:
        self._port = port
    def xǁUseCaseDependencyGraphUseCaseǁ__init____mutmut_1(self, port: ServiceDependencyGraphPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut)
    def execute(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_orig(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_1(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = None
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_2(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=None)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_3(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = None
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_4(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(None)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_5(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = None
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_6(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=None, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_7(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=None)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_8(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_9(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, )
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_10(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=None,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_11(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=None,
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_12(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=None,
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_13(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_14(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            edges=[asdict(e) for e in g.edges],
        )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_15(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            )

    def xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_16(self, command: ServiceDependencyGraphCommand) -> ServiceDependencyGraphResponse:
        req = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw = self._port.fetch_edges(req)
        g = DependencyGraph.compute(request=req, raw_edges=raw)
        return ServiceDependencyGraphResponse(
            time_window_minutes=g.time_window_minutes,
            nodes=[n.service_name for n in g.nodes],
            edges=[asdict(None) for e in g.edges],
        )

mutants_xǁUseCaseDependencyGraphUseCaseǁ__init____mutmut['_mutmut_orig'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁ__init____mutmut['xǁUseCaseDependencyGraphUseCaseǁ__init____mutmut_1'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['_mutmut_orig'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_1'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_2'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_3'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_4'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_5'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_6'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_7'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_8'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_9'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_10'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_11'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_12'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_13'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_14'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_15'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut['xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_16'] = UseCaseDependencyGraphUseCase.xǁUseCaseDependencyGraphUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
