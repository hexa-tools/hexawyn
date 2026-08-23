"""Unit tests for MCP tool: keda_scaledobject_status."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestKedaScaledObjectStatusTool:
    def _mock_imports(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.keda.keda_scaledobject_status.keda_scaledobject_status_use_case"
        ] = MagicMock()
        sys.modules["hexawyn.application.use_case.keda.keda_scaledobject_status.command"] = (
            MagicMock()
        )

    def test_keda_scaledobject_status_returns_dict(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.keda_scaledobject_status import (
            keda_scaledobject_status,
        )

        mock_uc = MagicMock()
        mock_uc.execute.return_value = MagicMock()

        with (
            patch(
                "hexawyn.mcp.tools.keda_scaledobject_status.KedaScaledobjectStatusUseCase",
                return_value=mock_uc,
            ),
            patch("hexawyn.mcp.server.build_keda_adapter", return_value=MagicMock()),
        ):
            result = keda_scaledobject_status()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_keda_scaledobject_status_handles_error(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.keda_scaledobject_status import (
            keda_scaledobject_status,
        )

        with patch(
            "hexawyn.mcp.server.build_keda_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = keda_scaledobject_status()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        self._mock_imports()
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.keda_scaledobject_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
