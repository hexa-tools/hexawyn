from textual.widgets import Static

from hexawyn.domain.models.quota import QuotaState, QuotaUsage


def _quota_bar(quota: QuotaUsage, width: int = 20) -> str:
    """Render a single quota line as text for Textual display."""
    fill = chr(9608)
    empty = chr(9617)

    resource_labels: dict[str, str] = {
        "investigations": "Investigations",
        "slack_alerts": "Slack alerts",
    }
    label = resource_labels.get(quota.resource, quota.resource)

    if quota.state == QuotaState.UNLIMITED:
        return f"  {label}: \u221e Illimit\u00e9"

    if quota.state == QuotaState.LOCKED:
        tier = quota.available_from_tier or "unknown"
        return f"  {label}: \U0001f512 Available from {tier}"

    limit = quota.limit or 0
    pct = min(100.0, (quota.used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    bar = f"[{fill * filled}{empty * (width - filled)}]"

    state_icon = {
        QuotaState.NORMAL: "",
        QuotaState.WARNING: "\u26a0\ufe0f ",
        QuotaState.CRITICAL: "\U0001f534 ",
        QuotaState.EXHAUSTED: "\u274c ",
    }.get(quota.state, "")

    remaining = limit - quota.used
    return f"  {label}: {state_icon}{quota.used}/{limit} {bar} {remaining} remaining"


class QuotaProgressBar(Static):
    """Textual widget displaying quota progress bars for all resources."""

    def update_quotas(self, quotas: list[QuotaUsage]) -> None:
        lines = ["\n[bold]Quota Usage[/bold]", "\u2500" * 52]
        for quota in quotas:
            lines.append(_quota_bar(quota))

        exhausted = [q for q in quotas if q.state == QuotaState.EXHAUSTED]
        if exhausted:
            lines.append("\n\u274c Quota exceeded! Upgrade: https://hexawyn.com/pricing")

        self.update("\n".join(lines))
