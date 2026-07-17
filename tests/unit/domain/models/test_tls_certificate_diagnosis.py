from __future__ import annotations

import datetime

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509 import random_serial_number
from cryptography.x509.oid import NameOID
from hexawyn.domain.models.tls_certificate_diagnosis import (
    CertificateDiagnosis,
    CertificateStatus,
    TLSCertificateDiagnosticRequest,
)


def _make_cert(common_name: str, sans: list[str], days_ahead: int, add_san: bool = True) -> str:
    key = rsa.generate_private_key(65537, 2048)
    now = datetime.datetime.now(datetime.UTC)
    builder = (
        x509.CertificateBuilder()
        .subject_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, common_name)]))
        .issuer_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "Test CA")]))
        .public_key(key.public_key())
        .serial_number(random_serial_number())
        .not_valid_before(now - datetime.timedelta(days=30))
        .not_valid_after(now + datetime.timedelta(days=days_ahead))
    )
    if add_san:
        san_dns = [x509.DNSName(s) for s in sans]
        builder = builder.add_extension(x509.SubjectAlternativeName(san_dns), critical=False)
    cert = builder.sign(key, hashes.SHA256())
    return cert.public_bytes(serialization.Encoding.PEM).decode()


class TestCertificateDiagnosis:
    def test_expired_no_cert(self) -> None:
        result = CertificateDiagnosis.compute(
            request=TLSCertificateDiagnosticRequest(
                ingress_name="payment-service",
                namespace="production",
            ),
            cert_pem=None,
            hostname="payment.example.com",
        )
        assert result.status == CertificateStatus.ERROR

    def test_valid(self) -> None:
        cert_pem = _make_cert("payment.example.com", ["payment.example.com"], 45)
        result = CertificateDiagnosis.compute(
            request=TLSCertificateDiagnosticRequest(
                ingress_name="payment-service", namespace="production"
            ),
            cert_pem=cert_pem,
            hostname="payment.example.com",
        )
        assert result.status == CertificateStatus.VALID
        assert result.days_remaining >= 44

    def test_san_mismatch(self) -> None:
        cert_pem = _make_cert("other.example.com", ["other.example.com"], 45)
        result = CertificateDiagnosis.compute(
            request=TLSCertificateDiagnosticRequest(
                ingress_name="payment-service", namespace="production"
            ),
            cert_pem=cert_pem,
            hostname="payment.example.com",
        )
        assert result.status == CertificateStatus.MISCONFIGURED

    def test_parsing_error(self) -> None:
        result = CertificateDiagnosis.compute(
            request=TLSCertificateDiagnosticRequest(ingress_name="svc", namespace="ns"),
            cert_pem="not-a-cert",
            hostname="example.com",
        )
        assert result.status == CertificateStatus.ERROR

    def test_san_wildcard_match(self) -> None:
        cert_pem = _make_cert("*.example.com", ["*.example.com"], 60)
        result = CertificateDiagnosis.compute(
            request=TLSCertificateDiagnosticRequest(ingress_name="svc", namespace="ns"),
            cert_pem=cert_pem,
            hostname="payment.example.com",
        )
        assert result.status == CertificateStatus.VALID

    def test_expired_cert(self) -> None:
        cert_pem = _make_cert("payment.example.com", ["payment.example.com"], -5)
        result = CertificateDiagnosis.compute(
            request=TLSCertificateDiagnosticRequest(ingress_name="svc", namespace="ns"),
            cert_pem=cert_pem,
            hostname="payment.example.com",
        )
        assert result.status == CertificateStatus.EXPIRED

    def test_expiring_soon(self) -> None:
        cert_pem = _make_cert("payment.example.com", ["payment.example.com"], 15)
        result = CertificateDiagnosis.compute(
            request=TLSCertificateDiagnosticRequest(ingress_name="svc", namespace="ns"),
            cert_pem=cert_pem,
            hostname="payment.example.com",
        )
        assert result.status == CertificateStatus.EXPIRING_SOON

    def test_no_san_extension(self) -> None:
        cert_pem = _make_cert("payment.example.com", [], 45, add_san=False)
        result = CertificateDiagnosis.compute(
            request=TLSCertificateDiagnosticRequest(ingress_name="svc", namespace="ns"),
            cert_pem=cert_pem,
            hostname="payment.example.com",
        )
        assert result.status == CertificateStatus.VALID
        assert result.san_list == []
