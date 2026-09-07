"""MCP tool: list_task_runs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.pipelines.list_task_runs.command import ListTaskRunsCommand
from hexawyn.application.use_case.pipelines.list_task_runs.list_task_runs_use_case import (
    ListTaskRunsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_list_task_runs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_task_runs__mutmut)
def list_task_runs(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_orig(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_1(pipeline_name: str = "XXXX", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_2(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = None
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_3(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=None)
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_4(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = None
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_5(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(None)
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_6(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=None, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_7(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=None))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_8(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_9(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, ))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_10(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"XXtask_runsXX": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_11(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"TASK_RUNS": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_12(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "XXerrorXX": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_13(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "ERROR": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(exc)}


def x_list_task_runs__mutmut_14(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"XXtask_runsXX": [], "error": str(exc)}


def x_list_task_runs__mutmut_15(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"TASK_RUNS": [], "error": str(exc)}


def x_list_task_runs__mutmut_16(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "XXerrorXX": str(exc)}


def x_list_task_runs__mutmut_17(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "ERROR": str(exc)}


def x_list_task_runs__mutmut_18(pipeline_name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_tekton_adapter

    try:
        use_case = ListTaskRunsUseCase(tekton_port=build_tekton_adapter())
        r = use_case.execute(ListTaskRunsCommand(pipeline_name=pipeline_name, namespace=namespace))
        return {"task_runs": r.task_runs, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"task_runs": [], "error": str(None)}

mutants_x_list_task_runs__mutmut['_mutmut_orig'] = x_list_task_runs__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_1'] = x_list_task_runs__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_2'] = x_list_task_runs__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_3'] = x_list_task_runs__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_4'] = x_list_task_runs__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_5'] = x_list_task_runs__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_6'] = x_list_task_runs__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_7'] = x_list_task_runs__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_8'] = x_list_task_runs__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_9'] = x_list_task_runs__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_10'] = x_list_task_runs__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_11'] = x_list_task_runs__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_12'] = x_list_task_runs__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_13'] = x_list_task_runs__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_14'] = x_list_task_runs__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_15'] = x_list_task_runs__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_16'] = x_list_task_runs__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_17'] = x_list_task_runs__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_task_runs__mutmut['x_list_task_runs__mutmut_18'] = x_list_task_runs__mutmut_18 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(list_task_runs)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(list_task_runs)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
