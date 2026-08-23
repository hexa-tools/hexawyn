"""Unit tests for MCP tool: keda_scaledjob_get."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestKedaScaledJobGetTool:
    def _mock_imports(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.keda.keda_scaledjob_get.keda_scaledjob_get_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.keda.keda_scaledjob_get.command"] = MagicMock()

    def test_keda_scaledjob_get_returns_dict(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.keda_scaledjob_get import keda_scaledjob_get

        with patch("hexawyn.mcp.server.build_keda_adapter", return_value=MagicMock()):
            result = keda_scaledjob_get("test-job", "test-ns")

        assert isinstance(result, dict)

    def test_keda_scaledjob_get_handles_error(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.keda_scaledjob_get import keda_scaledjob_get

        with patch(
            "hexawyn.mcp.server.build_keda_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = keda_scaledjob_get("test-job", "test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        self._mock_imports()
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.keda_scaledjob_get")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
