from dataclasses import dataclass, field

from hexawyn.domain.models.resource_usage import (
    NamespaceResourceUsageSummary,
    PodResourceUsage,
)


@dataclass
class GetResourceUsageResponse:
    pods: list[PodResourceUsage] = field(default_factory=list)
    namespace_summary: list[NamespaceResourceUsageSummary] = field(default_factory=list)
    metrics_server_available: bool = False
    source: str = ""
