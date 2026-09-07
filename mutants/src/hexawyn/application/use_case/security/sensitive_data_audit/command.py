from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class SensitiveDataAuditCommand:
    pattern: str = ""
    time_window_minutes: int = 30
    allowlist: list[str] = field(default_factory=list)
