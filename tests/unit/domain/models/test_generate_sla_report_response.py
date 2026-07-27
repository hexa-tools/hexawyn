from hexawyn.domain.models.sla_report import SlaReport


class TestGenerateSLAReportResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.use_case.workloads.generate_sla_report.response import (  # noqa: E501
            GenerateSLAReportResponse,
        )

        report = SlaReport(quarter_label="2026-Q1")
        response = GenerateSLAReportResponse(result=report)

        assert response.result is report
        assert response.result.quarter_label == "2026-Q1"
