from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class GetCalicoNetworkPolicyCommand:
    """Name (required) and optional namespace of the Calico policy to fetch.

    An empty ``namespace`` targets a cluster-wide GlobalNetworkPolicy.
    """

    name: str = ""
    namespace: str | None = None
