"""MCP tool: keda_scaledjobs_list — List KEDA ScaledJobs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.keda.keda_scaledjobs_list.command import KedaScaledjobsListCommand
from hexawyn.application.use_case.keda.keda_scaledjobs_list.keda_scaledjobs_list_use_case import (
    KedaScaledjobsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_keda_scaledjobs_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_keda_scaledjobs_list__mutmut)
def keda_scaledjobs_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = None
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = None
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=None)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = None
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(None)
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=None))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"XXscaled_jobsXX": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"SCALED_JOBS": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "XXerrorXX": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "ERROR": response.error}
    except Exception as exc:
        return {"error": str(exc)}


def x_keda_scaledjobs_list__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_keda_scaledjobs_list__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_keda_scaledjobs_list__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_keda_adapter

    try:
        adapter = build_keda_adapter()
        use_case = KedaScaledjobsListUseCase(port=adapter)
        response = use_case.execute(KedaScaledjobsListCommand(namespace=namespace))
        return {"scaled_jobs": response.scaled_jobs, "error": response.error}
    except Exception as exc:
        return {"error": str(None)}

mutants_x_keda_scaledjobs_list__mutmut['_mutmut_orig'] = x_keda_scaledjobs_list__mutmut_orig # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_1'] = x_keda_scaledjobs_list__mutmut_1 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_2'] = x_keda_scaledjobs_list__mutmut_2 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_3'] = x_keda_scaledjobs_list__mutmut_3 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_4'] = x_keda_scaledjobs_list__mutmut_4 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_5'] = x_keda_scaledjobs_list__mutmut_5 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_6'] = x_keda_scaledjobs_list__mutmut_6 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_7'] = x_keda_scaledjobs_list__mutmut_7 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_8'] = x_keda_scaledjobs_list__mutmut_8 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_9'] = x_keda_scaledjobs_list__mutmut_9 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_10'] = x_keda_scaledjobs_list__mutmut_10 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_11'] = x_keda_scaledjobs_list__mutmut_11 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_12'] = x_keda_scaledjobs_list__mutmut_12 # type: ignore # mutmut generated
mutants_x_keda_scaledjobs_list__mutmut['x_keda_scaledjobs_list__mutmut_13'] = x_keda_scaledjobs_list__mutmut_13 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledjobs_list)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(keda_scaledjobs_list)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
