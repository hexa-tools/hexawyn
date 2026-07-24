from abc import ABC, abstractmethod

from hexawyn.application.use_case.list_pipeline_runs.command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.use_case.list_pipeline_runs.response import (
    ListPipelineRunsResponse,
)


class ListPipelineRunsServicePort(ABC):
    @abstractmethod
    def list_pipeline_runs(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse: ...
