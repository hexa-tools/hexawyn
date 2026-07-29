from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.list_task_runs.command import (
    ListTaskRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_task_runs.response import (
    ListTaskRunsResponse,
)


class ListTaskRunsServicePort(ABC):
    @abstractmethod
    def list_task_runs(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse: ...
