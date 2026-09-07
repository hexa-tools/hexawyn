"""Base for config-file-driven MCP client integrations.

Clients such as OpenCode, Cursor and Gemini CLI configure MCP servers through
a JSON configuration file rather than an MCP CLI. These integrations edit only
the hexawyn entry under the client's config root key and preserve every other
server.
"""

from __future__ import annotations

import json
import shutil
from abc import abstractmethod
from pathlib import Path

from hexawyn.cli.integrations.mcp.base import (
    MCP_SERVER_NAME,
    MCP_TRANSPORT,
    IntegrationResult,
    IntegrationStatus,
    MCPClientIntegration,
)
from hexawyn.cli.integrations.mcp.command import mcp_stdio_command


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMcpConfigFileIntegrationǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁMcpConfigFileIntegrationǁis_available__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMcpConfigFileIntegrationǁis_installed__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMcpConfigFileIntegrationǁ_servers__mutmut: MutantDict = {}  # type: ignore


class McpConfigFileIntegration(MCPClientIntegration):
    """Base for coding agents configured through a JSON config file."""

    binary: str = ""
    display_name: str = ""

    @_mutmut_mutated(mutants_xǁMcpConfigFileIntegrationǁ__init____mutmut)
    def __init__(self, config_path: Path) -> None:
        self._config_path = config_path

    def xǁMcpConfigFileIntegrationǁ__init____mutmut_orig(self, config_path: Path) -> None:
        self._config_path = config_path

    def xǁMcpConfigFileIntegrationǁ__init____mutmut_1(self, config_path: Path) -> None:
        self._config_path = None

    @_mutmut_mutated(mutants_xǁMcpConfigFileIntegrationǁis_available__mutmut)
    def is_available(self) -> bool:
        return shutil.which(self.binary) is not None or self._config_path.parent.exists()

    def xǁMcpConfigFileIntegrationǁis_available__mutmut_orig(self) -> bool:
        return shutil.which(self.binary) is not None or self._config_path.parent.exists()

    def xǁMcpConfigFileIntegrationǁis_available__mutmut_1(self) -> bool:
        return shutil.which(self.binary) is not None and self._config_path.parent.exists()

    def xǁMcpConfigFileIntegrationǁis_available__mutmut_2(self) -> bool:
        return shutil.which(None) is not None or self._config_path.parent.exists()

    def xǁMcpConfigFileIntegrationǁis_available__mutmut_3(self) -> bool:
        return shutil.which(self.binary) is None or self._config_path.parent.exists()

    @_mutmut_mutated(mutants_xǁMcpConfigFileIntegrationǁis_installed__mutmut)
    def is_installed(self) -> bool:
        status = self.status()
        return status.configured

    def xǁMcpConfigFileIntegrationǁis_installed__mutmut_orig(self) -> bool:
        status = self.status()
        return status.configured

    def xǁMcpConfigFileIntegrationǁis_installed__mutmut_1(self) -> bool:
        status = None
        return status.configured

    @_mutmut_mutated(mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut)
    def install(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_orig(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_1(self) -> IntegrationResult:
        if self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_2(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=None, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_3(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=None
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_4(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_5(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_6(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=True, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_7(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = None
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_8(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is not None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_9(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=None, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_10(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=None)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_11(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_12(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, )
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_13(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=True, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_14(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = None
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_15(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(None)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_16(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_17(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=None, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_18(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message=None, already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_19(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=None
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_20(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_21(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_22(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_23(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=False, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_24(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="XXalready configuredXX", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_25(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="ALREADY CONFIGURED", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_26(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=False
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_27(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = None
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_28(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(None)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_29(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = None
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_30(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None and MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_31(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is not None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_32(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_33(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(None):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_34(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = None
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_35(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error and "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_36(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "XXconfiguration could not be verified after installXX"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_37(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "CONFIGURATION COULD NOT BE VERIFIED AFTER INSTALL"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_38(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=None, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_39(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=None)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_40(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_41(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, )
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_42(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=True, message=detail)
        return IntegrationResult(success=True, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_43(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=None, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_44(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message=None)

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_45(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_46(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, )

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_47(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=False, message="configured")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_48(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="XXconfiguredXX")

    def xǁMcpConfigFileIntegrationǁinstall__mutmut_49(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="CONFIGURED")

    @_mutmut_mutated(mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut)
    def uninstall(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_orig(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_1(self) -> IntegrationResult:
        if self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_2(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=None, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_3(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=None
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_4(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_5(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_6(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=True, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_7(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = None
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_8(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is not None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_9(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=None, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_10(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=None)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_11(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_12(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, )
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_13(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=True, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_14(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = None
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_15(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(None)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_16(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_17(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=None, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_18(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message=None)
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_19(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_20(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, )
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_21(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=False, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_22(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="XXnot configuredXX")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_23(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="NOT CONFIGURED")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_24(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(None)
        return IntegrationResult(success=True, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_25(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=None, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_26(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message=None)

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_27(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_28(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, )

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_29(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=False, message="removed")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_30(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="XXremovedXX")

    def xǁMcpConfigFileIntegrationǁuninstall__mutmut_31(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="REMOVED")

    @_mutmut_mutated(mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut)
    def status(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_orig(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_1(self) -> IntegrationStatus:
        command = None
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_2(self) -> IntegrationStatus:
        command = " ".join(None)
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_3(self) -> IntegrationStatus:
        command = "XX XX".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_4(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_5(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=None,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_6(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=None,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_7(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=None,
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_8(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_9(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_10(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_11(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=True,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_12(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = None
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_13(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is not None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_14(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=None, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_15(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=None, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_16(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=None)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_17(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_18(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_19(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, )
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_20(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=True, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_21(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_22(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(None):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_23(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=None, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_24(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=None)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_25(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_26(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, )
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_27(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=True, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_28(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=None, transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_29(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=None, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_30(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=None)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_31(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(transport=MCP_TRANSPORT, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_32(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, command=command)

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_33(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, )

    def xǁMcpConfigFileIntegrationǁstatus__mutmut_34(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=False, transport=MCP_TRANSPORT, command=command)

    @_mutmut_mutated(mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut)
    def _read_config(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(self._config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_orig(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(self._config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_1(self) -> tuple[dict[str, object] | None, str]:
        if self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(self._config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_2(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, "XXXX"
        try:
            data = json.loads(self._config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_3(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = None
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_4(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(None)
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_5(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(self._config_path.read_text(encoding=None))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_6(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(self._config_path.read_text(encoding="XXutf-8XX"))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_7(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(self._config_path.read_text(encoding="UTF-8"))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_8(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(self._config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def xǁMcpConfigFileIntegrationǁ_read_config__mutmut_9(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(self._config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, "XXXX"

    @_mutmut_mutated(mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut)
    def _write_config(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_orig(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_1(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=None, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_2(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=None)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_3(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_4(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, )
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_5(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=False, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_6(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=False)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_7(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(None, encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_8(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding=None)

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_9(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_10(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", )

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_11(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) - "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_12(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(None, indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_13(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=None) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_14(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(indent=2) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_15(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, ) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_16(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=3) + "\n", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_17(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "XX\nXX", encoding="utf-8")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_18(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="XXutf-8XX")

    def xǁMcpConfigFileIntegrationǁ_write_config__mutmut_19(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="UTF-8")

    @_mutmut_mutated(mutants_xǁMcpConfigFileIntegrationǁ_servers__mutmut)
    def _servers(self, config: dict[str, object]) -> dict[str, object]:
        root = config.get(self._config_root_key())
        if not isinstance(root, dict):
            root = {}
            config[self._config_root_key()] = root
        return root

    def xǁMcpConfigFileIntegrationǁ_servers__mutmut_orig(self, config: dict[str, object]) -> dict[str, object]:
        root = config.get(self._config_root_key())
        if not isinstance(root, dict):
            root = {}
            config[self._config_root_key()] = root
        return root

    def xǁMcpConfigFileIntegrationǁ_servers__mutmut_1(self, config: dict[str, object]) -> dict[str, object]:
        root = None
        if not isinstance(root, dict):
            root = {}
            config[self._config_root_key()] = root
        return root

    def xǁMcpConfigFileIntegrationǁ_servers__mutmut_2(self, config: dict[str, object]) -> dict[str, object]:
        root = config.get(None)
        if not isinstance(root, dict):
            root = {}
            config[self._config_root_key()] = root
        return root

    def xǁMcpConfigFileIntegrationǁ_servers__mutmut_3(self, config: dict[str, object]) -> dict[str, object]:
        root = config.get(self._config_root_key())
        if isinstance(root, dict):
            root = {}
            config[self._config_root_key()] = root
        return root

    def xǁMcpConfigFileIntegrationǁ_servers__mutmut_4(self, config: dict[str, object]) -> dict[str, object]:
        root = config.get(self._config_root_key())
        if not isinstance(root, dict):
            root = None
            config[self._config_root_key()] = root
        return root

    def xǁMcpConfigFileIntegrationǁ_servers__mutmut_5(self, config: dict[str, object]) -> dict[str, object]:
        root = config.get(self._config_root_key())
        if not isinstance(root, dict):
            root = {}
            config[self._config_root_key()] = None
        return root

    @abstractmethod
    def _config_root_key(self) -> str:
        """Return the top-level key holding the MCP servers map."""

    @abstractmethod
    def _build_entry(self) -> dict[str, object]:
        """Return the config entry for the hexawyn MCP server."""

mutants_xǁMcpConfigFileIntegrationǁ__init____mutmut['_mutmut_orig'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ__init____mutmut['xǁMcpConfigFileIntegrationǁ__init____mutmut_1'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁMcpConfigFileIntegrationǁis_available__mutmut['_mutmut_orig'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁis_available__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁis_available__mutmut['xǁMcpConfigFileIntegrationǁis_available__mutmut_1'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁis_available__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁis_available__mutmut['xǁMcpConfigFileIntegrationǁis_available__mutmut_2'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁis_available__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁis_available__mutmut['xǁMcpConfigFileIntegrationǁis_available__mutmut_3'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁis_available__mutmut_3 # type: ignore # mutmut generated

mutants_xǁMcpConfigFileIntegrationǁis_installed__mutmut['_mutmut_orig'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁis_installed__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁis_installed__mutmut['xǁMcpConfigFileIntegrationǁis_installed__mutmut_1'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁis_installed__mutmut_1 # type: ignore # mutmut generated

mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['_mutmut_orig'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_1'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_2'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_3'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_4'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_5'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_6'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_7'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_8'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_9'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_10'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_11'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_12'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_13'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_14'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_15'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_16'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_17'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_18'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_19'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_20'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_21'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_22'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_23'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_24'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_25'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_26'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_27'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_28'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_29'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_30'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_31'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_32'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_33'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_34'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_35'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_36'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_36 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_37'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_37 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_38'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_38 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_39'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_39 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_40'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_40 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_41'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_41 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_42'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_42 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_43'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_43 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_44'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_44 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_45'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_45 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_46'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_46 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_47'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_47 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_48'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_48 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁinstall__mutmut['xǁMcpConfigFileIntegrationǁinstall__mutmut_49'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁinstall__mutmut_49 # type: ignore # mutmut generated

mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['_mutmut_orig'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_1'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_2'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_3'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_4'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_5'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_6'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_7'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_8'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_9'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_10'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_11'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_12'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_13'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_14'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_15'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_16'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_17'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_18'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_19'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_20'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_21'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_22'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_23'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_24'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_25'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_26'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_27'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_28'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_29'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_30'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁuninstall__mutmut['xǁMcpConfigFileIntegrationǁuninstall__mutmut_31'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁuninstall__mutmut_31 # type: ignore # mutmut generated

mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['_mutmut_orig'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_1'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_2'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_3'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_4'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_5'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_6'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_7'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_8'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_9'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_10'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_11'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_12'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_13'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_14'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_15'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_16'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_17'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_18'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_19'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_20'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_21'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_22'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_23'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_24'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_25'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_26'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_27'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_28'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_29'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_30'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_31'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_32'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_33'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁstatus__mutmut['xǁMcpConfigFileIntegrationǁstatus__mutmut_34'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁstatus__mutmut_34 # type: ignore # mutmut generated

mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['_mutmut_orig'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['xǁMcpConfigFileIntegrationǁ_read_config__mutmut_1'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['xǁMcpConfigFileIntegrationǁ_read_config__mutmut_2'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['xǁMcpConfigFileIntegrationǁ_read_config__mutmut_3'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['xǁMcpConfigFileIntegrationǁ_read_config__mutmut_4'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['xǁMcpConfigFileIntegrationǁ_read_config__mutmut_5'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['xǁMcpConfigFileIntegrationǁ_read_config__mutmut_6'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['xǁMcpConfigFileIntegrationǁ_read_config__mutmut_7'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['xǁMcpConfigFileIntegrationǁ_read_config__mutmut_8'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_read_config__mutmut['xǁMcpConfigFileIntegrationǁ_read_config__mutmut_9'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_read_config__mutmut_9 # type: ignore # mutmut generated

mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['_mutmut_orig'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_1'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_2'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_3'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_4'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_5'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_6'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_7'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_8'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_9'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_10'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_11'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_12'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_13'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_14'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_15'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_16'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_17'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_18'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_write_config__mutmut['xǁMcpConfigFileIntegrationǁ_write_config__mutmut_19'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_write_config__mutmut_19 # type: ignore # mutmut generated

mutants_xǁMcpConfigFileIntegrationǁ_servers__mutmut['_mutmut_orig'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_servers__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_servers__mutmut['xǁMcpConfigFileIntegrationǁ_servers__mutmut_1'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_servers__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_servers__mutmut['xǁMcpConfigFileIntegrationǁ_servers__mutmut_2'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_servers__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_servers__mutmut['xǁMcpConfigFileIntegrationǁ_servers__mutmut_3'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_servers__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_servers__mutmut['xǁMcpConfigFileIntegrationǁ_servers__mutmut_4'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_servers__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMcpConfigFileIntegrationǁ_servers__mutmut['xǁMcpConfigFileIntegrationǁ_servers__mutmut_5'] = McpConfigFileIntegration.xǁMcpConfigFileIntegrationǁ_servers__mutmut_5 # type: ignore # mutmut generated
