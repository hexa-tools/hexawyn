from __future__ import annotations

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialRaw
from hexawyn.domain.models.stale_credentials import StaleCredential, StaleCredentialsReport


def compute_stale_credentials_report(
    credentials: list[StaleCredentialRaw], has_data: bool, period: str
) -> StaleCredentialsReport:
    if not has_data:
        return StaleCredentialsReport(
            period_label=period, has_data=False, warning="Aucune donnee de rotation disponible."
        )

    stale = [cred for cred in credentials if cred["days_unrotated"] >= 90]
    critical = sum(1 for cred in stale if cred["risk_level"] == "critical")
    return StaleCredentialsReport(
        period_label=period,
        total_stale=len(stale),
        critical_count=critical,
        credentials=[StaleCredential(**cred) for cred in stale],
        has_data=True,
    )
