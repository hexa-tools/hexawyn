"""Unit tests for certificate domain models."""

import dataclasses
from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.certificate import CertificateInfo, CertificateStatus


class TestCertificateInfo:
    def test_minimal_construction(self) -> None:
        cert = CertificateInfo(subject_cn="example.com", issuer_cn="CA Inc")
        assert cert.subject_cn == "example.com"
        assert cert.issuer_cn == "CA Inc"
        assert cert.san_list == []
        assert cert.days_remaining == 0
        assert cert.is_ca is False
        assert cert.key_size == 0

    def test_full_construction(self) -> None:
        now = datetime.now(UTC)
        expiry = now + timedelta(days=30)
        cert = CertificateInfo(
            subject_cn="api.hexawyn.com",
            issuer_cn="LetsEncrypt R3",
            not_before=now,
            not_after=expiry,
            days_remaining=30,
            san_list=["api.hexawyn.com", "*.hexawyn.com"],
            is_ca=False,
            key_size=2048,
            serial_number="AB:CD:EF",
            signature_algorithm="sha256WithRSAEncryption",
        )
        assert cert.days_remaining == 30
        assert len(cert.san_list) == 2
        assert cert.key_size == 2048

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(CertificateInfo)


class TestCertificateStatus:
    def test_all_values(self) -> None:
        assert CertificateStatus.HEALTHY.value == "healthy"
        assert CertificateStatus.WARNING.value == "warning"
        assert CertificateStatus.CRITICAL.value == "critical"
        assert CertificateStatus.EXPIRED.value == "expired"
