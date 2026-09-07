"""MCP tool: check_resource_constraints — CPU/memory pressure report for a namespace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.check_resource_constraints.check_resource_constraints_use_case import (  # noqa: E501
    CheckResourceConstraintsUseCase,
)
from hexawyn.application.use_case.cluster.check_resource_constraints.command import (
    CheckResourceConstraintsCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_check_resource_constraints__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_check_resource_constraints__mutmut)
def check_resource_constraints(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_orig(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_1(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = None  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_2(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=None)  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_3(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = None  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_4(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(None)  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_5(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=None))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_6(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"XXcontainersXX": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_7(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"CONTAINERS": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_8(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "XXsummaryXX": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_9(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "SUMMARY": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_10(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "XXerrorXX": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_11(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "ERROR": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_12(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"XXcontainersXX": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_13(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"CONTAINERS": [], "summary": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_14(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "XXsummaryXX": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_15(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "SUMMARY": "", "error": str(exc)}


def x_check_resource_constraints__mutmut_16(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "XXXX", "error": str(exc)}


def x_check_resource_constraints__mutmut_17(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "XXerrorXX": str(exc)}


def x_check_resource_constraints__mutmut_18(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "ERROR": str(exc)}


def x_check_resource_constraints__mutmut_19(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        use_case = CheckResourceConstraintsUseCase(port=build_k8s_adapter())  # type: ignore
        r = use_case.execute(CheckResourceConstraintsCommand(namespace=namespace))  # type: ignore
        return {"containers": r.containers, "summary": r.summary, "error": r.error}  # type: ignore
    except Exception as exc:
        return {"containers": [], "summary": "", "error": str(None)}

mutants_x_check_resource_constraints__mutmut['_mutmut_orig'] = x_check_resource_constraints__mutmut_orig # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_1'] = x_check_resource_constraints__mutmut_1 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_2'] = x_check_resource_constraints__mutmut_2 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_3'] = x_check_resource_constraints__mutmut_3 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_4'] = x_check_resource_constraints__mutmut_4 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_5'] = x_check_resource_constraints__mutmut_5 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_6'] = x_check_resource_constraints__mutmut_6 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_7'] = x_check_resource_constraints__mutmut_7 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_8'] = x_check_resource_constraints__mutmut_8 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_9'] = x_check_resource_constraints__mutmut_9 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_10'] = x_check_resource_constraints__mutmut_10 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_11'] = x_check_resource_constraints__mutmut_11 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_12'] = x_check_resource_constraints__mutmut_12 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_13'] = x_check_resource_constraints__mutmut_13 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_14'] = x_check_resource_constraints__mutmut_14 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_15'] = x_check_resource_constraints__mutmut_15 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_16'] = x_check_resource_constraints__mutmut_16 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_17'] = x_check_resource_constraints__mutmut_17 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_18'] = x_check_resource_constraints__mutmut_18 # type: ignore # mutmut generated
mutants_x_check_resource_constraints__mutmut['x_check_resource_constraints__mutmut_19'] = x_check_resource_constraints__mutmut_19 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(check_resource_constraints)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(check_resource_constraints)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
