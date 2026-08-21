from __future__ import annotations

from hexawyn.cli.integrations.mcp.command import mcp_stdio_command


class TestMcpStdioCommand:
    def test_returns_python_module_launch(self) -> None:
        assert mcp_stdio_command() == ["python", "-m", "hexawyn.mcp.stdio"]
