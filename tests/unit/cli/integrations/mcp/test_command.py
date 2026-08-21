from __future__ import annotations

import sys

from hexawyn.cli.integrations.mcp.command import mcp_stdio_command


class TestMcpStdioCommand:
    def test_returns_current_python_module_launch(self) -> None:
        assert mcp_stdio_command() == [sys.executable, "-m", "hexawyn.mcp.stdio"]
