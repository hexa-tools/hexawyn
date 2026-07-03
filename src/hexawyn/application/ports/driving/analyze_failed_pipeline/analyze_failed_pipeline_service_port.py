from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_response import (
    AnalyzeFailedPipelineResponse,
)


class AnalyzeFailedPipelineServicePort(ABC):
    @abstractmethod
    def analyze(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse: ...
