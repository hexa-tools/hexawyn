"""MCP tool: custom_tools_list — List all registered custom tools."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_custom_tools_list__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_custom_tools_list__mutmut)
def custom_tools_list() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_orig() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_1() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = None
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_2() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_3() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"XXtoolsXX": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_4() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"TOOLS": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_5() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "XXcountXX": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_6() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "COUNT": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_7() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 1, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_8() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "XXerrorXX": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_9() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "ERROR": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_10() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "XXRuntime endpoint not configuredXX"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_11() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_12() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "RUNTIME ENDPOINT NOT CONFIGURED"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_13() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = None
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_14() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=None)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_15() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = None
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_16() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"XXtoolsXX": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_17() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"TOOLS": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_18() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "XXcountXX": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_19() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "COUNT": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_20() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "XXerrorXX": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_21() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "ERROR": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_22() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"XXtoolsXX": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_23() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"TOOLS": [], "count": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_24() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "XXcountXX": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_25() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "COUNT": 0, "error": str(exc)}


def x_custom_tools_list__mutmut_26() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 1, "error": str(exc)}


def x_custom_tools_list__mutmut_27() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "XXerrorXX": str(exc)}


def x_custom_tools_list__mutmut_28() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "ERROR": str(exc)}


def x_custom_tools_list__mutmut_29() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"tools": [], "count": 0, "error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        tools = client.list_custom_tools()
        client.close()
        return {"tools": tools, "count": len(tools), "error": None}
    except Exception as exc:
        return {"tools": [], "count": 0, "error": str(None)}

mutants_x_custom_tools_list__mutmut['_mutmut_orig'] = x_custom_tools_list__mutmut_orig # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_1'] = x_custom_tools_list__mutmut_1 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_2'] = x_custom_tools_list__mutmut_2 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_3'] = x_custom_tools_list__mutmut_3 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_4'] = x_custom_tools_list__mutmut_4 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_5'] = x_custom_tools_list__mutmut_5 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_6'] = x_custom_tools_list__mutmut_6 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_7'] = x_custom_tools_list__mutmut_7 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_8'] = x_custom_tools_list__mutmut_8 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_9'] = x_custom_tools_list__mutmut_9 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_10'] = x_custom_tools_list__mutmut_10 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_11'] = x_custom_tools_list__mutmut_11 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_12'] = x_custom_tools_list__mutmut_12 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_13'] = x_custom_tools_list__mutmut_13 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_14'] = x_custom_tools_list__mutmut_14 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_15'] = x_custom_tools_list__mutmut_15 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_16'] = x_custom_tools_list__mutmut_16 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_17'] = x_custom_tools_list__mutmut_17 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_18'] = x_custom_tools_list__mutmut_18 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_19'] = x_custom_tools_list__mutmut_19 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_20'] = x_custom_tools_list__mutmut_20 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_21'] = x_custom_tools_list__mutmut_21 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_22'] = x_custom_tools_list__mutmut_22 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_23'] = x_custom_tools_list__mutmut_23 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_24'] = x_custom_tools_list__mutmut_24 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_25'] = x_custom_tools_list__mutmut_25 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_26'] = x_custom_tools_list__mutmut_26 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_27'] = x_custom_tools_list__mutmut_27 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_28'] = x_custom_tools_list__mutmut_28 # type: ignore # mutmut generated
mutants_x_custom_tools_list__mutmut['x_custom_tools_list__mutmut_29'] = x_custom_tools_list__mutmut_29 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(custom_tools_list)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(custom_tools_list)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
