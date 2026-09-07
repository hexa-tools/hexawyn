from __future__ import annotations

from hexawyn.domain.models.certificate import CertificateInfo, CertificateStatus
from hexawyn.domain.services.certificate.checker import CertificateChecker


def _make_cert(  # noqa: PLR0913
    subject_cn: str = "example.com",
    issuer_cn: str = "CA Corp",
    days_remaining: int = 365,
    key_size: int = 2048,
    is_ca: bool = False,
    san_list: list[str] | None = None,
) -> CertificateInfo:
    if san_list is None:
        san_list = ["example.com"]
    return CertificateInfo(
        subject_cn=subject_cn,
        issuer_cn=issuer_cn,
        days_remaining=days_remaining,
        key_size=key_size,
        is_ca=is_ca,
        san_list=san_list,
    )


class TestCertificateCheckerCheck:
    def test_healthy_when_days_above_warning(self) -> None:
        checker = CertificateChecker(warning_days=30, critical_days=7)
        cert = _make_cert(days_remaining=60)

        result = checker.check(cert)

        assert result == CertificateStatus.HEALTHY

    def test_warning_when_days_at_warning_threshold(self) -> None:
        checker = CertificateChecker(warning_days=30, critical_days=7)
        cert = _make_cert(days_remaining=30)

        result = checker.check(cert)

        assert result == CertificateStatus.WARNING

    def test_warning_when_days_between_critical_and_warning(self) -> None:
        checker = CertificateChecker(warning_days=30, critical_days=7)
        cert = _make_cert(days_remaining=15)

        result = checker.check(cert)

        assert result == CertificateStatus.WARNING

    def test_critical_when_days_at_critical_threshold(self) -> None:
        checker = CertificateChecker(warning_days=30, critical_days=7)
        cert = _make_cert(days_remaining=7)

        result = checker.check(cert)

        assert result == CertificateStatus.CRITICAL

    def test_critical_when_days_between_zero_and_critical(self) -> None:
        checker = CertificateChecker(warning_days=30, critical_days=7)
        cert = _make_cert(days_remaining=1)

        result = checker.check(cert)

        assert result == CertificateStatus.CRITICAL

    def test_expired_when_days_negative(self) -> None:
        checker = CertificateChecker()
        cert = _make_cert(days_remaining=-1)

        result = checker.check(cert)

        assert result == CertificateStatus.EXPIRED

    def test_expired_when_days_zero(self) -> None:
        checker = CertificateChecker()
        cert = _make_cert(days_remaining=0)

        result = checker.check(cert)

        assert result == CertificateStatus.CRITICAL

    def test_custom_thresholds_applied(self) -> None:
        checker = CertificateChecker(warning_days=60, critical_days=14)
        cert = _make_cert(days_remaining=50)

        result = checker.check(cert)

        assert result == CertificateStatus.WARNING

    def test_zero_warning_threshold_healthy_passes(self) -> None:
        checker = CertificateChecker(warning_days=0, critical_days=0)
        healthy_cert = _make_cert(days_remaining=1)

        assert checker.check(healthy_cert) == CertificateStatus.HEALTHY

    def test_zero_warning_threshold_day_zero_is_critical(self) -> None:
        checker = CertificateChecker(warning_days=0, critical_days=0)
        cert = _make_cert(days_remaining=0)

        assert checker.check(cert) == CertificateStatus.CRITICAL

    def test_zero_warning_threshold_negative_is_expired(self) -> None:
        checker = CertificateChecker(warning_days=0, critical_days=0)
        cert = _make_cert(days_remaining=-1)

        assert checker.check(cert) == CertificateStatus.EXPIRED

    def test_very_large_days_remaining_healthy(self) -> None:
        checker = CertificateChecker()
        cert = _make_cert(days_remaining=9999)

        result = checker.check(cert)

        assert result == CertificateStatus.HEALTHY


class TestCertificateCheckerAssess:
    def test_happy_path_full_assessment(self) -> None:
        checker = CertificateChecker()
        cert = _make_cert(
            subject_cn="app.internal",
            issuer_cn="CA Corp",
            days_remaining=365,
            key_size=2048,
            san_list=["app.internal", "*.internal"],
        )

        result = checker.assess(cert)

        assert result["status"] == "healthy"
        assert result["days_remaining"] == 365  # noqa: PLR2004
        assert result["subject_cn"] == "app.internal"
        assert result["issuer_cn"] == "CA Corp"
        assert result["is_self_signed"] is False
        assert result["is_ca"] is False
        assert result["key_size"] == 2048  # noqa: PLR2004
        assert result["key_size_ok"] is True
        assert result["has_san"] is True
        assert result["san_count"] == 2  # noqa: PLR2004

    def test_self_signed_detected(self) -> None:
        checker = CertificateChecker()
        cert = _make_cert(subject_cn="self-signed", issuer_cn="self-signed")

        result = checker.assess(cert)

        assert result["is_self_signed"] is True

    def test_key_size_below_minimum(self) -> None:
        checker = CertificateChecker(min_key_size=2048)
        cert = _make_cert(key_size=1024)

        result = checker.assess(cert)

        assert result["key_size_ok"] is False

    def test_no_san_entries(self) -> None:
        checker = CertificateChecker()
        cert = _make_cert(san_list=[])

        result = checker.assess(cert)

        assert result["has_san"] is False
        assert result["san_count"] == 0

    def test_ca_certificate(self) -> None:
        checker = CertificateChecker()
        cert = _make_cert(is_ca=True)

        result = checker.assess(cert)

        assert result["is_ca"] is True

    def test_assess_expired_cert(self) -> None:
        checker = CertificateChecker()
        cert = _make_cert(days_remaining=-5)

        result = checker.assess(cert)

        assert result["status"] == "expired"
        assert result["days_remaining"] == -5  # noqa: PLR2004

    def test_custom_min_key_size(self) -> None:
        checker = CertificateChecker(min_key_size=4096)
        cert = _make_cert(key_size=2048)

        result = checker.assess(cert)

        assert result["key_size_ok"] is False
