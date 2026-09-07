"""Get namespace resource allocation — use case."""

from hexawyn.application.use_case.cluster.get_namespace_resource_allocation.get_namespace_resource_allocation_use_case import (  # noqa: E501
    GetNamespaceResourceAllocationUseCase,
)

__all__ = ["GetNamespaceResourceAllocationUseCase"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
