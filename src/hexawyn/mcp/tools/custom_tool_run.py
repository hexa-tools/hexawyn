"""MCP tool: custom_tool_run — Execute a custom tool via the control-plane."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def custom_tool_run(name: str, params: str = "{}") -> dict[str, object]:
    """Run a custom tool by name with JSON-encoded params. Returns findings, success, provenance."""
    import json

    from hexawyn.adapters.secondary.runtime_client import RuntimeClient
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


def register(mcp: FastMCP) -> None:
    mcp.tool()(custom_tool_run)
