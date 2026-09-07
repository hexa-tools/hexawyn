"""MCP tool: custom_tool_describe — Show a custom tool's contract."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_custom_tool_describe__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_custom_tool_describe__mutmut)
def custom_tool_describe(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_orig(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_1(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = None
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_2(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_3(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"XXerrorXX": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_4(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"ERROR": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_5(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "XXRuntime endpoint not configuredXX"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_6(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_7(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "RUNTIME ENDPOINT NOT CONFIGURED"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_8(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = None
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_9(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=None)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_10(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = None
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_11(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(None)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_12(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = ""
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_13(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["XXerrorXX"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_14(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["ERROR"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_describe__mutmut_15(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_custom_tool_describe__mutmut_16(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_custom_tool_describe__mutmut_17(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.describe_custom_tool(name)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(None)}

mutants_x_custom_tool_describe__mutmut['_mutmut_orig'] = x_custom_tool_describe__mutmut_orig # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_1'] = x_custom_tool_describe__mutmut_1 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_2'] = x_custom_tool_describe__mutmut_2 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_3'] = x_custom_tool_describe__mutmut_3 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_4'] = x_custom_tool_describe__mutmut_4 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_5'] = x_custom_tool_describe__mutmut_5 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_6'] = x_custom_tool_describe__mutmut_6 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_7'] = x_custom_tool_describe__mutmut_7 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_8'] = x_custom_tool_describe__mutmut_8 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_9'] = x_custom_tool_describe__mutmut_9 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_10'] = x_custom_tool_describe__mutmut_10 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_11'] = x_custom_tool_describe__mutmut_11 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_12'] = x_custom_tool_describe__mutmut_12 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_13'] = x_custom_tool_describe__mutmut_13 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_14'] = x_custom_tool_describe__mutmut_14 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_15'] = x_custom_tool_describe__mutmut_15 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_16'] = x_custom_tool_describe__mutmut_16 # type: ignore # mutmut generated
mutants_x_custom_tool_describe__mutmut['x_custom_tool_describe__mutmut_17'] = x_custom_tool_describe__mutmut_17 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(custom_tool_describe)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(custom_tool_describe)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
