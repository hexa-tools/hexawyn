from hexawyn.domain.models.cache import CacheEntry, CACHE_TTL_SECONDS


class TestCache:
    def test_model_exists(self):
        entry = CacheEntry(query_hash="test", result="ok")
        assert entry.query_hash == "test"
        assert CACHE_TTL_SECONDS == 300
