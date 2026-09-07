from hexawyn.domain.models.cache import CACHE_TTL_SECONDS, CacheEntry


class TestCache:
    def test_model_exists(self):
        entry = CacheEntry(query_hash="test", result="ok")
        assert entry.query_hash == "test"
        assert CACHE_TTL_SECONDS == 300  # noqa: PLR2004
