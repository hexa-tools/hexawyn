from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class SensitiveDataAuditResponse:
    pattern: str = ""
    total_matches: int = 0
    flagged: list[dict[str, object]] = field(default_factory=list)
    unflagged: list[dict[str, object]] = field(default_factory=list)
    alert_level: str = "normal"
