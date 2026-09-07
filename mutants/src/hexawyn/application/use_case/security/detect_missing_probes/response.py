from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class DetectMissingProbesResponse:
    result: dict[str, object] = field(default_factory=dict)
