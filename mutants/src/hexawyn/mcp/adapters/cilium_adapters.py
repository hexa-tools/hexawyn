from __future__ import annotations

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_cilium_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cilium_adapter__mutmut)
def build_cilium_adapter() -> CiliumPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CiliumAdapter(VanillaAdapter(cluster_name="default"))


def x_build_cilium_adapter__mutmut_orig() -> CiliumPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CiliumAdapter(VanillaAdapter(cluster_name="default"))


def x_build_cilium_adapter__mutmut_1() -> CiliumPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CiliumAdapter(None)


def x_build_cilium_adapter__mutmut_2() -> CiliumPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CiliumAdapter(VanillaAdapter(cluster_name=None))


def x_build_cilium_adapter__mutmut_3() -> CiliumPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CiliumAdapter(VanillaAdapter(cluster_name="XXdefaultXX"))


def x_build_cilium_adapter__mutmut_4() -> CiliumPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.cilium_adapter import CiliumAdapter
    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return CiliumAdapter(VanillaAdapter(cluster_name="DEFAULT"))

mutants_x_build_cilium_adapter__mutmut['_mutmut_orig'] = x_build_cilium_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cilium_adapter__mutmut['x_build_cilium_adapter__mutmut_1'] = x_build_cilium_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cilium_adapter__mutmut['x_build_cilium_adapter__mutmut_2'] = x_build_cilium_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_cilium_adapter__mutmut['x_build_cilium_adapter__mutmut_3'] = x_build_cilium_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_cilium_adapter__mutmut['x_build_cilium_adapter__mutmut_4'] = x_build_cilium_adapter__mutmut_4 # type: ignore # mutmut generated


def build_cilium_hubble_adapter() -> CiliumHubblePort:
    from hexawyn.infrastructure.adapters.secondary.cilium.cilium_hubble_adapter import (
        CiliumHubbleAdapter,
    )

    return CiliumHubbleAdapter()
mutants_x_build_cilium_service_graph_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cilium_service_graph_adapter__mutmut)
def build_cilium_service_graph_adapter() -> ServiceDependencyGraphPort:
    from hexawyn.infrastructure.adapters.secondary.cilium.cilium_hubble_graph_adapter import (
        HubbleDependencyGraphAdapter,
    )

    return HubbleDependencyGraphAdapter(build_cilium_hubble_adapter())


def x_build_cilium_service_graph_adapter__mutmut_orig() -> ServiceDependencyGraphPort:
    from hexawyn.infrastructure.adapters.secondary.cilium.cilium_hubble_graph_adapter import (
        HubbleDependencyGraphAdapter,
    )

    return HubbleDependencyGraphAdapter(build_cilium_hubble_adapter())


def x_build_cilium_service_graph_adapter__mutmut_1() -> ServiceDependencyGraphPort:
    from hexawyn.infrastructure.adapters.secondary.cilium.cilium_hubble_graph_adapter import (
        HubbleDependencyGraphAdapter,
    )

    return HubbleDependencyGraphAdapter(None)

mutants_x_build_cilium_service_graph_adapter__mutmut['_mutmut_orig'] = x_build_cilium_service_graph_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cilium_service_graph_adapter__mutmut['x_build_cilium_service_graph_adapter__mutmut_1'] = x_build_cilium_service_graph_adapter__mutmut_1 # type: ignore # mutmut generated
