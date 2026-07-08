from dataclasses import dataclass


class CheckerVerdict(str):
    PASS = "PASS"
    FAIL = "FAIL"
    BLOCKED = "BLOCKED"
    DEGRADED = "DEGRADED"


@dataclass
class SemanticCheckResult:
    verdict: str  # PASS | FAIL | BLOCKED | DEGRADED
    score: float  # 0.0 - 1.0
    reason: str
    retry_count: int = 0
    max_retries: int = 3
