"""ListCalicoIpPoolsUseCase — lists Calico IPPools cluster-wide."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.list_calico_ip_pools.command import (
    ListCalicoIpPoolsCommand,
)
from hexawyn.application.use_case.calico.list_calico_ip_pools.response import (
    ListCalicoIpPoolsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListCalicoIpPoolsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListCalicoIpPoolsUseCase:
    """Orchestrates Calico IPPool listing — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁListCalicoIpPoolsUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁListCalicoIpPoolsUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁListCalicoIpPoolsUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut)
    def execute(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_orig(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_1(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = None
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_2(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_3(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=None,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_4(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=None,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_5(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=None,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_6(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=None,
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_7(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=None,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_8(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_9(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_10(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_11(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_12(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_13(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=True,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_14(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=1,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_15(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = None
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_16(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=None,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_17(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=None,
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_18(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=None,
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_19(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_20(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_21(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_22(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_23(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_24(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=False,
            not_installed_marker=None,
            total=len(pools),
            pools=list(pools),
            error=None,
        )

    def xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_25(self, command: ListCalicoIpPoolsCommand) -> ListCalicoIpPoolsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoIpPoolsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                pools=[],
                error=detection.error,
            )
        pools = self._port.list_ip_pools()
        return ListCalicoIpPoolsResponse(
            installed=True,
            not_installed_marker=None,
            total=len(pools),
            pools=list(None),
            error=None,
        )

mutants_xǁListCalicoIpPoolsUseCaseǁ__init____mutmut['_mutmut_orig'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁ__init____mutmut['xǁListCalicoIpPoolsUseCaseǁ__init____mutmut_1'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['_mutmut_orig'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_1'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_2'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_3'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_4'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_5'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_6'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_7'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_8'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_9'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_10'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_11'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_12'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_13'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_14'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_15'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_16'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_17'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_18'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_19'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_20'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_21'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_22'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_23'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_24'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁListCalicoIpPoolsUseCaseǁexecute__mutmut['xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_25'] = ListCalicoIpPoolsUseCase.xǁListCalicoIpPoolsUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
