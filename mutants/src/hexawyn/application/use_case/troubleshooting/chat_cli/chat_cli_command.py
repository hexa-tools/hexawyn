from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class ChatCliCommand:
    query: str
    conversation_history: list[dict[str, str]] = field(default_factory=list)
