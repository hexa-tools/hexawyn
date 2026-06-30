from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_response import (
    ListPipelineRunsInNamespaceResponse,
)


class ListPipelineRunsInNamespaceServicePort(ABC):
    @abstractmethod
    def list_pipeline_runs_in_namespace(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse: ...
