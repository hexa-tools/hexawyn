from datetime import UTC, datetime

from hexawyn.application.ports.driven.tekton_port import NamespacedPipelineRunInfo

_STUCK_THRESHOLD_SECONDS = 3600
_STATUS_PRIORITY: dict[str, int] = {"Failed": 0, "Running": 1, "Succeeded": 2}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_sort_by_status_then_time__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_sort_by_status_then_time__mutmut)
def sort_by_status_then_time(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_orig(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_1(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = None
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_2(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        None,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_3(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=None,
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_4(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=None,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_5(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_6(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_7(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_8(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: None,
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_9(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] and "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_10(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["XXstart_timeXX"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_11(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["START_TIME"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_12(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "XXXX",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_13(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=False,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_14(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        None,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_15(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=None,
    )


def x_sort_by_status_then_time__mutmut_16(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 3),
    )


def x_sort_by_status_then_time__mutmut_17(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        )


def x_sort_by_status_then_time__mutmut_18(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: None,
    )


def x_sort_by_status_then_time__mutmut_19(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(None, 3),
    )


def x_sort_by_status_then_time__mutmut_20(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], None),
    )


def x_sort_by_status_then_time__mutmut_21(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(3),
    )


def x_sort_by_status_then_time__mutmut_22(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], ),
    )


def x_sort_by_status_then_time__mutmut_23(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["XXstatusXX"], 3),
    )


def x_sort_by_status_then_time__mutmut_24(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["STATUS"], 3),
    )


def x_sort_by_status_then_time__mutmut_25(
    runs: list[NamespacedPipelineRunInfo],
) -> list[NamespacedPipelineRunInfo]:
    by_time = sorted(
        runs,
        key=lambda r: r["start_time"] or "",
        reverse=True,
    )
    return sorted(
        by_time,
        key=lambda r: _STATUS_PRIORITY.get(r["status"], 4),
    )

mutants_x_sort_by_status_then_time__mutmut['_mutmut_orig'] = x_sort_by_status_then_time__mutmut_orig # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_1'] = x_sort_by_status_then_time__mutmut_1 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_2'] = x_sort_by_status_then_time__mutmut_2 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_3'] = x_sort_by_status_then_time__mutmut_3 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_4'] = x_sort_by_status_then_time__mutmut_4 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_5'] = x_sort_by_status_then_time__mutmut_5 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_6'] = x_sort_by_status_then_time__mutmut_6 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_7'] = x_sort_by_status_then_time__mutmut_7 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_8'] = x_sort_by_status_then_time__mutmut_8 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_9'] = x_sort_by_status_then_time__mutmut_9 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_10'] = x_sort_by_status_then_time__mutmut_10 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_11'] = x_sort_by_status_then_time__mutmut_11 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_12'] = x_sort_by_status_then_time__mutmut_12 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_13'] = x_sort_by_status_then_time__mutmut_13 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_14'] = x_sort_by_status_then_time__mutmut_14 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_15'] = x_sort_by_status_then_time__mutmut_15 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_16'] = x_sort_by_status_then_time__mutmut_16 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_17'] = x_sort_by_status_then_time__mutmut_17 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_18'] = x_sort_by_status_then_time__mutmut_18 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_19'] = x_sort_by_status_then_time__mutmut_19 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_20'] = x_sort_by_status_then_time__mutmut_20 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_21'] = x_sort_by_status_then_time__mutmut_21 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_22'] = x_sort_by_status_then_time__mutmut_22 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_23'] = x_sort_by_status_then_time__mutmut_23 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_24'] = x_sort_by_status_then_time__mutmut_24 # type: ignore # mutmut generated
mutants_x_sort_by_status_then_time__mutmut['x_sort_by_status_then_time__mutmut_25'] = x_sort_by_status_then_time__mutmut_25 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_stuck_runs__mutmut)
def find_stuck_runs(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_orig(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_1(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = None
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_2(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(None)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_3(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = None
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_4(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" and run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_5(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["XXstatusXX"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_6(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["STATUS"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_7(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] == "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_8(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "XXRunningXX" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_9(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_10(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "RUNNING" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_11(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["XXstart_timeXX"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_12(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["START_TIME"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_13(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is not None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_14(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            break
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_15(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = None
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_16(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=None)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_17(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                None,
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_18(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                None,
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_19(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_20(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_21(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["XXstart_timeXX"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_22(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["START_TIME"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_23(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "XX%Y-%m-%dT%H:%M:%SZXX",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_24(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%y-%m-%dt%h:%m:%sz",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_25(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%M-%DT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_26(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now + started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_27(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() >= _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_28(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(None)
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_29(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["XXnameXX"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_30(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["NAME"])
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_31(
    runs: list[NamespacedPipelineRunInfo],
) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run["status"] != "Running" or run["start_time"] is None:
            continue
        try:
            started = datetime.strptime(
                run["start_time"],
                "%Y-%m-%dT%H:%M:%SZ",
            ).replace(tzinfo=UTC)
            if (now - started).total_seconds() > _STUCK_THRESHOLD_SECONDS:
                stuck.append(run["name"])
        except ValueError:
            break
    return stuck

mutants_x_find_stuck_runs__mutmut['_mutmut_orig'] = x_find_stuck_runs__mutmut_orig # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_1'] = x_find_stuck_runs__mutmut_1 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_2'] = x_find_stuck_runs__mutmut_2 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_3'] = x_find_stuck_runs__mutmut_3 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_4'] = x_find_stuck_runs__mutmut_4 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_5'] = x_find_stuck_runs__mutmut_5 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_6'] = x_find_stuck_runs__mutmut_6 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_7'] = x_find_stuck_runs__mutmut_7 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_8'] = x_find_stuck_runs__mutmut_8 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_9'] = x_find_stuck_runs__mutmut_9 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_10'] = x_find_stuck_runs__mutmut_10 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_11'] = x_find_stuck_runs__mutmut_11 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_12'] = x_find_stuck_runs__mutmut_12 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_13'] = x_find_stuck_runs__mutmut_13 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_14'] = x_find_stuck_runs__mutmut_14 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_15'] = x_find_stuck_runs__mutmut_15 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_16'] = x_find_stuck_runs__mutmut_16 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_17'] = x_find_stuck_runs__mutmut_17 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_18'] = x_find_stuck_runs__mutmut_18 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_19'] = x_find_stuck_runs__mutmut_19 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_20'] = x_find_stuck_runs__mutmut_20 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_21'] = x_find_stuck_runs__mutmut_21 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_22'] = x_find_stuck_runs__mutmut_22 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_23'] = x_find_stuck_runs__mutmut_23 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_24'] = x_find_stuck_runs__mutmut_24 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_25'] = x_find_stuck_runs__mutmut_25 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_26'] = x_find_stuck_runs__mutmut_26 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_27'] = x_find_stuck_runs__mutmut_27 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_28'] = x_find_stuck_runs__mutmut_28 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_29'] = x_find_stuck_runs__mutmut_29 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_30'] = x_find_stuck_runs__mutmut_30 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_31'] = x_find_stuck_runs__mutmut_31 # type: ignore # mutmut generated
