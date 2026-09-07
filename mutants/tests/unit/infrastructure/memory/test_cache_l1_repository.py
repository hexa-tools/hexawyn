from datetime import datetime, timedelta

from hexawyn.domain.models.cache import CacheEntry
from hexawyn.infrastructure.memory.cache_l1_repository import CacheL1Repository


class TestCacheL1Repo:
    def test_initially_empty(self) -> None:
        repo = CacheL1Repository()
        assert repo.size() == 0

    def test_get_returns_none_for_missing_key(self) -> None:
        repo = CacheL1Repository()
        assert repo.get("nonexistent") is None

    def test_set_and_get(self) -> None:
        repo = CacheL1Repository()
        entry = CacheEntry(query_hash="abc", result="test")
        repo.set("abc", entry)
        result = repo.get("abc")
        assert result is not None
        assert result.query_hash == "abc"
        assert result.result == "test"

    def test_get_evicts_expired_entry(self) -> None:
        repo = CacheL1Repository()
        entry = CacheEntry(
            query_hash="expired",
            result="test",
            created_at=datetime.now() - timedelta(seconds=9999),
        )
        repo.set("expired", entry)
        assert repo.get("expired") is None
        assert repo.size() == 0

    def test_size_counts_only_valid_entries(self) -> None:
        repo = CacheL1Repository()
        fresh = CacheEntry(query_hash="fresh", result="test")
        expired = CacheEntry(
            query_hash="expired",
            result="test",
            created_at=datetime.now() - timedelta(seconds=9999),
        )
        repo.set("fresh", fresh)
        repo.set("expired", expired)
        assert repo.size() == 1

    def test_invalidate_removes_entry(self) -> None:
        repo = CacheL1Repository()
        entry = CacheEntry(query_hash="abc", result="test")
        repo.set("abc", entry)
        repo.invalidate("abc")
        assert repo.get("abc") is None
        assert repo.size() == 0

    def test_invalidate_nonexistent_is_safe(self) -> None:
        repo = CacheL1Repository()
        repo.invalidate("nonexistent")  # no exception

    def test_clear_removes_all(self) -> None:
        repo = CacheL1Repository()
        repo.set("a", CacheEntry(query_hash="a", result="x"))
        repo.set("b", CacheEntry(query_hash="b", result="y"))
        assert repo.size() == 2  # noqa: PLR2004
        repo.clear()
        assert repo.size() == 0

    def test_evict_expired_removes_only_expired(self) -> None:
        repo = CacheL1Repository()
        fresh = CacheEntry(query_hash="fresh", result="test")
        expired = CacheEntry(
            query_hash="expired",
            result="test",
            created_at=datetime.now() - timedelta(seconds=9999),
        )
        repo.set("fresh", fresh)
        repo.set("expired", expired)
        count = repo.evict_expired()
        assert count == 1
        assert repo.get("fresh") is not None
        assert repo.get("expired") is None

    def test_evict_expired_returns_zero_when_all_fresh(self) -> None:
        repo = CacheL1Repository()
        repo.set("a", CacheEntry(query_hash="a", result="x"))
        repo.set("b", CacheEntry(query_hash="b", result="y"))
        assert repo.evict_expired() == 0

    def test_multiple_entries_same_hash_overwrites(self) -> None:
        repo = CacheL1Repository()
        repo.set("abc", CacheEntry(query_hash="abc", result="old"))
        repo.set("abc", CacheEntry(query_hash="abc", result="new"))
        assert repo.get("abc").result == "new"

    def test_evict_expired_on_empty_store_returns_zero(self) -> None:
        repo = CacheL1Repository()
        assert repo.evict_expired() == 0

    def test_evict_expired_when_all_expired_returns_count(self) -> None:
        repo = CacheL1Repository()
        for i in range(5):
            repo.set(
                str(i),
                CacheEntry(
                    query_hash=str(i),
                    result="x",
                    created_at=datetime.now() - timedelta(seconds=9999),
                ),
            )
        assert repo.evict_expired() == 5  # noqa: PLR2004
        assert repo.size() == 0

    def test_size_zero_when_all_expired_no_get_called(self) -> None:
        repo = CacheL1Repository()
        for i in range(3):
            repo.set(
                str(i),
                CacheEntry(
                    query_hash=str(i),
                    result="x",
                    created_at=datetime.now() - timedelta(seconds=9999),
                ),
            )
        assert repo.size() == 0

    def test_get_expired_twice_returns_none_both_times(self) -> None:
        repo = CacheL1Repository()
        repo.set(
            "exp",
            CacheEntry(
                query_hash="exp",
                result="test",
                created_at=datetime.now() - timedelta(seconds=9999),
            ),
        )
        assert repo.get("exp") is None
        assert repo.get("exp") is None

    def test_empty_key_accepted(self) -> None:
        repo = CacheL1Repository()
        entry = CacheEntry(query_hash="", result="empty")
        repo.set("", entry)
        assert repo.get("").result == "empty"

    def test_get_with_empty_key_returns_none_when_missing(self) -> None:
        repo = CacheL1Repository()
        assert repo.get("") is None


class TestCacheL1RepoEdgeCases:
    def test_invalidate_nonexistent_is_idempotent(self) -> None:
        repo = CacheL1Repository()
        repo.invalidate("missing")
        assert repo.size() == 0

    def test_size_zero_after_clear(self) -> None:
        repo = CacheL1Repository()
        repo.set("a", CacheEntry(query_hash="a", result="x"))
        repo.clear()
        assert repo.size() == 0
        assert repo.get("a") is None
