from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class CertificateStatus(Enum):
    HEALTHY = "healthy"
    WARNING = "warning"
    CRITICAL = "critical"
    EXPIRED = "expired"


@dataclass
class CertificateInfo:
    """Parsed X.509 certificate information."""

    subject_cn: str
    issuer_cn: str
    not_before: datetime | None = None
    not_after: datetime | None = None
    days_remaining: int = 0
    san_list: list[str] = field(default_factory=list)
    is_ca: bool = False
    key_size: int = 0
    serial_number: str = ""
    signature_algorithm: str = ""
    subject_full: str = ""
    issuer_full: str = ""
