from hexawyn.domain.models.certificate import CertificateInfo, CertificateStatus


class CertificateChecker:
    """Business logic for certificate health assessment.

    Categorizes certificates based on days remaining until expiry.
    Provides a full assessment report including self-signed detection,
    key size validation, and SAN presence.
    """

    def __init__(
        self,
        warning_days: int = 30,
        critical_days: int = 7,
        min_key_size: int = 2048,
    ) -> None:
        self.warning_days = warning_days
        self.critical_days = critical_days
        self.min_key_size = min_key_size

    def check(self, cert: CertificateInfo) -> CertificateStatus:
        if cert.days_remaining < 0:
            return CertificateStatus.EXPIRED
        if cert.days_remaining <= self.critical_days:
            return CertificateStatus.CRITICAL
        if cert.days_remaining <= self.warning_days:
            return CertificateStatus.WARNING
        return CertificateStatus.HEALTHY

    def assess(self, cert: CertificateInfo) -> dict[str, str | int | bool]:
        status = self.check(cert)
        return {
            "status": status.value,
            "days_remaining": cert.days_remaining,
            "subject_cn": cert.subject_cn,
            "issuer_cn": cert.issuer_cn,
            "is_self_signed": cert.subject_cn == cert.issuer_cn,
            "is_ca": cert.is_ca,
            "key_size": cert.key_size,
            "key_size_ok": cert.key_size >= self.min_key_size,
            "has_san": len(cert.san_list) > 0,
            "san_count": len(cert.san_list),
        }
