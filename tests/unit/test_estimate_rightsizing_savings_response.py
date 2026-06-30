"""RED tests — EstimateRightsizingSavingsResponse"""

from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_response import (
    EstimateRightsizingSavingsResponse,
)
from hexawyn.domain.models.rightsizing import RightsizingReport


class TestEstimateRightsizingSavingsResponse:
    def test_stores_report(self) -> None:
        report = RightsizingReport()
        resp = EstimateRightsizingSavingsResponse(report=report)
        assert resp.report is report

    def test_metrics_server_available_defaults_true(self) -> None:
        resp = EstimateRightsizingSavingsResponse(report=RightsizingReport())
        assert resp.metrics_server_available is True
