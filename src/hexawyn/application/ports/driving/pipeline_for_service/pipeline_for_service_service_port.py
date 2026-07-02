from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_command import (
    PipelineForServiceCommand,
)
from hexawyn.application.ports.driving.pipeline_for_service.pipeline_for_service_response import (
    PipelineForServiceResponse,
)


class PipelineForServiceServicePort(ABC):
    @abstractmethod
    def find(self, command: PipelineForServiceCommand) -> PipelineForServiceResponse: ...
