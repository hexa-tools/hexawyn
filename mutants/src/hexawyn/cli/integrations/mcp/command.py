"""Hexawyn MCP stdio launch command — derived from the running interpreter.

Coding agents (Claude Code, ...) spawn the Hexawyn MCP server as a subprocess
over stdio, so the server lifecycle follows the client. The launch command
uses the module entrypoint (python -m) with the interpreter currently running
the `hexa` CLI — `sys.executable` — so it works no matter how the package was
installed (pip, pipx, venv, poetry) or on which operating system.
"""

from __future__ import annotations

import sys

MCP_STDIO_MODULE = "hexawyn.mcp.stdio"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_mcp_stdio_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_mcp_stdio_command__mutmut)
def mcp_stdio_command() -> list[str]:
    return [sys.executable, "-m", MCP_STDIO_MODULE]


def x_mcp_stdio_command__mutmut_orig() -> list[str]:
    return [sys.executable, "-m", MCP_STDIO_MODULE]


def x_mcp_stdio_command__mutmut_1() -> list[str]:
    return [sys.executable, "XX-mXX", MCP_STDIO_MODULE]


def x_mcp_stdio_command__mutmut_2() -> list[str]:
    return [sys.executable, "-M", MCP_STDIO_MODULE]

mutants_x_mcp_stdio_command__mutmut['_mutmut_orig'] = x_mcp_stdio_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_mcp_stdio_command__mutmut['x_mcp_stdio_command__mutmut_1'] = x_mcp_stdio_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_mcp_stdio_command__mutmut['x_mcp_stdio_command__mutmut_2'] = x_mcp_stdio_command__mutmut_2 # type: ignore # mutmut generated
