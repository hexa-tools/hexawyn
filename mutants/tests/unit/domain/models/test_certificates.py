from __future__ import annotations

from hexawyn.domain.models.certificates import (
    AcmeChallenge,
    Certificate,
    CertificateIssuer,
    CertificateStatus,
    CertManagerDetectionResult,
    IssuerType,
)


class TestCertificateStatus:
    def test_values(self) -> None:
        assert CertificateStatus.READY.value == "ready"
        assert CertificateStatus.NOT_READY.value == "not_ready"
        assert CertificateStatus.FAILED.value == "failed"


class TestIssuerType:
    def test_values(self) -> None:
        assert IssuerType.LETS_ENCRYPT.value == "lets_encrypt"
        assert IssuerType.SELF_SIGNED.value == "self_signed"


class TestCertificate:
    def test_valid_cert(self) -> None:
        c = Certificate(
            name="payments-tls",
            namespace="production",
            status=CertificateStatus.READY,
            issuer_name="letsencrypt-prod",
            issuer_type=IssuerType.LETS_ENCRYPT,
            dns_names=["payments.example.com"],
            not_before="2026-06-01T00:00:00Z",
            not_after="2026-09-01T00:00:00Z",
            days_until_expiry=60,
            renewal_time="2026-08-01T00:00:00Z",
            auto_renew=True,
            message=None,
        )
        assert c.days_until_expiry == 60  # noqa: PLR2004
        assert c.auto_renew is True

    def test_expired_cert(self) -> None:
        c = Certificate(
            name="old-cert",
            namespace="staging",
            status=CertificateStatus.NOT_READY,
            issuer_name="letsencrypt-staging",
            issuer_type=IssuerType.LETS_ENCRYPT,
            dns_names=["staging.example.com"],
            not_before=None,
            not_after=None,
            days_until_expiry=None,
            renewal_time=None,
            auto_renew=False,
            message="Certificate expired: renewal failed — ACME challenge timeout",
        )
        assert c.days_until_expiry is None
        assert c.message is not None


class TestCertificateIssuer:
    def test_cluster_issuer(self) -> None:
        i = CertificateIssuer(
            name="letsencrypt-prod",
            namespace=None,
            kind="ClusterIssuer",
            issuer_type=IssuerType.LETS_ENCRYPT,
            ready=True,
            server="https://acme-v02.api.letsencrypt.org/directory",
            message=None,
        )
        assert i.namespace is None
        assert i.kind == "ClusterIssuer"


class TestAcmeChallenge:
    def test_pending_challenge(self) -> None:
        ch = AcmeChallenge(
            name="payments-tls-abc-123",
            namespace="production",
            type="dns-01",
            domain="payments.example.com",
            state="pending",
            reason=None,
            age_seconds=45,
        )
        assert ch.type == "dns-01"
        assert ch.state == "pending"


class TestCertManagerDetectionResult:
    def test_installed(self) -> None:
        r = CertManagerDetectionResult(
            installed=True,
            version="v1.16.2",
            namespace="cert-manager",
            total_certs=15,
            ready_certs=12,
            expiring_soon=3,
            failed_certs=1,
            active_challenges=2,
        )
        assert r.expiring_soon == 3  # noqa: PLR2004
