from abc import ABC, abstractmethod

from hexawyn.domain.models.pipeline_for_service import PipelineForServiceRequest, ServicePipeline


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PipelineForServicePort(ABC):
    @abstractmethod
    def find_pipelines(self, request: PipelineForServiceRequest) -> list[ServicePipeline]: ...
