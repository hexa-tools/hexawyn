"""Unit tests for MCP tool: check_machine_config_pool_status."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCheckMachineConfigPoolStatusTool:
    def test_check_machine_config_pool_status_returns_dict(self) -> None:
        from hexawyn.mcp.tools.check_machine_config_pool_status import (
            check_machine_config_pool_status,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_machine_config_pool_adapter", return_value=MagicMock()),
        ):
            result = check_machine_config_pool_status()

        assert isinstance(result, dict)

    def test_check_machine_config_pool_status_handles_error(self) -> None:
        from hexawyn.mcp.tools.check_machine_config_pool_status import (
            check_machine_config_pool_status,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_machine_config_pool_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = check_machine_config_pool_status()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.check_machine_config_pool_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
