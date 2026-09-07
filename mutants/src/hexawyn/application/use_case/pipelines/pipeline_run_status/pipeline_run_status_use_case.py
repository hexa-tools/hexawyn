# mypy: ignore-errors
from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.tekton_pipeline_status_port import (
    PipelineRunRecord,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)
from hexawyn.domain.models.pipeline import PipelineRunStatusReport, PipelineRunSummary


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__filter_by_window__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__filter_by_window__mutmut)
def _filter_by_window(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_orig(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_1(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = None
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_2(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) + timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_3(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(None) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_4(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=None)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_5(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = None
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_6(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["XXstart_timeXX"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_7(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["START_TIME"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_8(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is not None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_9(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(None)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_10(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            break
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_11(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = None
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_12(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(None)
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_13(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace(None, "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_14(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", None))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_15(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_16(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", ))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_17(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["XXstart_timeXX"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_18(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["START_TIME"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_19(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("XXZXX", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_20(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_21(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "XX+00:00XX"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_22(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started > cutoff:
                result.append(run)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_23(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(None)
        except ValueError:
            continue
    return result


def x__filter_by_window__mutmut_24(runs: list[PipelineRunRecord], hours: int) -> list[PipelineRunRecord]:
    cutoff = datetime.now(UTC) - timedelta(hours=hours)
    result: list[PipelineRunRecord] = []
    for run in runs:
        if run["start_time"] is None:
            result.append(run)
            continue
        try:
            started = datetime.fromisoformat(run["start_time"].replace("Z", "+00:00"))
            if started >= cutoff:
                result.append(run)
        except ValueError:
            break
    return result

mutants_x__filter_by_window__mutmut['_mutmut_orig'] = x__filter_by_window__mutmut_orig # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_1'] = x__filter_by_window__mutmut_1 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_2'] = x__filter_by_window__mutmut_2 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_3'] = x__filter_by_window__mutmut_3 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_4'] = x__filter_by_window__mutmut_4 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_5'] = x__filter_by_window__mutmut_5 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_6'] = x__filter_by_window__mutmut_6 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_7'] = x__filter_by_window__mutmut_7 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_8'] = x__filter_by_window__mutmut_8 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_9'] = x__filter_by_window__mutmut_9 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_10'] = x__filter_by_window__mutmut_10 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_11'] = x__filter_by_window__mutmut_11 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_12'] = x__filter_by_window__mutmut_12 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_13'] = x__filter_by_window__mutmut_13 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_14'] = x__filter_by_window__mutmut_14 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_15'] = x__filter_by_window__mutmut_15 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_16'] = x__filter_by_window__mutmut_16 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_17'] = x__filter_by_window__mutmut_17 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_18'] = x__filter_by_window__mutmut_18 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_19'] = x__filter_by_window__mutmut_19 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_20'] = x__filter_by_window__mutmut_20 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_21'] = x__filter_by_window__mutmut_21 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_22'] = x__filter_by_window__mutmut_22 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_23'] = x__filter_by_window__mutmut_23 # type: ignore # mutmut generated
mutants_x__filter_by_window__mutmut['x__filter_by_window__mutmut_24'] = x__filter_by_window__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_summary__mutmut)
def _to_summary(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_orig(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_1(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=None,
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_2(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=None,
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_3(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=None,
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_4(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=None,
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_5(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=None,
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_6(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=None,
    )


def x__to_summary__mutmut_7(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_8(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_9(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_10(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_11(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_12(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        )


def x__to_summary__mutmut_13(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["XXnameXX"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_14(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["NAME"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_15(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["XXstatusXX"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_16(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["STATUS"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_17(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["XXstart_timeXX"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_18(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["START_TIME"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_19(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["XXduration_secondsXX"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_20(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["DURATION_SECONDS"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_21(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["XXfailure_reasonXX"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_22(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["FAILURE_REASON"],
        pipeline_ref=run["pipeline_ref"],
    )


def x__to_summary__mutmut_23(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["XXpipeline_refXX"],
    )


def x__to_summary__mutmut_24(run: PipelineRunRecord) -> PipelineRunSummary:
    return PipelineRunSummary(
        name=run["name"],
        status=run["status"],
        start_time=run["start_time"],
        duration_seconds=run["duration_seconds"],
        failure_reason=run["failure_reason"],
        pipeline_ref=run["PIPELINE_REF"],
    )

mutants_x__to_summary__mutmut['_mutmut_orig'] = x__to_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_1'] = x__to_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_2'] = x__to_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_3'] = x__to_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_4'] = x__to_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_5'] = x__to_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_6'] = x__to_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_7'] = x__to_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_8'] = x__to_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_9'] = x__to_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_10'] = x__to_summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_11'] = x__to_summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_12'] = x__to_summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_13'] = x__to_summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_14'] = x__to_summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_15'] = x__to_summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_16'] = x__to_summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_17'] = x__to_summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_18'] = x__to_summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_19'] = x__to_summary__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_20'] = x__to_summary__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_21'] = x__to_summary__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_22'] = x__to_summary__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_23'] = x__to_summary__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_24'] = x__to_summary__mutmut_24 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__find_most_recent_failed__mutmut)
def _find_most_recent_failed(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_orig(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_1(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = None
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_2(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["XXstatusXX"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_3(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["STATUS"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_4(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] != "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_5(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "XXFailedXX"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_6(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_7(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "FAILED"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_8(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_9(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = None
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_10(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(None, key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_11(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=None)
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_12(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(key=lambda r: r["start_time"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_13(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, )
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_14(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: None)
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_15(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] and "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_16(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["XXstart_timeXX"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_17(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["START_TIME"] or "")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_18(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "XXXX")
    return _to_summary(most_recent)


def x__find_most_recent_failed__mutmut_19(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    failed = [r for r in runs if r["status"] == "Failed"]
    if not failed:
        return None
    most_recent = max(failed, key=lambda r: r["start_time"] or "")
    return _to_summary(None)

mutants_x__find_most_recent_failed__mutmut['_mutmut_orig'] = x__find_most_recent_failed__mutmut_orig # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_1'] = x__find_most_recent_failed__mutmut_1 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_2'] = x__find_most_recent_failed__mutmut_2 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_3'] = x__find_most_recent_failed__mutmut_3 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_4'] = x__find_most_recent_failed__mutmut_4 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_5'] = x__find_most_recent_failed__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_6'] = x__find_most_recent_failed__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_7'] = x__find_most_recent_failed__mutmut_7 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_8'] = x__find_most_recent_failed__mutmut_8 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_9'] = x__find_most_recent_failed__mutmut_9 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_10'] = x__find_most_recent_failed__mutmut_10 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_11'] = x__find_most_recent_failed__mutmut_11 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_12'] = x__find_most_recent_failed__mutmut_12 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_13'] = x__find_most_recent_failed__mutmut_13 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_14'] = x__find_most_recent_failed__mutmut_14 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_15'] = x__find_most_recent_failed__mutmut_15 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_16'] = x__find_most_recent_failed__mutmut_16 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_17'] = x__find_most_recent_failed__mutmut_17 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_18'] = x__find_most_recent_failed__mutmut_18 # type: ignore # mutmut generated
mutants_x__find_most_recent_failed__mutmut['x__find_most_recent_failed__mutmut_19'] = x__find_most_recent_failed__mutmut_19 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__find_slowest_run__mutmut)
def _find_slowest_run(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_orig(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_1(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = None
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_2(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None or r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_3(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["XXduration_secondsXX"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_4(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["DURATION_SECONDS"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_5(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_6(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["XXstatusXX"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_7(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["STATUS"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_8(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] not in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_9(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("XXSucceededXX", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_10(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_11(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("SUCCEEDED", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_12(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "XXFailedXX")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_13(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_14(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "FAILED")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_15(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_16(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = None
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_17(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(None, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_18(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=None)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_19(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_20(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, )
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_21(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: None)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_22(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] and 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_23(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["XXduration_secondsXX"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_24(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["DURATION_SECONDS"] or 0)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_25(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 1)
    return _to_summary(slowest)


def x__find_slowest_run__mutmut_26(runs: list[PipelineRunRecord]) -> PipelineRunSummary | None:
    completed = [
        r
        for r in runs
        if r["duration_seconds"] is not None and r["status"] in ("Succeeded", "Failed")
    ]
    if not completed:
        return None
    slowest = max(completed, key=lambda r: r["duration_seconds"] or 0)
    return _to_summary(None)

mutants_x__find_slowest_run__mutmut['_mutmut_orig'] = x__find_slowest_run__mutmut_orig # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_1'] = x__find_slowest_run__mutmut_1 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_2'] = x__find_slowest_run__mutmut_2 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_3'] = x__find_slowest_run__mutmut_3 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_4'] = x__find_slowest_run__mutmut_4 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_5'] = x__find_slowest_run__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_6'] = x__find_slowest_run__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_7'] = x__find_slowest_run__mutmut_7 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_8'] = x__find_slowest_run__mutmut_8 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_9'] = x__find_slowest_run__mutmut_9 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_10'] = x__find_slowest_run__mutmut_10 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_11'] = x__find_slowest_run__mutmut_11 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_12'] = x__find_slowest_run__mutmut_12 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_13'] = x__find_slowest_run__mutmut_13 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_14'] = x__find_slowest_run__mutmut_14 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_15'] = x__find_slowest_run__mutmut_15 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_16'] = x__find_slowest_run__mutmut_16 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_17'] = x__find_slowest_run__mutmut_17 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_18'] = x__find_slowest_run__mutmut_18 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_19'] = x__find_slowest_run__mutmut_19 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_20'] = x__find_slowest_run__mutmut_20 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_21'] = x__find_slowest_run__mutmut_21 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_22'] = x__find_slowest_run__mutmut_22 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_23'] = x__find_slowest_run__mutmut_23 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_24'] = x__find_slowest_run__mutmut_24 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_25'] = x__find_slowest_run__mutmut_25 # type: ignore # mutmut generated
mutants_x__find_slowest_run__mutmut['x__find_slowest_run__mutmut_26'] = x__find_slowest_run__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut: MutantDict = {}  # type: ignore


class PipelineRunStatusUseCase:
    @_mutmut_mutated(mutants_xǁPipelineRunStatusUseCaseǁ__init____mutmut)
    def __init__(self, port: TektonPipelineStatusPort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁPipelineRunStatusUseCaseǁ__init____mutmut_orig(self, port: TektonPipelineStatusPort) -> None:  # noqa: F821  # type: ignore
        self._port = port
    def xǁPipelineRunStatusUseCaseǁ__init____mutmut_1(self, port: TektonPipelineStatusPort) -> None:  # noqa: F821  # type: ignore
        self._port = None

    @_mutmut_mutated(mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut)
    def get_pipeline_run_status(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_orig(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_1(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = None
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_2(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=None, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_3(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=None)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_4(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_5(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, )
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_6(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = None

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_7(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(None, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_8(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, None)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_9(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_10(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, )

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_11(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = None
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_12(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(None)
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_13(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(2 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_14(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["XXstatusXX"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_15(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["STATUS"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_16(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] != "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_17(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "XXRunningXX")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_18(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_19(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "RUNNING")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_20(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = None
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_21(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(None)
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_22(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(2 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_23(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["XXstatusXX"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_24(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["STATUS"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_25(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] != "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_26(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "XXSucceededXX")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_27(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_28(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "SUCCEEDED")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_29(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = None
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_30(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(None)
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_31(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(2 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_32(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["XXstatusXX"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_33(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["STATUS"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_34(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] != "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_35(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "XXFailedXX")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_36(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_37(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "FAILED")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_38(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = None
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_39(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(None)
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_40(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(2 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_41(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["XXstatusXX"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_42(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["STATUS"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_43(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] != "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_44(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "XXCancelledXX")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_45(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_46(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "CANCELLED")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_47(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = None

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_48(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(None)

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_49(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(2 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_50(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["XXstatusXX"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_51(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["STATUS"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_52(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] != "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_53(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "XXNotStartedXX")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_54(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "notstarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_55(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NOTSTARTED")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_56(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = None
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_57(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=None,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_58(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=None,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_59(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=None,
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_60(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=None,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_61(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=None,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_62(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=None,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_63(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=None,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_64(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=None,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_65(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=None,
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_66(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=None,
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_67(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_68(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_69(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_70(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_71(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_72(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_73(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_74(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_75(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_76(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_77(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(None),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_78(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(None),
        )
        return GetPipelineRunStatusResponse(report=report)

    def xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_79(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse:
        all_runs = self._port.list_pipeline_runs(namespace=command.namespace, limit=command.limit)
        runs = _filter_by_window(all_runs, command.hours_window)

        running = sum(1 for r in runs if r["status"] == "Running")
        succeeded = sum(1 for r in runs if r["status"] == "Succeeded")
        failed = sum(1 for r in runs if r["status"] == "Failed")
        cancelled = sum(1 for r in runs if r["status"] == "Cancelled")
        not_started = sum(1 for r in runs if r["status"] == "NotStarted")

        report = PipelineRunStatusReport(
            namespace=command.namespace,
            window_hours=command.hours_window,
            total=len(runs),
            running=running,
            succeeded=succeeded,
            failed=failed,
            cancelled=cancelled,
            not_started=not_started,
            most_recent_failed=_find_most_recent_failed(runs),
            slowest_run=_find_slowest_run(runs),
        )
        return GetPipelineRunStatusResponse(report=None)

mutants_xǁPipelineRunStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁ__init____mutmut['xǁPipelineRunStatusUseCaseǁ__init____mutmut_1'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['_mutmut_orig'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_1'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_2'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_3'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_4'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_5'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_6'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_7'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_8'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_9'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_10'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_11'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_12'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_13'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_14'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_15'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_16'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_17'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_18'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_19'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_20'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_21'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_22'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_23'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_24'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_25'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_26'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_27'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_28'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_29'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_30'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_31'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_32'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_33'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_34'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_35'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_36'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_37'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_38'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_39'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_40'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_41'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_42'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_43'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_44'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_45'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_46'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_47'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_48'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_49'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_49 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_50'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_50 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_51'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_51 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_52'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_52 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_53'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_53 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_54'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_54 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_55'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_55 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_56'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_56 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_57'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_57 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_58'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_58 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_59'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_59 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_60'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_60 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_61'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_61 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_62'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_62 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_63'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_63 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_64'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_64 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_65'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_65 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_66'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_66 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_67'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_67 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_68'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_68 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_69'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_69 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_70'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_70 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_71'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_71 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_72'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_72 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_73'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_73 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_74'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_74 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_75'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_75 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_76'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_76 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_77'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_77 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_78'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_78 # type: ignore # mutmut generated
mutants_xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut['xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_79'] = PipelineRunStatusUseCase.xǁPipelineRunStatusUseCaseǁget_pipeline_run_status__mutmut_79 # type: ignore # mutmut generated
