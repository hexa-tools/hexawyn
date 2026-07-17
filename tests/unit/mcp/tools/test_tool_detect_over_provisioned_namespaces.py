"""Unit tests for MCP tool: detect_over_provisioned_namespaces."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectOverProvisionedNamespacesTool:
    def test_detect_over_provisioned_namespaces_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_over_provisioned_namespaces import (
            detect_over_provisioned_namespaces,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_waste_adapter", return_value=MagicMock()),
        ):
            result = detect_over_provisioned_namespaces()

        assert isinstance(result, dict)

    def test_detect_over_provisioned_namespaces_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_over_provisioned_namespaces import (
            detect_over_provisioned_namespaces,
        )

        with (
            patch("hexawyn.mcp.server.build_waste_adapter", side_effect=RuntimeError("test error")),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_over_provisioned_namespaces()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_over_provisioned_namespaces")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
