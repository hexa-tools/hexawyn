from hexawyn.domain.models.cache import CacheEntry


class CacheL1Repository:
    """
    In-memory Cache L1 repository — exact match by query hash.

    Storage: Python dict (not DuckDB — must be sub-millisecond).
    Scope: current hexawyn session only (cleared on restart).
    TTL: 5 minutes per entry (enforced by CacheEntry.is_valid).

    Thread safety: not required — hexawyn is single-user CLI.

    Used by:
    - cache_manager.get_l1() → called by check_cache LangGraph node
    - cache_manager.set_l1() → called by store_memory LangGraph node
    """

    def __init__(self) -> None:
        self._store: dict[str, CacheEntry] = {}

    def get(self, query_hash: str) -> CacheEntry | None:
        entry = self._store.get(query_hash)
        if entry is None:
            return None
        if not entry.is_valid:
            del self._store[query_hash]
            return None
        return entry

    def set(self, query_hash: str, entry: CacheEntry) -> None:
        self._store[query_hash] = entry

    def invalidate(self, query_hash: str) -> None:
        self._store.pop(query_hash, None)

    def clear(self) -> None:
        self._store.clear()

    def size(self) -> int:
        return sum(1 for e in self._store.values() if e.is_valid)

    def evict_expired(self) -> int:
        expired_keys = [k for k, v in self._store.items() if not v.is_valid]
        for key in expired_keys:
            del self._store[key]
        return len(expired_keys)
