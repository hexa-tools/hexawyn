from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.list_task_runs.list_task_runs_command import (
    ListTaskRunsCommand,
)
from hexawyn.application.ports.driving.list_task_runs.list_task_runs_response import (
    ListTaskRunsResponse,
)


class ListTaskRunsServicePort(ABC):
    @abstractmethod
    def list_task_runs(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse: ...
