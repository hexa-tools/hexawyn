"""Unit tests for the Kubernetes Secret Rotation Audit domain models."""

from __future__ import annotations

import dataclasses

import pytest


class TestManagedFieldsEntry:
    def test_creates_entry_with_expected_fields(self) -> None:
        from hexawyn.domain.models.secret_rotation import ManagedFieldsEntry

        entry = ManagedFieldsEntry(
            manager="kubectl-client-side-apply",
            operation="Update",
            time="2025-12-17T00:00:00+00:00",
            fields_v1_raw={"f:data": {"f:PASSWORD": {}}},
        )

        assert entry.manager == "kubectl-client-side-apply"
        assert entry.operation == "Update"
        assert entry.time == "2025-12-17T00:00:00+00:00"
        assert entry.fields_v1_raw == {"f:data": {"f:PASSWORD": {}}}

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.secret_rotation import ManagedFieldsEntry

        entry = ManagedFieldsEntry(manager="m", operation="Update", time="t", fields_v1_raw={})

        with pytest.raises(dataclasses.FrozenInstanceError):
            entry.manager = "other"  # type: ignore[misc]


class TestStaleSecretFinding:
    def test_creates_finding_with_expected_fields(self) -> None:
        from hexawyn.domain.models.secret_rotation import StaleSecretFinding

        finding = StaleSecretFinding(
            name="db-password",
            namespace="production",
            secret_type="Opaque",
            age_days=180,
            last_modified="2025-12-17",
            referenced_by=["payment-deploy", "checkout-deploy"],
            risk_level="critical",
            urgency_score=95,
            note=None,
        )

        assert finding.name == "db-password"
        assert finding.namespace == "production"
        assert finding.secret_type == "Opaque"
        assert finding.age_days == 180
        assert finding.last_modified == "2025-12-17"
        assert finding.referenced_by == ["payment-deploy", "checkout-deploy"]
        assert finding.risk_level == "critical"
        assert finding.urgency_score == 95
        assert finding.note is None

    def test_note_can_flag_unused_secret(self) -> None:
        from hexawyn.domain.models.secret_rotation import StaleSecretFinding

        finding = StaleSecretFinding(
            name="orphan-secret",
            namespace="staging",
            secret_type="Opaque",
            age_days=200,
            last_modified="2025-06-01",
            referenced_by=[],
            risk_level="low",
            urgency_score=20,
            note="unused by any pod or deployment — safe to delete",
        )

        assert finding.referenced_by == []
        assert finding.note == "unused by any pod or deployment — safe to delete"

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.secret_rotation import StaleSecretFinding

        finding = StaleSecretFinding(
            name="s",
            namespace="n",
            secret_type="Opaque",
            age_days=1,
            last_modified="2026-01-01",
            referenced_by=[],
            risk_level="low",
            urgency_score=0,
            note=None,
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            finding.urgency_score = 50  # type: ignore[misc]


class TestExcludedSecret:
    def test_creates_excluded_secret_with_expected_fields(self) -> None:
        from hexawyn.domain.models.secret_rotation import ExcludedSecret

        excluded = ExcludedSecret(
            name="tls-cert",
            namespace="production",
            reason="auto-rotated (cert-manager)",
        )

        assert excluded.name == "tls-cert"
        assert excluded.namespace == "production"
        assert excluded.reason == "auto-rotated (cert-manager)"


class TestSecretRotationReport:
    def test_creates_report_with_expected_fields(self) -> None:
        from hexawyn.domain.models.secret_rotation import (
            ExcludedSecret,
            SecretRotationReport,
            StaleSecretFinding,
        )

        finding = StaleSecretFinding(
            name="db-password",
            namespace="production",
            secret_type="Opaque",
            age_days=180,
            last_modified="2025-12-17",
            referenced_by=["payment-deploy"],
            risk_level="critical",
            urgency_score=95,
            note=None,
        )
        excluded = ExcludedSecret(
            name="tls-cert", namespace="production", reason="auto-rotated (cert-manager)"
        )
        report = SecretRotationReport(
            findings=[finding],
            excluded_secrets=[excluded],
            total_secrets_checked=10,
            rotation_threshold_days=90,
            summary="1 secret stale (>90 days) out of 10 checked.",
        )

        assert report.findings == [finding]
        assert report.excluded_secrets == [excluded]
        assert report.total_secrets_checked == 10
        assert report.rotation_threshold_days == 90
        assert "1 secret stale" in report.summary
