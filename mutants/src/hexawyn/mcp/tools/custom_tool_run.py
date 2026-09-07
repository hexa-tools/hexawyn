"""MCP tool: custom_tool_run — Execute a custom tool via the control-plane."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_custom_tool_run__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_custom_tool_run__mutmut)
def custom_tool_run(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_orig(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_1(name: str, params: str = "XX{}XX") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_2(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = None
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_3(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(None) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_4(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"XXerrorXX": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_5(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"ERROR": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_6(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = None
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_7(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_8(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"XXerrorXX": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_9(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"ERROR": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_10(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "XXRuntime endpoint not configuredXX"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_11(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_12(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "RUNTIME ENDPOINT NOT CONFIGURED"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_13(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = None
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_14(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=None)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_15(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

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


def x_custom_tool_run__mutmut_16(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(None, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_17(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, None)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_18(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_19(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, )
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_20(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = ""
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_21(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["XXerrorXX"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_22(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["ERROR"] = None
        return result
    except Exception as exc:
        return {"error": str(exc)}


def x_custom_tool_run__mutmut_23(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_custom_tool_run__mutmut_24(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_custom_tool_run__mutmut_25(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.infrastructure.adapters.secondary.runtime_client import RuntimeClient
    from hexawyn.infrastructure.config.config_manager import get_runtime_endpoint

    try:
        parsed_params: dict[str, object] = json.loads(params) if isinstance(params, str) else {}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON params: {params}"}

    try:
        endpoint = get_runtime_endpoint()
        if not endpoint:
            return {"error": "Runtime endpoint not configured"}
        client = RuntimeClient(endpoint=endpoint)
        result = client.run_custom_tool(name, parsed_params)
        client.close()
        result["error"] = None
        return result
    except Exception as exc:
        return {"error": str(None)}

mutants_x_custom_tool_run__mutmut['_mutmut_orig'] = x_custom_tool_run__mutmut_orig # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_1'] = x_custom_tool_run__mutmut_1 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_2'] = x_custom_tool_run__mutmut_2 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_3'] = x_custom_tool_run__mutmut_3 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_4'] = x_custom_tool_run__mutmut_4 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_5'] = x_custom_tool_run__mutmut_5 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_6'] = x_custom_tool_run__mutmut_6 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_7'] = x_custom_tool_run__mutmut_7 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_8'] = x_custom_tool_run__mutmut_8 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_9'] = x_custom_tool_run__mutmut_9 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_10'] = x_custom_tool_run__mutmut_10 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_11'] = x_custom_tool_run__mutmut_11 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_12'] = x_custom_tool_run__mutmut_12 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_13'] = x_custom_tool_run__mutmut_13 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_14'] = x_custom_tool_run__mutmut_14 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_15'] = x_custom_tool_run__mutmut_15 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_16'] = x_custom_tool_run__mutmut_16 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_17'] = x_custom_tool_run__mutmut_17 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_18'] = x_custom_tool_run__mutmut_18 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_19'] = x_custom_tool_run__mutmut_19 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_20'] = x_custom_tool_run__mutmut_20 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_21'] = x_custom_tool_run__mutmut_21 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_22'] = x_custom_tool_run__mutmut_22 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_23'] = x_custom_tool_run__mutmut_23 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_24'] = x_custom_tool_run__mutmut_24 # type: ignore # mutmut generated
mutants_x_custom_tool_run__mutmut['x_custom_tool_run__mutmut_25'] = x_custom_tool_run__mutmut_25 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(custom_tool_run)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(custom_tool_run)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
