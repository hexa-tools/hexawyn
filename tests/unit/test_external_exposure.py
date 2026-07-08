"""Unit tests for the Unintended External Exposure domain models."""

from __future__ import annotations

import dataclasses

import pytest


class TestExternalExposureFinding:
    def test_creates_finding_with_expected_fields(self) -> None:
        from hexawyn.domain.models.external_exposure import ExternalExposureFinding

        finding = ExternalExposureFinding(
            name="postgres-svc",
            namespace="production",
            service_type="LoadBalancer",
            ports=[5432],
            external_ip="34.120.45.12",
            external_hostname=None,
            node_port=None,
            is_pending=False,
            risk_level="critical",
            note=None,
        )

        assert finding.name == "postgres-svc"
        assert finding.namespace == "production"
        assert finding.service_type == "LoadBalancer"
        assert finding.ports == [5432]
        assert finding.external_ip == "34.120.45.12"
        assert finding.external_hostname is None
        assert finding.node_port is None
        assert finding.is_pending is False
        assert finding.risk_level == "critical"
        assert finding.note is None

    def test_node_port_finding_has_no_external_ip(self) -> None:
        from hexawyn.domain.models.external_exposure import ExternalExposureFinding

        finding = ExternalExposureFinding(
            name="redis-svc",
            namespace="staging",
            service_type="NodePort",
            ports=[6379],
            external_ip=None,
            external_hostname=None,
            node_port=31234,
            is_pending=False,
            risk_level="high",
            note=None,
        )

        assert finding.node_port == 31234
        assert finding.external_ip is None

    def test_pending_load_balancer_finding(self) -> None:
        from hexawyn.domain.models.external_exposure import ExternalExposureFinding

        finding = ExternalExposureFinding(
            name="new-svc",
            namespace="production",
            service_type="LoadBalancer",
            ports=[443],
            external_ip=None,
            external_hostname=None,
            node_port=None,
            is_pending=True,
            risk_level="medium",
            note=None,
        )

        assert finding.is_pending is True

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.external_exposure import ExternalExposureFinding

        finding = ExternalExposureFinding(
            name="s",
            namespace="n",
            service_type="NodePort",
            ports=[],
            external_ip=None,
            external_hostname=None,
            node_port=None,
            is_pending=False,
            risk_level="low",
            note=None,
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            finding.risk_level = "critical"  # type: ignore[misc]


class TestExcludedExposure:
    def test_creates_excluded_exposure_with_expected_fields(self) -> None:
        from hexawyn.domain.models.external_exposure import ExcludedExposure

        excluded = ExcludedExposure(
            name="api-gateway", namespace="production", reason="allowlisted"
        )

        assert excluded.name == "api-gateway"
        assert excluded.namespace == "production"
        assert excluded.reason == "allowlisted"


class TestExternalExposureReport:
    def test_creates_report_with_expected_fields(self) -> None:
        from hexawyn.domain.models.external_exposure import (
            ExcludedExposure,
            ExternalExposureFinding,
            ExternalExposureReport,
        )

        finding = ExternalExposureFinding(
            name="postgres-svc",
            namespace="production",
            service_type="LoadBalancer",
            ports=[5432],
            external_ip="34.120.45.12",
            external_hostname=None,
            node_port=None,
            is_pending=False,
            risk_level="critical",
            note=None,
        )
        excluded = ExcludedExposure(
            name="api-gateway", namespace="production", reason="allowlisted"
        )
        report = ExternalExposureReport(
            findings=[finding],
            excluded_exposures=[excluded],
            total_external_services_checked=5,
            summary="1 unintended external service found out of 5 checked.",
        )

        assert report.findings == [finding]
        assert report.excluded_exposures == [excluded]
        assert report.total_external_services_checked == 5
        assert "1 unintended" in report.summary
