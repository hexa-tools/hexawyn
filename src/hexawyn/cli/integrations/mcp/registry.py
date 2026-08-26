"""MCP client integration registry — maps client names to implementations.

Future coding-agent integrations (OpenCode, Codex, Cursor, ...) register
here without touching the CLI command architecture.
"""

from __future__ import annotations

from collections.abc import Callable

from hexawyn.cli.integrations.mcp.base import MCPClientIntegration
from hexawyn.cli.integrations.mcp.claude import ClaudeCodeIntegration
from hexawyn.cli.integrations.mcp.codex import CodexIntegration
from hexawyn.cli.integrations.mcp.cursor import CursorIntegration
from hexawyn.cli.integrations.mcp.deepseek import DeepSeekHarnessIntegration
from hexawyn.cli.integrations.mcp.gemini import GeminiIntegration
from hexawyn.cli.integrations.mcp.opencode import OpenCodeIntegration

_CLIENT_REGISTRY: dict[str, Callable[..., MCPClientIntegration]] = {
    "claude": ClaudeCodeIntegration,
    "codex": CodexIntegration,
    "opencode": OpenCodeIntegration,
    "cursor": CursorIntegration,
    "gemini": GeminiIntegration,
    "deepseek": DeepSeekHarnessIntegration,
}


def list_clients() -> list[str]:
    return sorted(_CLIENT_REGISTRY)


def get_integration(client: str) -> MCPClientIntegration:
    factory = _CLIENT_REGISTRY.get(client)
    if factory is None:
        available = ", ".join(list_clients())
        raise KeyError(f"Unknown MCP client {client!r}. Available: {available}")
    return factory()
