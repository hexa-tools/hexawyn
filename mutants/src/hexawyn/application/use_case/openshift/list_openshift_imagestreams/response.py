from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ListOpenshiftImagestreamsResponse:
    items: list[dict[str, object]] = field(default_factory=list)
    count: int = 0
    error: str | None = None
