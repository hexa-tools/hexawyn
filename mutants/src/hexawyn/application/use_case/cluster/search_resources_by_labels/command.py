from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class SearchResourcesByLabelsCommand:
    namespace: str | None = None
    label_selector: str = ""
    resource_types: list[str] = field(default_factory=list)
