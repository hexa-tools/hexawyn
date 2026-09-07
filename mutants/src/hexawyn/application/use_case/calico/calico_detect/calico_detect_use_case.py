"""CalicoDetectUseCase — reports whether Calico is the active CNI and its health."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_detect.command import CalicoDetectCommand
from hexawyn.application.use_case.calico.calico_detect.response import CalicoDetectResponse
from hexawyn.domain.models.calico import CalicoDetectionStatus


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCalicoDetectUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CalicoDetectUseCase:
    """Orchestrates Calico detection — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁCalicoDetectUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoDetectUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoDetectUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCalicoDetectUseCaseǁexecute__mutmut)
    def execute(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_orig(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_1(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = None
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_2(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = None
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_3(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=None,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_4(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=None,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_5(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=None,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_6(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=None,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_7(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=None,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_8(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=None,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_9(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=None,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_10(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=None,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_11(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=None,
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_12(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=None,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_13(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=None,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_14(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=None,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_15(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=None,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_16(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=None,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_17(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_18(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_19(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_20(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_21(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_22(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_23(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_24(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_25(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_26(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_27(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_28(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_29(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            error=result.error,
        )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_30(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(result.agents),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            )

    def xǁCalicoDetectUseCaseǁexecute__mutmut_31(self, command: CalicoDetectCommand) -> CalicoDetectResponse:
        result = self._port.detect()
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return CalicoDetectResponse(
            installed=result.installed,
            status=status,
            not_installed_marker=result.not_installed_marker,
            version=result.version,
            mode=result.mode,
            namespace=result.namespace,
            tigera_operator=result.tigera_operator,
            enterprise=result.enterprise,
            agents=list(None),
            total_nodes=result.total_nodes,
            ready_agents=result.ready_agents,
            degraded_agents=result.degraded_agents,
            degraded_summary=result.degraded_summary,
            error=result.error,
        )

mutants_xǁCalicoDetectUseCaseǁ__init____mutmut['_mutmut_orig'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁ__init____mutmut['xǁCalicoDetectUseCaseǁ__init____mutmut_1'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['_mutmut_orig'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_1'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_2'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_3'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_4'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_5'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_6'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_7'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_8'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_9'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_10'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_11'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_12'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_13'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_14'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_15'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_16'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_17'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_18'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_19'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_20'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_21'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_22'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_23'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_24'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_25'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_26'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_27'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_28'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_29'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_30'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCalicoDetectUseCaseǁexecute__mutmut['xǁCalicoDetectUseCaseǁexecute__mutmut_31'] = CalicoDetectUseCase.xǁCalicoDetectUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
