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
