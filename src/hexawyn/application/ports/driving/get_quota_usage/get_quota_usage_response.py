from dataclasses import dataclass, field

from hexawyn.domain.models.quota import QuotaUsage


@dataclass
class GetQuotaUsageResponse:
    quotas: list[QuotaUsage] = field(default_factory=list)
