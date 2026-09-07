"""Integration tests: DuckDBCacheAdapter → real DuckDB — store, retrieve, expire, invalidate."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

import duckdb
import pytest
from hexawyn.domain.models.cache import CachedInvestigation
from hexawyn.infrastructure.memory.duckdb_cache_adapter import (
    DuckDBCacheAdapter,
    compute_cache_key,
)


@pytest.fixture
def cache_conn() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(":memory:")
    yield conn
    conn.close()


@pytest.fixture
def cache_adapter(
    cache_conn: duckdb.DuckDBPyConnection,
) -> DuckDBCacheAdapter:
    return DuckDBCacheAdapter(conn=cache_conn)


def _make_investigation(  # noqa: PLR0913
    cache_key: str = "abc123",
    cluster: str = "prod-eu",
    namespace: str = "payments",
    resource: str = "payments-api",
    root_cause: str = "OOMKilled",
    expires_at: datetime | None = None,
    pod_status: str = "Running",
    restart_count: int = 0,
) -> CachedInvestigation:
    return CachedInvestigation(
        id="",
        cache_key=cache_key,
        finding_type="CrashLoopBackOff",
        root_cause=root_cause,
        recommendation="Increase memory limit",
        severity="high",
        cluster_name=cluster,
        namespace=namespace,
        resource_name=resource,
        resource_kind="Deployment",
        pod_status_at_cache_time=pod_status,
        pod_restart_count_at_cache=restart_count,
        tool_name="get_resource_usage",
        created_at=datetime.now(UTC),
        expires_at=expires_at,
        sanitized=True,
    )


@pytest.mark.integration
class TestDuckDBCacheAdapterIntegration:
    def test_store_and_retrieve(self, cache_adapter: DuckDBCacheAdapter) -> None:
        key = compute_cache_key(
            "prod-eu",
            "get_resource_usage",
            "payments",
            "payments-api",
            "how much CPU is payments-api using?",
        )  # noqa: E501
        inv = _make_investigation(cache_key=key)
        cache_adapter.set(inv)

        result = cache_adapter.get(key)

        assert result is not None
        assert result.cache_key == key
        assert result.root_cause == "OOMKilled"
        assert result.cluster_name == "prod-eu"

    def test_miss_on_unknown_key(self, cache_adapter: DuckDBCacheAdapter) -> None:
        result = cache_adapter.get("nonexistent-key")

        assert result is None

    def test_expired_entry_returns_none(self, cache_adapter: DuckDBCacheAdapter) -> None:
        key = compute_cache_key("prod-eu", "get_resource_usage", "payments", "x", "query")
        expired = datetime.now(UTC) - timedelta(hours=1)
        inv = _make_investigation(cache_key=key, expires_at=expired)
        cache_adapter.set(inv)

        result = cache_adapter.get(key)

        assert result is None

    def test_invalidate_removes_entry(self, cache_adapter: DuckDBCacheAdapter) -> None:
        key = compute_cache_key("prod-eu", "get_resource_usage", "payments", "api", "query")
        inv = _make_investigation(cache_key=key)
        cache_adapter.set(inv)

        cache_adapter.invalidate(key)

        result = cache_adapter.get(key)
        assert result is None

    def test_invalidate_by_resource_removes_matching(
        self, cache_adapter: DuckDBCacheAdapter
    ) -> None:  # noqa: E501
        key_a = compute_cache_key("prod-eu", "get_resource_usage", "ns", "svc-a", "q1")
        key_b = compute_cache_key("prod-eu", "get_resource_usage", "ns", "svc-b", "q2")
        cache_adapter.set(_make_investigation(cache_key=key_a, namespace="ns", resource="svc-a"))
        cache_adapter.set(_make_investigation(cache_key=key_b, namespace="ns", resource="svc-b"))

        removed = cache_adapter.invalidate_by_resource("prod-eu", "ns", "svc-a")

        assert removed == 1  # noqa: PLR2004
        assert cache_adapter.get(key_a) is None
        assert cache_adapter.get(key_b) is not None

    def test_clear_removes_all(self, cache_adapter: DuckDBCacheAdapter) -> None:
        cache_adapter.set(_make_investigation(cache_key="k1"))
        cache_adapter.set(_make_investigation(cache_key="k2"))

        cache_adapter.clear()

        stats = cache_adapter.stats()
        assert stats["total"] == 0

    def test_stats_counts_correctly(self, cache_adapter: DuckDBCacheAdapter) -> None:
        key = compute_cache_key("prod-eu", "get_resource_usage", "ns", "r", "q")
        cache_adapter.set(_make_investigation(cache_key=key))

        stats = cache_adapter.stats()

        assert stats["total"] == 1  # noqa: PLR2004
        assert stats["valid"] >= 0

    def test_get_with_validation_pod_status_changed(
        self, cache_adapter: DuckDBCacheAdapter
    ) -> None:  # noqa: E501
        key = compute_cache_key("prod-eu", "get_resource_usage", "ns", "pod-x", "q")
        inv = _make_investigation(cache_key=key, pod_status="Running")
        cache_adapter.set(inv)

        result, validation = cache_adapter.get_with_validation(key, "CrashLoopBackOff", 0)

        assert result is None
        assert validation.is_valid is False
        assert "POD_STATUS_CHANGED" in validation.reason

    def test_get_with_validation_restart_count_increased(
        self, cache_adapter: DuckDBCacheAdapter
    ) -> None:  # noqa: E501
        key = compute_cache_key("prod-eu", "get_resource_usage", "ns", "pod-x", "q")
        inv = _make_investigation(cache_key=key, pod_status="Running", restart_count=3)
        cache_adapter.set(inv)

        result, validation = cache_adapter.get_with_validation(key, "Running", 5)

        assert result is None
        assert validation.is_valid is False
        assert "RESTART_COUNT_CHANGED" in validation.reason

    def test_get_with_validation_valid(self, cache_adapter: DuckDBCacheAdapter) -> None:
        key = compute_cache_key("prod-eu", "get_resource_usage", "ns", "pod-x-ok", "q")
        inv = _make_investigation(cache_key=key, pod_status="Running", restart_count=2)
        cache_adapter.set(inv)

        result, validation = cache_adapter.get_with_validation(key, "Running", 2)

        assert result is not None
        assert validation.is_valid is True
        assert validation.reason == "VALID"
