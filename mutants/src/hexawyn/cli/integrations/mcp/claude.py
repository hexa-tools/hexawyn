"""Claude Code MCP integration — uses the official `claude mcp` CLI.

Configures Claude Code to consume the existing Hexawyn MCP server over the
stdio transport through the documented `claude mcp add / get / remove`
mechanism. Claude Code spawns the server per session, so no separate HTTP
server needs to run.
"""

from __future__ import annotations

from hexawyn.cli.integrations.mcp.base import MCP_SERVER_NAME, MCP_TRANSPORT
from hexawyn.cli.integrations.mcp.cli_mcp import (
    CliIntegrationStatus,
    CliMcpIntegration,
    _error_text,
)
from hexawyn.cli.integrations.mcp.command import mcp_stdio_command

CLAUDE_BINARY = "claude"
CLAUDE_DISPLAY_NAME = "Claude Code"
_NOT_CONFIGURED_MARKER = "No MCP server named"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁClaudeCodeIntegrationǁ_add_command__mutmut: MutantDict = {}  # type: ignore
mutants_xǁClaudeCodeIntegrationǁ_remove_command__mutmut: MutantDict = {}  # type: ignore


class ClaudeCodeIntegration(CliMcpIntegration):
    client_name = "claude"
    binary = CLAUDE_BINARY
    display_name = CLAUDE_DISPLAY_NAME

    @_mutmut_mutated(mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut)
    def _read_status(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_orig(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_1(self) -> CliIntegrationStatus:
        if self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_2(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=None, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_3(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=None
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_4(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_5(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_6(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=True, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_7(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = None
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_8(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run(None)
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_9(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "XXmcpXX", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_10(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "MCP", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_11(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "XXgetXX", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_12(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "GET", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_13(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = None
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_14(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER not in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_15(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=None)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_16(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=True)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_17(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode != 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_18(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 1:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_19(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = None
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_20(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(None)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_21(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = None
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_22(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) and MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_23(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(None) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_24(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get(None, MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_25(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", None)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_26(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get(MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_27(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", )) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_28(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("XXtypeXX", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_29(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("TYPE", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_30(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=None,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_31(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=None,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_32(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=None,
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_33(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=None,
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_34(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_35(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_36(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_37(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_38(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=False,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_39(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(None),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_40(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") and ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_41(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get(None, "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_42(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", None) or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_43(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_44(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", ) or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_45(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("XXurlXX", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_46(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("URL", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_47(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "XXXX") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_48(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or "XXXX"),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_49(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(None),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_50(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=None, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_51(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=None)

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_52(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_53(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, )

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_54(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=True, error=_error_text(result))

    def xǁClaudeCodeIntegrationǁ_read_status__mutmut_55(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(None))

    @_mutmut_mutated(mutants_xǁClaudeCodeIntegrationǁ_add_command__mutmut)
    def _add_command(self) -> list[str]:
        return [self.binary, "mcp", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁClaudeCodeIntegrationǁ_add_command__mutmut_orig(self) -> list[str]:
        return [self.binary, "mcp", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁClaudeCodeIntegrationǁ_add_command__mutmut_1(self) -> list[str]:
        return [self.binary, "XXmcpXX", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁClaudeCodeIntegrationǁ_add_command__mutmut_2(self) -> list[str]:
        return [self.binary, "MCP", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁClaudeCodeIntegrationǁ_add_command__mutmut_3(self) -> list[str]:
        return [self.binary, "mcp", "XXaddXX", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁClaudeCodeIntegrationǁ_add_command__mutmut_4(self) -> list[str]:
        return [self.binary, "mcp", "ADD", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁClaudeCodeIntegrationǁ_add_command__mutmut_5(self) -> list[str]:
        return [self.binary, "mcp", "add", MCP_SERVER_NAME, "XX--XX", *mcp_stdio_command()]

    @_mutmut_mutated(mutants_xǁClaudeCodeIntegrationǁ_remove_command__mutmut)
    def _remove_command(self) -> list[str]:
        return [self.binary, "mcp", "remove", MCP_SERVER_NAME]

    def xǁClaudeCodeIntegrationǁ_remove_command__mutmut_orig(self) -> list[str]:
        return [self.binary, "mcp", "remove", MCP_SERVER_NAME]

    def xǁClaudeCodeIntegrationǁ_remove_command__mutmut_1(self) -> list[str]:
        return [self.binary, "XXmcpXX", "remove", MCP_SERVER_NAME]

    def xǁClaudeCodeIntegrationǁ_remove_command__mutmut_2(self) -> list[str]:
        return [self.binary, "MCP", "remove", MCP_SERVER_NAME]

    def xǁClaudeCodeIntegrationǁ_remove_command__mutmut_3(self) -> list[str]:
        return [self.binary, "mcp", "XXremoveXX", MCP_SERVER_NAME]

    def xǁClaudeCodeIntegrationǁ_remove_command__mutmut_4(self) -> list[str]:
        return [self.binary, "mcp", "REMOVE", MCP_SERVER_NAME]

mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['_mutmut_orig'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_1'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_2'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_3'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_4'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_5'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_6'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_7'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_8'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_9'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_10'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_11'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_12'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_13'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_14'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_15'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_16'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_17'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_18'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_19'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_20'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_21'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_22'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_23'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_24'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_25'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_26'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_27'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_28'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_29'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_30'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_30 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_31'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_31 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_32'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_32 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_33'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_33 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_34'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_34 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_35'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_35 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_36'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_36 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_37'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_37 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_38'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_38 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_39'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_39 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_40'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_40 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_41'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_41 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_42'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_42 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_43'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_43 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_44'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_44 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_45'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_45 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_46'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_46 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_47'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_47 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_48'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_48 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_49'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_49 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_50'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_50 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_51'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_51 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_52'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_52 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_53'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_53 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_54'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_54 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_read_status__mutmut['xǁClaudeCodeIntegrationǁ_read_status__mutmut_55'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_read_status__mutmut_55 # type: ignore # mutmut generated

mutants_xǁClaudeCodeIntegrationǁ_add_command__mutmut['_mutmut_orig'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_add_command__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_add_command__mutmut['xǁClaudeCodeIntegrationǁ_add_command__mutmut_1'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_add_command__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_add_command__mutmut['xǁClaudeCodeIntegrationǁ_add_command__mutmut_2'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_add_command__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_add_command__mutmut['xǁClaudeCodeIntegrationǁ_add_command__mutmut_3'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_add_command__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_add_command__mutmut['xǁClaudeCodeIntegrationǁ_add_command__mutmut_4'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_add_command__mutmut_4 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_add_command__mutmut['xǁClaudeCodeIntegrationǁ_add_command__mutmut_5'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_add_command__mutmut_5 # type: ignore # mutmut generated

mutants_xǁClaudeCodeIntegrationǁ_remove_command__mutmut['_mutmut_orig'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_remove_command__mutmut_orig # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_remove_command__mutmut['xǁClaudeCodeIntegrationǁ_remove_command__mutmut_1'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_remove_command__mutmut_1 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_remove_command__mutmut['xǁClaudeCodeIntegrationǁ_remove_command__mutmut_2'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_remove_command__mutmut_2 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_remove_command__mutmut['xǁClaudeCodeIntegrationǁ_remove_command__mutmut_3'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_remove_command__mutmut_3 # type: ignore # mutmut generated
mutants_xǁClaudeCodeIntegrationǁ_remove_command__mutmut['xǁClaudeCodeIntegrationǁ_remove_command__mutmut_4'] = ClaudeCodeIntegration.xǁClaudeCodeIntegrationǁ_remove_command__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_entry__mutmut)
def _parse_entry(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_orig(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_1(text: str) -> dict[str, object]:
    entry: dict[str, object] = None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_2(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = None
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_3(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(None):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_4(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("XXType:XX"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_5(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_6(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("TYPE:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_7(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = None
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_8(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["XXtypeXX"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_9(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["TYPE"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_10(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(None, 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_11(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", None)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_12(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_13(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", )[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_14(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.rsplit(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_15(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split("XX:XX", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_16(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 2)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_17(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[2].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_18(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith(None):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_19(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("XXURL:XX"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_20(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("url:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_21(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = None
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_22(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["XXurlXX"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_23(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["URL"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_24(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(None, 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_25(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", None)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_26(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_27(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", )[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_28(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.rsplit(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_29(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split("XX:XX", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_30(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 2)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_31(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[2].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_32(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith(None):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_33(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("XXCommand:XX"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_34(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_35(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("COMMAND:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_36(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = None
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_37(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["XXcommandXX"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_38(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["COMMAND"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_39(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(None, 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_40(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", None)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_41(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_42(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", )[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_43(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.rsplit(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_44(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split("XX:XX", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_45(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 2)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_46(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[2].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_47(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith(None):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_48(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("XXArgs:XX"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_49(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_50(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("ARGS:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_51(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = None
    return entry


def x__parse_entry__mutmut_52(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["XXargsXX"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_53(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["ARGS"] = stripped.split(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_54(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(None, 1)[1].strip()
    return entry


def x__parse_entry__mutmut_55(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", None)[1].strip()
    return entry


def x__parse_entry__mutmut_56(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(1)[1].strip()
    return entry


def x__parse_entry__mutmut_57(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", )[1].strip()
    return entry


def x__parse_entry__mutmut_58(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.rsplit(":", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_59(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split("XX:XX", 1)[1].strip()
    return entry


def x__parse_entry__mutmut_60(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 2)[1].strip()
    return entry


def x__parse_entry__mutmut_61(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[2].strip()
    return entry

mutants_x__parse_entry__mutmut['_mutmut_orig'] = x__parse_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_1'] = x__parse_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_2'] = x__parse_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_3'] = x__parse_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_4'] = x__parse_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_5'] = x__parse_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_6'] = x__parse_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_7'] = x__parse_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_8'] = x__parse_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_9'] = x__parse_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_10'] = x__parse_entry__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_11'] = x__parse_entry__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_12'] = x__parse_entry__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_13'] = x__parse_entry__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_14'] = x__parse_entry__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_15'] = x__parse_entry__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_16'] = x__parse_entry__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_17'] = x__parse_entry__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_18'] = x__parse_entry__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_19'] = x__parse_entry__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_20'] = x__parse_entry__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_21'] = x__parse_entry__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_22'] = x__parse_entry__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_23'] = x__parse_entry__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_24'] = x__parse_entry__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_25'] = x__parse_entry__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_26'] = x__parse_entry__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_27'] = x__parse_entry__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_28'] = x__parse_entry__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_29'] = x__parse_entry__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_30'] = x__parse_entry__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_31'] = x__parse_entry__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_32'] = x__parse_entry__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_33'] = x__parse_entry__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_34'] = x__parse_entry__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_35'] = x__parse_entry__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_36'] = x__parse_entry__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_37'] = x__parse_entry__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_38'] = x__parse_entry__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_39'] = x__parse_entry__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_40'] = x__parse_entry__mutmut_40 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_41'] = x__parse_entry__mutmut_41 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_42'] = x__parse_entry__mutmut_42 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_43'] = x__parse_entry__mutmut_43 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_44'] = x__parse_entry__mutmut_44 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_45'] = x__parse_entry__mutmut_45 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_46'] = x__parse_entry__mutmut_46 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_47'] = x__parse_entry__mutmut_47 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_48'] = x__parse_entry__mutmut_48 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_49'] = x__parse_entry__mutmut_49 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_50'] = x__parse_entry__mutmut_50 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_51'] = x__parse_entry__mutmut_51 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_52'] = x__parse_entry__mutmut_52 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_53'] = x__parse_entry__mutmut_53 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_54'] = x__parse_entry__mutmut_54 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_55'] = x__parse_entry__mutmut_55 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_56'] = x__parse_entry__mutmut_56 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_57'] = x__parse_entry__mutmut_57 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_58'] = x__parse_entry__mutmut_58 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_59'] = x__parse_entry__mutmut_59 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_60'] = x__parse_entry__mutmut_60 # type: ignore # mutmut generated
mutants_x__parse_entry__mutmut['x__parse_entry__mutmut_61'] = x__parse_entry__mutmut_61 # type: ignore # mutmut generated
mutants_x__command_string__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__command_string__mutmut)
def _command_string(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_orig(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_1(entry: dict[str, object]) -> str:
    command = None
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_2(entry: dict[str, object]) -> str:
    command = str(None)
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_3(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") and "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_4(entry: dict[str, object]) -> str:
    command = str(entry.get(None, "") or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_5(entry: dict[str, object]) -> str:
    command = str(entry.get("command", None) or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_6(entry: dict[str, object]) -> str:
    command = str(entry.get("") or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_7(entry: dict[str, object]) -> str:
    command = str(entry.get("command", ) or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_8(entry: dict[str, object]) -> str:
    command = str(entry.get("XXcommandXX", "") or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_9(entry: dict[str, object]) -> str:
    command = str(entry.get("COMMAND", "") or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_10(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "XXXX") or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_11(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "XXXX")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_12(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = None
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_13(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(None)
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_14(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("args", "") and "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_15(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get(None, "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_16(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("args", None) or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_17(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_18(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("args", ) or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_19(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("XXargsXX", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_20(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("ARGS", "") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_21(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("args", "XXXX") or "")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_22(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("args", "") or "XXXX")
    if command and args:
        return f"{command} {args}"
    return command


def x__command_string__mutmut_23(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("args", "") or "")
    if command or args:
        return f"{command} {args}"
    return command

mutants_x__command_string__mutmut['_mutmut_orig'] = x__command_string__mutmut_orig # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_1'] = x__command_string__mutmut_1 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_2'] = x__command_string__mutmut_2 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_3'] = x__command_string__mutmut_3 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_4'] = x__command_string__mutmut_4 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_5'] = x__command_string__mutmut_5 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_6'] = x__command_string__mutmut_6 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_7'] = x__command_string__mutmut_7 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_8'] = x__command_string__mutmut_8 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_9'] = x__command_string__mutmut_9 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_10'] = x__command_string__mutmut_10 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_11'] = x__command_string__mutmut_11 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_12'] = x__command_string__mutmut_12 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_13'] = x__command_string__mutmut_13 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_14'] = x__command_string__mutmut_14 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_15'] = x__command_string__mutmut_15 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_16'] = x__command_string__mutmut_16 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_17'] = x__command_string__mutmut_17 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_18'] = x__command_string__mutmut_18 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_19'] = x__command_string__mutmut_19 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_20'] = x__command_string__mutmut_20 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_21'] = x__command_string__mutmut_21 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_22'] = x__command_string__mutmut_22 # type: ignore # mutmut generated
mutants_x__command_string__mutmut['x__command_string__mutmut_23'] = x__command_string__mutmut_23 # type: ignore # mutmut generated
