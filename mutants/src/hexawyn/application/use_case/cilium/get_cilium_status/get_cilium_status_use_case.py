from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.get_cilium_status.command import (
    GetCiliumStatusCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_status.response import (
    CiliumStatusNodeOutput,
    GetCiliumStatusResponse,
)
from hexawyn.domain.models.cilium import CiliumAgentHealth


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetCiliumStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut: MutantDict = {}  # type: ignore


class GetCiliumStatusUseCase:
    @_mutmut_mutated(mutants_xǁGetCiliumStatusUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumPort) -> None:
        self._port = port
    def xǁGetCiliumStatusUseCaseǁ__init____mutmut_orig(self, port: CiliumPort) -> None:
        self._port = port
    def xǁGetCiliumStatusUseCaseǁ__init____mutmut_1(self, port: CiliumPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut)
    def execute(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_orig(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_1(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = None
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_2(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = ""
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_3(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_4(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = None
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_5(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(None) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_6(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=None,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_7(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=None,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_8(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=None,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_9(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=None,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_10(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=None,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_11(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=None,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_12(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=None,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_13(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=None,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_14(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=None,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_15(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_16(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_17(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_18(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_19(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_20(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            connectivity=status.connectivity,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_21(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            nodes=nodes,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_22(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            note=status.note,
        )

    def xǁGetCiliumStatusUseCaseǁexecute__mutmut_23(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse:
        status = self._port.status()
        nodes: list[CiliumStatusNodeOutput] | None = None
        if status.nodes is not None:
            nodes = [self._to_node(node) for node in status.nodes]
        return GetCiliumStatusResponse(
            installed=status.installed,
            status=status.status,
            ready_agents=status.ready_agents,
            total_agents=status.total_agents,
            degraded_summary=status.degraded_summary,
            controller_errors=status.controller_errors,
            connectivity=status.connectivity,
            nodes=nodes,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut)
    def _to_node(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_orig(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_1(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "XXnodeXX": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_2(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "NODE": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_3(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "XXpod_nameXX": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_4(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "POD_NAME": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_5(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "XXnamespaceXX": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_6(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "NAMESPACE": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_7(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "XXreadyXX": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_8(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "READY": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_9(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "XXphaseXX": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_10(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "PHASE": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_11(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "XXrestart_countXX": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_12(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "RESTART_COUNT": node.restart_count,
            "image": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_13(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "XXimageXX": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_14(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "IMAGE": node.image,
            "message": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_15(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "XXmessageXX": node.message,
        }

    @staticmethod
    def xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_16(node: CiliumAgentHealth) -> CiliumStatusNodeOutput:
        return {
            "node": node.node,
            "pod_name": node.pod_name,
            "namespace": node.namespace,
            "ready": node.ready,
            "phase": node.phase,
            "restart_count": node.restart_count,
            "image": node.image,
            "MESSAGE": node.message,
        }

mutants_xǁGetCiliumStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ__init____mutmut['xǁGetCiliumStatusUseCaseǁ__init____mutmut_1'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['_mutmut_orig'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_1'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_2'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_3'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_4'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_5'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_6'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_7'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_8'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_9'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_10'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_11'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_12'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_13'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_14'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_15'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_16'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_17'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_18'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_19'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_20'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_21'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_22'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁexecute__mutmut['xǁGetCiliumStatusUseCaseǁexecute__mutmut_23'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated

mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['_mutmut_orig'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_1'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_2'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_3'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_4'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_5'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_6'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_7'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_8'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_9'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_10'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_11'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_12'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_13'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_14'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_15'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetCiliumStatusUseCaseǁ_to_node__mutmut['xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_16'] = GetCiliumStatusUseCase.xǁGetCiliumStatusUseCaseǁ_to_node__mutmut_16 # type: ignore # mutmut generated
