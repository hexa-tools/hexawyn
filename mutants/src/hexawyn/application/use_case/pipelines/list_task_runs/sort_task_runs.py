from hexawyn.application.ports.driven.tekton_port import TaskRunInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_sort_by_start_time_desc__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_sort_by_start_time_desc__mutmut)
def sort_by_start_time_desc(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(task_runs, key=_start_time_sort_key, reverse=True)


def x_sort_by_start_time_desc__mutmut_orig(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(task_runs, key=_start_time_sort_key, reverse=True)


def x_sort_by_start_time_desc__mutmut_1(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(None, key=_start_time_sort_key, reverse=True)


def x_sort_by_start_time_desc__mutmut_2(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(task_runs, key=None, reverse=True)


def x_sort_by_start_time_desc__mutmut_3(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(task_runs, key=_start_time_sort_key, reverse=None)


def x_sort_by_start_time_desc__mutmut_4(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(key=_start_time_sort_key, reverse=True)


def x_sort_by_start_time_desc__mutmut_5(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(task_runs, reverse=True)


def x_sort_by_start_time_desc__mutmut_6(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(task_runs, key=_start_time_sort_key, )


def x_sort_by_start_time_desc__mutmut_7(task_runs: list[TaskRunInfo]) -> list[TaskRunInfo]:
    return sorted(task_runs, key=_start_time_sort_key, reverse=False)

mutants_x_sort_by_start_time_desc__mutmut['_mutmut_orig'] = x_sort_by_start_time_desc__mutmut_orig # type: ignore # mutmut generated
mutants_x_sort_by_start_time_desc__mutmut['x_sort_by_start_time_desc__mutmut_1'] = x_sort_by_start_time_desc__mutmut_1 # type: ignore # mutmut generated
mutants_x_sort_by_start_time_desc__mutmut['x_sort_by_start_time_desc__mutmut_2'] = x_sort_by_start_time_desc__mutmut_2 # type: ignore # mutmut generated
mutants_x_sort_by_start_time_desc__mutmut['x_sort_by_start_time_desc__mutmut_3'] = x_sort_by_start_time_desc__mutmut_3 # type: ignore # mutmut generated
mutants_x_sort_by_start_time_desc__mutmut['x_sort_by_start_time_desc__mutmut_4'] = x_sort_by_start_time_desc__mutmut_4 # type: ignore # mutmut generated
mutants_x_sort_by_start_time_desc__mutmut['x_sort_by_start_time_desc__mutmut_5'] = x_sort_by_start_time_desc__mutmut_5 # type: ignore # mutmut generated
mutants_x_sort_by_start_time_desc__mutmut['x_sort_by_start_time_desc__mutmut_6'] = x_sort_by_start_time_desc__mutmut_6 # type: ignore # mutmut generated
mutants_x_sort_by_start_time_desc__mutmut['x_sort_by_start_time_desc__mutmut_7'] = x_sort_by_start_time_desc__mutmut_7 # type: ignore # mutmut generated
mutants_x__start_time_sort_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__start_time_sort_key__mutmut)
def _start_time_sort_key(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["start_time"]
    if start_time is None:
        return (0, "")
    return (1, start_time)


def x__start_time_sort_key__mutmut_orig(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["start_time"]
    if start_time is None:
        return (0, "")
    return (1, start_time)


def x__start_time_sort_key__mutmut_1(run: TaskRunInfo) -> tuple[int, str]:
    start_time = None
    if start_time is None:
        return (0, "")
    return (1, start_time)


def x__start_time_sort_key__mutmut_2(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["XXstart_timeXX"]
    if start_time is None:
        return (0, "")
    return (1, start_time)


def x__start_time_sort_key__mutmut_3(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["START_TIME"]
    if start_time is None:
        return (0, "")
    return (1, start_time)


def x__start_time_sort_key__mutmut_4(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["start_time"]
    if start_time is not None:
        return (0, "")
    return (1, start_time)


def x__start_time_sort_key__mutmut_5(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["start_time"]
    if start_time is None:
        return (1, "")
    return (1, start_time)


def x__start_time_sort_key__mutmut_6(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["start_time"]
    if start_time is None:
        return (0, "XXXX")
    return (1, start_time)


def x__start_time_sort_key__mutmut_7(run: TaskRunInfo) -> tuple[int, str]:
    start_time = run["start_time"]
    if start_time is None:
        return (0, "")
    return (2, start_time)

mutants_x__start_time_sort_key__mutmut['_mutmut_orig'] = x__start_time_sort_key__mutmut_orig # type: ignore # mutmut generated
mutants_x__start_time_sort_key__mutmut['x__start_time_sort_key__mutmut_1'] = x__start_time_sort_key__mutmut_1 # type: ignore # mutmut generated
mutants_x__start_time_sort_key__mutmut['x__start_time_sort_key__mutmut_2'] = x__start_time_sort_key__mutmut_2 # type: ignore # mutmut generated
mutants_x__start_time_sort_key__mutmut['x__start_time_sort_key__mutmut_3'] = x__start_time_sort_key__mutmut_3 # type: ignore # mutmut generated
mutants_x__start_time_sort_key__mutmut['x__start_time_sort_key__mutmut_4'] = x__start_time_sort_key__mutmut_4 # type: ignore # mutmut generated
mutants_x__start_time_sort_key__mutmut['x__start_time_sort_key__mutmut_5'] = x__start_time_sort_key__mutmut_5 # type: ignore # mutmut generated
mutants_x__start_time_sort_key__mutmut['x__start_time_sort_key__mutmut_6'] = x__start_time_sort_key__mutmut_6 # type: ignore # mutmut generated
mutants_x__start_time_sort_key__mutmut['x__start_time_sort_key__mutmut_7'] = x__start_time_sort_key__mutmut_7 # type: ignore # mutmut generated
