"""HubbleDependencyGraphAdapter — builds the service graph from real Cilium flows."""

from __future__ import annotations

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.domain.models.cilium import CiliumFlowQuery
from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest
from hexawyn.domain.services.cilium.graph_builder import build_graph_edges


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁHubbleDependencyGraphAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut: MutantDict = {}  # type: ignore


class HubbleDependencyGraphAdapter(ServiceDependencyGraphPort):
    """Service graph from observed Hubble flows (vs inferred topology)."""

    @_mutmut_mutated(mutants_xǁHubbleDependencyGraphAdapterǁ__init____mutmut)
    def __init__(self, hubble_port: CiliumHubblePort) -> None:
        self._hubble_port = hubble_port

    def xǁHubbleDependencyGraphAdapterǁ__init____mutmut_orig(self, hubble_port: CiliumHubblePort) -> None:
        self._hubble_port = hubble_port

    def xǁHubbleDependencyGraphAdapterǁ__init____mutmut_1(self, hubble_port: CiliumHubblePort) -> None:
        self._hubble_port = None

    @_mutmut_mutated(mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut)
    def fetch_edges(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                window_minutes=request.time_window_minutes,
                limit=1000,
            )
        )
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_orig(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                window_minutes=request.time_window_minutes,
                limit=1000,
            )
        )
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_1(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = None
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_2(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            None
        )
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_3(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                window_minutes=None,
                limit=1000,
            )
        )
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_4(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                window_minutes=request.time_window_minutes,
                limit=None,
            )
        )
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_5(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                limit=1000,
            )
        )
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_6(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                window_minutes=request.time_window_minutes,
                )
        )
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_7(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                window_minutes=request.time_window_minutes,
                limit=1001,
            )
        )
        if not flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_8(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                window_minutes=request.time_window_minutes,
                limit=1000,
            )
        )
        if flows.installed:
            return []
        return build_graph_edges(flows.flows)

    def xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_9(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        flows = self._hubble_port.get_flows(
            CiliumFlowQuery(
                window_minutes=request.time_window_minutes,
                limit=1000,
            )
        )
        if not flows.installed:
            return []
        return build_graph_edges(None)

mutants_xǁHubbleDependencyGraphAdapterǁ__init____mutmut['_mutmut_orig'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁ__init____mutmut['xǁHubbleDependencyGraphAdapterǁ__init____mutmut_1'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['_mutmut_orig'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_1'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_2'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_3'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_4'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_5'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_6'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_7'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_8'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut['xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_9'] = HubbleDependencyGraphAdapter.xǁHubbleDependencyGraphAdapterǁfetch_edges__mutmut_9 # type: ignore # mutmut generated
