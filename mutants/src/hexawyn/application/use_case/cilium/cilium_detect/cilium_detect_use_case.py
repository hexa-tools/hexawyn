from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_detect.command import (
    CiliumDetectCommand,
)
from hexawyn.application.use_case.cilium.cilium_detect.response import (
    CiliumAgentOutput,
    CiliumDetectResponse,
)
from hexawyn.domain.models.cilium import CiliumAgentHealth


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCiliumDetectUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut: MutantDict = {}  # type: ignore


class CiliumDetectUseCase:
    @_mutmut_mutated(mutants_xǁCiliumDetectUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumDetectUseCaseǁ__init____mutmut_orig(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumDetectUseCaseǁ__init____mutmut_1(self, port: CiliumPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCiliumDetectUseCaseǁexecute__mutmut)
    def execute(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_orig(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_1(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = None
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_2(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = ""
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_3(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_4(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = None
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_5(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(None) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_6(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=None,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_7(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=None,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_8(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=None,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_9(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=None,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_10(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=None,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_11(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=None,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_12(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=None,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_13(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=None,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_14(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=None,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_15(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=None,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_16(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_17(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_18(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_19(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_20(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_21(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_22(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_23(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            agents=agents,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_24(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            note=detection.note,
        )

    def xǁCiliumDetectUseCaseǁexecute__mutmut_25(self, command: CiliumDetectCommand) -> CiliumDetectResponse:
        detection = self._port.detect()
        agents: list[CiliumAgentOutput] | None = None
        if detection.agents is not None:
            agents = [self._to_output(agent) for agent in detection.agents]
        return CiliumDetectResponse(
            installed=detection.installed,
            status=detection.status,
            version=detection.version,
            mode=detection.mode,
            namespace=detection.namespace,
            total_agents=detection.total_agents,
            ready_agents=detection.ready_agents,
            degraded_summary=detection.degraded_summary,
            agents=agents,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut)
    def _to_output(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_orig(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_1(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "XXnodeXX": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_2(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "NODE": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_3(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "XXpod_nameXX": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_4(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "POD_NAME": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_5(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "XXnamespaceXX": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_6(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "NAMESPACE": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_7(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "XXreadyXX": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_8(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "READY": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_9(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "XXphaseXX": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_10(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "PHASE": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_11(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "XXrestart_countXX": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_12(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "RESTART_COUNT": agent.restart_count,
            "image": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_13(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "XXimageXX": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_14(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "IMAGE": agent.image,
            "message": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_15(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "XXmessageXX": agent.message,
        }

    @staticmethod
    def xǁCiliumDetectUseCaseǁ_to_output__mutmut_16(agent: CiliumAgentHealth) -> CiliumAgentOutput:
        return {
            "node": agent.node,
            "pod_name": agent.pod_name,
            "namespace": agent.namespace,
            "ready": agent.ready,
            "phase": agent.phase,
            "restart_count": agent.restart_count,
            "image": agent.image,
            "MESSAGE": agent.message,
        }

mutants_xǁCiliumDetectUseCaseǁ__init____mutmut['_mutmut_orig'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ__init____mutmut['xǁCiliumDetectUseCaseǁ__init____mutmut_1'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['_mutmut_orig'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_1'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_2'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_3'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_4'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_5'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_6'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_7'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_8'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_9'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_10'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_11'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_12'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_13'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_14'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_15'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_16'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_17'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_18'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_19'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_20'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_21'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_22'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_23'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_24'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁexecute__mutmut['xǁCiliumDetectUseCaseǁexecute__mutmut_25'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated

mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['_mutmut_orig'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_1'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_2'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_3'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_4'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_5'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_6'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_7'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_8'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_9'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_10'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_11'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_12'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_13'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_14'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_15'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCiliumDetectUseCaseǁ_to_output__mutmut['xǁCiliumDetectUseCaseǁ_to_output__mutmut_16'] = CiliumDetectUseCase.xǁCiliumDetectUseCaseǁ_to_output__mutmut_16 # type: ignore # mutmut generated
