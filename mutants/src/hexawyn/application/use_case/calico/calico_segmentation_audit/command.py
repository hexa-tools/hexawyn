from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class CalicoSegmentationAuditCommand:
    """Optional namespace filter and excluded namespaces for the audit."""

    namespace: str | None = None
    excluded_namespaces: tuple[str, ...] = field(default_factory=tuple)
