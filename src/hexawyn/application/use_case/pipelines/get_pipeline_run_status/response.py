from dataclasses import dataclass

from hexawyn.domain.models.pipeline import PipelineRunStatusReport


@dataclass
class GetPipelineRunStatusResponse:
    report: PipelineRunStatusReport | None = None
