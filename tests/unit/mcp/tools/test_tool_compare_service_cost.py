"""Unit tests for MCP tool: compare_service_cost."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestCompareServiceCostTool:
    def test_compare_service_cost_returns_dict(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.finops.compare_service_cost.compare_service_cost_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.finops.compare_service_cost.command"] = (
            MagicMock()
        )

        from hexawyn.mcp.tools.compare_service_cost import compare_service_cost

        with patch("hexawyn.mcp.server.build_service_cost_adapter", return_value=MagicMock()):
            result = compare_service_cost("test-service")

        assert isinstance(result, dict)
        assert "error" in result

    def test_compare_service_cost_handles_error(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.finops.compare_service_cost.compare_service_cost_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.finops.compare_service_cost.command"] = (
            MagicMock()
        )

        from hexawyn.mcp.tools.compare_service_cost import compare_service_cost

        with patch(
            "hexawyn.mcp.server.build_service_cost_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = compare_service_cost("test-service")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.finops.compare_service_cost.compare_service_cost_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.finops.compare_service_cost.command"] = (
            MagicMock()
        )
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compare_service_cost")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
