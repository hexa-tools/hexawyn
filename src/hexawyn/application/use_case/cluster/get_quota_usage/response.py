from dataclasses import dataclass, field

from hexawyn.domain.models.quota import QuotaUsage


@dataclass
class GetQuotaUsageResponse:
    quotas: list[QuotaUsage] = field(default_factory=list)
    investigations_used: int = 0
    investigations_limit: int = 0
    error: str | None = None
