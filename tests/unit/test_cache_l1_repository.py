from hexawyn.infrastructure.memory.cache_l1_repository import CacheL1Repository


class TestCacheL1Repo:
    def test_initially_empty(self):
        repo = CacheL1Repository()
        assert repo.size() == 0
