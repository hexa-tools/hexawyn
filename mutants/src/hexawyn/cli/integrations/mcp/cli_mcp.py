"""Shared base for CLI-driven MCP client integrations.

Clients such as Claude Code and Codex configure MCP servers through their own
CLI (`<client> mcp add / get|list / remove`). This base implements the
idempotent install / safe uninstall / status lifecycle, leaving each client to
provide its binary, display name, state probe and add/remove commands.
"""

from __future__ import annotations

import shutil
from abc import abstractmethod
from dataclasses import dataclass

from hexawyn.cli.integrations.mcp.base import (
    MCP_TRANSPORT,
    CommandResult,
    CommandRunner,
    IntegrationResult,
    IntegrationStatus,
    MCPClientIntegration,
    SubprocessRunner,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class CliIntegrationStatus:
    configured: bool
    error: str = ""
    transport: str = MCP_TRANSPORT
    endpoint: str = ""
    command: str = ""
mutants_xǁCliMcpIntegrationǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCliMcpIntegrationǁis_available__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCliMcpIntegrationǁinstall__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCliMcpIntegrationǁuninstall__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCliMcpIntegrationǁstatus__mutmut: MutantDict = {}  # type: ignore


class CliMcpIntegration(MCPClientIntegration):
    """Base for coding agents configured through their own MCP CLI."""

    binary: str = ""
    display_name: str = ""

    @_mutmut_mutated(mutants_xǁCliMcpIntegrationǁ__init____mutmut)
    def __init__(self, runner: CommandRunner | None = None) -> None:
        self._runner = runner if runner is not None else SubprocessRunner()

    def xǁCliMcpIntegrationǁ__init____mutmut_orig(self, runner: CommandRunner | None = None) -> None:
        self._runner = runner if runner is not None else SubprocessRunner()

    def xǁCliMcpIntegrationǁ__init____mutmut_1(self, runner: CommandRunner | None = None) -> None:
        self._runner = None

    def xǁCliMcpIntegrationǁ__init____mutmut_2(self, runner: CommandRunner | None = None) -> None:
        self._runner = runner if runner is None else SubprocessRunner()

    @_mutmut_mutated(mutants_xǁCliMcpIntegrationǁis_available__mutmut)
    def is_available(self) -> bool:
        return shutil.which(self.binary) is not None

    def xǁCliMcpIntegrationǁis_available__mutmut_orig(self) -> bool:
        return shutil.which(self.binary) is not None

    def xǁCliMcpIntegrationǁis_available__mutmut_1(self) -> bool:
        return shutil.which(None) is not None

    def xǁCliMcpIntegrationǁis_available__mutmut_2(self) -> bool:
        return shutil.which(self.binary) is None

    def is_installed(self) -> bool:
        return self._read_status().configured

    @_mutmut_mutated(mutants_xǁCliMcpIntegrationǁinstall__mutmut)
    def install(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_orig(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_1(self) -> IntegrationResult:
        status = None
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_2(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=None, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_3(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=None)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_4(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_5(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, )
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_6(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=True, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_7(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=None, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_8(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message=None, already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_9(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=None
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_10(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_11(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_12(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_13(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=False, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_14(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="XXalready configuredXX", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_15(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="ALREADY CONFIGURED", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_16(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=False
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_17(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = None
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_18(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(None)
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_19(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode == 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_20(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 1:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_21(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=None, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_22(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=None
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_23(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_24(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_25(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=True, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_26(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(None, result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_27(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", None)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_28(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_29(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", )
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_30(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = None
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_31(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error and not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_32(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_33(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = None
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_34(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error and "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_35(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "XXconfiguration could not be verified after installXX"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_36(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "CONFIGURATION COULD NOT BE VERIFIED AFTER INSTALL"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_37(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=None, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_38(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=None)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_39(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_40(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, )
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_41(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=True, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_42(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=None, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_43(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message=None)

    def xǁCliMcpIntegrationǁinstall__mutmut_44(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_45(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, )

    def xǁCliMcpIntegrationǁinstall__mutmut_46(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=False, message="configured")

    def xǁCliMcpIntegrationǁinstall__mutmut_47(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="XXconfiguredXX")

    def xǁCliMcpIntegrationǁinstall__mutmut_48(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="CONFIGURED")

    @_mutmut_mutated(mutants_xǁCliMcpIntegrationǁuninstall__mutmut)
    def uninstall(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_orig(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_1(self) -> IntegrationResult:
        status = None
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_2(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=None, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_3(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=None)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_4(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_5(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, )
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_6(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=True, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_7(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_8(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=None, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_9(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message=None)
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_10(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_11(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, )
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_12(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=False, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_13(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="XXnot configuredXX")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_14(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="NOT CONFIGURED")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_15(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = None
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_16(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(None)
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_17(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode == 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_18(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 1:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_19(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=None, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_20(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=None
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_21(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_22(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_23(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=True, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_24(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(None, result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_25(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", None)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_26(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_27(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", )
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_28(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = None
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_29(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=None, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_30(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message=None)
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_31(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_32(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, )
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_33(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=True, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_34(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="XXhexawyn still present after removalXX")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_35(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="HEXAWYN STILL PRESENT AFTER REMOVAL")
        return IntegrationResult(success=True, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_36(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=None, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_37(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message=None)

    def xǁCliMcpIntegrationǁuninstall__mutmut_38(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_39(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, )

    def xǁCliMcpIntegrationǁuninstall__mutmut_40(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=False, message="removed")

    def xǁCliMcpIntegrationǁuninstall__mutmut_41(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="XXremovedXX")

    def xǁCliMcpIntegrationǁuninstall__mutmut_42(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="REMOVED")

    @_mutmut_mutated(mutants_xǁCliMcpIntegrationǁstatus__mutmut)
    def status(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=status.endpoint,
            command=status.command,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_orig(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=status.endpoint,
            command=status.command,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_1(self) -> IntegrationStatus:
        status = None
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=status.endpoint,
            command=status.command,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_2(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=None,
            transport=status.transport,
            endpoint=status.endpoint,
            command=status.command,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_3(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=None,
            endpoint=status.endpoint,
            command=status.command,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_4(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=None,
            command=status.command,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_5(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=status.endpoint,
            command=None,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_6(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=status.endpoint,
            command=status.command,
            error=None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_7(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            transport=status.transport,
            endpoint=status.endpoint,
            command=status.command,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_8(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            endpoint=status.endpoint,
            command=status.command,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_9(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            command=status.command,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_10(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=status.endpoint,
            error=status.error or None,
        )

    def xǁCliMcpIntegrationǁstatus__mutmut_11(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=status.endpoint,
            command=status.command,
            )

    def xǁCliMcpIntegrationǁstatus__mutmut_12(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=status.endpoint,
            command=status.command,
            error=status.error and None,
        )

    @abstractmethod
    def _read_status(self) -> CliIntegrationStatus:
        """Return the client's MCP state for the hexawyn server."""

    @abstractmethod
    def _add_command(self) -> list[str]:
        """Return the CLI command that registers the hexawyn MCP server."""

    @abstractmethod
    def _remove_command(self) -> list[str]:
        """Return the CLI command that removes the hexawyn MCP server."""

mutants_xǁCliMcpIntegrationǁ__init____mutmut['_mutmut_orig'] = CliMcpIntegration.xǁCliMcpIntegrationǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁ__init____mutmut['xǁCliMcpIntegrationǁ__init____mutmut_1'] = CliMcpIntegration.xǁCliMcpIntegrationǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁ__init____mutmut['xǁCliMcpIntegrationǁ__init____mutmut_2'] = CliMcpIntegration.xǁCliMcpIntegrationǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁCliMcpIntegrationǁis_available__mutmut['_mutmut_orig'] = CliMcpIntegration.xǁCliMcpIntegrationǁis_available__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁis_available__mutmut['xǁCliMcpIntegrationǁis_available__mutmut_1'] = CliMcpIntegration.xǁCliMcpIntegrationǁis_available__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁis_available__mutmut['xǁCliMcpIntegrationǁis_available__mutmut_2'] = CliMcpIntegration.xǁCliMcpIntegrationǁis_available__mutmut_2 # type: ignore # mutmut generated

mutants_xǁCliMcpIntegrationǁinstall__mutmut['_mutmut_orig'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_1'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_2'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_3'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_4'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_5'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_6'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_7'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_8'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_9'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_10'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_11'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_12'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_13'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_14'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_15'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_16'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_17'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_18'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_19'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_20'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_21'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_22'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_23'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_24'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_25'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_26'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_27'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_28'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_29'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_30'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_31'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_32'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_33'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_34'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_35'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_36'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_37'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_38'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_39'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_40'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_41'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_42'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_43'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_44'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_45'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_45 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_46'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_46 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_47'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_47 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁinstall__mutmut['xǁCliMcpIntegrationǁinstall__mutmut_48'] = CliMcpIntegration.xǁCliMcpIntegrationǁinstall__mutmut_48 # type: ignore # mutmut generated

mutants_xǁCliMcpIntegrationǁuninstall__mutmut['_mutmut_orig'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_1'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_2'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_3'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_4'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_5'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_6'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_7'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_8'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_9'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_10'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_11'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_12'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_13'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_14'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_15'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_16'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_17'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_18'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_19'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_20'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_21'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_22'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_23'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_24'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_25'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_26'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_27'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_28'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_29'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_30'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_31'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_32'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_33'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_34'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_35'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_36'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_37'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_38'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_39'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_40'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_41'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁuninstall__mutmut['xǁCliMcpIntegrationǁuninstall__mutmut_42'] = CliMcpIntegration.xǁCliMcpIntegrationǁuninstall__mutmut_42 # type: ignore # mutmut generated

mutants_xǁCliMcpIntegrationǁstatus__mutmut['_mutmut_orig'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_1'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_2'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_3'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_4'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_5'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_6'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_7'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_8'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_9'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_10'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_11'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCliMcpIntegrationǁstatus__mutmut['xǁCliMcpIntegrationǁstatus__mutmut_12'] = CliMcpIntegration.xǁCliMcpIntegrationǁstatus__mutmut_12 # type: ignore # mutmut generated
mutants_x__failure__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__failure__mutmut)
def _failure(operation: str, result: CommandResult) -> str:
    return f"{operation} failed: {_error_text(result)}"


def x__failure__mutmut_orig(operation: str, result: CommandResult) -> str:
    return f"{operation} failed: {_error_text(result)}"


def x__failure__mutmut_1(operation: str, result: CommandResult) -> str:
    return f"{operation} failed: {_error_text(None)}"

mutants_x__failure__mutmut['_mutmut_orig'] = x__failure__mutmut_orig # type: ignore # mutmut generated
mutants_x__failure__mutmut['x__failure__mutmut_1'] = x__failure__mutmut_1 # type: ignore # mutmut generated
mutants_x__error_text__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__error_text__mutmut)
def _error_text(result: CommandResult) -> str:
    return result.stderr.strip() or result.stdout.strip() or "unknown error"


def x__error_text__mutmut_orig(result: CommandResult) -> str:
    return result.stderr.strip() or result.stdout.strip() or "unknown error"


def x__error_text__mutmut_1(result: CommandResult) -> str:
    return result.stderr.strip() or result.stdout.strip() and "unknown error"


def x__error_text__mutmut_2(result: CommandResult) -> str:
    return result.stderr.strip() and result.stdout.strip() or "unknown error"


def x__error_text__mutmut_3(result: CommandResult) -> str:
    return result.stderr.strip() or result.stdout.strip() or "XXunknown errorXX"


def x__error_text__mutmut_4(result: CommandResult) -> str:
    return result.stderr.strip() or result.stdout.strip() or "UNKNOWN ERROR"

mutants_x__error_text__mutmut['_mutmut_orig'] = x__error_text__mutmut_orig # type: ignore # mutmut generated
mutants_x__error_text__mutmut['x__error_text__mutmut_1'] = x__error_text__mutmut_1 # type: ignore # mutmut generated
mutants_x__error_text__mutmut['x__error_text__mutmut_2'] = x__error_text__mutmut_2 # type: ignore # mutmut generated
mutants_x__error_text__mutmut['x__error_text__mutmut_3'] = x__error_text__mutmut_3 # type: ignore # mutmut generated
mutants_x__error_text__mutmut['x__error_text__mutmut_4'] = x__error_text__mutmut_4 # type: ignore # mutmut generated
