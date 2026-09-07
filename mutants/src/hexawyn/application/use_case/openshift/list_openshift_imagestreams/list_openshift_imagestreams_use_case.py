# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.use_case.openshift.list_openshift_imagestreams.command import (  # noqa: E501
    ListOpenshiftImagestreamsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_imagestreams.response import (  # noqa: E501
    ListOpenshiftImagestreamsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListOpenshiftImagestreamsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListOpenshiftImagestreamsUseCase:
    @_mutmut_mutated(mutants_xǁListOpenshiftImagestreamsUseCaseǁ__init____mutmut)
    def __init__(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁListOpenshiftImagestreamsUseCaseǁ__init____mutmut_orig(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁListOpenshiftImagestreamsUseCaseǁ__init____mutmut_1(self, port: OpenShiftResourcePort) -> None:  # noqa: F821  # type: ignore
        self._port = None

    @_mutmut_mutated(mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut)
    def execute(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_orig(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_1(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = None
            return ListOpenshiftImagestreamsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_2(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=None)
            return ListOpenshiftImagestreamsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_3(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                items=None,
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_4(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                items=[dict(i) for i in items],
                count=None,
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_5(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_6(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                items=[dict(i) for i in items],
                )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_7(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                items=[dict(None) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(exc))

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_8(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=None)

    def xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_9(
        self, command: ListOpenshiftImagestreamsCommand
    ) -> ListOpenshiftImagestreamsResponse:
        try:
            items = self._port.list_image_streams(namespace=command.namespace)
            return ListOpenshiftImagestreamsResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListOpenshiftImagestreamsResponse(error=str(None))

mutants_xǁListOpenshiftImagestreamsUseCaseǁ__init____mutmut['_mutmut_orig'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁ__init____mutmut['xǁListOpenshiftImagestreamsUseCaseǁ__init____mutmut_1'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['_mutmut_orig'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_1'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_2'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_3'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_4'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_5'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_6'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_7'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_8'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut['xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_9'] = ListOpenshiftImagestreamsUseCase.xǁListOpenshiftImagestreamsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
