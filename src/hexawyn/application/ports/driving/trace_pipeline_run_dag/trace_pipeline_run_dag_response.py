from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.pipeline_dag import PipelineDAG


@dataclass
class TracePipelineRunDAGResponse:
    dag: PipelineDAG
