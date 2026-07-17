"""Tests for DetectOverProvisionedNamespacesResponse."""

from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_response import (
    DetectOverProvisionedNamespacesResponse,
)
from hexawyn.domain.models.namespace_waste import OverProvisioningReport


def _empty_report() -> OverProvisioningReport:
    return OverProvisioningReport(
        namespaces=[],
        excluded=[],
        total_wasted_cpu_cores=0.0,
        total_wasted_memory_gb=0.0,
        analysis_window_days=7,
    )


class TestDetectOverProvisionedNamespacesResponse:
    def test_stores_report(self) -> None:
        report = _empty_report()
        response = DetectOverProvisionedNamespacesResponse(report=report, prometheus_available=True)
        assert response.report is report

    def test_prometheus_available_flag(self) -> None:
        response = DetectOverProvisionedNamespacesResponse(
            report=_empty_report(), prometheus_available=False
        )
        assert response.prometheus_available is False
