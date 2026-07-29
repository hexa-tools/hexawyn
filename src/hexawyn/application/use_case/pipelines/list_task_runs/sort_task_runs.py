from hexawyn.application.ports.driven.tekton_port import TaskRunInfo


def sort_by_start_time_desc(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(task_runs, key=_start_time_sort_key, reverse=True)


def _start_time_sort_key(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["start_time"]
    if start_time is None:
        return (0, "")
    return (1, start_time)
