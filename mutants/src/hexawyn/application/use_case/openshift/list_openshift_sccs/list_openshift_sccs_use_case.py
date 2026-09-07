# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.use_case.openshift.list_openshift_sccs.command import (
    ListOpenshiftSccsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_sccs.response import (
    ListOpenshiftSccsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListOpenshiftSccsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListOpenshiftSccsUseCase:
    @_mutmut_mutated(mutants_xǁListOpenshiftSccsUseCaseǁ__init____mutmut)
    def __init__(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁListOpenshiftSccsUseCaseǁ__init____mutmut_orig(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁListOpenshiftSccsUseCaseǁ__init____mutmut_1(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = None

    @_mutmut_mutated(mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut)
    def execute(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(exc))

    def xǁListOpenshiftSccsUseCaseǁexecute__mutmut_orig(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(exc))

    def xǁListOpenshiftSccsUseCaseǁexecute__mutmut_1(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = None
            return ListOpenshiftSccsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(exc))

    def xǁListOpenshiftSccsUseCaseǁexecute__mutmut_2(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                items=None,
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(exc))

    def xǁListOpenshiftSccsUseCaseǁexecute__mutmut_3(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                items=[dict(i) for i in items],
                count=None,
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(exc))

    def xǁListOpenshiftSccsUseCaseǁexecute__mutmut_4(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(exc))

    def xǁListOpenshiftSccsUseCaseǁexecute__mutmut_5(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                items=[dict(i) for i in items],
                )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(exc))

    def xǁListOpenshiftSccsUseCaseǁexecute__mutmut_6(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                items=[dict(None) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(exc))

    def xǁListOpenshiftSccsUseCaseǁexecute__mutmut_7(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=None)

    def xǁListOpenshiftSccsUseCaseǁexecute__mutmut_8(self, command: ListOpenshiftSccsCommand) -> ListOpenshiftSccsResponse:
        try:
            items = self._port.list_security_context_constraints()
            return ListOpenshiftSccsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftSccsResponse(error=str(None))

mutants_xǁListOpenshiftSccsUseCaseǁ__init____mutmut['_mutmut_orig'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListOpenshiftSccsUseCaseǁ__init____mutmut['xǁListOpenshiftSccsUseCaseǁ__init____mutmut_1'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut['_mutmut_orig'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut['xǁListOpenshiftSccsUseCaseǁexecute__mutmut_1'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut['xǁListOpenshiftSccsUseCaseǁexecute__mutmut_2'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut['xǁListOpenshiftSccsUseCaseǁexecute__mutmut_3'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut['xǁListOpenshiftSccsUseCaseǁexecute__mutmut_4'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut['xǁListOpenshiftSccsUseCaseǁexecute__mutmut_5'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut['xǁListOpenshiftSccsUseCaseǁexecute__mutmut_6'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut['xǁListOpenshiftSccsUseCaseǁexecute__mutmut_7'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListOpenshiftSccsUseCaseǁexecute__mutmut['xǁListOpenshiftSccsUseCaseǁexecute__mutmut_8'] = ListOpenshiftSccsUseCase.xǁListOpenshiftSccsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
