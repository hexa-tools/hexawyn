"""MCP tool: custom_tool_describe — Show a custom tool's contract."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def custom_tool_describe(name: str) -> dict[str, object]:
    """Describe a custom tool: parameters, output schema, transport, endpoint."""
    from hexawyn.adapters.secondary.runtime_client import RuntimeClient
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


def register(mcp: FastMCP) -> None:
    mcp.tool()(custom_tool_describe)
