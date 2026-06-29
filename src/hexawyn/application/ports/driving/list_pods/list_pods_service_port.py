from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.list_pods.list_pods_command import ListPodsCommand
from hexawyn.application.ports.driving.list_pods.list_pods_response import ListPodsResponse


class ListPodsServicePort(ABC):
    @abstractmethod
    def list_pods(self, command: ListPodsCommand) -> ListPodsResponse: ...
