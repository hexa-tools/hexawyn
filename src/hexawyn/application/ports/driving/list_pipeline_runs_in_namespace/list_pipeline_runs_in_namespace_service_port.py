from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.command import (  # noqa: E501
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.response import (  # noqa: E501
    ListPipelineRunsInNamespaceResponse,
)


class ListPipelineRunsInNamespaceServicePort(ABC):
    @abstractmethod
    def list_pipeline_runs_in_namespace(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse: ...
