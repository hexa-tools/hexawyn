"""Codex MCP integration — uses the official `codex mcp` CLI.

Configures Codex to consume the existing Hexawyn MCP server over the stdio
transport through the documented `codex mcp add / list / remove` mechanism.
"""

from __future__ import annotations

from hexawyn.cli.integrations.mcp.base import MCP_SERVER_NAME
from hexawyn.cli.integrations.mcp.cli_mcp import (
    CliIntegrationStatus,
    CliMcpIntegration,
    _error_text,
)
from hexawyn.cli.integrations.mcp.command import mcp_stdio_command

CODEX_BINARY = "codex"
CODEX_DISPLAY_NAME = "Codex"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCodexIntegrationǁ_read_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCodexIntegrationǁ_add_command__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCodexIntegrationǁ_remove_command__mutmut: MutantDict = {}  # type: ignore


class CodexIntegration(CliMcpIntegration):
    client_name = "codex"
    binary = CODEX_BINARY
    display_name = CODEX_DISPLAY_NAME

    @_mutmut_mutated(mutants_xǁCodexIntegrationǁ_read_status__mutmut)
    def _read_status(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_orig(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_1(self) -> CliIntegrationStatus:
        if self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_2(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=None, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_3(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=None
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_4(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_5(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_6(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=True, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_7(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = None
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_8(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run(None)
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_9(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "XXmcpXX", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_10(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "MCP", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_11(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "XXlistXX"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_12(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "LIST"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_13(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode == 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_14(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 1:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_15(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=None, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_16(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=None)
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_17(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_18(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, )
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_19(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=True, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_20(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(None))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_21(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = None
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_22(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME not in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_23(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.upper()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_24(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=None,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_25(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=None,
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_26(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_27(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            )

    def xǁCodexIntegrationǁ_read_status__mutmut_28(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(None) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_29(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command="XX XX".join(mcp_stdio_command()) if configured else "",
        )

    def xǁCodexIntegrationǁ_read_status__mutmut_30(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "XXXX",
        )

    @_mutmut_mutated(mutants_xǁCodexIntegrationǁ_add_command__mutmut)
    def _add_command(self) -> list[str]:
        return [self.binary, "mcp", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁCodexIntegrationǁ_add_command__mutmut_orig(self) -> list[str]:
        return [self.binary, "mcp", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁCodexIntegrationǁ_add_command__mutmut_1(self) -> list[str]:
        return [self.binary, "XXmcpXX", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁCodexIntegrationǁ_add_command__mutmut_2(self) -> list[str]:
        return [self.binary, "MCP", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁCodexIntegrationǁ_add_command__mutmut_3(self) -> list[str]:
        return [self.binary, "mcp", "XXaddXX", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁCodexIntegrationǁ_add_command__mutmut_4(self) -> list[str]:
        return [self.binary, "mcp", "ADD", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def xǁCodexIntegrationǁ_add_command__mutmut_5(self) -> list[str]:
        return [self.binary, "mcp", "add", MCP_SERVER_NAME, "XX--XX", *mcp_stdio_command()]

    @_mutmut_mutated(mutants_xǁCodexIntegrationǁ_remove_command__mutmut)
    def _remove_command(self) -> list[str]:
        return [self.binary, "mcp", "remove", MCP_SERVER_NAME]

    def xǁCodexIntegrationǁ_remove_command__mutmut_orig(self) -> list[str]:
        return [self.binary, "mcp", "remove", MCP_SERVER_NAME]

    def xǁCodexIntegrationǁ_remove_command__mutmut_1(self) -> list[str]:
        return [self.binary, "XXmcpXX", "remove", MCP_SERVER_NAME]

    def xǁCodexIntegrationǁ_remove_command__mutmut_2(self) -> list[str]:
        return [self.binary, "MCP", "remove", MCP_SERVER_NAME]

    def xǁCodexIntegrationǁ_remove_command__mutmut_3(self) -> list[str]:
        return [self.binary, "mcp", "XXremoveXX", MCP_SERVER_NAME]

    def xǁCodexIntegrationǁ_remove_command__mutmut_4(self) -> list[str]:
        return [self.binary, "mcp", "REMOVE", MCP_SERVER_NAME]

mutants_xǁCodexIntegrationǁ_read_status__mutmut['_mutmut_orig'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_1'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_2'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_3'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_4'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_5'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_6'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_7'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_8'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_9'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_10'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_11'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_12'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_13'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_14'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_15'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_16'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_17'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_18'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_19'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_20'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_21'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_22'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_23'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_24'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_25'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_26'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_27'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_28'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_29'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_read_status__mutmut['xǁCodexIntegrationǁ_read_status__mutmut_30'] = CodexIntegration.xǁCodexIntegrationǁ_read_status__mutmut_30 # type: ignore # mutmut generated

mutants_xǁCodexIntegrationǁ_add_command__mutmut['_mutmut_orig'] = CodexIntegration.xǁCodexIntegrationǁ_add_command__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_add_command__mutmut['xǁCodexIntegrationǁ_add_command__mutmut_1'] = CodexIntegration.xǁCodexIntegrationǁ_add_command__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_add_command__mutmut['xǁCodexIntegrationǁ_add_command__mutmut_2'] = CodexIntegration.xǁCodexIntegrationǁ_add_command__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_add_command__mutmut['xǁCodexIntegrationǁ_add_command__mutmut_3'] = CodexIntegration.xǁCodexIntegrationǁ_add_command__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_add_command__mutmut['xǁCodexIntegrationǁ_add_command__mutmut_4'] = CodexIntegration.xǁCodexIntegrationǁ_add_command__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_add_command__mutmut['xǁCodexIntegrationǁ_add_command__mutmut_5'] = CodexIntegration.xǁCodexIntegrationǁ_add_command__mutmut_5 # type: ignore # mutmut generated

mutants_xǁCodexIntegrationǁ_remove_command__mutmut['_mutmut_orig'] = CodexIntegration.xǁCodexIntegrationǁ_remove_command__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_remove_command__mutmut['xǁCodexIntegrationǁ_remove_command__mutmut_1'] = CodexIntegration.xǁCodexIntegrationǁ_remove_command__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_remove_command__mutmut['xǁCodexIntegrationǁ_remove_command__mutmut_2'] = CodexIntegration.xǁCodexIntegrationǁ_remove_command__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_remove_command__mutmut['xǁCodexIntegrationǁ_remove_command__mutmut_3'] = CodexIntegration.xǁCodexIntegrationǁ_remove_command__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCodexIntegrationǁ_remove_command__mutmut['xǁCodexIntegrationǁ_remove_command__mutmut_4'] = CodexIntegration.xǁCodexIntegrationǁ_remove_command__mutmut_4 # type: ignore # mutmut generated
