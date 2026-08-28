from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort


def build_cilium_adapter() -> CiliumPort:
    from hexawyn.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CiliumAdapter(VanillaAdapter(cluster_name="default"))
