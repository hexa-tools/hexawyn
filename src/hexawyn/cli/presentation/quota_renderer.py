from hexawyn.domain.models.quota import QuotaState

QUOTA_STATE_ICONS: dict[QuotaState, str] = {
    QuotaState.NORMAL: "",
    QuotaState.WARNING: "\u26a0\ufe0f ",
    QuotaState.CRITICAL: "\U0001f534 ",
    QuotaState.EXHAUSTED: "\u274c ",
    QuotaState.UNLIMITED: "",
    QuotaState.LOCKED: "\U0001f512 ",
}

QUOTA_RESOURCE_LABELS: dict[str, str] = {
    "investigations": "Investigations",
    "slack_alerts": "Slack alerts",
}

UPGRADE_URL = "https://hexawyn.com/pricing"

FILL_CHAR = chr(9608)
EMPTY_CHAR = chr(9617)
BAR_WIDTH = 20


def compute_bar_fill(used: int, limit: int, width: int = BAR_WIDTH) -> tuple[int, float]:
    pct = min(100.0, (used / limit) * 100) if limit > 0 else 0.0
    filled = int((pct / 100.0) * width)
    return filled, pct


def format_quota_exceeded(
    used: int,
    limit: int,
    *,
    resource: str = "investigations",
) -> str:
    """Build the CLI message shown when a quota is exceeded.

    CLI-only: the pricing link and the license-activation command are only
    actionable from a terminal. MCP tools surface the neutral exception
    message; the Slack adapter builds its own. Do not call this from the
    application core or the MCP/Slack adapters.
    """
    label = QUOTA_RESOURCE_LABELS.get(resource, resource)
    return (
        f"\u274c Quota exceeded \u2014 {label} ({used}/{limit})\n"
        f"Upgrade your plan: {UPGRADE_URL}\n"
        f"Activate: hexa license activate <YOUR-KEY>"
    )
