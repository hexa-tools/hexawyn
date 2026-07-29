"""Unit tests for MCP tool: certs_detect."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCertsDetectTool:
    def test_certs_detect_returns_dict(self) -> None:
        from hexawyn.mcp.tools.certs_detect import certs_detect

        with patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()):
            result = certs_detect()

        assert isinstance(result, dict)
        assert "error" in result

    def test_certs_detect_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_detect import certs_detect

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = certs_detect()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_certs_detect_success_path(self) -> None:
        from hexawyn.mcp.tools.certs_detect import certs_detect

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.version = "v1.0.0"
        mock_response.namespace = "cert-manager"
        mock_response.total_certs = 5
        mock_response.ready_certs = 5
        mock_response.expiring_soon = 0
        mock_response.failed_certs = 0
        mock_response.active_challenges = 0
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.certs_detect.CertsDetectUseCase",
                return_value=mock_uc,
            ),
        ):
            result = certs_detect()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.certs_detect")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
