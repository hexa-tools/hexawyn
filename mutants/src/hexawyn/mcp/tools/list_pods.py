"""MCP tool: list_pods — List all pods in a namespace."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.list_pods.command import ListPodsCommand
from hexawyn.application.use_case.workloads.list_pods.list_pods_use_case import ListPodsUseCase

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_list_pods__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_pods__mutmut)
def list_pods(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_orig(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_1(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = None
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_2(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = None
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_3(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=None)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_4(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = None
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_5(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(None)
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_6(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=None))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_7(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"XXpodsXX": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_8(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"PODS": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_9(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(None), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_10(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "XXerrorXX": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_11(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "ERROR": None}
    except Exception as exc:
        return {"pods": [], "error": str(exc)}


def x_list_pods__mutmut_12(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"XXpodsXX": [], "error": str(exc)}


def x_list_pods__mutmut_13(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"PODS": [], "error": str(exc)}


def x_list_pods__mutmut_14(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "XXerrorXX": str(exc)}


def x_list_pods__mutmut_15(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "ERROR": str(exc)}


def x_list_pods__mutmut_16(namespace: str) -> dict[str, object]:
    """List all pods in a namespace with health overview."""
    from hexawyn.mcp.server import build_k8s_adapter

    try:
        adapter = build_k8s_adapter()
        use_case = ListPodsUseCase(k8s_port=adapter)
        response = use_case.execute(ListPodsCommand(namespace=namespace))
        return {"pods": list(response.pods), "error": None}
    except Exception as exc:
        return {"pods": [], "error": str(None)}

mutants_x_list_pods__mutmut['_mutmut_orig'] = x_list_pods__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_1'] = x_list_pods__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_2'] = x_list_pods__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_3'] = x_list_pods__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_4'] = x_list_pods__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_5'] = x_list_pods__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_6'] = x_list_pods__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_7'] = x_list_pods__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_8'] = x_list_pods__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_9'] = x_list_pods__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_10'] = x_list_pods__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_11'] = x_list_pods__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_12'] = x_list_pods__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_13'] = x_list_pods__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_14'] = x_list_pods__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_15'] = x_list_pods__mutmut_15 # type: ignore # mutmut generated
mutants_x_list_pods__mutmut['x_list_pods__mutmut_16'] = x_list_pods__mutmut_16 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(list_pods)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(list_pods)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
