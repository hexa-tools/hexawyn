from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class GetPipelineRunStatusCommand:
    namespace: str = ""
    limit: int = 50
    hours_window: int = 24
