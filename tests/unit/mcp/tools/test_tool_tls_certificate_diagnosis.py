"""Unit tests for MCP tool: tls_certificate_diagnosis."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestTlsCertificateDiagnosisTool:
    def test_tls_certificate_diagnosis_returns_dict(self) -> None:
        from hexawyn.mcp.tools.tls_certificate_diagnosis import tls_certificate_diagnosis

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_certificate_investigation_adapter",
                return_value=MagicMock(),
            ),
        ):
            result = tls_certificate_diagnosis(
                ingress_name="test-ingress_name", namespace="test-ns"
            )

        assert isinstance(result, dict)

    def test_tls_certificate_diagnosis_handles_error(self) -> None:
        from hexawyn.mcp.tools.tls_certificate_diagnosis import tls_certificate_diagnosis

        with (
            patch(
                "hexawyn.mcp.server.build_certificate_investigation_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = tls_certificate_diagnosis(
                ingress_name="test-ingress_name", namespace="test-ns"
            )

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.tls_certificate_diagnosis")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
