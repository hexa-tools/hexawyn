from dataclasses import dataclass, field

from hexawyn.application.ports.driven.k8s_port import PodInfo


@dataclass
class ListPodsResponse:
    pods: list[PodInfo] = field(default_factory=list)
