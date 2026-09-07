"""Gemini CLI MCP integration — configures ~/.gemini/settings.json `mcpServers`.

Gemini CLI configures MCP servers in `~/.gemini/settings.json` under the
`mcpServers` key. This integration edits only the hexawyn entry and preserves
every other server.
"""

from __future__ import annotations

from pathlib import Path

from hexawyn.cli.integrations.mcp.command import mcp_stdio_command
from hexawyn.cli.integrations.mcp.file import McpConfigFileIntegration

GEMINI_BINARY = "gemini"
GEMINI_DISPLAY_NAME = "Gemini CLI"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGeminiIntegrationǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGeminiIntegrationǁ_config_root_key__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGeminiIntegrationǁ_build_entry__mutmut: MutantDict = {}  # type: ignore


class GeminiIntegration(McpConfigFileIntegration):
    client_name = "gemini"
    binary = GEMINI_BINARY
    display_name = GEMINI_DISPLAY_NAME
    default_config_path = Path.home() / ".gemini" / "settings.json"

    @_mutmut_mutated(mutants_xǁGeminiIntegrationǁ__init____mutmut)
    def __init__(self, config_path: Path | None = None) -> None:
        super().__init__(config_path or self.default_config_path)

    def xǁGeminiIntegrationǁ__init____mutmut_orig(self, config_path: Path | None = None) -> None:
        super().__init__(config_path or self.default_config_path)

    def xǁGeminiIntegrationǁ__init____mutmut_1(self, config_path: Path | None = None) -> None:
        super().__init__(None)

    def xǁGeminiIntegrationǁ__init____mutmut_2(self, config_path: Path | None = None) -> None:
        super().__init__(config_path and self.default_config_path)

    @_mutmut_mutated(mutants_xǁGeminiIntegrationǁ_config_root_key__mutmut)
    def _config_root_key(self) -> str:
        return "mcpServers"

    def xǁGeminiIntegrationǁ_config_root_key__mutmut_orig(self) -> str:
        return "mcpServers"

    def xǁGeminiIntegrationǁ_config_root_key__mutmut_1(self) -> str:
        return "XXmcpServersXX"

    def xǁGeminiIntegrationǁ_config_root_key__mutmut_2(self) -> str:
        return "mcpservers"

    def xǁGeminiIntegrationǁ_config_root_key__mutmut_3(self) -> str:
        return "MCPSERVERS"

    @_mutmut_mutated(mutants_xǁGeminiIntegrationǁ_build_entry__mutmut)
    def _build_entry(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}

    def xǁGeminiIntegrationǁ_build_entry__mutmut_orig(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}

    def xǁGeminiIntegrationǁ_build_entry__mutmut_1(self) -> dict[str, object]:
        return {"XXcommandXX": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}

    def xǁGeminiIntegrationǁ_build_entry__mutmut_2(self) -> dict[str, object]:
        return {"COMMAND": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}

    def xǁGeminiIntegrationǁ_build_entry__mutmut_3(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[1], "args": mcp_stdio_command()[1:]}

    def xǁGeminiIntegrationǁ_build_entry__mutmut_4(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "XXargsXX": mcp_stdio_command()[1:]}

    def xǁGeminiIntegrationǁ_build_entry__mutmut_5(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "ARGS": mcp_stdio_command()[1:]}

    def xǁGeminiIntegrationǁ_build_entry__mutmut_6(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "args": mcp_stdio_command()[2:]}

mutants_xǁGeminiIntegrationǁ__init____mutmut['_mutmut_orig'] = GeminiIntegration.xǁGeminiIntegrationǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ__init____mutmut['xǁGeminiIntegrationǁ__init____mutmut_1'] = GeminiIntegration.xǁGeminiIntegrationǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ__init____mutmut['xǁGeminiIntegrationǁ__init____mutmut_2'] = GeminiIntegration.xǁGeminiIntegrationǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGeminiIntegrationǁ_config_root_key__mutmut['_mutmut_orig'] = GeminiIntegration.xǁGeminiIntegrationǁ_config_root_key__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ_config_root_key__mutmut['xǁGeminiIntegrationǁ_config_root_key__mutmut_1'] = GeminiIntegration.xǁGeminiIntegrationǁ_config_root_key__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ_config_root_key__mutmut['xǁGeminiIntegrationǁ_config_root_key__mutmut_2'] = GeminiIntegration.xǁGeminiIntegrationǁ_config_root_key__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ_config_root_key__mutmut['xǁGeminiIntegrationǁ_config_root_key__mutmut_3'] = GeminiIntegration.xǁGeminiIntegrationǁ_config_root_key__mutmut_3 # type: ignore # mutmut generated

mutants_xǁGeminiIntegrationǁ_build_entry__mutmut['_mutmut_orig'] = GeminiIntegration.xǁGeminiIntegrationǁ_build_entry__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ_build_entry__mutmut['xǁGeminiIntegrationǁ_build_entry__mutmut_1'] = GeminiIntegration.xǁGeminiIntegrationǁ_build_entry__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ_build_entry__mutmut['xǁGeminiIntegrationǁ_build_entry__mutmut_2'] = GeminiIntegration.xǁGeminiIntegrationǁ_build_entry__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ_build_entry__mutmut['xǁGeminiIntegrationǁ_build_entry__mutmut_3'] = GeminiIntegration.xǁGeminiIntegrationǁ_build_entry__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ_build_entry__mutmut['xǁGeminiIntegrationǁ_build_entry__mutmut_4'] = GeminiIntegration.xǁGeminiIntegrationǁ_build_entry__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ_build_entry__mutmut['xǁGeminiIntegrationǁ_build_entry__mutmut_5'] = GeminiIntegration.xǁGeminiIntegrationǁ_build_entry__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGeminiIntegrationǁ_build_entry__mutmut['xǁGeminiIntegrationǁ_build_entry__mutmut_6'] = GeminiIntegration.xǁGeminiIntegrationǁ_build_entry__mutmut_6 # type: ignore # mutmut generated
