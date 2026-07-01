from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CertsGetResponse:
    name: str = ""
    namespace: str = ""
    status: str = "unknown"
    issuer_name: str = ""
    issuer_type: str = "unknown"
    dns_names: list[str] | None = None
    not_before: str | None = None
    not_after: str | None = None
    days_until_expiry: int | None = None
    renewal_time: str | None = None
    auto_renew: bool = False
    message: str | None = None
    error: str | None = None
