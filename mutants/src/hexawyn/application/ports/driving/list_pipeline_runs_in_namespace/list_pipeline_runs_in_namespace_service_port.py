from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.command import (  # noqa: E501
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.response import (  # noqa: E501
    ListPipelineRunsInNamespaceResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ListPipelineRunsInNamespaceServicePort(ABC):
    @abstractmethod
    def list_pipeline_runs_in_namespace(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse: ...
