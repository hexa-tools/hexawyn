"""MCP tool: list_openshift_sccs."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.openshift.list_openshift_sccs.command import (
    ListOpenshiftSccsCommand,
)
from hexawyn.application.use_case.openshift.list_openshift_sccs.list_openshift_sccs_use_case import (  # noqa: E501
    ListOpenshiftSccsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_list_openshift_sccs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_openshift_sccs__mutmut)
def list_openshift_sccs() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = None
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=None)
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = None
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(None)
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"XXitemsXX": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"ITEMS": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "XXcountXX": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "COUNT": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "XXerrorXX": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "ERROR": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"XXitemsXX": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"ITEMS": [], "count": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "XXcountXX": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "COUNT": 0, "error": str(exc)}


def x_list_openshift_sccs__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 1, "error": str(exc)}


def x_list_openshift_sccs__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "XXerrorXX": str(exc)}


def x_list_openshift_sccs__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "ERROR": str(exc)}


def x_list_openshift_sccs__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_openshift_resource_adapter

    try:
        use_case = ListOpenshiftSccsUseCase(port=build_openshift_resource_adapter())
        r = use_case.execute(ListOpenshiftSccsCommand())
        return {"items": r.items, "count": r.count, "error": r.error}
    except Exception as exc:
        return {"items": [], "count": 0, "error": str(None)}

mutants_x_list_openshift_sccs__mutmut['_mutmut_orig'] = x_list_openshift_sccs__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_1'] = x_list_openshift_sccs__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_2'] = x_list_openshift_sccs__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_3'] = x_list_openshift_sccs__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_4'] = x_list_openshift_sccs__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_5'] = x_list_openshift_sccs__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_6'] = x_list_openshift_sccs__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_7'] = x_list_openshift_sccs__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_8'] = x_list_openshift_sccs__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_9'] = x_list_openshift_sccs__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_10'] = x_list_openshift_sccs__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_11'] = x_list_openshift_sccs__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_12'] = x_list_openshift_sccs__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_13'] = x_list_openshift_sccs__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_14'] = x_list_openshift_sccs__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_15'] = x_list_openshift_sccs__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_16'] = x_list_openshift_sccs__mutmut_16 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_17'] = x_list_openshift_sccs__mutmut_17 # type: ignore # mutmut generated
mutants_x_list_openshift_sccs__mutmut['x_list_openshift_sccs__mutmut_18'] = x_list_openshift_sccs__mutmut_18 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(list_openshift_sccs)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(list_openshift_sccs)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
