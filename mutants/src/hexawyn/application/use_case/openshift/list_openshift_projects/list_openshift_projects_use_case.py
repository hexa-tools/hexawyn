# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.use_case.openshift.list_openshift_projects.command import (
    ListOpenshiftProjectsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_projects.response import (
    ListOpenshiftProjectsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListOpenshiftProjectsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListOpenshiftProjectsUseCase:
    @_mutmut_mutated(mutants_xǁListOpenshiftProjectsUseCaseǁ__init____mutmut)
    def __init__(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁListOpenshiftProjectsUseCaseǁ__init____mutmut_orig(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁListOpenshiftProjectsUseCaseǁ__init____mutmut_1(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = None

    @_mutmut_mutated(mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut)
    def execute(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(exc))

    def xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_orig(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(exc))

    def xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_1(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = None
            return ListOpenshiftProjectsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(exc))

    def xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_2(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                items=None,
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(exc))

    def xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_3(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                items=[dict(i) for i in items],
                count=None,
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(exc))

    def xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_4(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(exc))

    def xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_5(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                items=[dict(i) for i in items],
                )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(exc))

    def xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_6(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                items=[dict(None) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(exc))

    def xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_7(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=None)

    def xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_8(self, command: ListOpenshiftProjectsCommand) -> ListOpenshiftProjectsResponse:
        try:
            items = self._port.list_projects()
            return ListOpenshiftProjectsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftProjectsResponse(error=str(None))

mutants_xǁListOpenshiftProjectsUseCaseǁ__init____mutmut['_mutmut_orig'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListOpenshiftProjectsUseCaseǁ__init____mutmut['xǁListOpenshiftProjectsUseCaseǁ__init____mutmut_1'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut['_mutmut_orig'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut['xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_1'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut['xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_2'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut['xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_3'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut['xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_4'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut['xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_5'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut['xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_6'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut['xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_7'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListOpenshiftProjectsUseCaseǁexecute__mutmut['xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_8'] = ListOpenshiftProjectsUseCase.xǁListOpenshiftProjectsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
