"""MCP tool: get_namespace_resource_allocation — Rank namespaces by CPU/memory requests + pod count."""  # noqa: E501

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.command import (
    GetNamespaceResourceAllocationCommand,
)
from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.get_namespace_resource_allocation_use_case import (  # noqa: E501
    GetNamespaceResourceAllocationUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_namespace_resource_allocation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_namespace_resource_allocation__mutmut)
def get_namespace_resource_allocation() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_orig() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_1() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = None
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_2() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = None
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_3() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=None)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_4() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = None
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_5() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(None)
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_6() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"XXallocationsXX": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_7() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"ALLOCATIONS": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_8() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(None), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_9() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "XXerrorXX": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_10() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "ERROR": None}
    except Exception as exc:
        return {"allocations": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_11() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"XXallocationsXX": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_12() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"ALLOCATIONS": [], "error": str(exc)}


def x_get_namespace_resource_allocation__mutmut_13() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "XXerrorXX": str(exc)}


def x_get_namespace_resource_allocation__mutmut_14() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "ERROR": str(exc)}


def x_get_namespace_resource_allocation__mutmut_15() -> dict[str, object]:
    """Rank all namespaces by total CPU and memory requests, including pod count."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = GetNamespaceResourceAllocationUseCase(k8s_port=adapter)
        response = use_case.execute(GetNamespaceResourceAllocationCommand())
        return {"allocations": list(response.allocations), "error": None}
    except Exception as exc:
        return {"allocations": [], "error": str(None)}

mutants_x_get_namespace_resource_allocation__mutmut['_mutmut_orig'] = x_get_namespace_resource_allocation__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_1'] = x_get_namespace_resource_allocation__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_2'] = x_get_namespace_resource_allocation__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_3'] = x_get_namespace_resource_allocation__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_4'] = x_get_namespace_resource_allocation__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_5'] = x_get_namespace_resource_allocation__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_6'] = x_get_namespace_resource_allocation__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_7'] = x_get_namespace_resource_allocation__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_8'] = x_get_namespace_resource_allocation__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_9'] = x_get_namespace_resource_allocation__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_10'] = x_get_namespace_resource_allocation__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_11'] = x_get_namespace_resource_allocation__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_12'] = x_get_namespace_resource_allocation__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_13'] = x_get_namespace_resource_allocation__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_14'] = x_get_namespace_resource_allocation__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_namespace_resource_allocation__mutmut['x_get_namespace_resource_allocation__mutmut_15'] = x_get_namespace_resource_allocation__mutmut_15 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(get_namespace_resource_allocation)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(get_namespace_resource_allocation)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
