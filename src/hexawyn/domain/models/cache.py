from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta

CACHE_TTL_SECONDS = 300  # 5 minutes — cluster state changes fast


@dataclass
class CacheEntry:
    """
    A Cache L1 entry — exact match by query hash.
    TTL: 5 minutes (CACHE_TTL_SECONDS).

    Used by:
    - CacheL1Repository.get() → returns entry if valid
    - check_cache LangGraph node → L1 check before L2 VSS

    Why 5 minutes?
    Kubernetes state changes fast — a pod that was CrashLooping
    5 minutes ago may already be fixed. Longer TTL = stale answers.
    """

    query_hash: str  # SHA-256 of (query + cluster_name)
    result: str  # serialized InvestigationResult JSON
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def is_valid(self) -> bool:
        """True if entry is within TTL window."""
        age = datetime.now() - self.created_at
        return age < timedelta(seconds=CACHE_TTL_SECONDS)

    @property
    def age_seconds(self) -> float:
        """Age of entry in seconds."""
        return (datetime.now() - self.created_at).total_seconds()


# ── Investigation Cache (DuckDB, RGPD-compliant) ─────────────────────────

_CACHE_TTL_BY_LICENSE: dict[str, int] = {
    "free": 6 * 3600,
    "dev": 24 * 3600,
    "pro": 48 * 3600,
}


@dataclass
class CachedInvestigation:
    """A sanitized investigation result stored in local DuckDB."""

    id: str
    cache_key: str  # sha256(cluster + tool + namespace + resource + query)
    finding_type: str
    root_cause: str
    recommendation: str
    severity: str
    cluster_name: str
    namespace: str
    resource_name: str
    resource_kind: str
    pod_status_at_cache_time: str
    pod_restart_count_at_cache: int
    tool_name: str
    created_at: datetime = field(default_factory=datetime.now)
    expires_at: datetime | None = None
    sanitized: bool = True

    def __post_init__(self) -> None:
        if self.expires_at is None:
            self.expires_at = self.created_at + timedelta(
                seconds=_CACHE_TTL_BY_LICENSE.get("free", 21600)
            )

    @property
    def is_expired(self) -> bool:
        if self.expires_at is None:
            return False
        return datetime.now(UTC) > self.expires_at


@dataclass
class CacheValidationResult:
    is_valid: bool
    reason: str  # TTL_EXPIRED | POD_STATUS_CHANGED | RESTART_COUNT_CHANGED | FORCE_REFRESH | VALID
