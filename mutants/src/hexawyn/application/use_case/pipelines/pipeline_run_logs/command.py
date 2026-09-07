from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class PipelineRunLogsCommand:
    pipeline_run_name: str
    namespace: str
    task_name: str | None = None
