from __future__ import annotations

from unittest.mock import patch

from hexawyn.mcp.stdio import main


class TestMcpStdioEntrypoint:
    def test_main_runs_server_over_stdio(self) -> None:
        with patch("hexawyn.mcp.server.mcp.run") as mock_run:
            main()

        mock_run.assert_called_once_with()
