from dataclasses import dataclass, field

from hexawyn.application.ports.driven.k8s_port import PodInfo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ListPodsResponse:
    pods: list[PodInfo] = field(default_factory=list)
