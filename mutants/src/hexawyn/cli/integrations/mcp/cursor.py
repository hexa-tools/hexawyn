"""Cursor MCP integration — configures ~/.cursor/mcp.json `mcpServers`.

Cursor configures MCP servers through the `mcp.json` file (global or project);
there is no `cursor mcp` CLI. This integration edits only the hexawyn entry
and preserves every other server.
"""

from __future__ import annotations

from pathlib import Path

from hexawyn.cli.integrations.mcp.command import mcp_stdio_command
from hexawyn.cli.integrations.mcp.file import McpConfigFileIntegration

CURSOR_BINARY = "cursor"
CURSOR_DISPLAY_NAME = "Cursor"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCursorIntegrationǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCursorIntegrationǁ_config_root_key__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCursorIntegrationǁ_build_entry__mutmut: MutantDict = {}  # type: ignore


class CursorIntegration(McpConfigFileIntegration):
    client_name = "cursor"
    binary = CURSOR_BINARY
    display_name = CURSOR_DISPLAY_NAME
    default_config_path = Path.home() / ".cursor" / "mcp.json"

    @_mutmut_mutated(mutants_xǁCursorIntegrationǁ__init____mutmut)
    def __init__(self, config_path: Path | None = None) -> None:
        super().__init__(config_path or self.default_config_path)

    def xǁCursorIntegrationǁ__init____mutmut_orig(self, config_path: Path | None = None) -> None:
        super().__init__(config_path or self.default_config_path)

    def xǁCursorIntegrationǁ__init____mutmut_1(self, config_path: Path | None = None) -> None:
        super().__init__(None)

    def xǁCursorIntegrationǁ__init____mutmut_2(self, config_path: Path | None = None) -> None:
        super().__init__(config_path and self.default_config_path)

    @_mutmut_mutated(mutants_xǁCursorIntegrationǁ_config_root_key__mutmut)
    def _config_root_key(self) -> str:
        return "mcpServers"

    def xǁCursorIntegrationǁ_config_root_key__mutmut_orig(self) -> str:
        return "mcpServers"

    def xǁCursorIntegrationǁ_config_root_key__mutmut_1(self) -> str:
        return "XXmcpServersXX"

    def xǁCursorIntegrationǁ_config_root_key__mutmut_2(self) -> str:
        return "mcpservers"

    def xǁCursorIntegrationǁ_config_root_key__mutmut_3(self) -> str:
        return "MCPSERVERS"

    @_mutmut_mutated(mutants_xǁCursorIntegrationǁ_build_entry__mutmut)
    def _build_entry(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}

    def xǁCursorIntegrationǁ_build_entry__mutmut_orig(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}

    def xǁCursorIntegrationǁ_build_entry__mutmut_1(self) -> dict[str, object]:
        return {"XXcommandXX": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}

    def xǁCursorIntegrationǁ_build_entry__mutmut_2(self) -> dict[str, object]:
        return {"COMMAND": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}

    def xǁCursorIntegrationǁ_build_entry__mutmut_3(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[1], "args": mcp_stdio_command()[1:]}

    def xǁCursorIntegrationǁ_build_entry__mutmut_4(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "XXargsXX": mcp_stdio_command()[1:]}

    def xǁCursorIntegrationǁ_build_entry__mutmut_5(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "ARGS": mcp_stdio_command()[1:]}

    def xǁCursorIntegrationǁ_build_entry__mutmut_6(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "args": mcp_stdio_command()[2:]}

mutants_xǁCursorIntegrationǁ__init____mutmut['_mutmut_orig'] = CursorIntegration.xǁCursorIntegrationǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ__init____mutmut['xǁCursorIntegrationǁ__init____mutmut_1'] = CursorIntegration.xǁCursorIntegrationǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ__init____mutmut['xǁCursorIntegrationǁ__init____mutmut_2'] = CursorIntegration.xǁCursorIntegrationǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁCursorIntegrationǁ_config_root_key__mutmut['_mutmut_orig'] = CursorIntegration.xǁCursorIntegrationǁ_config_root_key__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ_config_root_key__mutmut['xǁCursorIntegrationǁ_config_root_key__mutmut_1'] = CursorIntegration.xǁCursorIntegrationǁ_config_root_key__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ_config_root_key__mutmut['xǁCursorIntegrationǁ_config_root_key__mutmut_2'] = CursorIntegration.xǁCursorIntegrationǁ_config_root_key__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ_config_root_key__mutmut['xǁCursorIntegrationǁ_config_root_key__mutmut_3'] = CursorIntegration.xǁCursorIntegrationǁ_config_root_key__mutmut_3 # type: ignore # mutmut generated

mutants_xǁCursorIntegrationǁ_build_entry__mutmut['_mutmut_orig'] = CursorIntegration.xǁCursorIntegrationǁ_build_entry__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ_build_entry__mutmut['xǁCursorIntegrationǁ_build_entry__mutmut_1'] = CursorIntegration.xǁCursorIntegrationǁ_build_entry__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ_build_entry__mutmut['xǁCursorIntegrationǁ_build_entry__mutmut_2'] = CursorIntegration.xǁCursorIntegrationǁ_build_entry__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ_build_entry__mutmut['xǁCursorIntegrationǁ_build_entry__mutmut_3'] = CursorIntegration.xǁCursorIntegrationǁ_build_entry__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ_build_entry__mutmut['xǁCursorIntegrationǁ_build_entry__mutmut_4'] = CursorIntegration.xǁCursorIntegrationǁ_build_entry__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ_build_entry__mutmut['xǁCursorIntegrationǁ_build_entry__mutmut_5'] = CursorIntegration.xǁCursorIntegrationǁ_build_entry__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCursorIntegrationǁ_build_entry__mutmut['xǁCursorIntegrationǁ_build_entry__mutmut_6'] = CursorIntegration.xǁCursorIntegrationǁ_build_entry__mutmut_6 # type: ignore # mutmut generated
