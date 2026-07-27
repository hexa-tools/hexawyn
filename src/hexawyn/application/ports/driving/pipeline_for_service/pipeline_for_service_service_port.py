from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.pipeline_for_service.command import (
    PipelineForServiceCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_for_service.response import (
    PipelineForServiceResponse,
)


class PipelineForServiceServicePort(ABC):
    @abstractmethod
    def find(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse: ...
