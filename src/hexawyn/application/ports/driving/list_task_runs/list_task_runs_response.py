from dataclasses import dataclass, field

from hexawyn.application.ports.driven.tekton_port import TaskRunInfo


@dataclass
class ListTaskRunsResponse:
    task_runs: list[TaskRunInfo] = field(default_factory=list)
