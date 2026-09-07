from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class ETCDLogsResponse:
    etcd_accessible: bool = False
    total_log_lines: int = 0
    error_count: int = 0
    leader_election_count: int = 0
    compaction_errors: int = 0
    leader_instability: bool = False
    summary: str = ""
    errors: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
