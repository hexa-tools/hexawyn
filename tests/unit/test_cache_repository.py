from datetime import datetime, timedelta

from hexawyn.domain.models.cache import CACHE_TTL_SECONDS, CacheEntry
from hexawyn.infrastructure.memory.cache_l1_repository import CacheL1Repository


class TestCacheL1Repository:
    def setup_method(self):
        self.repo = CacheL1Repository()

    def test_get_returns_none_when_empty(self):
        result = self.repo.get("nonexistent_hash")
        assert result is None

    def test_set_and_get_returns_entry(self):
        entry = CacheEntry(
            query_hash="abc123",
            result="OOM detected",
            created_at=datetime.now(),
        )
        self.repo.set("abc123", entry)
        retrieved = self.repo.get("abc123")
        assert retrieved is not None
        assert retrieved.result == "OOM detected"

    def test_get_returns_none_for_expired_entry(self):
        entry = CacheEntry(
            query_hash="abc123",
            result="OOM detected",
            created_at=datetime.now() - timedelta(seconds=301),
        )
        self.repo.set("abc123", entry)
        result = self.repo.get("abc123")
        assert result is None

    def test_invalidate_removes_entry(self):
        entry = CacheEntry(
            query_hash="abc123",
            result="OOM detected",
            created_at=datetime.now(),
        )
        self.repo.set("abc123", entry)
        self.repo.invalidate("abc123")
        assert self.repo.get("abc123") is None

    def test_clear_removes_all_entries(self):
        for i in range(5):
            self.repo.set(
                f"hash_{i}",
                CacheEntry(
                    query_hash=f"hash_{i}",
                    result=f"result_{i}",
                    created_at=datetime.now(),
                ),
            )
        self.repo.clear()
        for i in range(5):
            assert self.repo.get(f"hash_{i}") is None

    def test_size_returns_valid_entry_count(self):
        self.repo.set(
            "fresh",
            CacheEntry(
                query_hash="fresh",
                result="fresh result",
                created_at=datetime.now(),
            ),
        )
        self.repo.set(
            "expired",
            CacheEntry(
                query_hash="expired",
                result="expired result",
                created_at=datetime.now() - timedelta(seconds=301),
            ),
        )
        assert self.repo.size() == 1

    def test_evict_expired_removes_old_entries(self):
        self.repo.set(
            "expired",
            CacheEntry(
                query_hash="expired",
                result="old result",
                created_at=datetime.now() - timedelta(seconds=301),
            ),
        )
        self.repo.evict_expired()
        assert len(self.repo._store) == 0
