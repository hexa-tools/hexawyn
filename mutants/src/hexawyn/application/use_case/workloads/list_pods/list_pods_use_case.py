from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.workloads.list_pods.command import ListPodsCommand
from hexawyn.application.use_case.workloads.list_pods.response import ListPodsResponse
from hexawyn.application.use_case.workloads.list_pods.sort_pods import sort_pods_unsafe_first


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁListPodsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁListPodsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ListPodsUseCase:
    """Lists pods in a namespace, sorted unhealthy first."""

    @_mutmut_mutated(mutants_xǁListPodsUseCaseǁ__init____mutmut)
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def xǁListPodsUseCaseǁ__init____mutmut_orig(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def xǁListPodsUseCaseǁ__init____mutmut_1(self, k8s_port: K8sPort) -> None:
        self._k8s = None

    @_mutmut_mutated(mutants_xǁListPodsUseCaseǁexecute__mutmut)
    def execute(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        sorted_pods = sort_pods_unsafe_first(pods)
        return ListPodsResponse(pods=sorted_pods)

    def xǁListPodsUseCaseǁexecute__mutmut_orig(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        sorted_pods = sort_pods_unsafe_first(pods)
        return ListPodsResponse(pods=sorted_pods)

    def xǁListPodsUseCaseǁexecute__mutmut_1(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = None
        sorted_pods = sort_pods_unsafe_first(pods)
        return ListPodsResponse(pods=sorted_pods)

    def xǁListPodsUseCaseǁexecute__mutmut_2(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = self._k8s.list_pods(namespace=None)
        sorted_pods = sort_pods_unsafe_first(pods)
        return ListPodsResponse(pods=sorted_pods)

    def xǁListPodsUseCaseǁexecute__mutmut_3(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        sorted_pods = None
        return ListPodsResponse(pods=sorted_pods)

    def xǁListPodsUseCaseǁexecute__mutmut_4(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        sorted_pods = sort_pods_unsafe_first(None)
        return ListPodsResponse(pods=sorted_pods)

    def xǁListPodsUseCaseǁexecute__mutmut_5(self, command: ListPodsCommand) -> ListPodsResponse:
        pods = self._k8s.list_pods(namespace=command.namespace)
        sorted_pods = sort_pods_unsafe_first(pods)
        return ListPodsResponse(pods=None)

mutants_xǁListPodsUseCaseǁ__init____mutmut['_mutmut_orig'] = ListPodsUseCase.xǁListPodsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁListPodsUseCaseǁ__init____mutmut['xǁListPodsUseCaseǁ__init____mutmut_1'] = ListPodsUseCase.xǁListPodsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁListPodsUseCaseǁexecute__mutmut['_mutmut_orig'] = ListPodsUseCase.xǁListPodsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁListPodsUseCaseǁexecute__mutmut['xǁListPodsUseCaseǁexecute__mutmut_1'] = ListPodsUseCase.xǁListPodsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁListPodsUseCaseǁexecute__mutmut['xǁListPodsUseCaseǁexecute__mutmut_2'] = ListPodsUseCase.xǁListPodsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁListPodsUseCaseǁexecute__mutmut['xǁListPodsUseCaseǁexecute__mutmut_3'] = ListPodsUseCase.xǁListPodsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁListPodsUseCaseǁexecute__mutmut['xǁListPodsUseCaseǁexecute__mutmut_4'] = ListPodsUseCase.xǁListPodsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁListPodsUseCaseǁexecute__mutmut['xǁListPodsUseCaseǁexecute__mutmut_5'] = ListPodsUseCase.xǁListPodsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
