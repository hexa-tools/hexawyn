from __future__ import annotations

from hexawyn.application.ports.driven.ingress_port import IngressPort
from hexawyn.application.use_case.ingress.list_ingresses.command import (
    ListIngressesCommand,
)
from hexawyn.application.use_case.ingress.list_ingresses.response import (
    ListIngressesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListIngressesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListIngressesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListIngressesUseCase:
    @_mutmut_mutated(mutants_xǁListIngressesUseCaseǁ__init____mutmut)
    def __init__(self, port: IngressPort) -> None:
        self._port = port
    def xǁListIngressesUseCaseǁ__init____mutmut_orig(self, port: IngressPort) -> None:
        self._port = port
    def xǁListIngressesUseCaseǁ__init____mutmut_1(self, port: IngressPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁListIngressesUseCaseǁexecute__mutmut)
    def execute(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_orig(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_1(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = None
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_2(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace and "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_3(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "XXdefaultXX"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_4(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "DEFAULT"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_5(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = None
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_6(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=None)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_7(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=None,
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_8(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=None,
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_9(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_10(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_11(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(None) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(exc))

    def xǁListIngressesUseCaseǁexecute__mutmut_12(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=None)

    def xǁListIngressesUseCaseǁexecute__mutmut_13(self, command: ListIngressesCommand) -> ListIngressesResponse:
        try:
            namespace = command.namespace or "default"
            items = self._port.list_ingresses(namespace=namespace)
            return ListIngressesResponse(
                items=[dict(i) for i in items],
                count=len(items),
            )
        except Exception as exc:
            return ListIngressesResponse(error=str(None))

mutants_xǁListIngressesUseCaseǁ__init____mutmut['_mutmut_orig'] = ListIngressesUseCase.xǁListIngressesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁ__init____mutmut['xǁListIngressesUseCaseǁ__init____mutmut_1'] = ListIngressesUseCase.xǁListIngressesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListIngressesUseCaseǁexecute__mutmut['_mutmut_orig'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_1'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_2'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_3'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_4'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_5'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_6'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_7'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_8'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_9'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_10'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_11'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_12'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁListIngressesUseCaseǁexecute__mutmut['xǁListIngressesUseCaseǁexecute__mutmut_13'] = ListIngressesUseCase.xǁListIngressesUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
