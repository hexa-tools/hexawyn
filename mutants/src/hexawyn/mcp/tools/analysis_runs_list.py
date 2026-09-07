"""MCP tool: analysis_runs_list — List AnalysisRuns."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.analysis_runs_list.analysis_runs_list_use_case import (
    AnalysisRunsListUseCase,
)
from hexawyn.application.use_case.pipelines.analysis_runs_list.command import (
    AnalysisRunsListCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_analysis_runs_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analysis_runs_list__mutmut)
def analysis_runs_list(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_orig(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_1(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = None
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_2(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=None)
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_3(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = None
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_4(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            None
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_5(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=None, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_6(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=None)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_7(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_8(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, )
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_9(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"XXanalysis_runsXX": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_10(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"ANALYSIS_RUNS": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_11(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "XXerrorXX": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_12(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "ERROR": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_13(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"XXanalysis_runsXX": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_14(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"ANALYSIS_RUNS": [], "error": str(exc)}


def x_analysis_runs_list__mutmut_15(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "XXerrorXX": str(exc)}


def x_analysis_runs_list__mutmut_16(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "ERROR": str(exc)}


def x_analysis_runs_list__mutmut_17(
    rollout_name: str | None = None, namespace: str | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        use_case = AnalysisRunsListUseCase(rollouts_port=build_rollouts_adapter())
        r = use_case.execute(
            AnalysisRunsListCommand(namespace=namespace, rollout_name=rollout_name)
        )
        return {"analysis_runs": r.analysis_runs, "error": r.error}
    except Exception as exc:
        return {"analysis_runs": [], "error": str(None)}

mutants_x_analysis_runs_list__mutmut['_mutmut_orig'] = x_analysis_runs_list__mutmut_orig # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_1'] = x_analysis_runs_list__mutmut_1 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_2'] = x_analysis_runs_list__mutmut_2 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_3'] = x_analysis_runs_list__mutmut_3 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_4'] = x_analysis_runs_list__mutmut_4 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_5'] = x_analysis_runs_list__mutmut_5 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_6'] = x_analysis_runs_list__mutmut_6 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_7'] = x_analysis_runs_list__mutmut_7 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_8'] = x_analysis_runs_list__mutmut_8 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_9'] = x_analysis_runs_list__mutmut_9 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_10'] = x_analysis_runs_list__mutmut_10 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_11'] = x_analysis_runs_list__mutmut_11 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_12'] = x_analysis_runs_list__mutmut_12 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_13'] = x_analysis_runs_list__mutmut_13 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_14'] = x_analysis_runs_list__mutmut_14 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_15'] = x_analysis_runs_list__mutmut_15 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_16'] = x_analysis_runs_list__mutmut_16 # type: ignore # mutmut generated
mutants_x_analysis_runs_list__mutmut['x_analysis_runs_list__mutmut_17'] = x_analysis_runs_list__mutmut_17 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(analysis_runs_list)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(analysis_runs_list)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
