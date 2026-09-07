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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_list_clients__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_clients__mutmut)
def list_clients() -> list[str]:
    return sorted(_CLIENT_REGISTRY)


def x_list_clients__mutmut_orig() -> list[str]:
    return sorted(_CLIENT_REGISTRY)


def x_list_clients__mutmut_1() -> list[str]:
    return sorted(None)

mutants_x_list_clients__mutmut['_mutmut_orig'] = x_list_clients__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_clients__mutmut['x_list_clients__mutmut_1'] = x_list_clients__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_integration__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_integration__mutmut)
def get_integration(client: str) -> MCPClientIntegration:
    factory = _CLIENT_REGISTRY.get(client)
    if factory is None:
        available = ", ".join(list_clients())
        raise KeyError(f"Unknown MCP client {client!r}. Available: {available}")
    return factory()


def x_get_integration__mutmut_orig(client: str) -> MCPClientIntegration:
    factory = _CLIENT_REGISTRY.get(client)
    if factory is None:
        available = ", ".join(list_clients())
        raise KeyError(f"Unknown MCP client {client!r}. Available: {available}")
    return factory()


def x_get_integration__mutmut_1(client: str) -> MCPClientIntegration:
    factory = None
    if factory is None:
        available = ", ".join(list_clients())
        raise KeyError(f"Unknown MCP client {client!r}. Available: {available}")
    return factory()


def x_get_integration__mutmut_2(client: str) -> MCPClientIntegration:
    factory = _CLIENT_REGISTRY.get(None)
    if factory is None:
        available = ", ".join(list_clients())
        raise KeyError(f"Unknown MCP client {client!r}. Available: {available}")
    return factory()


def x_get_integration__mutmut_3(client: str) -> MCPClientIntegration:
    factory = _CLIENT_REGISTRY.get(client)
    if factory is not None:
        available = ", ".join(list_clients())
        raise KeyError(f"Unknown MCP client {client!r}. Available: {available}")
    return factory()


def x_get_integration__mutmut_4(client: str) -> MCPClientIntegration:
    factory = _CLIENT_REGISTRY.get(client)
    if factory is None:
        available = None
        raise KeyError(f"Unknown MCP client {client!r}. Available: {available}")
    return factory()


def x_get_integration__mutmut_5(client: str) -> MCPClientIntegration:
    factory = _CLIENT_REGISTRY.get(client)
    if factory is None:
        available = ", ".join(None)
        raise KeyError(f"Unknown MCP client {client!r}. Available: {available}")
    return factory()


def x_get_integration__mutmut_6(client: str) -> MCPClientIntegration:
    factory = _CLIENT_REGISTRY.get(client)
    if factory is None:
        available = "XX, XX".join(list_clients())
        raise KeyError(f"Unknown MCP client {client!r}. Available: {available}")
    return factory()


def x_get_integration__mutmut_7(client: str) -> MCPClientIntegration:
    factory = _CLIENT_REGISTRY.get(client)
    if factory is None:
        available = ", ".join(list_clients())
        raise KeyError(None)
    return factory()

mutants_x_get_integration__mutmut['_mutmut_orig'] = x_get_integration__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_integration__mutmut['x_get_integration__mutmut_1'] = x_get_integration__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_integration__mutmut['x_get_integration__mutmut_2'] = x_get_integration__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_integration__mutmut['x_get_integration__mutmut_3'] = x_get_integration__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_integration__mutmut['x_get_integration__mutmut_4'] = x_get_integration__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_integration__mutmut['x_get_integration__mutmut_5'] = x_get_integration__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_integration__mutmut['x_get_integration__mutmut_6'] = x_get_integration__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_integration__mutmut['x_get_integration__mutmut_7'] = x_get_integration__mutmut_7 # type: ignore # mutmut generated
