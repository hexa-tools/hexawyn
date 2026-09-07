from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class DiffHelmValuesResponse:
    release: str = ""
    source_namespace: str = ""
    target_namespace: str = ""
    diff_count: int = 0
    result: dict[str, object] = field(default_factory=dict)
    error: str | None = None
