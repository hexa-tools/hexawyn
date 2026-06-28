"""Unit tests for the certificate checker service."""

from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.certificate import CertificateInfo, CertificateStatus
from hexawyn.domain.services.certificate.checker import CertificateChecker


class TestCertificateChecker:
    def test_healthy_certificate(self) -> None:
        checker = CertificateChecker(warning_days=30, critical_days=7)
        now = datetime.now(UTC)
        cert = CertificateInfo(
            subject_cn="example.com",
            issuer_cn="CA",
            not_after=now + timedelta(days=90),
            days_remaining=90,
        )
        status = checker.check(cert)
        assert status == CertificateStatus.HEALTHY

    def test_warning_certificate(self) -> None:
        checker = CertificateChecker(warning_days=30, critical_days=7)
        now = datetime.now(UTC)
        cert = CertificateInfo(
            subject_cn="example.com",
            issuer_cn="CA",
            not_after=now + timedelta(days=20),
            days_remaining=20,
        )
        status = checker.check(cert)
        assert status == CertificateStatus.WARNING

    def test_critical_certificate(self) -> None:
        checker = CertificateChecker(warning_days=30, critical_days=7)
        now = datetime.now(UTC)
        cert = CertificateInfo(
            subject_cn="example.com",
            issuer_cn="CA",
            not_after=now + timedelta(days=3),
            days_remaining=3,
        )
        status = checker.check(cert)
        assert status == CertificateStatus.CRITICAL

    def test_expired_certificate(self) -> None:
        checker = CertificateChecker(warning_days=30, critical_days=7)
        cert = CertificateInfo(
            subject_cn="expired.com",
            issuer_cn="CA",
            days_remaining=-5,
        )
        status = checker.check(cert)
        assert status == CertificateStatus.EXPIRED

    def test_custom_thresholds(self) -> None:
        checker = CertificateChecker(warning_days=60, critical_days=15)
        now = datetime.now(UTC)
        cert = CertificateInfo(
            subject_cn="example.com",
            issuer_cn="CA",
            not_after=now + timedelta(days=45),
            days_remaining=45,
        )
        assert checker.check(cert) == CertificateStatus.WARNING

    def test_self_signed_certificate_flag(self) -> None:
        checker = CertificateChecker()
        cert = CertificateInfo(
            subject_cn="self-signed.local",
            issuer_cn="self-signed.local",
            is_ca=True,
        )
        result = checker.assess(cert)
        assert result["is_self_signed"] is True
        assert result["is_ca"] is True

    def test_assess_returns_full_report(self) -> None:
        checker = CertificateChecker()
        now = datetime.now(UTC)
        cert = CertificateInfo(
            subject_cn="api.hexawyn.com",
            issuer_cn="LetsEncrypt",
            not_after=now + timedelta(days=60),
            days_remaining=60,
            key_size=2048,
            san_list=["api.hexawyn.com"],
        )
        report = checker.assess(cert)
        assert report["status"] == "healthy"
        assert report["days_remaining"] == 60
        assert report["key_size_ok"] is True
        assert report["has_san"] is True
