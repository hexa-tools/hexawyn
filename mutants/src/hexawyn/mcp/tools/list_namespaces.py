"""MCP tool: list_namespaces — List all namespaces with age overview."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.list_namespaces.command import ListNamespacesCommand
from hexawyn.application.use_case.cluster.list_namespaces.list_namespaces_use_case import (
    ListNamespacesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_list_namespaces__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_namespaces__mutmut)
def list_namespaces() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_orig() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_1() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = None
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_2() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = None
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_3() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=None)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_4() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = None
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_5() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(None)
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_6() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"XXnamespacesXX": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_7() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"NAMESPACES": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_8() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(None), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_9() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "XXerrorXX": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_10() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "ERROR": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(exc)}


def x_list_namespaces__mutmut_11() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"XXnamespacesXX": [], "error": str(exc)}


def x_list_namespaces__mutmut_12() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"NAMESPACES": [], "error": str(exc)}


def x_list_namespaces__mutmut_13() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "XXerrorXX": str(exc)}


def x_list_namespaces__mutmut_14() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "ERROR": str(exc)}


def x_list_namespaces__mutmut_15() -> dict[str, object]:
    """List all Kubernetes namespaces with a quick age overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListNamespacesUseCase(k8s_port=adapter)
        response = use_case.execute(ListNamespacesCommand())
        return {"namespaces": list(response.namespaces), "error": None}
    except Exception as exc:
        return {"namespaces": [], "error": str(None)}

mutants_x_list_namespaces__mutmut['_mutmut_orig'] = x_list_namespaces__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_1'] = x_list_namespaces__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_2'] = x_list_namespaces__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_3'] = x_list_namespaces__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_4'] = x_list_namespaces__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_5'] = x_list_namespaces__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_6'] = x_list_namespaces__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_7'] = x_list_namespaces__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_8'] = x_list_namespaces__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_9'] = x_list_namespaces__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_10'] = x_list_namespaces__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_11'] = x_list_namespaces__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_12'] = x_list_namespaces__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_13'] = x_list_namespaces__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_14'] = x_list_namespaces__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_namespaces__mutmut['x_list_namespaces__mutmut_15'] = x_list_namespaces__mutmut_15 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(list_namespaces)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(list_namespaces)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
