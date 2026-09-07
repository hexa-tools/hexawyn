from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.list_pods.command import ListPodsCommand
from hexawyn.application.use_case.workloads.list_pods.response import ListPodsResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ListPodsServicePort(ABC):
    @abstractmethod
    def list_pods(self, command: ListPodsCommand) -> ListPodsResponse: ...
