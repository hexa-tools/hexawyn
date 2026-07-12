"""MCP tool: custom_tools_list — List all registered custom tools."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def custom_tools_list() -> dict[str, object]:
    """List all registered custom tools with transport, endpoint, and description."""
    from hexawyn.adapters.secondary.runtime_client import RuntimeClient
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


def register(mcp: FastMCP) -> None:
    mcp.tool()(custom_tools_list)
