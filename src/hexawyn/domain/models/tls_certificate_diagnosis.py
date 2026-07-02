from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import ExtensionOID


class CertificateStatus(Enum):
    VALID = "valid"
    EXPIRED = "expired"
    EXPIRING_SOON = "expiring_soon"
    MISCONFIGURED = "misconfigured"
    DEPRECATED_CIPHER = "deprecated_cipher"
    ERROR = "error"


DEPRECATED_CIPHERS: frozenset[str] = frozenset({"RC4", "3DES", "EXP", "EXPORT"})


@dataclass(frozen=True)
class CertificateDiagnosis:
    status: CertificateStatus
    expiry_date: str | None
    days_remaining: int | None
    cipher_info: str
    san_list: list[str]
    hostname: str
    diagnosis: str
    findings: list[str] = field(default_factory=list)

    @staticmethod
    def compute(
        request: TLSCertificateDiagnosticRequest,
        cert_pem: str | None,
        hostname: str,
    ) -> CertificateDiagnosis:
        if cert_pem is None:
            return CertificateDiagnosis(
                status=CertificateStatus.ERROR,
                expiry_date=None,
                days_remaining=None,
                cipher_info="unknown",
                san_list=[],
                hostname=hostname,
                diagnosis="No TLS certificate data available",
                findings=["Certificate PEM not provided"],
            )

        try:
            cert_bytes = cert_pem.encode() if isinstance(cert_pem, str) else cert_pem
            cert = x509.load_pem_x509_certificate(cert_bytes, default_backend())
        except Exception:
            return CertificateDiagnosis(
                status=CertificateStatus.ERROR,
                expiry_date=None,
                days_remaining=None,
                cipher_info="unknown",
                san_list=[],
                hostname=hostname,
                diagnosis="Failed to parse certificate PEM data",
                findings=["X.509 parsing failed"],
            )

        # Expiry check
        now = datetime.now(UTC)
        expiry = cert.not_valid_after_utc
        days = (expiry - now).days
        expiry_str = expiry.isoformat()

        findings: list[str] = []
        if days < 0:
            status = CertificateStatus.EXPIRED
            findings.append(f"Certificate expired on {expiry_str}")
        elif days <= 30:
            status = CertificateStatus.EXPIRING_SOON
            findings.append(f"Certificate expires in {days} days")
        else:
            status = CertificateStatus.VALID
            findings.append(f"Certificate valid until {expiry_str}")

        # Cipher check
        cipher_info = "unknown"
        try:
            sig_algo = str(cert.signature_algorithm_oid)
            cipher_info = str(sig_algo)
            if any(dep in str(sig_algo).upper() for dep in DEPRECATED_CIPHERS):
                status = CertificateStatus.DEPRECATED_CIPHER
                findings.append(f"Deprecated signature algorithm: {sig_algo}")
        except Exception:
            cipher_info = "unknown"

        # SAN check
        san_list: list[str] = []
        try:
            san_ext = cert.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
            sans = san_ext.value.get_values_for_type(x509.DNSName)  # type: ignore[attr-defined]
            san_list = [str(s) for s in sans]
        except Exception:
            san_list = []

        if san_list and not CertificateDiagnosis._match_san(san_list, hostname):
            status = CertificateStatus.MISCONFIGURED
            findings.append(f"SAN mismatch: hostname '{hostname}' not in {san_list}")

        diagnosis = "; ".join(findings)
        return CertificateDiagnosis(
            status=status,
            expiry_date=expiry_str,
            days_remaining=days,
            cipher_info=cipher_info,
            san_list=san_list,
            hostname=hostname,
            diagnosis=diagnosis,
            findings=findings,
        )

    @staticmethod
    def _match_san(sans: list[str], hostname: str) -> bool:
        for san in sans:
            if san.startswith("*."):
                suffix = san[1:]
                if hostname.endswith(suffix) and "." in hostname:
                    return True
            elif san == hostname:
                return True
        return False


@dataclass(frozen=True)
class TLSCertificateDiagnosticRequest:
    ingress_name: str
    namespace: str
