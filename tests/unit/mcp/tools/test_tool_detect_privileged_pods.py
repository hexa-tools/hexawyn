"""Unit tests for MCP tool: detect_privileged_pods."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectPrivilegedPodsTool:
    def test_detect_privileged_pods_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_privileged_pods import detect_privileged_pods

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pod_security_adapter", return_value=MagicMock()),
        ):
            result = detect_privileged_pods()

        assert isinstance(result, dict)

    def test_detect_privileged_pods_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_privileged_pods import detect_privileged_pods

        with (
            patch(
                "hexawyn.mcp.server.build_pod_security_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_privileged_pods()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_privileged_pods")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
