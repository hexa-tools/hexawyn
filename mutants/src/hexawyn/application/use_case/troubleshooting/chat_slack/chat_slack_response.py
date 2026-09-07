from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ChatSlackResponse:
    message: str
    quota_display: str
    suggestions: list[str] = field(default_factory=list)
    is_pro: bool = False
