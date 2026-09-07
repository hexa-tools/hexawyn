"""GetCalicoHostEndpointsUseCase — lists Calico HostEndpoints cluster-wide."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.get_calico_host_endpoints.command import (
    GetCalicoHostEndpointsCommand,
)
from hexawyn.application.use_case.calico.get_calico_host_endpoints.response import (
    GetCalicoHostEndpointsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGetCalicoHostEndpointsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class GetCalicoHostEndpointsUseCase:
    """Orchestrates Calico HostEndpoint listing — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁGetCalicoHostEndpointsUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁGetCalicoHostEndpointsUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁGetCalicoHostEndpointsUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut)
    def execute(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_orig(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_1(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = None
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_2(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_3(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=None,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_4(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=None,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_5(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=None,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_6(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=None,
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_7(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=None,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_8(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_9(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_10(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_11(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_12(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_13(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=True,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_14(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=1,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_15(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = None
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_16(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=None,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_17(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=None,
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_18(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=None,
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_19(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_20(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_21(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_22(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_23(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_24(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=False,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(endpoints),
            error=None,
        )

    def xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_25(self, command: GetCalicoHostEndpointsCommand) -> GetCalicoHostEndpointsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return GetCalicoHostEndpointsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                endpoints=[],
                error=detection.error,
            )
        endpoints = self._port.list_host_endpoints()
        return GetCalicoHostEndpointsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(endpoints),
            endpoints=list(None),
            error=None,
        )

mutants_xǁGetCalicoHostEndpointsUseCaseǁ__init____mutmut['_mutmut_orig'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁ__init____mutmut['xǁGetCalicoHostEndpointsUseCaseǁ__init____mutmut_1'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['_mutmut_orig'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_1'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_2'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_3'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_4'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_5'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_6'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_7'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_8'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_9'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_10'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_11'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_12'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_13'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_14'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_15'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_16'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_17'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_18'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_19'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_20'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_21'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_22'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_23'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_24'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut['xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_25'] = GetCalicoHostEndpointsUseCase.xǁGetCalicoHostEndpointsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
