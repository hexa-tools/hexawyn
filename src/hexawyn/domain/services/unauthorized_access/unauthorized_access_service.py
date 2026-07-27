from __future__ import annotations

from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessRaw
from hexawyn.domain.models.unauthorized_access import UnauthorizedAccessReport


def compute_unauthorized_access_report(
    raw: UnauthorizedAccessRaw, has_data: bool, period: str
) -> UnauthorizedAccessReport:
    if not has_data:
        return UnauthorizedAccessReport(
            period_label=period, has_data=False, warning="Aucune donnee d'acces disponible."
        )

    count = raw["attempt_count"]
    source = raw["source_type"]
    alert = _alert_level(count, source)

    return UnauthorizedAccessReport(
        period_label=period,
        attempt_count=count,
        window_minutes=raw["window_minutes"],
        source_type=source,
        alert_level=alert,
        has_data=True,
    )


def _alert_level(count: int, source: str) -> str:
    if source == "internal":
        return "medium" if count > 50 else "low"  # noqa: PLR2004
    if count > 20:  # noqa: PLR2004
        return "high"
    if count > 0:
        return "medium"
    return "low"
