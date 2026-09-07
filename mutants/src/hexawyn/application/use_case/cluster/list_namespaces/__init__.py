"""List namespaces — use case."""

from hexawyn.application.use_case.cluster.list_namespaces.list_namespaces_use_case import (
    ListNamespacesUseCase,
)

__all__ = ["ListNamespacesUseCase"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
