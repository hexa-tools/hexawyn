"""Unit tests for SecretRotationAuditService (mocks SecretRotationAuditPort).

Covers the ticket's five Test Scenarios (TC1-TC5) and its five Edge Cases by
name in the test names. All "days ago" values are computed relative to
date.today() so the tests remain correct regardless of when they run.
"""

from __future__ import annotations

from datetime import date, timedelta
from unittest.mock import MagicMock

from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.service.secret_rotation_audit_service import SecretRotationAuditService


def _days_ago(days: int) -> str:
    return (date.today() - timedelta(days=days)).isoformat() + "T00:00:00+00:00"


def _managed_field(time: str, touches_data: bool = True) -> dict:
    fields = {"f:data": {}} if touches_data else {"f:metadata": {"f:labels": {}}}
    return {
        "manager": "kubectl-client-side-apply",
        "operation": "Update",
        "time": time,
        "fields_v1_raw": fields,
    }


def _secret(
    name: str,
    namespace: str = "production",
    secret_type: str = "Opaque",
    data_keys: list[str] | None = None,
    managed_fields: list[dict] | None = None,
    creation_timestamp: str = "2000-01-01T00:00:00+00:00",
    annotations: dict[str, str] | None = None,
) -> dict:
    return {
        "name": name,
        "namespace": namespace,
        "secret_type": secret_type,
        "data_keys": data_keys or [],
        "managed_fields": managed_fields or [],
        "creation_timestamp": creation_timestamp,
        "annotations": annotations or {},
    }


def _reference(
    secret_name: str, namespace: str = "production", workload_name: str = "deploy"
) -> dict:
    return {"secret_name": secret_name, "namespace": namespace, "workload_name": workload_name}


def _make_service(
    secrets: list[dict] | None = None,
    references: list[dict] | None = None,
    exempt_namespaces: set[str] | None = None,
) -> tuple[SecretRotationAuditService, MagicMock]:
    port = MagicMock()
    port.list_secrets.return_value = secrets or []
    port.list_secret_references.return_value = references or []
    port.get_namespace_rotation_exemptions.return_value = exempt_namespaces or set()
    service = SecretRotationAuditService(secret_rotation_port=port)
    return service, port


