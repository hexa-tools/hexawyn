# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.use_case.openshift.list_openshift_routes.command import (
    ListOpenshiftRoutesCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_routes.response import (
    ListOpenshiftRoutesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListOpenshiftRoutesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListOpenshiftRoutesUseCase:
    @_mutmut_mutated(mutants_xǁListOpenshiftRoutesUseCaseǁ__init____mutmut)
    def __init__(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁListOpenshiftRoutesUseCaseǁ__init____mutmut_orig(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁListOpenshiftRoutesUseCaseǁ__init____mutmut_1(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = None

    @_mutmut_mutated(mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut)
    def execute(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_orig(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_1(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = None
            return ListOpenshiftRoutesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_2(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=None)
            return ListOpenshiftRoutesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_3(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                items=None,
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_4(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                items=[dict(i) for i in items],
                count=None,
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_5(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_6(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                items=[dict(i) for i in items],
                )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_7(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                items=[dict(None) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(exc))

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_8(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=None)

    def xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_9(self, command: ListOpenshiftRoutesCommand) -> ListOpenshiftRoutesResponse:
        try:
            items = self._port.list_routes(namespace=command.namespace)
            return ListOpenshiftRoutesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftRoutesResponse(error=str(None))

mutants_xǁListOpenshiftRoutesUseCaseǁ__init____mutmut['_mutmut_orig'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁ__init____mutmut['xǁListOpenshiftRoutesUseCaseǁ__init____mutmut_1'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['_mutmut_orig'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_1'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_2'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_3'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_4'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_5'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_6'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_7'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_8'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListOpenshiftRoutesUseCaseǁexecute__mutmut['xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_9'] = ListOpenshiftRoutesUseCase.xǁListOpenshiftRoutesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
