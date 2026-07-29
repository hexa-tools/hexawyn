from unittest.mock import patch

from hexawyn.infrastructure.config.cache_manager import get_cache_stats


class TestCacheStats:
    def test_returns_l1_size(self):
        with patch("hexawyn.infrastructure.config.cache_manager._repository") as mock_repo:
            mock_repo.size.return_value = 5
            stats = get_cache_stats()
            assert stats["l1_size"] == 5  # noqa: PLR2004

    def test_returns_ttl_seconds(self):
        stats = get_cache_stats()
        assert stats["l1_ttl_seconds"] == 300  # noqa: PLR2004

    def test_health_includes_cache_stats(self):
        with patch(
            "hexawyn.infrastructure.config.cache_manager.get_cache_stats",
            return_value={"l1_size": 3, "l1_ttl_seconds": 300},
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert "cache_l1_size" in result

    def test_returns_zero_for_empty_cache(self) -> None:
        with patch("hexawyn.infrastructure.config.cache_manager._repository") as mock_repo:
            mock_repo.size.return_value = 0
            stats = get_cache_stats()
            assert stats["l1_size"] == 0

    def test_returns_large_size(self) -> None:
        with patch("hexawyn.infrastructure.config.cache_manager._repository") as mock_repo:
            mock_repo.size.return_value = 9999
            stats = get_cache_stats()
            assert stats["l1_size"] == 9999  # noqa: PLR2004
