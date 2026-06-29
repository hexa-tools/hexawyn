from __future__ import annotations

from hexawyn.application.ports.driving.list_task_runs.list_task_runs_command import (
    ListTaskRunsCommand,
)
from hexawyn.application.ports.driving.list_task_runs.list_task_runs_response import (
    ListTaskRunsResponse,
)
from hexawyn.application.ports.driving.list_task_runs.list_task_runs_service_port import (
    ListTaskRunsServicePort,
)


class ListTaskRunsUseCase:
    """Entry point — depends on the service port abstraction."""

    def __init__(self, service: ListTaskRunsServicePort) -> None:
        self._service = service

    def execute(self, command: ListTaskRunsCommand) -> ListTaskRunsResponse:
        return self._service.list_task_runs(command)
