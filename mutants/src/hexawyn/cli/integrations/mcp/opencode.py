"""OpenCode MCP integration — configures the opencode.json `mcp` section.

OpenCode does not expose an `mcp add` CLI for local servers; local MCP servers
are declared in the config file under the `mcp` key. This integration edits
only the hexawyn entry and preserves every other server.
"""

from __future__ import annotations

from pathlib import Path

from hexawyn.cli.integrations.mcp.command import mcp_stdio_command
from hexawyn.cli.integrations.mcp.file import McpConfigFileIntegration

OPENCODE_BINARY = "opencode"
OPENCODE_DISPLAY_NAME = "OpenCode"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOpenCodeIntegrationǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenCodeIntegrationǁ_config_root_key__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenCodeIntegrationǁ_build_entry__mutmut: MutantDict = {}  # type: ignore


class OpenCodeIntegration(McpConfigFileIntegration):
    client_name = "opencode"
    binary = OPENCODE_BINARY
    display_name = OPENCODE_DISPLAY_NAME
    default_config_path = Path.home() / ".config" / "opencode" / "opencode.json"

    @_mutmut_mutated(mutants_xǁOpenCodeIntegrationǁ__init____mutmut)
    def __init__(self, config_path: Path | None = None) -> None:
        super().__init__(config_path or self.default_config_path)

    def xǁOpenCodeIntegrationǁ__init____mutmut_orig(self, config_path: Path | None = None) -> None:
        super().__init__(config_path or self.default_config_path)

    def xǁOpenCodeIntegrationǁ__init____mutmut_1(self, config_path: Path | None = None) -> None:
        super().__init__(None)

    def xǁOpenCodeIntegrationǁ__init____mutmut_2(self, config_path: Path | None = None) -> None:
        super().__init__(config_path and self.default_config_path)

    @_mutmut_mutated(mutants_xǁOpenCodeIntegrationǁ_config_root_key__mutmut)
    def _config_root_key(self) -> str:
        return "mcp"

    def xǁOpenCodeIntegrationǁ_config_root_key__mutmut_orig(self) -> str:
        return "mcp"

    def xǁOpenCodeIntegrationǁ_config_root_key__mutmut_1(self) -> str:
        return "XXmcpXX"

    def xǁOpenCodeIntegrationǁ_config_root_key__mutmut_2(self) -> str:
        return "MCP"

    @_mutmut_mutated(mutants_xǁOpenCodeIntegrationǁ_build_entry__mutmut)
    def _build_entry(self) -> dict[str, object]:
        return {"type": "local", "command": mcp_stdio_command()}

    def xǁOpenCodeIntegrationǁ_build_entry__mutmut_orig(self) -> dict[str, object]:
        return {"type": "local", "command": mcp_stdio_command()}

    def xǁOpenCodeIntegrationǁ_build_entry__mutmut_1(self) -> dict[str, object]:
        return {"XXtypeXX": "local", "command": mcp_stdio_command()}

    def xǁOpenCodeIntegrationǁ_build_entry__mutmut_2(self) -> dict[str, object]:
        return {"TYPE": "local", "command": mcp_stdio_command()}

    def xǁOpenCodeIntegrationǁ_build_entry__mutmut_3(self) -> dict[str, object]:
        return {"type": "XXlocalXX", "command": mcp_stdio_command()}

    def xǁOpenCodeIntegrationǁ_build_entry__mutmut_4(self) -> dict[str, object]:
        return {"type": "LOCAL", "command": mcp_stdio_command()}

    def xǁOpenCodeIntegrationǁ_build_entry__mutmut_5(self) -> dict[str, object]:
        return {"type": "local", "XXcommandXX": mcp_stdio_command()}

    def xǁOpenCodeIntegrationǁ_build_entry__mutmut_6(self) -> dict[str, object]:
        return {"type": "local", "COMMAND": mcp_stdio_command()}

mutants_xǁOpenCodeIntegrationǁ__init____mutmut['_mutmut_orig'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ__init____mutmut['xǁOpenCodeIntegrationǁ__init____mutmut_1'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ__init____mutmut['xǁOpenCodeIntegrationǁ__init____mutmut_2'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁOpenCodeIntegrationǁ_config_root_key__mutmut['_mutmut_orig'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_config_root_key__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ_config_root_key__mutmut['xǁOpenCodeIntegrationǁ_config_root_key__mutmut_1'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_config_root_key__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ_config_root_key__mutmut['xǁOpenCodeIntegrationǁ_config_root_key__mutmut_2'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_config_root_key__mutmut_2 # type: ignore # mutmut generated

mutants_xǁOpenCodeIntegrationǁ_build_entry__mutmut['_mutmut_orig'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_build_entry__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ_build_entry__mutmut['xǁOpenCodeIntegrationǁ_build_entry__mutmut_1'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_build_entry__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ_build_entry__mutmut['xǁOpenCodeIntegrationǁ_build_entry__mutmut_2'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_build_entry__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ_build_entry__mutmut['xǁOpenCodeIntegrationǁ_build_entry__mutmut_3'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_build_entry__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ_build_entry__mutmut['xǁOpenCodeIntegrationǁ_build_entry__mutmut_4'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_build_entry__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ_build_entry__mutmut['xǁOpenCodeIntegrationǁ_build_entry__mutmut_5'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_build_entry__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenCodeIntegrationǁ_build_entry__mutmut['xǁOpenCodeIntegrationǁ_build_entry__mutmut_6'] = OpenCodeIntegration.xǁOpenCodeIntegrationǁ_build_entry__mutmut_6 # type: ignore # mutmut generated
