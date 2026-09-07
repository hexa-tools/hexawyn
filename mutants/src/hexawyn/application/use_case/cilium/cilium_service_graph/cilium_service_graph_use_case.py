from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.command import (
    CiliumServiceGraphCommand,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.response import (
    CiliumServiceGraphResponse,
)
from hexawyn.domain.models.service_dependency_graph import (
    DependencyGraph,
    DependencyGraphRequest,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCiliumServiceGraphUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CiliumServiceGraphUseCase:
    @_mutmut_mutated(mutants_xǁCiliumServiceGraphUseCaseǁ__init____mutmut)
    def __init__(self, port: ServiceDependencyGraphPort) -> None:
        self._port = port
    def xǁCiliumServiceGraphUseCaseǁ__init____mutmut_orig(self, port: ServiceDependencyGraphPort) -> None:
        self._port = port
    def xǁCiliumServiceGraphUseCaseǁ__init____mutmut_1(self, port: ServiceDependencyGraphPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut)
    def execute(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_orig(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_1(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = None
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_2(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=None)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_3(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = None
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_4(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(None)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_5(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = None
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_6(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(None, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_7(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, None)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_8(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_9(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, )
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_10(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = ""
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_11(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_12(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = None
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_13(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "XXNo Cilium flow data (Hubble unavailable or no traffic in the window)XX"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_14(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "no cilium flow data (hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_15(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "NO CILIUM FLOW DATA (HUBBLE UNAVAILABLE OR NO TRAFFIC IN THE WINDOW)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_16(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=None,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_17(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=None,
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_18(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=None,
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_19(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=None,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_20(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_21(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            edges=[asdict(edge) for edge in graph.edges],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_22(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            note=note,
        )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_23(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(edge) for edge in graph.edges],
            )

    def xǁCiliumServiceGraphUseCaseǁexecute__mutmut_24(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse:
        request = DependencyGraphRequest(time_window_minutes=command.time_window_minutes)
        raw_edges = self._port.fetch_edges(request)
        graph = DependencyGraph.compute(request, raw_edges)
        note = None
        if not graph.nodes:
            note = "No Cilium flow data (Hubble unavailable or no traffic in the window)"
        return CiliumServiceGraphResponse(
            time_window_minutes=graph.time_window_minutes,
            nodes=[node.service_name for node in graph.nodes],
            edges=[asdict(None) for edge in graph.edges],
            note=note,
        )

mutants_xǁCiliumServiceGraphUseCaseǁ__init____mutmut['_mutmut_orig'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁ__init____mutmut['xǁCiliumServiceGraphUseCaseǁ__init____mutmut_1'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['_mutmut_orig'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_1'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_2'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_3'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_4'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_5'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_6'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_7'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_8'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_9'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_10'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_11'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_12'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_13'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_14'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_15'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_16'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_17'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_18'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_19'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_20'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_21'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_22'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_23'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCiliumServiceGraphUseCaseǁexecute__mutmut['xǁCiliumServiceGraphUseCaseǁexecute__mutmut_24'] = CiliumServiceGraphUseCase.xǁCiliumServiceGraphUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
