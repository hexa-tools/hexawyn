"""Unit tests for MCP tool: detect_missing_probes."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectMissingProbesTool:
    def test_detect_missing_probes_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_missing_probes import detect_missing_probes

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_probe_audit_adapter", return_value=MagicMock()),
        ):
            result = detect_missing_probes()

        assert isinstance(result, dict)

    def test_detect_missing_probes_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_missing_probes import detect_missing_probes

        with (
            patch(
                "hexawyn.mcp.server.build_probe_audit_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_missing_probes()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_missing_probes")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
