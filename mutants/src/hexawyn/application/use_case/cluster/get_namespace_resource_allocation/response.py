from dataclasses import dataclass, field

from hexawyn.domain.models.namespace_resource_allocation import (
    NamespaceResourceAllocation,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class GetNamespaceResourceAllocationResponse:
    allocations: list[NamespaceResourceAllocation] = field(default_factory=list)
