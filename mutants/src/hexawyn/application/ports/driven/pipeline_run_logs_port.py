from abc import ABC, abstractmethod

from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest, StepLog


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PipelineRunLogsPort(ABC):
    @abstractmethod
    def fetch_step_logs(self, request: PipelineRunLogsRequest) -> list[StepLog]: ...
