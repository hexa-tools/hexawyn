from datetime import UTC, datetime, timedelta

import duckdb
from hexawyn.domain.models.cache import CachedInvestigation
from hexawyn.infrastructure.memory.duckdb_cache_adapter import (
    DuckDBCacheAdapter,
    compute_cache_key,
)


def _make_entry(**kwargs: object) -> CachedInvestigation:
    defaults: dict[str, object] = {
        "id": "test-id-1",
        "cache_key": compute_cache_key("prod", "investigate_pod", "ns", "pod-1", "why?"),
        "finding_type": "CrashLoopBackOff",
        "root_cause": "OOMKilled",
        "recommendation": "increase memory to 512Mi",
        "severity": "high",
        "cluster_name": "prod",
        "namespace": "ns",
        "resource_name": "pod-1",
        "resource_kind": "Pod",
        "pod_status_at_cache_time": "CrashLoopBackOff",
        "pod_restart_count_at_cache": 3,
        "tool_name": "investigate_pod",
        "created_at": datetime.now(UTC),
        "sanitized": True,
    }
    defaults.update(kwargs)
    return CachedInvestigation(**defaults)


class TestDuckDBCacheAdapter:
    def test_set_and_get(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        entry = _make_entry()
        adapter.set(entry)

        cached = adapter.get(entry.cache_key)
        assert cached is not None
        assert cached.cache_key == entry.cache_key
        assert cached.root_cause == "OOMKilled"
        assert cached.recommendation == "increase memory to 512Mi"

    def test_get_returns_none_for_missing_key(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        assert adapter.get("nonexistent") is None

    def test_get_with_validation_returns_valid_when_pod_unchanged(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        entry = _make_entry(
            pod_status_at_cache_time="CrashLoopBackOff",
            pod_restart_count_at_cache=3,
        )
        adapter.set(entry)

        cached, result = adapter.get_with_validation(
            entry.cache_key,
            current_pod_status="CrashLoopBackOff",
            current_restart_count=3,
        )
        assert cached is not None
        assert result.is_valid is True
        assert result.reason == "VALID"

    def test_get_with_validation_invalidates_on_pod_status_change(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        entry = _make_entry(
            pod_status_at_cache_time="CrashLoopBackOff",
            pod_restart_count_at_cache=3,
        )
        adapter.set(entry)

        cached, result = adapter.get_with_validation(
            entry.cache_key,
            current_pod_status="Running",
            current_restart_count=3,
        )
        assert cached is None
        assert result.is_valid is False
        assert "POD_STATUS_CHANGED" in result.reason

    def test_get_with_validation_invalidates_on_restart_count_increase(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        entry = _make_entry(
            pod_status_at_cache_time="CrashLoopBackOff",
            pod_restart_count_at_cache=3,
        )
        adapter.set(entry)

        cached, result = adapter.get_with_validation(
            entry.cache_key,
            current_pod_status="CrashLoopBackOff",
            current_restart_count=5,
        )
        assert cached is None
        assert result.is_valid is False
        assert "RESTART_COUNT_CHANGED" in result.reason

    def test_invalidate_removes_entry(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        entry = _make_entry()
        adapter.set(entry)
        assert adapter.get(entry.cache_key) is not None

        adapter.invalidate(entry.cache_key)
        assert adapter.get(entry.cache_key) is None

    def test_clear_removes_all_entries(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        adapter.set(_make_entry(id="a", cache_key="k1"))
        adapter.set(_make_entry(id="b", cache_key="k2"))
        assert adapter.stats()["total"] == 2

        adapter.clear()
        assert adapter.stats()["total"] == 0

    def test_invalidate_by_resource(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        adapter.set(_make_entry(id="a", cache_key="k1", resource_name="pod-1"))
        adapter.set(_make_entry(id="b", cache_key="k2", resource_name="pod-2"))

        count = adapter.invalidate_by_resource("prod", "ns", "pod-1")
        assert count == 1
        assert adapter.get("k2") is not None

    def test_stats_counts_total_and_expired(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        entry = _make_entry(
            id="fresh",
            cache_key="fresh-key",
            created_at=datetime.now(UTC),
        )
        adapter.set(entry)

        old = _make_entry(
            id="old",
            cache_key="old-key",
            created_at=datetime.now(UTC) - timedelta(hours=7),
        )
        adapter.set(old)

        s = adapter.stats()
        assert s["total"] == 2
        assert s["expired"] >= 1
        assert s["valid"] >= 1

    def test_get_returns_none_when_expired(self):
        conn = duckdb.connect(":memory:")
        adapter = DuckDBCacheAdapter(conn=conn)
        entry = _make_entry(
            cache_key="expired-key",
            created_at=datetime.now(UTC) - timedelta(hours=7),
        )
        adapter.set(entry)

        assert adapter.get("expired-key") is None
