"""MCP tool: rollouts_list — List all Argo Rollouts."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.rollouts_list.command import RolloutsListCommand
from hexawyn.application.use_case.workloads.rollouts_list.rollouts_list_use_case import (
    RolloutsListUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_rollouts_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_rollouts_list__mutmut)
def rollouts_list(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = None
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = None
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=None)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = None
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(None)
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=None))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"XXrolloutsXX": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"ROLLOUTS": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "XXerrorXX": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "ERROR": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(exc)}


def x_rollouts_list__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"XXrolloutsXX": [], "error": str(exc)}


def x_rollouts_list__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"ROLLOUTS": [], "error": str(exc)}


def x_rollouts_list__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "XXerrorXX": str(exc)}


def x_rollouts_list__mutmut_14(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "ERROR": str(exc)}


def x_rollouts_list__mutmut_15(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_rollouts_adapter

    try:
        adapter = build_rollouts_adapter()
        use_case = RolloutsListUseCase(rollouts_port=adapter)
        response = use_case.execute(RolloutsListCommand(namespace=namespace))
        return {"rollouts": response.rollouts, "error": response.error}
    except Exception as exc:
        return {"rollouts": [], "error": str(None)}

mutants_x_rollouts_list__mutmut['_mutmut_orig'] = x_rollouts_list__mutmut_orig # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_1'] = x_rollouts_list__mutmut_1 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_2'] = x_rollouts_list__mutmut_2 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_3'] = x_rollouts_list__mutmut_3 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_4'] = x_rollouts_list__mutmut_4 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_5'] = x_rollouts_list__mutmut_5 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_6'] = x_rollouts_list__mutmut_6 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_7'] = x_rollouts_list__mutmut_7 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_8'] = x_rollouts_list__mutmut_8 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_9'] = x_rollouts_list__mutmut_9 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_10'] = x_rollouts_list__mutmut_10 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_11'] = x_rollouts_list__mutmut_11 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_12'] = x_rollouts_list__mutmut_12 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_13'] = x_rollouts_list__mutmut_13 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_14'] = x_rollouts_list__mutmut_14 # type: ignore # mutmut generated
mutants_x_rollouts_list__mutmut['x_rollouts_list__mutmut_15'] = x_rollouts_list__mutmut_15 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(rollouts_list)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(rollouts_list)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
