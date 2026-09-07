from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class PipelineRunStatusResponse:
    total_runs: int = 0
    runs: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
