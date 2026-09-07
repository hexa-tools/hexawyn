from __future__ import annotations

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.application.use_case.cilium.get_cilium_flows.command import (
    GetCiliumFlowsCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_flows.response import (
    CiliumFlowOutput,
    GetCiliumFlowsResponse,
)
from hexawyn.domain.models.cilium import CiliumFlowEntry, CiliumFlowQuery


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetCiliumFlowsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut: MutantDict = {}  # type: ignore


class GetCiliumFlowsUseCase:
    @_mutmut_mutated(mutants_xǁGetCiliumFlowsUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumHubblePort) -> None:
        self._port = port
    def xǁGetCiliumFlowsUseCaseǁ__init____mutmut_orig(self, port: CiliumHubblePort) -> None:
        self._port = port
    def xǁGetCiliumFlowsUseCaseǁ__init____mutmut_1(self, port: CiliumHubblePort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut)
    def execute(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_orig(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_1(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = None
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_2(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=None,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_3(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=None,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_4(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=None,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_5(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=None,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_6(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=None,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_7(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=None,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_8(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_9(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_10(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_11(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_12(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_13(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_14(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = None
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_15(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(None)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_16(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = ""
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_17(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_18(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = None
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_19(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(None) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_20(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=None,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_21(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=None,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_22(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=None,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_23(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=None,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_24(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=None,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_25(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_26(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            total_flows=result.total_flows,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_27(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            flows=flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_28(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            note=result.note,
        )

    def xǁGetCiliumFlowsUseCaseǁexecute__mutmut_29(self, command: GetCiliumFlowsCommand) -> GetCiliumFlowsResponse:
        query = CiliumFlowQuery(
            namespace=command.namespace,
            pod=command.pod,
            direction=command.direction,
            verdict=command.verdict,
            window_minutes=command.window_minutes,
            limit=command.limit,
        )
        result = self._port.get_flows(query)
        flows: list[CiliumFlowOutput] | None = None
        if result.flows is not None:
            flows = [self._to_flow(flow) for flow in result.flows]
        return GetCiliumFlowsResponse(
            installed=result.installed,
            status=result.status,
            total_flows=result.total_flows,
            flows=flows,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut)
    def _to_flow(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_orig(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_1(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "XXtimestampXX": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_2(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "TIMESTAMP": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_3(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "XXsourceXX": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_4(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "SOURCE": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_5(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "XXdestinationXX": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_6(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "DESTINATION": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_7(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "XXsource_namespaceXX": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_8(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "SOURCE_NAMESPACE": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_9(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "XXdestination_namespaceXX": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_10(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "DESTINATION_NAMESPACE": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_11(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "XXsource_identityXX": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_12(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "SOURCE_IDENTITY": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_13(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "XXdestination_identityXX": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_14(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "DESTINATION_IDENTITY": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_15(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "XXverdictXX": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_16(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "VERDICT": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_17(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "XXdrop_reasonXX": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_18(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "DROP_REASON": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_19(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "XXprotocolXX": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_20(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "PROTOCOL": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_21(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "XXdestination_portXX": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_22(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "DESTINATION_PORT": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_23(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "XXl7_protocolXX": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_24(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "L7_PROTOCOL": flow.l7_protocol,
            "direction": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_25(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "XXdirectionXX": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_26(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "DIRECTION": flow.direction,
            "policy": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_27(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "XXpolicyXX": flow.policy,
        }

    @staticmethod
    def xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_28(flow: CiliumFlowEntry) -> CiliumFlowOutput:
        return {
            "timestamp": flow.timestamp,
            "source": flow.source,
            "destination": flow.destination,
            "source_namespace": flow.source_namespace,
            "destination_namespace": flow.destination_namespace,
            "source_identity": flow.source_identity,
            "destination_identity": flow.destination_identity,
            "verdict": flow.verdict,
            "drop_reason": flow.drop_reason,
            "protocol": flow.protocol,
            "destination_port": flow.destination_port,
            "l7_protocol": flow.l7_protocol,
            "direction": flow.direction,
            "POLICY": flow.policy,
        }

mutants_xǁGetCiliumFlowsUseCaseǁ__init____mutmut['_mutmut_orig'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ__init____mutmut['xǁGetCiliumFlowsUseCaseǁ__init____mutmut_1'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['_mutmut_orig'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_1'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_2'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_3'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_4'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_5'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_6'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_7'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_8'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_9'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_10'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_11'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_12'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_13'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_14'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_15'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_16'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_17'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_18'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_19'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_20'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_21'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_22'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_23'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_24'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_25'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_26'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_27'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_28'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁexecute__mutmut['xǁGetCiliumFlowsUseCaseǁexecute__mutmut_29'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated

mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['_mutmut_orig'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_1'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_2'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_3'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_4'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_5'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_6'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_7'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_8'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_9'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_10'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_11'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_12'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_13'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_14'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_15'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_16'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_17'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_18'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_19'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_20'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_21'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_22'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_23'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_24'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_25'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_26'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_27'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut['xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_28'] = GetCiliumFlowsUseCase.xǁGetCiliumFlowsUseCaseǁ_to_flow__mutmut_28 # type: ignore # mutmut generated
