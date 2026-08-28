from __future__ import annotations

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)


def build_cilium_adapter() -> CiliumPort:
    from hexawyn.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CiliumAdapter(VanillaAdapter(cluster_name="default"))


def build_cilium_hubble_adapter() -> CiliumHubblePort:
    from hexawyn.adapters.secondary.cilium.cilium_hubble_adapter import (
        CiliumHubbleAdapter,
    )

    return CiliumHubbleAdapter()


def build_cilium_service_graph_adapter() -> ServiceDependencyGraphPort:
    from hexawyn.adapters.secondary.cilium.cilium_hubble_graph_adapter import (
        HubbleDependencyGraphAdapter,
    )

    return HubbleDependencyGraphAdapter(build_cilium_hubble_adapter())
