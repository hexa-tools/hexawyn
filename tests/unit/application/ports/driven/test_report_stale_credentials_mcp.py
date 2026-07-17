from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.stale_credentials_port import (
    StaleCredentialRaw,
    StaleCredentialsPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _creds() -> list[StaleCredentialRaw]:
    return [
        StaleCredentialRaw(name="db-password", risk_level="critical", days_unrotated=120),
        StaleCredentialRaw(name="api-key", risk_level="critical", days_unrotated=95),
        StaleCredentialRaw(name="tls-cert", risk_level="critical", days_unrotated=100),
    ] + [
        StaleCredentialRaw(name=f"svc-{i}", risk_level="medium", days_unrotated=100)
        for i in range(5)
    ]


def _port(creds: list[StaleCredentialRaw]) -> MagicMock:
    port = MagicMock(spec=StaleCredentialsPort)
    port.get_stale_credentials.return_value = creds
    return port


class TestReportStaleCredentialsTool:
    def test_eight_stale_three_critical(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_stale_credentials_adapter", return_value=_port(_creds())
        ):
            from hexawyn.mcp.tools.report_stale_credentials import report_stale_credentials

            result = report_stale_credentials()

        assert result["total_stale"] == 8
        assert result["critical_count"] == 3
        assert result["credentials"][0]["name"] == "db-password"
        assert result["error"] is None

    def test_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_stale_credentials_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.report_stale_credentials import report_stale_credentials

            result = report_stale_credentials()
        assert "down" in result["error"]

    def test_has_register(self) -> None:
        from hexawyn.mcp.tools.report_stale_credentials import register

        assert callable(register)
