from datetime import datetime, timedelta

from hexawyn.domain.models.cache import CACHE_TTL_SECONDS, CacheEntry


class TestCacheEntry:
    def test_ttl_is_300_seconds(self):
        assert CACHE_TTL_SECONDS == 300

    def test_is_valid_when_fresh(self):
        entry = CacheEntry(
            query_hash="abc123",
            result="CrashLoopBackOff detected",
            created_at=datetime.now(),
        )
        assert entry.is_valid is True

    def test_is_expired_when_old(self):
        entry = CacheEntry(
            query_hash="abc123",
            result="CrashLoopBackOff detected",
            created_at=datetime.now() - timedelta(seconds=301),
        )
        assert entry.is_valid is False

    def test_is_expired_exactly_at_ttl(self):
        entry = CacheEntry(
            query_hash="abc123",
            result="CrashLoopBackOff detected",
            created_at=datetime.now() - timedelta(seconds=300),
        )
        assert entry.is_valid is False

    def test_stores_result(self):
        entry = CacheEntry(
            query_hash="abc123",
            result="OOM detected",
            created_at=datetime.now(),
        )
        assert entry.result == "OOM detected"

    def test_stores_query_hash(self):
        entry = CacheEntry(
            query_hash="abc123",
            result="OOM detected",
            created_at=datetime.now(),
        )
        assert entry.query_hash == "abc123"
