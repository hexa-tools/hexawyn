from dataclasses import dataclass, field

from hexawyn.domain.models.namespace_resource_allocation import (
    NamespaceResourceAllocation,
)


@dataclass
class GetNamespaceResourceAllocationResponse:
    allocations: list[NamespaceResourceAllocation] = field(default_factory=list)
