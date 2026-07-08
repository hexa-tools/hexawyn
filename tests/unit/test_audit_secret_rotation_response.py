from __future__ import annotations


class TestAuditSecretRotationResponse:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_response import (
            AuditSecretRotationResponse,
        )

        response = AuditSecretRotationResponse()

        assert response.findings == []
        assert response.excluded_secrets == []
        assert response.total_secrets_checked == 0
        assert response.rotation_threshold_days == 0
        assert response.summary == ""
        assert response.error is None

    def test_accepts_explicit_values(self) -> None:
        from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_response import (
            AuditSecretRotationResponse,
            ExcludedSecretDict,
            StaleSecretFindingDict,
        )

        finding: StaleSecretFindingDict = {
            "name": "db-password",
            "namespace": "production",
            "secret_type": "Opaque",
            "age_days": 180,
            "last_modified": "2025-12-17",
            "referenced_by": ["payment-deploy", "checkout-deploy"],
            "risk_level": "critical",
            "urgency_score": 95,
            "note": None,
        }
        excluded: ExcludedSecretDict = {
            "name": "tls-cert",
            "namespace": "production",
            "reason": "auto-rotated (cert-manager)",
        }

        response = AuditSecretRotationResponse(
            findings=[finding],
            excluded_secrets=[excluded],
            total_secrets_checked=10,
            rotation_threshold_days=90,
            summary="1 secret stale (>90 days) out of 10 checked.",
            error=None,
        )

        assert response.findings == [finding]
        assert response.excluded_secrets == [excluded]
        assert response.total_secrets_checked == 10
        assert response.rotation_threshold_days == 90
        assert "1 secret stale" in response.summary
