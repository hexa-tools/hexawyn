"""Unit tests for the Configuration Drift Detection domain models — pure
dataclasses, no I/O."""

from __future__ import annotations

from hexawyn.domain.models.configuration_drift import (
    ConfigurationDriftReport,
    ConfigurationDriftRequest,
    DriftedField,
    DriftResult,
    ResourceManifest,
)


class TestDriftedField:
    def test_fields(self) -> None:
        field = DriftedField(
            field_path="spec.template.spec.containers[0].image",
            desired_value="payment:v1.2",
            live_value="payment:v1.3-hotfix",
            severity="critical",
        )

        assert field.severity == "critical"
        assert field.desired_value == "payment:v1.2"


class TestResourceManifest:
    def test_fields(self) -> None:
        manifest = ResourceManifest(
            kind="Deployment", name="payment-service", namespace="production", data={}
        )

        assert manifest.kind == "Deployment"
        assert manifest.data == {}


class TestConfigurationDriftRequest:
    def test_defaults(self) -> None:
        request = ConfigurationDriftRequest(namespace="production")

        assert request.kustomize_paths == []


class TestDriftResult:
    def test_fields(self) -> None:
        result = DriftResult(
            kind="Deployment",
            name="payment-service",
            namespace="production",
            managed_by="helm",
            release_or_source="payment-chart",
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=False,
        )

        assert result.managed_by == "helm"
        assert result.is_orphaned is False


class TestConfigurationDriftReport:
    def test_defaults(self) -> None:
        report = ConfigurationDriftReport(
            drifted_resources=[],
            drifted_by_namespace={},
            in_sync_count=42,
            excluded_resources=[],
            total_checked=42,
            summary="All resources in sync.",
        )

        assert report.in_sync_count == 42
        assert report.drifted_by_namespace == {}
