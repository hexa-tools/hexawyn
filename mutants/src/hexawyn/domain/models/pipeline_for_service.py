from __future__ import annotations

from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ServicePipeline:
    pipeline_name: str
    namespace: str
    repo_url: str
    branch: str
    trigger: str
    last_run_status: str
    last_run_timestamp: str


@dataclass(frozen=True)
class PipelineForServiceRequest:
    service_name: str


@dataclass(frozen=True)
class PipelineForServiceResult:
    service_name: str
    pipelines_found: int
    pipelines: list[ServicePipeline]

    @staticmethod
    def compute(
        request: PipelineForServiceRequest,
        pipelines: list[ServicePipeline],
    ) -> PipelineForServiceResult:
        return PipelineForServiceResult(
            service_name=request.service_name,
            pipelines_found=len(pipelines),
            pipelines=pipelines,
        )
