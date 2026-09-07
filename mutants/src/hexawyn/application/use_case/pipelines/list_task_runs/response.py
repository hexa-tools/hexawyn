from dataclasses import dataclass, field

from hexawyn.application.ports.driven.tekton_port import TaskRunInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ListTaskRunsResponse:
    task_runs: list[TaskRunInfo] = field(default_factory=list)
