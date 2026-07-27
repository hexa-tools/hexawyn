from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.list_pods.command import ListPodsCommand
from hexawyn.application.use_case.workloads.list_pods.response import ListPodsResponse


class ListPodsServicePort(ABC):
    @abstractmethod
    def list_pods(self, command: ListPodsCommand) -> ListPodsResponse: ...
