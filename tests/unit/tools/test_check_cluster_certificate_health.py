from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCheckClusterCertificateHealthMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        mock_port = MagicMock()
        mock_port.list_namespaces.return_value = []
        mock_port.list_tls_secrets.return_value = []
        mock_port.list_ingresses.return_value = []

        with patch(
            "hexawyn.mcp.server.build_cluster_certificate_health_adapter",
            return_value=mock_port,
        ):
            result = check_cluster_certificate_health()

        assert isinstance(result, dict)
        assert result["error"] is None

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        with patch(
            "hexawyn.mcp.server.build_cluster_certificate_health_adapter",
            side_effect=RuntimeError("connection failed"),
        ):
            result = check_cluster_certificate_health()

        assert isinstance(result, dict)
        assert "connection failed" in str(result["error"])
