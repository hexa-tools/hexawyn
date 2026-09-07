from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class CalicoBgpAuditCommand:
    """Empty command — Calico BGP config is cluster-scoped."""

    pass
