"""ListCalicoNetworkPoliciesUseCase — lists Calico namespaced + global policies."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.list_calico_network_policies.command import (
    ListCalicoNetworkPoliciesCommand,
)
from hexawyn.application.use_case.calico.list_calico_network_policies.response import (
    ListCalicoNetworkPoliciesResponse,
)

_KIND_GLOBAL = "GlobalNetworkPolicy"
_KIND_NAMESPACED = "CalicoNetworkPolicy"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListCalicoNetworkPoliciesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListCalicoNetworkPoliciesUseCase:
    """Orchestrates Calico policy listing — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁListCalicoNetworkPoliciesUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁListCalicoNetworkPoliciesUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁListCalicoNetworkPoliciesUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut)
    def execute(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_orig(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_1(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = None
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_2(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_3(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=None,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_4(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=None,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_5(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=None,
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_6(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=None,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_7(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=None,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_8(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=None,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_9(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=None,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_10(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_11(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_12(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_13(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_14(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_15(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_16(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_17(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=True,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_18(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=1,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_19(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=1,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_20(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=1,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_21(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = None
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_22(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(None)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_23(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = None
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_24(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(None)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_25(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(2 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_26(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind != _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_27(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = None
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_28(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(None)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_29(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(2 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_30(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind != _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_31(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=None,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_32(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=None,
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_33(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=None,
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_34(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=None,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_35(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=None,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_36(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_37(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_38(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_39(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_40(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_41(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_42(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_43(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=False,
            not_installed_marker=None,
            policies=list(policies),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

    def xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_44(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse:
        detection = self._port.detect()
        if not detection.installed:
            return ListCalicoNetworkPoliciesResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                policies=[],
                total=0,
                global_count=0,
                namespaced_count=0,
                error=detection.error,
            )
        policies = self._port.list_network_policies(command.namespace)
        global_count = sum(1 for policy in policies if policy.kind == _KIND_GLOBAL)
        namespaced_count = sum(1 for policy in policies if policy.kind == _KIND_NAMESPACED)
        return ListCalicoNetworkPoliciesResponse(
            installed=True,
            not_installed_marker=None,
            policies=list(None),
            total=len(policies),
            global_count=global_count,
            namespaced_count=namespaced_count,
            error=None,
        )

mutants_xǁListCalicoNetworkPoliciesUseCaseǁ__init____mutmut['_mutmut_orig'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁ__init____mutmut['xǁListCalicoNetworkPoliciesUseCaseǁ__init____mutmut_1'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['_mutmut_orig'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_1'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_2'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_3'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_4'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_5'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_6'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_7'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_8'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_9'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_10'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_11'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_12'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_13'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_14'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_15'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_16'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_17'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_18'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_19'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_20'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_21'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_22'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_23'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_24'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_25'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_26'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_27'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_28'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_29'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_30'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_31'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_32'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_33'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_34'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_35'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_36'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_37'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_38'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_39'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_40'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_41'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_42'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_43'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut['xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_44'] = ListCalicoNetworkPoliciesUseCase.xǁListCalicoNetworkPoliciesUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
