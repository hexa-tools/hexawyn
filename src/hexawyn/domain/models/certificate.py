from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
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


@dataclass
class CertificateEntry:
    """A TLS secret with its parsed certificate info and cluster context."""

    secret_name: str
    namespace: str
    info: CertificateInfo
    status: CertificateStatus
    days_remaining: int
    ingress_refs: list[str] = field(default_factory=list)
    is_orphan: bool = True
    cert_manager_managed: bool = False
    cert_manager_auto_renewing: bool = False
    is_wildcard: bool = False


@dataclass
class ClusterCertificateReport:
    """Full TLS certificate health report for a cluster, sorted by urgency."""

    cluster_name: str
    critical: list[CertificateEntry] = field(default_factory=list)
    warning: list[CertificateEntry] = field(default_factory=list)
    healthy: list[CertificateEntry] = field(default_factory=list)
    expired: list[CertificateEntry] = field(default_factory=list)
    skipped_namespaces: list[str] = field(default_factory=list)
    total_scanned: int = 0
    scanned_at: datetime = field(default_factory=lambda: datetime.now(UTC))
