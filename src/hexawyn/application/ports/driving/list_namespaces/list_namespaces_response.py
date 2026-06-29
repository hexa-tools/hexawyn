from dataclasses import dataclass, field

from hexawyn.application.ports.driven.k8s_port import NamespaceInfo


@dataclass
class ListNamespacesResponse:
    namespaces: list[NamespaceInfo] = field(default_factory=list)
