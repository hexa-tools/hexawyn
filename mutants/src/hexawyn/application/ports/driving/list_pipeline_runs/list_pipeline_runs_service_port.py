from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.list_pipeline_runs.command import (  # noqa: E501
    ListPipelineRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (  # noqa: E501
    ListPipelineRunsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ListPipelineRunsServicePort(ABC):
    @abstractmethod
    def list_pipeline_runs(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse: ...
