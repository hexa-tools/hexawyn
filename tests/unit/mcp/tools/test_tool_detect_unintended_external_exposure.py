"""Unit tests for MCP tool: detect_unintended_external_exposure."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectUnintendedExternalExposureTool:
    def test_detect_unintended_external_exposure_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_unintended_external_exposure import (
            detect_unintended_external_exposure,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_external_exposure_audit_adapter", return_value=MagicMock()
            ),
        ):
            result = detect_unintended_external_exposure()

        assert isinstance(result, dict)

    def test_detect_unintended_external_exposure_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_unintended_external_exposure import (
            detect_unintended_external_exposure,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_external_exposure_audit_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_unintended_external_exposure()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_unintended_external_exposure")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
