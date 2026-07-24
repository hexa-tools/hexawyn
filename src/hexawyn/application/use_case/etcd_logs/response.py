from dataclasses import dataclass, field


@dataclass
class EtcdLogsResponse:
    etcd_accessible: bool = False
    total_log_lines: int = 0
    error_count: int = 0
    leader_election_count: int = 0
    compaction_errors: int = 0
    leader_instability: bool = False
    summary: str = ""
    errors: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
