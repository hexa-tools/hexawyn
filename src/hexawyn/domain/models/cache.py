from dataclasses import dataclass, field
from datetime import datetime, timedelta

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
