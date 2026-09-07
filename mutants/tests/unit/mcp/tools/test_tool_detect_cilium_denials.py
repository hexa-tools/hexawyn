"""Unit tests for MCP tool: detect_cilium_denials."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectCiliumDenialsTool:
    def test_detect_cilium_denials_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_cilium_denials import detect_cilium_denials

        mock_group = MagicMock()
        mock_group.policy = "default/deny-all"
        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "present"
        mock_response.total_denials = 2
        mock_response.groups = [mock_group]
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_cilium_hubble_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.detect_cilium_denials.DetectCiliumDenialsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = detect_cilium_denials(namespace="payments")

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["status"] == "present"
        assert result["error"] is None

    def test_detect_cilium_denials_error_returns_unknown(self) -> None:
        from hexawyn.mcp.tools.detect_cilium_denials import detect_cilium_denials

        with patch(
            "hexawyn.mcp.server.build_cilium_hubble_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = detect_cilium_denials()

        assert isinstance(result, dict)
        assert result["installed"] is False
        assert result["status"] == "unknown"
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_cilium_denials")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
