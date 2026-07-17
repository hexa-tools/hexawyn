from dataclasses import dataclass


@dataclass(frozen=True)
class GetQuotaUsageCommand:
    """No input needed — reads current tier from environment."""

    pass
