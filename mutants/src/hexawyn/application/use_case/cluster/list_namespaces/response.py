from dataclasses import dataclass, field

from hexawyn.application.ports.driven.k8s_port import NamespaceInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ListNamespacesResponse:
    namespaces: list[NamespaceInfo] = field(default_factory=list)
