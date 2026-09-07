from __future__ import annotations

import statistics
from typing import TypedDict

from hexawyn.domain.models.pipeline_baseline import PipelineBaselineResult, StageStats


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PipelineRunRecord(TypedDict):
    name: str
    status: str
    duration_seconds: int | None
    start_time: str | None
    completion_time: str | None


class TaskRunRecord(TypedDict):
    name: str
    task_name: str
    pipeline_run_name: str
    duration_seconds: int | None


_SIGNIFICANT_TREND_PCT = 0.10
_OUTLIER_MULTIPLIER = 2.0
mutants_x__parse_stage_name__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_stage_name__mutmut)
def _parse_stage_name(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_orig(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_1(task_name: str) -> str:
    lower = None
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_2(task_name: str) -> str:
    lower = task_name.upper()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_3(task_name: str) -> str:
    lower = task_name.lower()
    if "XXbuildXX" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_4(task_name: str) -> str:
    lower = task_name.lower()
    if "BUILD" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_5(task_name: str) -> str:
    lower = task_name.lower()
    if "build" not in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_6(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "XXbuildXX"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_7(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "BUILD"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_8(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "XXtestXX" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_9(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "TEST" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_10(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" not in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_11(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "XXtestXX"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_12(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "TEST"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_13(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "XXdeployXX" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_14(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "DEPLOY" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_15(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" not in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_16(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "XXdeployXX"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_17(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "DEPLOY"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_18(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "XXlintXX" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_19(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "LINT" in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_20(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" not in lower:
        return "lint"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_21(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "XXlintXX"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_22(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "LINT"
    if "scan" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_23(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "XXscanXX" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_24(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "SCAN" in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_25(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" not in lower:
        return "scan"
    return task_name


def x__parse_stage_name__mutmut_26(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "XXscanXX"
    return task_name


def x__parse_stage_name__mutmut_27(task_name: str) -> str:
    lower = task_name.lower()
    if "build" in lower:
        return "build"
    if "test" in lower:
        return "test"
    if "deploy" in lower:
        return "deploy"
    if "lint" in lower:
        return "lint"
    if "scan" in lower:
        return "SCAN"
    return task_name

mutants_x__parse_stage_name__mutmut['_mutmut_orig'] = x__parse_stage_name__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_1'] = x__parse_stage_name__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_2'] = x__parse_stage_name__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_3'] = x__parse_stage_name__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_4'] = x__parse_stage_name__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_5'] = x__parse_stage_name__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_6'] = x__parse_stage_name__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_7'] = x__parse_stage_name__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_8'] = x__parse_stage_name__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_9'] = x__parse_stage_name__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_10'] = x__parse_stage_name__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_11'] = x__parse_stage_name__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_12'] = x__parse_stage_name__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_13'] = x__parse_stage_name__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_14'] = x__parse_stage_name__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_15'] = x__parse_stage_name__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_16'] = x__parse_stage_name__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_17'] = x__parse_stage_name__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_18'] = x__parse_stage_name__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_19'] = x__parse_stage_name__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_20'] = x__parse_stage_name__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_21'] = x__parse_stage_name__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_22'] = x__parse_stage_name__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_23'] = x__parse_stage_name__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_24'] = x__parse_stage_name__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_25'] = x__parse_stage_name__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_26'] = x__parse_stage_name__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_stage_name__mutmut['x__parse_stage_name__mutmut_27'] = x__parse_stage_name__mutmut_27 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_stats__mutmut)
def _compute_stats(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_orig(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_1(durations: list[float]) -> StageStats:
    if durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_2(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=None,
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_3(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=None,
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_4(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=None,  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_5(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=None,
    )


def x__compute_stats__mutmut_6(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_7(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_8(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_9(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        )


def x__compute_stats__mutmut_10(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(None, 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_11(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), None),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_12(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_13(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), ),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_14(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(None), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_15(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 2),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_16(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(None, 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_17(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), None),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_18(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_19(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), ),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_20(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(None), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_21(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 2),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_22(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(None, 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_23(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), None) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_24(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_25(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), ) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_26(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(None, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_27(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, None), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_28(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_29(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, ), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_30(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 96), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_31(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 2) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_32(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) > 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_33(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 3 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_34(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(None, 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_35(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], None),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_36(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_37(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], ),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_38(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[1], 1),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_39(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 2),  # noqa: PLR2004
        max=round(max(durations), 1),
    )


def x__compute_stats__mutmut_40(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(None, 1),
    )


def x__compute_stats__mutmut_41(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), None),
    )


def x__compute_stats__mutmut_42(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(1),
    )


def x__compute_stats__mutmut_43(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), ),
    )


def x__compute_stats__mutmut_44(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(None), 1),
    )


def x__compute_stats__mutmut_45(durations: list[float]) -> StageStats:
    if not durations:
        return StageStats()
    return StageStats(
        avg=round(statistics.mean(durations), 1),
        p50=round(statistics.median(durations), 1),
        p95=round(_percentile(durations, 95), 1) if len(durations) >= 2 else round(durations[0], 1),  # noqa: PLR2004
        max=round(max(durations), 2),
    )

mutants_x__compute_stats__mutmut['_mutmut_orig'] = x__compute_stats__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_1'] = x__compute_stats__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_2'] = x__compute_stats__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_3'] = x__compute_stats__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_4'] = x__compute_stats__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_5'] = x__compute_stats__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_6'] = x__compute_stats__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_7'] = x__compute_stats__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_8'] = x__compute_stats__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_9'] = x__compute_stats__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_10'] = x__compute_stats__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_11'] = x__compute_stats__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_12'] = x__compute_stats__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_13'] = x__compute_stats__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_14'] = x__compute_stats__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_15'] = x__compute_stats__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_16'] = x__compute_stats__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_17'] = x__compute_stats__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_18'] = x__compute_stats__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_19'] = x__compute_stats__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_20'] = x__compute_stats__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_21'] = x__compute_stats__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_22'] = x__compute_stats__mutmut_22 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_23'] = x__compute_stats__mutmut_23 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_24'] = x__compute_stats__mutmut_24 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_25'] = x__compute_stats__mutmut_25 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_26'] = x__compute_stats__mutmut_26 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_27'] = x__compute_stats__mutmut_27 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_28'] = x__compute_stats__mutmut_28 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_29'] = x__compute_stats__mutmut_29 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_30'] = x__compute_stats__mutmut_30 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_31'] = x__compute_stats__mutmut_31 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_32'] = x__compute_stats__mutmut_32 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_33'] = x__compute_stats__mutmut_33 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_34'] = x__compute_stats__mutmut_34 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_35'] = x__compute_stats__mutmut_35 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_36'] = x__compute_stats__mutmut_36 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_37'] = x__compute_stats__mutmut_37 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_38'] = x__compute_stats__mutmut_38 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_39'] = x__compute_stats__mutmut_39 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_40'] = x__compute_stats__mutmut_40 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_41'] = x__compute_stats__mutmut_41 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_42'] = x__compute_stats__mutmut_42 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_43'] = x__compute_stats__mutmut_43 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_44'] = x__compute_stats__mutmut_44 # type: ignore # mutmut generated
mutants_x__compute_stats__mutmut['x__compute_stats__mutmut_45'] = x__compute_stats__mutmut_45 # type: ignore # mutmut generated
mutants_x__percentile__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__percentile__mutmut)
def _percentile(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_orig(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_1(data: list[float], pct: float) -> float:
    if data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_2(data: list[float], pct: float) -> float:
    if not data:
        return 1.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_3(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = None
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_4(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(None)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_5(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = None
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_6(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) / (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_7(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct * 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_8(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 101.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_9(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) + 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_10(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 2)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_11(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = None
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_12(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(None)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_13(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = None
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_14(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k + f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_15(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f - 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_16(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 2 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_17(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 <= len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_18(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] - c * (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_19(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c / (sorted_data[f + 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_20(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 1] + sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_21(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f - 1] - sorted_data[f])
    return sorted_data[f]


def x__percentile__mutmut_22(data: list[float], pct: float) -> float:
    if not data:
        return 0.0
    sorted_data = sorted(data)
    k = (pct / 100.0) * (len(sorted_data) - 1)
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_data):
        return sorted_data[f] + c * (sorted_data[f + 2] - sorted_data[f])
    return sorted_data[f]

mutants_x__percentile__mutmut['_mutmut_orig'] = x__percentile__mutmut_orig # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_1'] = x__percentile__mutmut_1 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_2'] = x__percentile__mutmut_2 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_3'] = x__percentile__mutmut_3 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_4'] = x__percentile__mutmut_4 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_5'] = x__percentile__mutmut_5 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_6'] = x__percentile__mutmut_6 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_7'] = x__percentile__mutmut_7 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_8'] = x__percentile__mutmut_8 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_9'] = x__percentile__mutmut_9 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_10'] = x__percentile__mutmut_10 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_11'] = x__percentile__mutmut_11 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_12'] = x__percentile__mutmut_12 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_13'] = x__percentile__mutmut_13 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_14'] = x__percentile__mutmut_14 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_15'] = x__percentile__mutmut_15 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_16'] = x__percentile__mutmut_16 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_17'] = x__percentile__mutmut_17 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_18'] = x__percentile__mutmut_18 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_19'] = x__percentile__mutmut_19 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_20'] = x__percentile__mutmut_20 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_21'] = x__percentile__mutmut_21 # type: ignore # mutmut generated
mutants_x__percentile__mutmut['x__percentile__mutmut_22'] = x__percentile__mutmut_22 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_outliers__mutmut)
def _detect_outliers(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_orig(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_1(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = None
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_2(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = None
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_3(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") and 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_4(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get(None) or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_5(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("XXduration_secondsXX") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_6(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("DURATION_SECONDS") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_7(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 1
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_8(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur < 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_9(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 1:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_10(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            break
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_11(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 or dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_12(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg >= 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_13(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 1 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_14(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur >= _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_15(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER / avg:
                if run["name"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_16(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["XXnameXX"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_17(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["NAME"] not in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_18(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] in outliers:
                    outliers.append(run["name"])
    return outliers


def x__detect_outliers__mutmut_19(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(None)
    return outliers


def x__detect_outliers__mutmut_20(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["XXnameXX"])
    return outliers


def x__detect_outliers__mutmut_21(runs: list[PipelineRunRecord], avgs: list[float]) -> list[str]:
    outliers: list[str] = []
    for run in runs:
        dur = run.get("duration_seconds") or 0
        if dur <= 0:
            continue
        for avg in avgs:
            if avg > 0 and dur > _OUTLIER_MULTIPLIER * avg:
                if run["name"] not in outliers:
                    outliers.append(run["NAME"])
    return outliers

mutants_x__detect_outliers__mutmut['_mutmut_orig'] = x__detect_outliers__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_1'] = x__detect_outliers__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_2'] = x__detect_outliers__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_3'] = x__detect_outliers__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_4'] = x__detect_outliers__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_5'] = x__detect_outliers__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_6'] = x__detect_outliers__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_7'] = x__detect_outliers__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_8'] = x__detect_outliers__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_9'] = x__detect_outliers__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_10'] = x__detect_outliers__mutmut_10 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_11'] = x__detect_outliers__mutmut_11 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_12'] = x__detect_outliers__mutmut_12 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_13'] = x__detect_outliers__mutmut_13 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_14'] = x__detect_outliers__mutmut_14 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_15'] = x__detect_outliers__mutmut_15 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_16'] = x__detect_outliers__mutmut_16 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_17'] = x__detect_outliers__mutmut_17 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_18'] = x__detect_outliers__mutmut_18 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_19'] = x__detect_outliers__mutmut_19 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_20'] = x__detect_outliers__mutmut_20 # type: ignore # mutmut generated
mutants_x__detect_outliers__mutmut['x__detect_outliers__mutmut_21'] = x__detect_outliers__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_trend__mutmut)
def _compute_trend(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_orig(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_1(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) <= 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_2(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 6:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_3(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "XXinsufficient_dataXX", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_4(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "INSUFFICIENT_DATA", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_5(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = None
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_6(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(None, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_7(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=None)
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_8(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_9(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, )
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_10(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: None)
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_11(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") and "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_12(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get(None) or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_13(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("XXstart_timeXX") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_14(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("START_TIME") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_15(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "XXXX")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_16(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = None
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_17(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:6] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_18(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get(None)]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_19(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("XXduration_secondsXX")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_20(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("DURATION_SECONDS")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_21(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = None
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_22(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[+5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_23(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-6:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_24(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get(None)]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_25(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("XXduration_secondsXX")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_26(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("DURATION_SECONDS")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_27(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 and len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_28(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) <= 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_29(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 4 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_30(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) <= 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_31(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 4:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_32(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "XXinsufficient_dataXX", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_33(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "INSUFFICIENT_DATA", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_34(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = None
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_35(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean(None)
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_36(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") and 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_37(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get(None) or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_38(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("XXduration_secondsXX") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_39(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("DURATION_SECONDS") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_40(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 1 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_41(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = None
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_42(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean(None)
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_43(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") and 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_44(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get(None) or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_45(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("XXduration_secondsXX") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_46(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("DURATION_SECONDS") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_47(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 1 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_48(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = None
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_49(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) * first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_50(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg + first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_51(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = None
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_52(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(None, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_53(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, None)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_54(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_55(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, )
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_56(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta / 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_57(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 101, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_58(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 2)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_59(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta <= -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_60(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < +_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_61(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "XXimprovingXX", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_62(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "IMPROVING", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_63(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta >= _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "stable", pct


def x__compute_trend__mutmut_64(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "XXdegradingXX", pct
    return "stable", pct


def x__compute_trend__mutmut_65(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "DEGRADING", pct
    return "stable", pct


def x__compute_trend__mutmut_66(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "XXstableXX", pct


def x__compute_trend__mutmut_67(runs: list[PipelineRunRecord]) -> tuple[str, float | None]:
    if len(runs) < 5:  # noqa: PLR2004
        return "insufficient_data", None
    sorted_runs = sorted(runs, key=lambda r: r.get("start_time") or "")
    first_5 = [r for r in sorted_runs[:5] if r.get("duration_seconds")]
    last_5 = [r for r in sorted_runs[-5:] if r.get("duration_seconds")]
    if len(first_5) < 3 or len(last_5) < 3:  # noqa: PLR2004
        return "insufficient_data", None
    first_avg = statistics.mean([r.get("duration_seconds") or 0 for r in first_5])
    last_avg = statistics.mean([r.get("duration_seconds") or 0 for r in last_5])
    delta = (last_avg - first_avg) / first_avg
    pct = round(delta * 100, 1)
    if delta < -_SIGNIFICANT_TREND_PCT:
        return "improving", pct
    if delta > _SIGNIFICANT_TREND_PCT:
        return "degrading", pct
    return "STABLE", pct

mutants_x__compute_trend__mutmut['_mutmut_orig'] = x__compute_trend__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_1'] = x__compute_trend__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_2'] = x__compute_trend__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_3'] = x__compute_trend__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_4'] = x__compute_trend__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_5'] = x__compute_trend__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_6'] = x__compute_trend__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_7'] = x__compute_trend__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_8'] = x__compute_trend__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_9'] = x__compute_trend__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_10'] = x__compute_trend__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_11'] = x__compute_trend__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_12'] = x__compute_trend__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_13'] = x__compute_trend__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_14'] = x__compute_trend__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_15'] = x__compute_trend__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_16'] = x__compute_trend__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_17'] = x__compute_trend__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_18'] = x__compute_trend__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_19'] = x__compute_trend__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_20'] = x__compute_trend__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_21'] = x__compute_trend__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_22'] = x__compute_trend__mutmut_22 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_23'] = x__compute_trend__mutmut_23 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_24'] = x__compute_trend__mutmut_24 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_25'] = x__compute_trend__mutmut_25 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_26'] = x__compute_trend__mutmut_26 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_27'] = x__compute_trend__mutmut_27 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_28'] = x__compute_trend__mutmut_28 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_29'] = x__compute_trend__mutmut_29 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_30'] = x__compute_trend__mutmut_30 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_31'] = x__compute_trend__mutmut_31 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_32'] = x__compute_trend__mutmut_32 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_33'] = x__compute_trend__mutmut_33 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_34'] = x__compute_trend__mutmut_34 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_35'] = x__compute_trend__mutmut_35 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_36'] = x__compute_trend__mutmut_36 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_37'] = x__compute_trend__mutmut_37 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_38'] = x__compute_trend__mutmut_38 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_39'] = x__compute_trend__mutmut_39 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_40'] = x__compute_trend__mutmut_40 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_41'] = x__compute_trend__mutmut_41 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_42'] = x__compute_trend__mutmut_42 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_43'] = x__compute_trend__mutmut_43 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_44'] = x__compute_trend__mutmut_44 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_45'] = x__compute_trend__mutmut_45 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_46'] = x__compute_trend__mutmut_46 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_47'] = x__compute_trend__mutmut_47 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_48'] = x__compute_trend__mutmut_48 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_49'] = x__compute_trend__mutmut_49 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_50'] = x__compute_trend__mutmut_50 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_51'] = x__compute_trend__mutmut_51 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_52'] = x__compute_trend__mutmut_52 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_53'] = x__compute_trend__mutmut_53 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_54'] = x__compute_trend__mutmut_54 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_55'] = x__compute_trend__mutmut_55 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_56'] = x__compute_trend__mutmut_56 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_57'] = x__compute_trend__mutmut_57 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_58'] = x__compute_trend__mutmut_58 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_59'] = x__compute_trend__mutmut_59 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_60'] = x__compute_trend__mutmut_60 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_61'] = x__compute_trend__mutmut_61 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_62'] = x__compute_trend__mutmut_62 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_63'] = x__compute_trend__mutmut_63 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_64'] = x__compute_trend__mutmut_64 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_65'] = x__compute_trend__mutmut_65 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_66'] = x__compute_trend__mutmut_66 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_67'] = x__compute_trend__mutmut_67 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__bucket_stage_durations_by_window__mutmut)
def _bucket_stage_durations_by_window(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_orig(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_1(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = None
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_2(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = None
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_3(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names or run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_4(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_5(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_6(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            break
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_7(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = None
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_8(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") and 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_9(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get(None) or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_10(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("XXduration_secondsXX") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_11(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("DURATION_SECONDS") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_12(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 1
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_13(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur < 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_14(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 1:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_15(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                break
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_16(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = None
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_17(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(None)
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_18(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get(None, "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_19(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", None))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_20(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_21(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", ))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_22(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("XXtask_nameXX", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_23(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("TASK_NAME", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_24(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "XXunknownXX"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_25(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "UNKNOWN"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_26(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name not in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_27(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(None)
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_28(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(None, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_29(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, None).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_30(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault([]).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_31(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, ).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_32(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(None))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_33(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name not in last_5_names:
                last_durations.setdefault(stage, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_34(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(None)
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_35(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(None, []).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_36(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, None).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_37(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault([]).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_38(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, ).append(float(dur))
    return first_durations, last_durations


def x__bucket_stage_durations_by_window__mutmut_39(
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
    first_5_names: set[str],
    last_5_names: set[str],
) -> tuple[dict[str, list[float]], dict[str, list[float]]]:
    """Split per-stage task durations into the first-5/last-5 run windows."""
    first_durations: dict[str, list[float]] = {}
    last_durations: dict[str, list[float]] = {}
    for run_name, tasks in task_runs_by_pipeline.items():
        if run_name not in first_5_names and run_name not in last_5_names:
            continue
        for tr in tasks:
            dur = tr.get("duration_seconds") or 0
            if dur <= 0:
                continue
            stage = _parse_stage_name(tr.get("task_name", "unknown"))
            if run_name in first_5_names:
                first_durations.setdefault(stage, []).append(float(dur))
            if run_name in last_5_names:
                last_durations.setdefault(stage, []).append(float(None))
    return first_durations, last_durations

mutants_x__bucket_stage_durations_by_window__mutmut['_mutmut_orig'] = x__bucket_stage_durations_by_window__mutmut_orig # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_1'] = x__bucket_stage_durations_by_window__mutmut_1 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_2'] = x__bucket_stage_durations_by_window__mutmut_2 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_3'] = x__bucket_stage_durations_by_window__mutmut_3 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_4'] = x__bucket_stage_durations_by_window__mutmut_4 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_5'] = x__bucket_stage_durations_by_window__mutmut_5 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_6'] = x__bucket_stage_durations_by_window__mutmut_6 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_7'] = x__bucket_stage_durations_by_window__mutmut_7 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_8'] = x__bucket_stage_durations_by_window__mutmut_8 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_9'] = x__bucket_stage_durations_by_window__mutmut_9 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_10'] = x__bucket_stage_durations_by_window__mutmut_10 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_11'] = x__bucket_stage_durations_by_window__mutmut_11 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_12'] = x__bucket_stage_durations_by_window__mutmut_12 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_13'] = x__bucket_stage_durations_by_window__mutmut_13 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_14'] = x__bucket_stage_durations_by_window__mutmut_14 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_15'] = x__bucket_stage_durations_by_window__mutmut_15 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_16'] = x__bucket_stage_durations_by_window__mutmut_16 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_17'] = x__bucket_stage_durations_by_window__mutmut_17 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_18'] = x__bucket_stage_durations_by_window__mutmut_18 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_19'] = x__bucket_stage_durations_by_window__mutmut_19 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_20'] = x__bucket_stage_durations_by_window__mutmut_20 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_21'] = x__bucket_stage_durations_by_window__mutmut_21 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_22'] = x__bucket_stage_durations_by_window__mutmut_22 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_23'] = x__bucket_stage_durations_by_window__mutmut_23 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_24'] = x__bucket_stage_durations_by_window__mutmut_24 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_25'] = x__bucket_stage_durations_by_window__mutmut_25 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_26'] = x__bucket_stage_durations_by_window__mutmut_26 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_27'] = x__bucket_stage_durations_by_window__mutmut_27 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_28'] = x__bucket_stage_durations_by_window__mutmut_28 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_29'] = x__bucket_stage_durations_by_window__mutmut_29 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_30'] = x__bucket_stage_durations_by_window__mutmut_30 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_31'] = x__bucket_stage_durations_by_window__mutmut_31 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_32'] = x__bucket_stage_durations_by_window__mutmut_32 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_33'] = x__bucket_stage_durations_by_window__mutmut_33 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_34'] = x__bucket_stage_durations_by_window__mutmut_34 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_35'] = x__bucket_stage_durations_by_window__mutmut_35 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_36'] = x__bucket_stage_durations_by_window__mutmut_36 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_37'] = x__bucket_stage_durations_by_window__mutmut_37 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_38'] = x__bucket_stage_durations_by_window__mutmut_38 # type: ignore # mutmut generated
mutants_x__bucket_stage_durations_by_window__mutmut['x__bucket_stage_durations_by_window__mutmut_39'] = x__bucket_stage_durations_by_window__mutmut_39 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__worst_degrading_stage__mutmut)
def _worst_degrading_stage(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_orig(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_1(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = ""
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_2(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = None
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_3(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = None
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_4(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(None)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_5(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list and not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_6(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_7(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_8(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            break
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_9(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = None
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_10(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(None)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_11(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg != 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_12(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 1:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_13(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            break
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_14(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = None
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_15(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) * first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_16(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) + first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_17(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(None) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_18(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta >= worst_delta:
            worst_delta = delta
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_19(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = None
            worst_stage = stage
    return worst_stage


def x__worst_degrading_stage__mutmut_20(
    first_durations: dict[str, list[float]],
    last_durations: dict[str, list[float]],
) -> str | None:
    """Pick the stage with the largest first-5-vs-last-5 relative increase,
    only if it clears the same significance threshold as _compute_trend.
    """
    worst_stage: str | None = None
    worst_delta = _SIGNIFICANT_TREND_PCT
    for stage, first_list in first_durations.items():
        last_list = last_durations.get(stage)
        if not last_list or not first_list:
            continue
        first_avg = statistics.mean(first_list)
        if first_avg == 0:
            continue
        delta = (statistics.mean(last_list) - first_avg) / first_avg
        if delta > worst_delta:
            worst_delta = delta
            worst_stage = None
    return worst_stage

mutants_x__worst_degrading_stage__mutmut['_mutmut_orig'] = x__worst_degrading_stage__mutmut_orig # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_1'] = x__worst_degrading_stage__mutmut_1 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_2'] = x__worst_degrading_stage__mutmut_2 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_3'] = x__worst_degrading_stage__mutmut_3 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_4'] = x__worst_degrading_stage__mutmut_4 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_5'] = x__worst_degrading_stage__mutmut_5 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_6'] = x__worst_degrading_stage__mutmut_6 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_7'] = x__worst_degrading_stage__mutmut_7 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_8'] = x__worst_degrading_stage__mutmut_8 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_9'] = x__worst_degrading_stage__mutmut_9 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_10'] = x__worst_degrading_stage__mutmut_10 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_11'] = x__worst_degrading_stage__mutmut_11 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_12'] = x__worst_degrading_stage__mutmut_12 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_13'] = x__worst_degrading_stage__mutmut_13 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_14'] = x__worst_degrading_stage__mutmut_14 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_15'] = x__worst_degrading_stage__mutmut_15 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_16'] = x__worst_degrading_stage__mutmut_16 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_17'] = x__worst_degrading_stage__mutmut_17 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_18'] = x__worst_degrading_stage__mutmut_18 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_19'] = x__worst_degrading_stage__mutmut_19 # type: ignore # mutmut generated
mutants_x__worst_degrading_stage__mutmut['x__worst_degrading_stage__mutmut_20'] = x__worst_degrading_stage__mutmut_20 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__find_bottleneck_stage__mutmut)
def _find_bottleneck_stage(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_orig(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_1(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) <= 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_2(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 6:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_3(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = None
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_4(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(None, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_5(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=None)
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_6(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_7(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, )
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_8(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: None)
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_9(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") and "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_10(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get(None) or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_11(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("XXstart_timeXX") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_12(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("START_TIME") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_13(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "XXXX")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_14(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = None
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_15(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["XXnameXX"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_16(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["NAME"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_17(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:6]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_18(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = None
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_19(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["XXnameXX"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_20(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["NAME"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_21(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[+5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_22(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-6:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_23(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = None
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_24(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        None, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_25(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, None, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_26(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, None
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_27(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_28(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, last_5_names
    )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_29(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, )
    return _worst_degrading_stage(first_durations, last_durations)


def x__find_bottleneck_stage__mutmut_30(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(None, last_durations)


def x__find_bottleneck_stage__mutmut_31(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, None)


def x__find_bottleneck_stage__mutmut_32(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(last_durations)


def x__find_bottleneck_stage__mutmut_33(
    succeeded_runs: list[PipelineRunRecord],
    task_runs_by_pipeline: dict[str, list[TaskRunRecord]],
) -> str | None:
    """Among all stages, find the one whose duration increased the most
    between the first 5 and last 5 runs (by start_time) — the same
    first-5-vs-last-5 comparison as _compute_trend, applied per stage
    instead of to the total run duration, to name which stage is actually
    driving an overall slowdown.
    """
    if len(succeeded_runs) < 5:  # noqa: PLR2004
        return None
    sorted_runs = sorted(succeeded_runs, key=lambda r: r.get("start_time") or "")
    first_5_names = {r["name"] for r in sorted_runs[:5]}
    last_5_names = {r["name"] for r in sorted_runs[-5:]}
    first_durations, last_durations = _bucket_stage_durations_by_window(
        task_runs_by_pipeline, first_5_names, last_5_names
    )
    return _worst_degrading_stage(first_durations, )

mutants_x__find_bottleneck_stage__mutmut['_mutmut_orig'] = x__find_bottleneck_stage__mutmut_orig # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_1'] = x__find_bottleneck_stage__mutmut_1 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_2'] = x__find_bottleneck_stage__mutmut_2 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_3'] = x__find_bottleneck_stage__mutmut_3 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_4'] = x__find_bottleneck_stage__mutmut_4 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_5'] = x__find_bottleneck_stage__mutmut_5 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_6'] = x__find_bottleneck_stage__mutmut_6 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_7'] = x__find_bottleneck_stage__mutmut_7 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_8'] = x__find_bottleneck_stage__mutmut_8 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_9'] = x__find_bottleneck_stage__mutmut_9 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_10'] = x__find_bottleneck_stage__mutmut_10 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_11'] = x__find_bottleneck_stage__mutmut_11 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_12'] = x__find_bottleneck_stage__mutmut_12 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_13'] = x__find_bottleneck_stage__mutmut_13 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_14'] = x__find_bottleneck_stage__mutmut_14 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_15'] = x__find_bottleneck_stage__mutmut_15 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_16'] = x__find_bottleneck_stage__mutmut_16 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_17'] = x__find_bottleneck_stage__mutmut_17 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_18'] = x__find_bottleneck_stage__mutmut_18 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_19'] = x__find_bottleneck_stage__mutmut_19 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_20'] = x__find_bottleneck_stage__mutmut_20 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_21'] = x__find_bottleneck_stage__mutmut_21 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_22'] = x__find_bottleneck_stage__mutmut_22 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_23'] = x__find_bottleneck_stage__mutmut_23 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_24'] = x__find_bottleneck_stage__mutmut_24 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_25'] = x__find_bottleneck_stage__mutmut_25 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_26'] = x__find_bottleneck_stage__mutmut_26 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_27'] = x__find_bottleneck_stage__mutmut_27 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_28'] = x__find_bottleneck_stage__mutmut_28 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_29'] = x__find_bottleneck_stage__mutmut_29 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_30'] = x__find_bottleneck_stage__mutmut_30 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_31'] = x__find_bottleneck_stage__mutmut_31 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_32'] = x__find_bottleneck_stage__mutmut_32 # type: ignore # mutmut generated
mutants_x__find_bottleneck_stage__mutmut['x__find_bottleneck_stage__mutmut_33'] = x__find_bottleneck_stage__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_baseline__mutmut)
def compute_baseline(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_orig(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_1(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 31,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_2(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = None
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_3(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" or r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_4(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get(None) == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_5(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("XXstatusXX") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_6(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("STATUS") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_7(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") != "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_8(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "XXsucceededXX" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_9(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "SUCCEEDED" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_10(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get(None) is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_11(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("XXcompletion_timeXX") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_12(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("COMPLETION_TIME") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_13(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_14(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = None
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_15(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = None

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_16(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_17(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=None,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_18(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=None,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_19(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=None,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_20(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=None,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_21(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note=None,
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_22(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_23(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_24(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_25(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_26(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_27(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="XXNo succeeded runs with completionTime availableXX",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_28(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="no succeeded runs with completiontime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_29(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="NO SUCCEEDED RUNS WITH COMPLETIONTIME AVAILABLE",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_30(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = None
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_31(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = None
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_32(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get(None)
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_33(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("XXpipeline_run_nameXX")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_34(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("PIPELINE_RUN_NAME")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_35(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(None)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_36(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(None, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_37(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, None).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_38(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault([]).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_39(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, ).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_40(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = None
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_41(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = None

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_42(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = None
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_43(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") and 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_44(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get(None) or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_45(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("XXduration_secondsXX") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_46(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("DURATION_SECONDS") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_47(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 1
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_48(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur >= 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_49(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 1:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_50(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(None)

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_51(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(None))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_52(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = None
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_53(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(None, [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_54(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], None)
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_55(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get([])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_56(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], )
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_57(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["XXnameXX"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_58(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["NAME"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_59(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = None
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_60(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") and 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_61(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get(None) or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_62(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("XXduration_secondsXX") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_63(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("DURATION_SECONDS") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_64(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 1
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_65(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur >= 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_66(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 1:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_67(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = None
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_68(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(None)
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_69(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get(None, "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_70(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", None))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_71(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_72(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", ))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_73(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("XXtask_nameXX", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_74(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("TASK_NAME", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_75(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "XXunknownXX"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_76(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "UNKNOWN"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_77(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(None)

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_78(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(None, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_79(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, None).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_80(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault([]).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_81(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, ).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_82(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(None))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_83(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = None
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_84(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(None):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_85(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = None

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_86(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(None)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_87(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_88(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(None) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_89(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = None
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_90(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(None)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_91(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = None

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_92(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(None, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_93(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, None)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_94(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_95(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, )

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_96(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = None
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_97(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(None)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_98(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = None

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_99(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(None, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_100(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, None)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_101(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_102(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, )

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_103(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = None
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_104(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = "XXXX"
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_105(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) <= requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_106(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = None

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_107(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=None,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_108(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=None,
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_109(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=None,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_110(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=None,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_111(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=None,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_112(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=None,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_113(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=None,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_114(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=None,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_115(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=None,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_116(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=None,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_117(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=None,
        note=note,
    )


def x_compute_baseline__mutmut_118(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=None,
    )


def x_compute_baseline__mutmut_119(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_120(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_121(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_122(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_123(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_124(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_125(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_126(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_127(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_128(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        bottleneck_stage=bottleneck_stage,
        note=note,
    )


def x_compute_baseline__mutmut_129(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        note=note,
    )


def x_compute_baseline__mutmut_130(  # noqa: C901
    pipeline_name: str,
    pipeline_runs: list[PipelineRunRecord],
    task_runs: list[TaskRunRecord],
    requested_limit: int = 30,
) -> PipelineBaselineResult:
    succeeded = [
        r
        for r in pipeline_runs
        if r.get("status") == "succeeded" and r.get("completion_time") is not None
    ]
    excluded_running = len([r for r in pipeline_runs if r.get("completion_time") is None])
    excluded_failed = len(
        [
            r
            for r in pipeline_runs
            if r.get("status") != "succeeded" and r.get("completion_time") is not None
        ]
    )

    if not succeeded:
        return PipelineBaselineResult(
            pipeline=pipeline_name,
            requested_limit=requested_limit,
            excluded_running=excluded_running,
            excluded_failed=excluded_failed,
            note="No succeeded runs with completionTime available",
        )

    task_runs_by_pipeline: dict[str, list[TaskRunRecord]] = {}
    for tr in task_runs:
        pr_name = tr.get("pipeline_run_name")
        if pr_name:
            task_runs_by_pipeline.setdefault(pr_name, []).append(tr)

    stage_durations: dict[str, list[float]] = {}
    total_durations: list[float] = []

    for run in succeeded:
        dur = run.get("duration_seconds") or 0
        if dur > 0:
            total_durations.append(float(dur))

        child_tasks = task_runs_by_pipeline.get(run["name"], [])
        for tr in child_tasks:
            tr_dur = tr.get("duration_seconds") or 0
            if tr_dur > 0:
                stage = _parse_stage_name(tr.get("task_name", "unknown"))
                stage_durations.setdefault(stage, []).append(float(tr_dur))

    stages = {}
    if stage_durations:
        for stage_name, durations in sorted(stage_durations.items()):
            if durations:
                stages[stage_name] = _compute_stats(durations)

    total_stats = _compute_stats(total_durations) if total_durations else None

    stage_avgs = [s.avg for s in stages.values()]
    if total_stats:
        stage_avgs.append(total_stats.avg)
    outliers = _detect_outliers(succeeded, stage_avgs)

    trend, trend_pct = _compute_trend(succeeded)
    bottleneck_stage = _find_bottleneck_stage(succeeded, task_runs_by_pipeline)

    note = ""
    if len(succeeded) < requested_limit:
        note = f"Only {len(succeeded)} runs available (requested {requested_limit})"

    return PipelineBaselineResult(
        pipeline=pipeline_name,
        runs_analyzed=len(succeeded),
        requested_limit=requested_limit,
        stages=stages,
        total_duration=total_stats,
        outliers=outliers,
        excluded_running=excluded_running,
        excluded_failed=excluded_failed,
        trend=trend,
        trend_pct=trend_pct,
        bottleneck_stage=bottleneck_stage,
        )

mutants_x_compute_baseline__mutmut['_mutmut_orig'] = x_compute_baseline__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_1'] = x_compute_baseline__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_2'] = x_compute_baseline__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_3'] = x_compute_baseline__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_4'] = x_compute_baseline__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_5'] = x_compute_baseline__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_6'] = x_compute_baseline__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_7'] = x_compute_baseline__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_8'] = x_compute_baseline__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_9'] = x_compute_baseline__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_10'] = x_compute_baseline__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_11'] = x_compute_baseline__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_12'] = x_compute_baseline__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_13'] = x_compute_baseline__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_14'] = x_compute_baseline__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_15'] = x_compute_baseline__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_16'] = x_compute_baseline__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_17'] = x_compute_baseline__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_18'] = x_compute_baseline__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_19'] = x_compute_baseline__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_20'] = x_compute_baseline__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_21'] = x_compute_baseline__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_22'] = x_compute_baseline__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_23'] = x_compute_baseline__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_24'] = x_compute_baseline__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_25'] = x_compute_baseline__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_26'] = x_compute_baseline__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_27'] = x_compute_baseline__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_28'] = x_compute_baseline__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_29'] = x_compute_baseline__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_30'] = x_compute_baseline__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_31'] = x_compute_baseline__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_32'] = x_compute_baseline__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_33'] = x_compute_baseline__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_34'] = x_compute_baseline__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_35'] = x_compute_baseline__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_36'] = x_compute_baseline__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_37'] = x_compute_baseline__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_38'] = x_compute_baseline__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_39'] = x_compute_baseline__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_40'] = x_compute_baseline__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_41'] = x_compute_baseline__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_42'] = x_compute_baseline__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_43'] = x_compute_baseline__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_44'] = x_compute_baseline__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_45'] = x_compute_baseline__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_46'] = x_compute_baseline__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_47'] = x_compute_baseline__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_48'] = x_compute_baseline__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_49'] = x_compute_baseline__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_50'] = x_compute_baseline__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_51'] = x_compute_baseline__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_52'] = x_compute_baseline__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_53'] = x_compute_baseline__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_54'] = x_compute_baseline__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_55'] = x_compute_baseline__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_56'] = x_compute_baseline__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_57'] = x_compute_baseline__mutmut_57 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_58'] = x_compute_baseline__mutmut_58 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_59'] = x_compute_baseline__mutmut_59 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_60'] = x_compute_baseline__mutmut_60 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_61'] = x_compute_baseline__mutmut_61 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_62'] = x_compute_baseline__mutmut_62 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_63'] = x_compute_baseline__mutmut_63 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_64'] = x_compute_baseline__mutmut_64 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_65'] = x_compute_baseline__mutmut_65 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_66'] = x_compute_baseline__mutmut_66 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_67'] = x_compute_baseline__mutmut_67 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_68'] = x_compute_baseline__mutmut_68 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_69'] = x_compute_baseline__mutmut_69 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_70'] = x_compute_baseline__mutmut_70 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_71'] = x_compute_baseline__mutmut_71 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_72'] = x_compute_baseline__mutmut_72 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_73'] = x_compute_baseline__mutmut_73 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_74'] = x_compute_baseline__mutmut_74 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_75'] = x_compute_baseline__mutmut_75 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_76'] = x_compute_baseline__mutmut_76 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_77'] = x_compute_baseline__mutmut_77 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_78'] = x_compute_baseline__mutmut_78 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_79'] = x_compute_baseline__mutmut_79 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_80'] = x_compute_baseline__mutmut_80 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_81'] = x_compute_baseline__mutmut_81 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_82'] = x_compute_baseline__mutmut_82 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_83'] = x_compute_baseline__mutmut_83 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_84'] = x_compute_baseline__mutmut_84 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_85'] = x_compute_baseline__mutmut_85 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_86'] = x_compute_baseline__mutmut_86 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_87'] = x_compute_baseline__mutmut_87 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_88'] = x_compute_baseline__mutmut_88 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_89'] = x_compute_baseline__mutmut_89 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_90'] = x_compute_baseline__mutmut_90 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_91'] = x_compute_baseline__mutmut_91 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_92'] = x_compute_baseline__mutmut_92 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_93'] = x_compute_baseline__mutmut_93 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_94'] = x_compute_baseline__mutmut_94 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_95'] = x_compute_baseline__mutmut_95 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_96'] = x_compute_baseline__mutmut_96 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_97'] = x_compute_baseline__mutmut_97 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_98'] = x_compute_baseline__mutmut_98 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_99'] = x_compute_baseline__mutmut_99 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_100'] = x_compute_baseline__mutmut_100 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_101'] = x_compute_baseline__mutmut_101 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_102'] = x_compute_baseline__mutmut_102 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_103'] = x_compute_baseline__mutmut_103 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_104'] = x_compute_baseline__mutmut_104 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_105'] = x_compute_baseline__mutmut_105 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_106'] = x_compute_baseline__mutmut_106 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_107'] = x_compute_baseline__mutmut_107 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_108'] = x_compute_baseline__mutmut_108 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_109'] = x_compute_baseline__mutmut_109 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_110'] = x_compute_baseline__mutmut_110 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_111'] = x_compute_baseline__mutmut_111 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_112'] = x_compute_baseline__mutmut_112 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_113'] = x_compute_baseline__mutmut_113 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_114'] = x_compute_baseline__mutmut_114 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_115'] = x_compute_baseline__mutmut_115 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_116'] = x_compute_baseline__mutmut_116 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_117'] = x_compute_baseline__mutmut_117 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_118'] = x_compute_baseline__mutmut_118 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_119'] = x_compute_baseline__mutmut_119 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_120'] = x_compute_baseline__mutmut_120 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_121'] = x_compute_baseline__mutmut_121 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_122'] = x_compute_baseline__mutmut_122 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_123'] = x_compute_baseline__mutmut_123 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_124'] = x_compute_baseline__mutmut_124 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_125'] = x_compute_baseline__mutmut_125 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_126'] = x_compute_baseline__mutmut_126 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_127'] = x_compute_baseline__mutmut_127 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_128'] = x_compute_baseline__mutmut_128 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_129'] = x_compute_baseline__mutmut_129 # type: ignore # mutmut generated
mutants_x_compute_baseline__mutmut['x_compute_baseline__mutmut_130'] = x_compute_baseline__mutmut_130 # type: ignore # mutmut generated
