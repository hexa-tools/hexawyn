from abc import ABC, abstractmethod

from hexawyn.domain.models.cache import CachedInvestigation, CacheValidationResult


class CacheStatsDict(dict[str, int]):
    pass


class CachePort(ABC):
    @abstractmethod
    def get(self, cache_key: str) -> CachedInvestigation | None:
        """Return cached result if valid (not expired), otherwise None."""

    @abstractmethod
    def get_with_validation(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        """Return cached result with validation against current pod state."""

    @abstractmethod
    def set(self, result: CachedInvestigation) -> None:
        """Store a sanitized investigation result."""

    @abstractmethod
    def invalidate(self, cache_key: str) -> None:
        """Invalidate a specific cache entry."""

    @abstractmethod
    def invalidate_by_resource(self, cluster: str, namespace: str, resource: str) -> int:
        """Invalidate all entries for a given resource."""

    @abstractmethod
    def clear(self) -> None:
        """Delete all cache entries (RGPD right to erasure)."""

    @abstractmethod
    def stats(self) -> dict[str, int]:
        """Return cache statistics: total, expired, valid, invalidated."""
