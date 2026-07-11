from hexawyn.domain.models.sla_report import SlaReport


class TestGenerateSlaReportResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_response import (  # noqa: E501
            GenerateSlaReportResponse,
        )

        report = SlaReport(quarter_label="2026-Q1")
        response = GenerateSlaReportResponse(result=report)

        assert response.result is report
        assert response.result.quarter_label == "2026-Q1"
