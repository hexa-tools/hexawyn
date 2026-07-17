from hexawyn.domain.models.platform_reliability import PlatformReliabilityReport


class TestReportPlatformReliabilityResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_response import (  # noqa: E501
            ReportPlatformReliabilityResponse,
        )

        report = PlatformReliabilityReport(period_label="2026-06", uptime_pct=99.95)
        response = ReportPlatformReliabilityResponse(result=report)

        assert response.result is report
        assert response.result.uptime_pct == 99.95
