import hashlib
from datetime import datetime

from hexawyn.domain.models.cache import CacheEntry
from hexawyn.infrastructure.memory.cache_l1_repository import CacheL1Repository

_repository = CacheL1Repository()


def compute_query_hash(query: str, cluster_name: str) -> str:
    normalized = query.lower().strip()
    key = f"{normalized}:{cluster_name}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()


def get_l1(query: str, cluster_name: str) -> CacheEntry | None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    return _repository.get(query_hash)


def set_l1(query: str, cluster_name: str, result: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    entry = CacheEntry(
        query_hash=query_hash,
        result=result,
        created_at=datetime.now(),
    )
    _repository.set(query_hash, entry)


def invalidate_l1(query: str, cluster_name: str) -> None:
    query_hash = compute_query_hash(query=query, cluster_name=cluster_name)
    _repository.invalidate(query_hash)


def clear_l1() -> None:
    _repository.clear()


def evict_expired_l1() -> int:
    return _repository.evict_expired()


def get_cache_stats() -> dict[str, int | float]:
    return {
        "l1_size": _repository.size(),
        "l1_ttl_seconds": 300,
    }
