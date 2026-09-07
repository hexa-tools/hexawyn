from __future__ import annotations

from unittest.mock import patch

from hexawyn.infrastructure.config.cache_manager import (
    clear_l1,
    compute_query_hash,
    evict_expired_l1,
    get_cache_stats,
    get_l1,
    invalidate_l1,
    set_l1,
)


class TestComputeQueryHash:
    def test_consistent_hash(self) -> None:
        h1 = compute_query_hash("why is it crashing?", "prod-eu")
        h2 = compute_query_hash("why is it crashing?", "prod-eu")
        assert h1 == h2

    def test_case_insensitive_query(self) -> None:
        h1 = compute_query_hash("WHY IS IT CRASHING?", "prod-eu")
        h2 = compute_query_hash("why is it crashing?", "prod-eu")
        assert h1 == h2

    def test_cluster_name_is_case_sensitive(self) -> None:
        h1 = compute_query_hash("crash", "PROD-EU")
        h2 = compute_query_hash("crash", "prod-eu")
        assert h1 != h2

    def test_different_clusters_different_hashes(self) -> None:
        h1 = compute_query_hash("crash", "prod-eu")
        h2 = compute_query_hash("crash", "prod-us")
        assert h1 != h2


class TestCacheOperations:
    def test_get_l1(self) -> None:
        with patch("hexawyn.infrastructure.config.cache_manager._repository") as mock_repo:
            mock_repo.get.return_value = None
            result = get_l1("crash?", "prod-eu")
            assert result is None
            mock_repo.get.assert_called_once()

    def test_set_l1(self) -> None:
        with patch("hexawyn.infrastructure.config.cache_manager._repository") as mock_repo:
            set_l1("crash?", "prod-eu", '{"status": "ok"}')
            mock_repo.set.assert_called_once()

    def test_invalidate_l1(self) -> None:
        with patch("hexawyn.infrastructure.config.cache_manager._repository") as mock_repo:
            invalidate_l1("crash?", "prod-eu")
            mock_repo.invalidate.assert_called_once()

    def test_clear_l1(self) -> None:
        with patch("hexawyn.infrastructure.config.cache_manager._repository") as mock_repo:
            clear_l1()
            mock_repo.clear.assert_called_once()

    def test_evict_expired_l1(self) -> None:
        with patch("hexawyn.infrastructure.config.cache_manager._repository") as mock_repo:
            mock_repo.evict_expired.return_value = 3
            result = evict_expired_l1()
            assert result == 3  # noqa: PLR2004

    def test_get_cache_stats(self) -> None:
        with patch("hexawyn.infrastructure.config.cache_manager._repository") as mock_repo:
            mock_repo.size.return_value = 10
            result = get_cache_stats()
            assert result["l1_size"] == 10  # noqa: PLR2004
            assert result["l1_ttl_seconds"] == 300  # noqa: PLR2004
