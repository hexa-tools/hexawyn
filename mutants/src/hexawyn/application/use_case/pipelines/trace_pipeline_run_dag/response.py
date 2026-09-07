from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class TracePipelineRunDagResponse:
    pipeline_run_name: str = ""
    namespace: str = ""
    dag: dict[str, object] = field(default_factory=dict)
    tasks: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
