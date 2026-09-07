from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.pipeline_for_service.command import (
    PipelineForServiceCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_for_service.response import (
    PipelineForServiceResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PipelineForServiceServicePort(ABC):
    @abstractmethod
    def find(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse: ...
