from textual.widgets import Static

from hexawyn.cli.presentation.quota_renderer import (
    EMPTY_CHAR,
    FILL_CHAR,
    QUOTA_RESOURCE_LABELS,
    QUOTA_STATE_ICONS,
    UPGRADE_URL,
    compute_bar_fill,
)
from hexawyn.domain.models.quota import QuotaState, QuotaUsage

_BAR_COLORS: dict[str, str] = {
    "normal": "#22c55e",
    "warning": "#f97316",
    "critical": "#ef4444",
    "exhausted": "#ef4444",
}


def _quota_bar(quota: QuotaUsage, width: int = 20) -> str:
    label = QUOTA_RESOURCE_LABELS.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    filled, _ = compute_bar_fill(quota.used, limit, width)

    color = _BAR_COLORS.get(quota.state.value, _BAR_COLORS["normal"])
    bar = f"[{color}]{FILL_CHAR * filled}[/][{EMPTY_CHAR * (width - filled)}]"

    state_icon = QUOTA_STATE_ICONS.get(quota.state, "")
    return f"  {label}: {state_icon}{quota.used}/{limit}    {bar}"


class QuotaProgressBar(Static):
    def update_quotas(self, quotas: list[QuotaUsage]) -> None:
        visible_quotas = [q for q in quotas if q.state != QuotaState.UNLIMITED]
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        any_above_normal = False

        for quota in visible_quotas:
            lines.append(_quota_bar(quota))
            if quota.state in (QuotaState.WARNING, QuotaState.CRITICAL, QuotaState.EXHAUSTED):
                any_above_normal = True

        if any_above_normal:
            lines.append(f"\n\U0001f680 Upgrade: {UPGRADE_URL}")

        self.update("\n".join(lines))