class TestDbPasswordCritical:
    def test_tc1_db_password_180_days_ago_is_critical(self) -> None:
        service, _ = _make_service(
            secrets=[
                _secret(
                    "db-password",
                    data_keys=["DB_PASSWORD"],
                    managed_fields=[_managed_field(_days_ago(180))],
                )
            ]
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        finding = response.findings[0]
        assert finding["risk_level"] == "critical"
        assert finding["age_days"] == 180


class TestTlsCritical:
    def test_tc2_tls_secret_95_days_is_critical(self) -> None:
        service, _ = _make_service(
            secrets=[
                _secret(
                    "ingress-tls",
                    secret_type="kubernetes.io/tls",
                    data_keys=["tls.crt", "tls.key"],
                    managed_fields=[_managed_field(_days_ago(95))],
                )
            ]
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        finding = response.findings[0]
        assert finding["risk_level"] == "critical"


class TestWithinThresholdHealthy:
    def test_tc3_token_30_days_is_within_threshold_not_stale(self) -> None:
        service, _ = _make_service(
            secrets=[
                _secret(
                    "api-token",
                    data_keys=["ACCESS_TOKEN"],
                    managed_fields=[_managed_field(_days_ago(30))],
                )
            ]
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        assert response.findings == []


class TestUnreferencedStaleSecret:
    def test_tc4_unreferenced_stale_secret_is_flagged_unused(self) -> None:
        service, _ = _make_service(
            secrets=[_secret("orphan-secret", managed_fields=[_managed_field(_days_ago(200))])],
            references=[],
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        finding = response.findings[0]
        assert finding["referenced_by"] == []
        assert finding["note"] is not None
        assert "safe to delete" in finding["note"]


class TestEightStaleSecretsRanked:
    def test_tc5_eight_stale_secrets_ranked_by_urgency(self) -> None:
        secrets = [
            _secret(
                f"secret-{i}",
                data_keys=["PASSWORD"],
                managed_fields=[_managed_field(_days_ago(180))],
            )
            for i in range(8)
        ]
        service, _ = _make_service(secrets=secrets)

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        assert len(response.findings) == 8
        urgencies = [finding["urgency_score"] for finding in response.findings]
        assert urgencies == sorted(urgencies, reverse=True)


class TestExternalSecretsOperatorExcluded:
    def test_edge_case_external_secrets_operator_managed_is_excluded(self) -> None:
        service, _ = _make_service(
            secrets=[
                _secret(
                    "es-managed",
                    managed_fields=[_managed_field(_days_ago(200))],
                    annotations={"externalsecrets.io/secret-store": "vault-backend"},
                )
            ]
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        assert response.findings == []
        assert any(
            "externally managed" in excluded["reason"] for excluded in response.excluded_secrets
        )


class TestCertManagerAutoRotated:
    def test_edge_case_cert_manager_tls_is_shown_as_auto_rotated(self) -> None:
        service, _ = _make_service(
            secrets=[
                _secret(
                    "cert-tls",
                    secret_type="kubernetes.io/tls",
                    managed_fields=[_managed_field(_days_ago(200))],
                    annotations={"cert-manager.io/certificate-name": "ingress-cert"},
                )
            ]
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        assert response.findings == []
        assert any("cert-manager" in excluded["reason"] for excluded in response.excluded_secrets)


class TestProjectedVolumeUsageDetected:
    def test_edge_case_multiple_workload_references_are_all_listed(self) -> None:
        """The adapter is responsible for detecting projected-volume refs;
        the service just needs to faithfully attach whatever references it
        receives, regardless of source (env, envFrom, volume, projected)."""
        service, _ = _make_service(
            secrets=[
                _secret(
                    "db-password",
                    data_keys=["DB_PASSWORD"],
                    managed_fields=[_managed_field(_days_ago(180))],
                )
            ],
            references=[
                _reference("db-password", workload_name="payment-deploy"),
                _reference("db-password", workload_name="checkout-deploy"),
            ],
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        finding = response.findings[0]
        assert set(finding["referenced_by"]) == {"payment-deploy", "checkout-deploy"}


class TestLabelOnlyUpdateIsNotRotation:
    def test_edge_case_label_only_update_is_not_treated_as_rotation(self) -> None:
        service, _ = _make_service(
            secrets=[
                _secret(
                    "db-password",
                    data_keys=["DB_PASSWORD"],
                    managed_fields=[
                        _managed_field(_days_ago(180), touches_data=True),
                        _managed_field(_days_ago(5), touches_data=False),
                    ],
                )
            ]
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        finding = response.findings[0]
        assert finding["age_days"] == 180


class TestNamespaceRotationExempt:
    def test_edge_case_namespace_rotation_exempt_is_excluded(self) -> None:
        service, _ = _make_service(
            secrets=[
                _secret(
                    "any-secret",
                    namespace="sandbox",
                    managed_fields=[_managed_field(_days_ago(200))],
                )
            ],
            exempt_namespaces={"sandbox"},
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        assert response.findings == []
        assert any("exempt" in excluded["reason"] for excluded in response.excluded_secrets)


class TestFallsBackToCreationTimestamp:
    def test_falls_back_to_creation_timestamp_when_no_managed_fields_touch_data(self) -> None:
        service, _ = _make_service(
            secrets=[
                _secret("no-managed-fields", creation_timestamp=_days_ago(200), managed_fields=[])
            ]
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        finding = response.findings[0]
        assert finding["age_days"] == 200


class TestCustomRotationThreshold:
    def test_custom_rotation_threshold_days(self) -> None:
        service, _ = _make_service(
            secrets=[_secret("s", managed_fields=[_managed_field(_days_ago(40))])]
        )

        response = service.audit_secret_rotation(
            AuditSecretRotationCommand(rotation_threshold_days=30)
        )

        assert len(response.findings) == 1
        assert response.rotation_threshold_days == 30


class TestTotalSecretsChecked:
    def test_total_secrets_checked_reflects_all_secrets(self) -> None:
        service, _ = _make_service(
            secrets=[
                _secret("a", managed_fields=[_managed_field(_days_ago(200))]),
                _secret("b", managed_fields=[_managed_field(_days_ago(10))]),
            ]
        )

        response = service.audit_secret_rotation(AuditSecretRotationCommand())

        assert response.total_secrets_checked == 2
