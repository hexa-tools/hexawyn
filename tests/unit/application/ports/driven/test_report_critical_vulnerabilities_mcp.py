from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort, CveRaw
from hexawyn.domain.errors import ClusterUnreachableError


def _cves() -> list[CveRaw]:
    return [
        CveRaw(
            business_service_name="payment-service",
            severity="critical",
            count=2,
            oldest_unresolved_days=12,
        ),
        CveRaw(
            business_service_name="auth-service",
            severity="critical",
            count=1,
            oldest_unresolved_days=5,
        ),
    ]


def _port(cves: list[CveRaw]) -> MagicMock:
    port = MagicMock(spec=CriticalCvePort)
    port.get_critical_cves.return_value = cves
    return port


class TestReportCriticalVulnerabilitiesTool:
    def test_three_critical_three_services(self) -> None:
        with patch("hexawyn.mcp.server.build_critical_cve_adapter", return_value=_port(_cves())):
            from hexawyn.mcp.tools.report_critical_vulnerabilities import (
                report_critical_vulnerabilities,
            )

            result = report_critical_vulnerabilities()

        assert result["total_critical_cves"] == 3
        assert result["affected_service_count"] == 2
        assert result["oldest_unresolved_days"] == 12
        assert result["cves"][0]["business_service_name"] == "payment-service"
        assert result["error"] is None

    def test_zero_cves_green(self) -> None:
        with patch("hexawyn.mcp.server.build_critical_cve_adapter", return_value=_port([])):
            from hexawyn.mcp.tools.report_critical_vulnerabilities import (
                report_critical_vulnerabilities,
            )

            result = report_critical_vulnerabilities()

        assert result["total_critical_cves"] == 0

    def test_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_critical_cve_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.report_critical_vulnerabilities import (
                report_critical_vulnerabilities,
            )

            result = report_critical_vulnerabilities()

        assert "down" in result["error"]

    def test_has_register(self) -> None:
        from hexawyn.mcp.tools.report_critical_vulnerabilities import register

        assert callable(register)
