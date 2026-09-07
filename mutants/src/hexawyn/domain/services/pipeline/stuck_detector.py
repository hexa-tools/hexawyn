from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.domain.models.constants import STUCK_PIPELINE_RUN_THRESHOLD_SECONDS


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_find_stuck_runs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_stuck_runs__mutmut)
def find_stuck_runs(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_orig(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_1(runs: list[dict[str, object]]) -> list[str]:
    now = None
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_2(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(None)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_3(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = None
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_4(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" and run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_5(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get(None) != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_6(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("XXstatusXX") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_7(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("STATUS") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_8(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") == "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_9(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "XXRunningXX" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_10(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_11(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "RUNNING" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_12(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get(None) is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_13(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("XXstart_timeXX") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_14(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("START_TIME") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_15(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is not None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_16(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            break
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_17(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = None
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_18(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=None
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_19(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(None, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_20(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), None).replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_21(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime("%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_22(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), ).replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_23(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(None), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_24(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get(None)), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_25(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("XXstart_timeXX")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_26(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("START_TIME")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_27(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "XX%Y-%m-%dT%H:%M:%SZXX").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_28(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%y-%m-%dt%h:%m:%sz").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_29(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%M-%DT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_30(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now + started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_31(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() >= STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_32(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(None)
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_33(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(None))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_34(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get(None, "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_35(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", None)))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_36(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_37(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", )))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_38(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("XXnameXX", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_39(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("NAME", "")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_40(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "XXXX")))
        except ValueError:
            continue
    return stuck


def x_find_stuck_runs__mutmut_41(runs: list[dict[str, object]]) -> list[str]:
    now = datetime.now(UTC)
    stuck: list[str] = []
    for run in runs:
        if run.get("status") != "Running" or run.get("start_time") is None:
            continue
        try:
            started = datetime.strptime(str(run.get("start_time")), "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=UTC
            )
            if (now - started).total_seconds() > STUCK_PIPELINE_RUN_THRESHOLD_SECONDS:
                stuck.append(str(run.get("name", "")))
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
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_32'] = x_find_stuck_runs__mutmut_32 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_33'] = x_find_stuck_runs__mutmut_33 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_34'] = x_find_stuck_runs__mutmut_34 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_35'] = x_find_stuck_runs__mutmut_35 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_36'] = x_find_stuck_runs__mutmut_36 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_37'] = x_find_stuck_runs__mutmut_37 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_38'] = x_find_stuck_runs__mutmut_38 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_39'] = x_find_stuck_runs__mutmut_39 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_40'] = x_find_stuck_runs__mutmut_40 # type: ignore # mutmut generated
mutants_x_find_stuck_runs__mutmut['x_find_stuck_runs__mutmut_41'] = x_find_stuck_runs__mutmut_41 # type: ignore # mutmut generated
