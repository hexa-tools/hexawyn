"""MCP tool: list_openshift_routes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.openshift.list_openshift_routes.command import (
    ListOpenshiftRoutesCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_routes.list_openshift_routes_use_case import (  # noqa: E501
    ListOpenshiftRoutesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_list_openshift_routes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_openshift_routes__mutmut)
def list_openshift_routes(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_orig(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_1(namespace: str = "XXdefaultXX") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_2(namespace: str = "DEFAULT") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_3(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = None
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_4(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=None)
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_5(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = None
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_6(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(None)
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_7(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=None))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_8(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"XXitemsXX": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_9(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"ITEMS": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_10(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "XXcountXX": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_11(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "COUNT": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_12(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "XXerrorXX": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_13(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "ERROR": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_14(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"XXitemsXX": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_15(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"ITEMS": [], "count": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_16(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "XXcountXX": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_17(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "COUNT": 0, "error": str(exc)}


def x_list_openshift_routes__mutmut_18(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 1, "error": str(exc)}


def x_list_openshift_routes__mutmut_19(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "XXerrorXX": str(exc)}


def x_list_openshift_routes__mutmut_20(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "ERROR": str(exc)}


def x_list_openshift_routes__mutmut_21(namespace: str = "default") -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftRoutesUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftRoutesCommand(namespace=namespace))
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(None)}

mutants_x_list_openshift_routes__mutmut['_mutmut_orig'] = x_list_openshift_routes__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_1'] = x_list_openshift_routes__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_2'] = x_list_openshift_routes__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_3'] = x_list_openshift_routes__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_4'] = x_list_openshift_routes__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_5'] = x_list_openshift_routes__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_6'] = x_list_openshift_routes__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_7'] = x_list_openshift_routes__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_8'] = x_list_openshift_routes__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_9'] = x_list_openshift_routes__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_10'] = x_list_openshift_routes__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_11'] = x_list_openshift_routes__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_12'] = x_list_openshift_routes__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_13'] = x_list_openshift_routes__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_14'] = x_list_openshift_routes__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_15'] = x_list_openshift_routes__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_16'] = x_list_openshift_routes__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_17'] = x_list_openshift_routes__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_18'] = x_list_openshift_routes__mutmut_18 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_19'] = x_list_openshift_routes__mutmut_19 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_20'] = x_list_openshift_routes__mutmut_20 # type: ignore # mutmut generated
mutants_x_list_openshift_routes__mutmut['x_list_openshift_routes__mutmut_21'] = x_list_openshift_routes__mutmut_21 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(list_openshift_routes)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(list_openshift_routes)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
