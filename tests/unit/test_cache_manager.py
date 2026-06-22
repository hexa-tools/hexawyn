from datetime import datetime
from unittest.mock import patch

from hexawyn.domain.models.cache import CacheEntry
from hexawyn.infrastructure.config.cache_manager import (
    clear_l1,
    compute_query_hash,
    get_l1,
    set_l1,
)


class TestComputeQueryHash:
    def test_same_query_same_cluster_same_hash(self):
        h1 = compute_query_hash(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
        )
        h2 = compute_query_hash(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
        )
        assert h1 == h2

    def test_different_query_different_hash(self):
        h1 = compute_query_hash(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
        )
        h2 = compute_query_hash(
            query="what is the SLO impact?",
            cluster_name="prod-eu",
        )
        assert h1 != h2

    def test_different_cluster_different_hash(self):
        h1 = compute_query_hash(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
        )
        h2 = compute_query_hash(
            query="why is payments-api crashing?",
            cluster_name="prod-us",
        )
        assert h1 != h2

    def test_hash_is_64_chars(self):
        h = compute_query_hash(
            query="test query",
            cluster_name="test-cluster",
        )
        assert len(h) == 64

    def test_hash_is_lowercase_hex(self):
        h = compute_query_hash(
            query="test query",
            cluster_name="test-cluster",
        )
        assert all(c in "0123456789abcdef" for c in h)

    def test_case_insensitive_query(self):
        h1 = compute_query_hash(
            query="Why is Payments-API crashing?",
            cluster_name="prod-eu",
        )
        h2 = compute_query_hash(
            query="why is payments-api crashing?",
            cluster_name="prod-eu",
        )
        assert h1 == h2


class TestGetL1:
    def test_returns_none_when_not_cached(self):
        with patch(
            "hexawyn.infrastructure.config.cache_manager._repository"
        ) as mock_repo:
            mock_repo.get.return_value = None
            result = get_l1(
                query="test query",
                cluster_name="prod-eu",
            )
            assert result is None

    def test_returns_entry_when_cached(self):
        entry = CacheEntry(
            query_hash="abc123",
            result="OOM detected",
            created_at=datetime.now(),
        )
        with patch(
            "hexawyn.infrastructure.config.cache_manager._repository"
        ) as mock_repo:
            mock_repo.get.return_value = entry
            result = get_l1(
                query="why is payments-api crashing?",
                cluster_name="prod-eu",
            )
            assert result is not None
            assert result.result == "OOM detected"


class TestSetL1:
    def test_stores_entry_in_repository(self):
        with patch(
            "hexawyn.infrastructure.config.cache_manager._repository"
        ) as mock_repo:
            set_l1(
                query="test query",
                cluster_name="prod-eu",
                result="test result",
            )
            mock_repo.set.assert_called_once()


class TestClearL1:
    def test_clears_repository(self):
        with patch(
            "hexawyn.infrastructure.config.cache_manager._repository"
        ) as mock_repo:
            clear_l1()
            mock_repo.clear.assert_called_once()
