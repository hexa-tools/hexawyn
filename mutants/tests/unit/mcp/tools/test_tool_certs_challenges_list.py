"""Unit tests for MCP tool: certs_challenges_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCertsChallengesListTool:
    def test_certs_challenges_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.certs_challenges_list import certs_challenges_list

        with patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()):
            result = certs_challenges_list()

        assert isinstance(result, dict)
        assert "error" in result

    def test_certs_challenges_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_challenges_list import certs_challenges_list

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = certs_challenges_list()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_certs_challenges_list_success_path(self) -> None:
        from hexawyn.mcp.tools.certs_challenges_list import certs_challenges_list

        mock_response = MagicMock()
        mock_response.challenges = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.certs_challenges_list.CertsChallengesListUseCase",
                return_value=mock_uc,
            ),
        ):
            result = certs_challenges_list()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.certs_challenges_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
