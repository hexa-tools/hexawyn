"""MCP tool: list_pipeline_runs."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

from hexawyn.application.use_case.pipelines.list_pipeline_runs.command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.list_pipeline_runs_use_case import (
    ListPipelineRunsUseCase,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
    PipelineRunStats,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PipelineRunStatsPayload(TypedDict):
    total_runs: int
    succeeded_runs: int
    failed_runs: int
    cancelled_runs: int
    success_rate: float
    average_duration_seconds: float | None
    fastest_run_name: str | None
    slowest_run_name: str | None
mutants_x__stats_payload__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__stats_payload__mutmut)
def _stats_payload(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_orig(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_1(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=None,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_2(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=None,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_3(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=None,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_4(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=None,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_5(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=None,
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_6(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=None,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_7(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=None,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_8(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=None,
    )


def x__stats_payload__mutmut_9(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_10(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_11(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_12(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_13(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_14(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_15(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_16(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        )


def x__stats_payload__mutmut_17(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(None, 1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_18(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, None),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_19(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(1),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_20(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, ),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )


def x__stats_payload__mutmut_21(stats: PipelineRunStats) -> PipelineRunStatsPayload:
    """Serialize the use case's already-computed PipelineRunStats.

    Previously this tool discarded `stats` entirely and recomputed a
    partial mean/median-only dict locally — success_rate (and the
    succeeded/failed/cancelled counts) never reached the LLM.
    """
    return PipelineRunStatsPayload(
        total_runs=stats.total_runs,
        succeeded_runs=stats.succeeded_runs,
        failed_runs=stats.failed_runs,
        cancelled_runs=stats.cancelled_runs,
        success_rate=round(stats.success_rate, 2),
        average_duration_seconds=stats.average_duration_seconds,
        fastest_run_name=stats.fastest_run_name,
        slowest_run_name=stats.slowest_run_name,
    )

mutants_x__stats_payload__mutmut['_mutmut_orig'] = x__stats_payload__mutmut_orig # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_1'] = x__stats_payload__mutmut_1 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_2'] = x__stats_payload__mutmut_2 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_3'] = x__stats_payload__mutmut_3 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_4'] = x__stats_payload__mutmut_4 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_5'] = x__stats_payload__mutmut_5 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_6'] = x__stats_payload__mutmut_6 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_7'] = x__stats_payload__mutmut_7 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_8'] = x__stats_payload__mutmut_8 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_9'] = x__stats_payload__mutmut_9 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_10'] = x__stats_payload__mutmut_10 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_11'] = x__stats_payload__mutmut_11 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_12'] = x__stats_payload__mutmut_12 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_13'] = x__stats_payload__mutmut_13 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_14'] = x__stats_payload__mutmut_14 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_15'] = x__stats_payload__mutmut_15 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_16'] = x__stats_payload__mutmut_16 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_17'] = x__stats_payload__mutmut_17 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_18'] = x__stats_payload__mutmut_18 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_19'] = x__stats_payload__mutmut_19 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_20'] = x__stats_payload__mutmut_20 # type: ignore # mutmut generated
mutants_x__stats_payload__mutmut['x__stats_payload__mutmut_21'] = x__stats_payload__mutmut_21 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_pipeline_runs__mutmut)
def list_pipeline_runs(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_orig(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_1(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = None
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_2(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = None
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_3(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=None)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_4(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = None
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_5(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            None
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_6(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=None, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_7(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=None)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_8(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_9(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, )
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_10(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = None  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_11(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(None)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_12(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "XXrunsXX": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_13(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "RUNS": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_14(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "XXstatsXX": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_15(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "STATS": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_16(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(None),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_17(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "XXoutliersXX": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_18(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "OUTLIERS": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_19(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "XXnoteXX": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_20(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "NOTE": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_21(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_22(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_23(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXrunsXX": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_24(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"RUNS": [], "error": str(exc)}


def x_list_pipeline_runs__mutmut_25(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "XXerrorXX": str(exc)}


def x_list_pipeline_runs__mutmut_26(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "ERROR": str(exc)}


def x_list_pipeline_runs__mutmut_27(
    service_name: str, namespace: str | None = None, limit: int | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        adapter = build_tekton_adapter()
        use_case = ListPipelineRunsUseCase(tekton_port=adapter)
        r = use_case.execute(
            ListPipelineRunsCommand(service_name=service_name, namespace=namespace)
        )
        runs: list[dict[str, object]] = list(r.runs)  # type: ignore[arg-type]
        return {
            "runs": runs,
            "stats": _stats_payload(r.stats),
            "outliers": r.outliers,
            "note": r.note,
            "error": r.error,
        }
    except Exception as exc:
        return {"runs": [], "error": str(None)}

mutants_x_list_pipeline_runs__mutmut['_mutmut_orig'] = x_list_pipeline_runs__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_1'] = x_list_pipeline_runs__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_2'] = x_list_pipeline_runs__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_3'] = x_list_pipeline_runs__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_4'] = x_list_pipeline_runs__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_5'] = x_list_pipeline_runs__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_6'] = x_list_pipeline_runs__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_7'] = x_list_pipeline_runs__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_8'] = x_list_pipeline_runs__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_9'] = x_list_pipeline_runs__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_10'] = x_list_pipeline_runs__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_11'] = x_list_pipeline_runs__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_12'] = x_list_pipeline_runs__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_13'] = x_list_pipeline_runs__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_14'] = x_list_pipeline_runs__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_15'] = x_list_pipeline_runs__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_16'] = x_list_pipeline_runs__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_17'] = x_list_pipeline_runs__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_18'] = x_list_pipeline_runs__mutmut_18 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_19'] = x_list_pipeline_runs__mutmut_19 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_20'] = x_list_pipeline_runs__mutmut_20 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_21'] = x_list_pipeline_runs__mutmut_21 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_22'] = x_list_pipeline_runs__mutmut_22 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_23'] = x_list_pipeline_runs__mutmut_23 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_24'] = x_list_pipeline_runs__mutmut_24 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_25'] = x_list_pipeline_runs__mutmut_25 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_26'] = x_list_pipeline_runs__mutmut_26 # type: ignore # mutmut generated
mutants_x_list_pipeline_runs__mutmut['x_list_pipeline_runs__mutmut_27'] = x_list_pipeline_runs__mutmut_27 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(list_pipeline_runs)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(list_pipeline_runs)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
