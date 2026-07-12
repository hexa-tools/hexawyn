from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.unauthorized_access_port import (
    UnauthorizedAccessPort,
    UnauthorizedAccessRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _raw(count: int = 52, source: str = "external") -> UnauthorizedAccessRaw:
    return UnauthorizedAccessRaw(attempt_count=count, window_minutes=30, source_type=source)


def _port(raw: UnauthorizedAccessRaw) -> MagicMock:
    port = MagicMock(spec=UnauthorizedAccessPort)
    port.get_unauthorized_access_data.return_value = raw
    return port


class TestReportUnauthorizedAccessTool:
    def test_fifty_two_external_high(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_unauthorized_access_adapter",
            return_value=_port(_raw(52, "external")),
        ):
            from hexawyn.mcp.tools.report_unauthorized_access import report_unauthorized_access

            result = report_unauthorized_access()

        assert result["attempt_count"] == 52
        assert result["alert_level"] == "high"
        assert result["source_type"] == "external"
        assert result["error"] is None

    def test_zero_attempts_low(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_unauthorized_access_adapter",
            return_value=_port(_raw(0)),
        ):
            from hexawyn.mcp.tools.report_unauthorized_access import report_unauthorized_access

            result = report_unauthorized_access()
        assert result["alert_level"] == "low"

    def test_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_unauthorized_access_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.report_unauthorized_access import report_unauthorized_access

            result = report_unauthorized_access()
        assert "down" in result["error"]

    def test_has_register(self) -> None:
        from hexawyn.mcp.tools.report_unauthorized_access import register

        assert callable(register)
