from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.response import (
    AnalyzeFailedPipelineResponse,
)


class AnalyzeFailedPipelineServicePort(ABC):
    @abstractmethod
    def analyze(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse: ...
