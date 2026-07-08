from datetime import datetime, timedelta

import pytest
from hexawyn.domain.models.cache import CACHE_TTL_SECONDS, CacheEntry
from hexawyn.infrastructure.config.cache_manager import (
    _repository,
    clear_l1,
    compute_query_hash,
    get_cache_stats,
    get_l1,
    set_l1,
)
from hexawyn.infrastructure.memory.cache_l1_repository import CacheL1Repository


@pytest.fixture(autouse=True)
def clear_cache_between_tests():
    clear_l1()
    yield
    clear_l1()


class TestCacheL1RepositoryIntegration:
    @pytest.mark.integration
    def test_set_then_get_returns_entry(self):
        repo = CacheL1Repository()
        entry = CacheEntry(
            query_hash="abc123",
            result="OOM detected",
            created_at=datetime.now(),
        )
        repo.set("abc123", entry)
        retrieved = repo.get("abc123")

        assert retrieved is not None
        assert retrieved.result == "OOM detected"
        assert retrieved.is_valid is True

    @pytest.mark.integration
    def test_expired_entry_returns_none(self):
        repo = CacheL1Repository()
        expired_entry = CacheEntry(
            query_hash="abc123",
            result="stale result",
            created_at=datetime.now() - timedelta(seconds=CACHE_TTL_SECONDS + 1),
        )
        repo.set("abc123", expired_entry)
        result = repo.get("abc123")
        assert result is None

    @pytest.mark.integration
    def test_evict_expired_cleans_store(self):
        repo = CacheL1Repository()

        for i in range(3):
            repo.set(
                f"fresh_{i}",
                CacheEntry(
                    query_hash=f"fresh_{i}",
                    result=f"result_{i}",
                    created_at=datetime.now(),
                ),
            )

        for i in range(2):
            repo.set(
                f"expired_{i}",
                CacheEntry(
                    query_hash=f"expired_{i}",
                    result=f"old_result_{i}",
                    created_at=datetime.now() - timedelta(seconds=CACHE_TTL_SECONDS + 1),
                ),
            )

        evicted = repo.evict_expired()
        assert evicted == 2
        assert repo.size() == 3

    @pytest.mark.integration
    def test_size_counts_only_valid_entries(self):
        repo = CacheL1Repository()
        repo.set(
            "fresh",
            CacheEntry(query_hash="fresh", result="fresh", created_at=datetime.now()),
        )
        repo.set(
            "expired",
            CacheEntry(
                query_hash="expired",
                result="expired",
                created_at=datetime.now() - timedelta(seconds=301),
            ),
        )
        assert repo.size() == 1


class TestCacheManagerIntegration:
    @pytest.mark.integration
    def test_set_l1_then_get_l1_same_query(self):
        set_l1(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
            result="OOM detected — increase memory limit",
        )
        entry = get_l1(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
        )
        assert entry is not None
        assert entry.result == "OOM detected — increase memory limit"

    @pytest.mark.integration
    def test_case_insensitive_query_hits_same_cache(self):
        set_l1(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
            result="OOM detected",
        )
        entry = get_l1(
            query="Why is Payments-API CRASHING?",
            cluster_name="prod-eu",
        )
        assert entry is not None
        assert entry.result == "OOM detected"

    @pytest.mark.integration
    def test_different_cluster_different_cache_entry(self):
        set_l1(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
            result="EU result",
        )
        entry_us = get_l1(
            query="why is payments-api crashing?",
            cluster_name="prod-us",
        )
        assert entry_us is None

    @pytest.mark.integration
    def test_clear_l1_removes_all_entries(self):
        for i in range(5):
            set_l1(
                query=f"question {i}",
                cluster_name="prod-eu",
                result=f"result {i}",
            )

        stats_before = get_cache_stats()
        assert stats_before["l1_size"] == 5

        clear_l1()

        stats_after = get_cache_stats()
        assert stats_after["l1_size"] == 0

    @pytest.mark.integration
    def test_get_l1_returns_none_after_ttl(self):
        query_hash = compute_query_hash(
            query="test query",
            cluster_name="prod-eu",
        )
        expired_entry = CacheEntry(
            query_hash=query_hash,
            result="stale result",
            created_at=datetime.now() - timedelta(seconds=CACHE_TTL_SECONDS + 1),
        )
        _repository.set(query_hash, expired_entry)

        result = get_l1(query="test query", cluster_name="prod-eu")
        assert result is None

    @pytest.mark.integration
    def test_cache_stats_reflect_real_state(self):
        set_l1(query="question 1", cluster_name="prod-eu", result="result 1")
        set_l1(query="question 2", cluster_name="prod-eu", result="result 2")
        stats = get_cache_stats()
        assert stats["l1_size"] == 2
        assert stats["l1_ttl_seconds"] == CACHE_TTL_SECONDS


class TestCacheAndQuotaIntegration:
    @pytest.mark.integration
    def test_cache_hit_does_not_prevent_quota_increment(self, monkeypatch):
        import duckdb
        from hexawyn.domain.models.quota import LicenseTier, get_investigation_limit
        from hexawyn.infrastructure.config.quota_manager import _get_current_month
        from hexawyn.infrastructure.memory.quota_repository import QuotaRepository

        conn = duckdb.connect(":memory:")
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")

        import pathlib

        schema_sql = (
            pathlib.Path(__file__).parent.parent.parent
            / "src/hexawyn/infrastructure/memory/sql/schema.sql"
        ).read_text(encoding="utf-8")
        conn.execute(schema_sql)

        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager.get_connection",
            lambda: conn,
        )

        set_l1(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
            result="OOM detected",
        )

        entry = get_l1(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
        )
        assert entry is not None

        repo = QuotaRepository(conn=conn)
        tier = LicenseTier.FREE
        repo.increment_investigation(
            month=_get_current_month(),
            tier=tier,
            limit=get_investigation_limit(tier),
        )
        quota = repo.get_investigation_quota(month=_get_current_month())
        assert quota.count == 1
