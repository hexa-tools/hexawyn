from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class CertificateStatus(Enum):
    READY = "ready"
    NOT_READY = "not_ready"
    ISSUING = "issuing"
    FAILED = "failed"
    UNKNOWN = "unknown"


class IssuerType(Enum):
    LETS_ENCRYPT = "lets_encrypt"
    VAULT = "vault"
    SELF_SIGNED = "self_signed"
    CA = "ca"
    VENAFI = "venafi"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Certificate:
    name: str
    namespace: str
    status: CertificateStatus
    issuer_name: str
    issuer_type: IssuerType
    dns_names: list[str]
    not_before: str | None
    not_after: str | None
    days_until_expiry: int | None
    renewal_time: str | None
    auto_renew: bool
    message: str | None


@dataclass(frozen=True)
class CertificateIssuer:
    name: str
    namespace: str | None
    kind: str
    issuer_type: IssuerType
    ready: bool
    server: str | None
    message: str | None


@dataclass(frozen=True)
class AcmeChallenge:
    name: str
    namespace: str
    type: str
    domain: str
    state: str
    reason: str | None
    age_seconds: int


@dataclass(frozen=True)
class CertManagerDetectionResult:
    installed: bool
    version: str | None
    namespace: str | None
    total_certs: int
    ready_certs: int
    expiring_soon: int
    failed_certs: int
    active_challenges: int
