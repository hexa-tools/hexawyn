from dataclasses import dataclass, field

from hexawyn.domain.models.resource_usage import (
    NamespaceResourceUsageSummary,
    PodResourceUsage,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GetResourceUsageResponse:
    pods: list[PodResourceUsage] = field(default_factory=list)
    namespace_summary: list[NamespaceResourceUsageSummary] = field(default_factory=list)
    metrics_server_available: bool = False
    source: str = ""
