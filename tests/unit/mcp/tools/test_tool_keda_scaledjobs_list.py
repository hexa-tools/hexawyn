"""Unit tests for MCP tool: keda_scaledjobs_list."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestKedaScaledJobsListTool:
    def _mock_imports(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.keda.keda_scaledjobs_list.keda_scaledjobs_list_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.keda.keda_scaledjobs_list.command"] = MagicMock()

    def test_keda_scaledjobs_list_returns_dict(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.keda_scaledjobs_list import keda_scaledjobs_list

        mock_response = MagicMock()
        mock_response.scaled_jobs = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.tools.keda_scaledjobs_list.KedaScaledJobsListUseCase",
                return_value=mock_uc,
            ),
            patch("hexawyn.mcp.server.build_keda_adapter", return_value=MagicMock()),
        ):
            result = keda_scaledjobs_list()

        assert isinstance(result, dict)
        assert "scaled_jobs" in result

    def test_keda_scaledjobs_list_handles_error(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.keda_scaledjobs_list import keda_scaledjobs_list

        with patch(
            "hexawyn.mcp.server.build_keda_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = keda_scaledjobs_list()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        self._mock_imports()
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.keda_scaledjobs_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
