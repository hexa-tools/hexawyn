"""Unit tests for MCP tool: tls_certificate_diagnosis."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestTlsCertificateDiagnosisTool:
    def _mock_imports(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.tls_certificate_diagnosis_use_case"
        ] = MagicMock()
        sys.modules[
            "hexawyn.application.use_case.cert_manager.tls_certificate_diagnosis.command"
        ] = MagicMock()

    def test_tls_certificate_diagnosis_returns_dict(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.tls_certificate_diagnosis import (
            tls_certificate_diagnosis,
        )

        with patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()):
            result = tls_certificate_diagnosis("test-ingress", "test-ns")

        assert isinstance(result, dict)
        assert "error" in result

    def test_tls_certificate_diagnosis_handles_error(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.tls_certificate_diagnosis import (
            tls_certificate_diagnosis,
        )

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = tls_certificate_diagnosis("test-ingress", "test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        self._mock_imports()
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.tls_certificate_diagnosis")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
