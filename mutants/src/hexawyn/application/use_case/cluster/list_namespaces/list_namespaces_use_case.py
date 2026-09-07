from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.cluster.list_namespaces.command import (
    ListNamespacesCommand,
)
from hexawyn.application.use_case.cluster.list_namespaces.response import (
    ListNamespacesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListNamespacesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListNamespacesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListNamespacesUseCase:
    """Lists all namespaces and their age from the K8s API."""

    @_mutmut_mutated(mutants_xǁListNamespacesUseCaseǁ__init____mutmut)
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def xǁListNamespacesUseCaseǁ__init____mutmut_orig(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def xǁListNamespacesUseCaseǁ__init____mutmut_1(self, k8s_port: K8sPort) -> None:
        self._k8s = None

    @_mutmut_mutated(mutants_xǁListNamespacesUseCaseǁexecute__mutmut)
    def execute(self, command: ListNamespacesCommand) -> ListNamespacesResponse:
        namespaces = self._k8s.list_namespaces()
        return ListNamespacesResponse(namespaces=namespaces)

    def xǁListNamespacesUseCaseǁexecute__mutmut_orig(self, command: ListNamespacesCommand) -> ListNamespacesResponse:
        namespaces = self._k8s.list_namespaces()
        return ListNamespacesResponse(namespaces=namespaces)

    def xǁListNamespacesUseCaseǁexecute__mutmut_1(self, command: ListNamespacesCommand) -> ListNamespacesResponse:
        namespaces = None
        return ListNamespacesResponse(namespaces=namespaces)

    def xǁListNamespacesUseCaseǁexecute__mutmut_2(self, command: ListNamespacesCommand) -> ListNamespacesResponse:
        namespaces = self._k8s.list_namespaces()
        return ListNamespacesResponse(namespaces=None)

mutants_xǁListNamespacesUseCaseǁ__init____mutmut['_mutmut_orig'] = ListNamespacesUseCase.xǁListNamespacesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListNamespacesUseCaseǁ__init____mutmut['xǁListNamespacesUseCaseǁ__init____mutmut_1'] = ListNamespacesUseCase.xǁListNamespacesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListNamespacesUseCaseǁexecute__mutmut['_mutmut_orig'] = ListNamespacesUseCase.xǁListNamespacesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListNamespacesUseCaseǁexecute__mutmut['xǁListNamespacesUseCaseǁexecute__mutmut_1'] = ListNamespacesUseCase.xǁListNamespacesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListNamespacesUseCaseǁexecute__mutmut['xǁListNamespacesUseCaseǁexecute__mutmut_2'] = ListNamespacesUseCase.xǁListNamespacesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
