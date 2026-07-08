from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_response import (
    ListPipelineRunsResponse,
)


class ListPipelineRunsServicePort(ABC):
    @abstractmethod
    def list_pipeline_runs(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse: ...
