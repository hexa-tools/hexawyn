from dataclasses import dataclass

from hexawyn.domain.models.pipeline import PipelineRunStatusReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GetPipelineRunStatusResponse:
    report: PipelineRunStatusReport | None = None
