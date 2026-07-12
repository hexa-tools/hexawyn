from __future__ import annotations

import importlib
from pathlib import Path

from hexawyn.application.ports.driven.tool_discovery_port import ToolDiscoveryPort
from hexawyn.domain.models.tool_registry import ToolRegistry, ToolSchema

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent.parent
_TOOLS_DIR = _REPO_ROOT / "src" / "hexawyn" / "mcp" / "tools"
_NAMESPACE = "hexawyn.mcp.tools"


class MCPToolDiscoveryAdapter(ToolDiscoveryPort):
    """Discovers MCP tools by scanning the mcp/tools/ directory.

    Each Python module in the directory corresponds to a tool. The tool name
    is the module name, and the description is extracted from the first line
    of the module docstring.
    """

    def discover(self) -> ToolRegistry:
        tools: list[ToolSchema] = []
        if not _TOOLS_DIR.exists():
            return ToolRegistry()

        for module_path in sorted(_TOOLS_DIR.glob("*.py")):
            module_name = module_path.stem
            if module_name.startswith("_"):
                continue

            try:
                mod = importlib.import_module(f"{_NAMESPACE}.{module_name}")
            except Exception:
                continue

            description = _extract_description(mod)
            tool = ToolSchema(name=module_name, description=description, input_schema={})
            tools.append(tool)

        return ToolRegistry(tools=tools)


def _extract_description(module: object) -> str:
    doc = getattr(module, "__doc__", None)
    if not isinstance(doc, str) or not doc.strip():
        return ""
    first_line = doc.strip().split("\n")[0].strip()
    # Remove the MCP tool: prefix if present
    if first_line.lower().startswith("mcp tool:"):
        first_line = first_line[len("mcp tool:") :].strip()
    return first_line
