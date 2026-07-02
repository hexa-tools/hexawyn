from __future__ import annotations

from dataclasses import dataclass

LEADER_ELECTION_KEYWORDS: frozenset[str] = frozenset(
    {"leader election started", "became leader", "lost leader"}
)
COMPACTION_ERROR_KEYWORDS: frozenset[str] = frozenset(
    {"database space exceeded", "compaction failed"}
)
LEADER_INSTABILITY_THRESHOLD: int = 2


@dataclass(frozen=True)
class ETCDLogLine:
    timestamp: str
    level: str
    message: str

    @property
    def is_error(self) -> bool:
        return self.level.upper() in ("ERROR", "FATAL", "WARN")


@dataclass(frozen=True)
class ETCDLogsRequest:
    time_window_minutes: int = 60


@dataclass(frozen=True)
class ETCDLogsResult:
    time_window_minutes: int
    etcd_accessible: bool
    total_log_lines: int
    error_count: int
    leader_election_count: int
    compaction_errors: int
    leader_instability: bool
    errors: list[ETCDLogLine]
    all_lines: list[ETCDLogLine]
    summary: str

    @staticmethod
    def compute(
        request: ETCDLogsRequest,
        log_lines: list[ETCDLogLine],
    ) -> ETCDLogsResult:
        if not log_lines:
            return ETCDLogsResult(
                time_window_minutes=request.time_window_minutes,
                etcd_accessible=False,
                total_log_lines=0,
                error_count=0,
                leader_election_count=0,
                compaction_errors=0,
                leader_instability=False,
                errors=[],
                all_lines=[],
                summary="etcd not accessible — no logs retrieved",
            )

        errors = [line for line in log_lines if line.is_error]
        leader_count = 0
        compaction_count = 0

        for line in log_lines:
            msg_lower = line.message.lower()
            if any(k in msg_lower for k in LEADER_ELECTION_KEYWORDS):
                leader_count += 1
            if any(k in msg_lower for k in COMPACTION_ERROR_KEYWORDS):
                compaction_count += 1

        parts: list[str] = [f"{len(log_lines)} log lines, {len(errors)} errors"]
        if leader_count >= LEADER_INSTABILITY_THRESHOLD:
            parts.append(f"leader instability detected ({leader_count} elections)")
        if compaction_count > 0:
            parts.append("compaction error — check disk space")

        return ETCDLogsResult(
            time_window_minutes=request.time_window_minutes,
            etcd_accessible=True,
            total_log_lines=len(log_lines),
            error_count=len(errors),
            leader_election_count=leader_count,
            compaction_errors=compaction_count,
            leader_instability=leader_count >= LEADER_INSTABILITY_THRESHOLD,
            errors=errors,
            all_lines=log_lines,
            summary="; ".join(parts),
        )
