from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.list_pipeline_runs.command import (  # noqa: E501
    ListPipelineRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (  # noqa: E501
    ListPipelineRunsResponse,
)


class ListPipelineRunsServicePort(ABC):
    @abstractmethod
    def list_pipeline_runs(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse: ...
