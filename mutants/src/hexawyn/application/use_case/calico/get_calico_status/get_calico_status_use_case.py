"""GetCalicoStatusUseCase — aggregated Calico datapath health & connectivity."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.get_calico_status.command import (
    GetCalicoStatusCommand,
)
from hexawyn.application.use_case.calico.get_calico_status.response import (
    GetCalicoStatusResponse,
)
from hexawyn.domain.models.calico import CalicoDetectionStatus
from hexawyn.domain.services.calico.get_calico_status_service import (
    build_calico_status_result,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetCalicoStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GetCalicoStatusUseCase:
    """Composes agent health, felix errors and the connectivity probe."""

    @_mutmut_mutated(mutants_xǁGetCalicoStatusUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁGetCalicoStatusUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁGetCalicoStatusUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut)
    def execute(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_orig(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_1(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = None
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_2(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = None
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_3(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = None
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_4(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = None
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_5(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=None, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_6(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=None, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_7(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=None
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_8(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_9(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_10(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_11(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = None
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_12(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=None,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_13(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=None,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_14(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=None,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_15(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=None,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_16(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=None,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_17(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=None,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_18(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=None,
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_19(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=None,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_20(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=None,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_21(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=None,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_22(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=None,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_23(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=None,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_24(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=None,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_25(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_26(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_27(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_28(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_29(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_30(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_31(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_32(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_33(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_34(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_35(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_36(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            error=result.error,
        )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_37(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(result.agents),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            )

    def xǁGetCalicoStatusUseCaseǁexecute__mutmut_38(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse:
        detection = self._port.status()
        connectivity = self._port.connectivity_health()
        felix = self._port.felix_metrics()
        result = build_calico_status_result(
            detection=detection, connectivity=connectivity, felix=felix
        )
        status = (
            result.status.value
            if isinstance(result.status, CalicoDetectionStatus)
            else result.status
        )
        return GetCalicoStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            status=status,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            degraded_summary=result.degraded_summary,
            agents=list(None),
            felix_errors_available=result.felix_errors_available,
            felix_errors=result.felix_errors,
            connectivity_available=result.connectivity_available,
            connectivity_status=result.connectivity_status,
            connectivity_detail=result.connectivity_detail,
            error=result.error,
        )

mutants_xǁGetCalicoStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁ__init____mutmut['xǁGetCalicoStatusUseCaseǁ__init____mutmut_1'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['_mutmut_orig'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_1'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_2'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_3'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_4'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_5'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_6'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_7'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_8'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_9'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_10'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_11'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_12'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_13'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_14'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_15'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_16'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_17'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_18'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_19'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_20'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_21'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_22'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_23'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_24'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_25'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_26'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_27'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_28'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_29'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_30'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_31'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_32'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_33'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_34'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_35'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_36'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_37'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGetCalicoStatusUseCaseǁexecute__mutmut['xǁGetCalicoStatusUseCaseǁexecute__mutmut_38'] = GetCalicoStatusUseCase.xǁGetCalicoStatusUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
