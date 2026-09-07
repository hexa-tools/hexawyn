from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class KedaScaledobjectsListResponse:
    scaled_objects: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
