# mypy: ignore-errors
from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.command import (  # noqa: E501  # type: ignore
    TracePipelineRunDAGCommand,
)
from hexawyn.application.use_case.pipelines.trace_pipeline_run_dag.response import (  # noqa: E501  # type: ignore
    TracePipelineRunDAGResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class TracePipelineRunDAGServicePort(ABC):
    @abstractmethod
    def trace_pipeline_run_dag(
        self, command: TracePipelineRunDAGCommand
    ) -> TracePipelineRunDAGResponse: ...
