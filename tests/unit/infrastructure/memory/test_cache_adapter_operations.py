from __future__ import annotations

import datetime
from unittest.mock import MagicMock, patch

from hexawyn.domain.models.cache import CachedInvestigation
from hexawyn.infrastructure.memory.duckdb_cache_adapter import (
    DuckDBCacheAdapter,
    compute_cache_key,
)


class TestComputeCacheKey:
    def test_consistent_hash(self) -> None:
        key1 = compute_cache_key(
            "prod-eu", "describe_pod", "default", "my-pod", "why is it crashing?"
        )
        key2 = compute_cache_key(
            "prod-eu", "describe_pod", "default", "my-pod", "why is it crashing?"
        )
        assert key1 == key2

    def test_case_insensitive(self) -> None:
        key1 = compute_cache_key("PROD-EU", "DESCRIBE_POD", "DEFAULT", "MY-POD", "WHY?")
        key2 = compute_cache_key("prod-eu", "describe_pod", "default", "my-pod", "why?")
        assert key1 == key2

    def test_different_clusters_different_keys(self) -> None:
        key1 = compute_cache_key("prod-eu", "describe_pod", "default", "pod", "query")
        key2 = compute_cache_key("prod-us", "describe_pod", "default", "pod", "query")
        assert key1 != key2

    def test_returns_hex_string(self) -> None:
        key = compute_cache_key("test", "tool", "ns", "res", "q")
        assert len(key) == 64  # noqa: PLR2004
        assert all(c in "0123456789abcdef" for c in key)


class TestDuckDBCacheAdapter:
    def test_initialization_with_conn(self) -> None:
        mock_conn = MagicMock()
        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            _adapter = DuckDBCacheAdapter(conn=mock_conn)
            mock_conn.execute.assert_called_once_with("SQL")

    def test_initialization_without_conn_creates_own_connection(self) -> None:
        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter.duckdb.connect",
        ) as mock_connect:
            mock_connect.return_value = MagicMock()
            with patch(
                "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
                return_value="SQL",
            ):
                adapter = DuckDBCacheAdapter()
                mock_connect.assert_called_once()
                assert adapter._owns_connection is True

    def test_close_does_nothing_when_injected_conn(self) -> None:
        mock_conn = MagicMock()
        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            adapter.close()
            mock_conn.close.assert_not_called()

    def test_close_calls_close_when_owns_connection(self) -> None:
        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter.duckdb.connect",
        ) as mock_connect:
            mock_conn = MagicMock()
            mock_connect.return_value = mock_conn
            with patch(
                "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
                return_value="SQL",
            ):
                adapter = DuckDBCacheAdapter()
                adapter.close()
                mock_conn.close.assert_called_once()

    def test_get_returns_none_when_no_row(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = None
        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            result = adapter.get("some-key")
            assert result is None

    def test_get_returns_cached_investigation(self) -> None:
        mock_conn = MagicMock()
        now = datetime.datetime.now(datetime.UTC)
        row = (
            "uuid-1",
            "cache-key-hash",
            "OOMKill",
            "Memory limit too low",
            "Increase memory limit to 1Gi",
            "critical",
            "prod-eu",
            "default",
            "my-pod",
            "Deployment",
            "CrashLoopBackOff",
            3,
            "describe_pod",
            now,
            now + datetime.timedelta(hours=6),
            True,
        )
        mock_conn.execute.return_value.fetchone.return_value = row
        mock_conn.execute.side_effect = None

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            result = adapter.get("cache-key-hash")
            assert result is not None
            assert result.finding_type == "OOMKill"
            assert result.severity == "critical"

    def test_get_suppresses_exceptions(self) -> None:
        mock_conn = MagicMock()

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            mock_conn.execute.side_effect = RuntimeError("db error")
            result = adapter.get("key")
            assert result is None

    def test_get_with_validation_cache_miss(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = None

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            cached, validation = adapter.get_with_validation("key", "Running", 0)
            assert cached is None
            assert validation.is_valid is False
            assert validation.reason == "CACHE_MISS"

    def test_get_with_validation_pod_status_changed(self) -> None:
        mock_conn = MagicMock()
        now = datetime.datetime.now(datetime.UTC)
        row = (
            "uuid-1",
            "key",
            "OOMKill",
            "cause",
            "fix",
            "critical",
            "prod",
            "ns",
            "pod",
            "Deployment",
            "CrashLoopBackOff",
            0,
            "tool",
            now,
            now + datetime.timedelta(hours=6),
            True,
        )
        mock_conn.execute.return_value.fetchone.return_value = row

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            cached, validation = adapter.get_with_validation("key", "Running", 0)
            assert cached is None
            assert "POD_STATUS_CHANGED" in validation.reason

    def test_get_with_validation_restart_count_changed(self) -> None:
        mock_conn = MagicMock()
        now = datetime.datetime.now(datetime.UTC)
        row = (
            "uuid-1",
            "key",
            "OOMKill",
            "cause",
            "fix",
            "critical",
            "prod",
            "ns",
            "pod",
            "Deployment",
            "CrashLoopBackOff",
            2,
            "tool",
            now,
            now + datetime.timedelta(hours=6),
            True,
        )
        mock_conn.execute.return_value.fetchone.return_value = row

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            cached, validation = adapter.get_with_validation("key", "CrashLoopBackOff", 5)
            assert cached is None
            assert "RESTART_COUNT_CHANGED" in validation.reason

    def test_get_with_validation_ttl_expired(self) -> None:
        mock_conn = MagicMock()
        now = datetime.datetime.now(datetime.UTC)
        row = (
            "uuid-1",
            "key",
            "OOMKill",
            "cause",
            "fix",
            "critical",
            "prod",
            "ns",
            "pod",
            "Deployment",
            "CrashLoopBackOff",
            0,
            "tool",
            now - datetime.timedelta(hours=10),
            now - datetime.timedelta(hours=4),
            False,
        )
        mock_conn.execute.return_value.fetchone.return_value = row

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            cached, validation = adapter.get_with_validation("key", "CrashLoopBackOff", 0)
            assert cached is None
            assert "TTL_EXPIRED" in validation.reason

    def test_set_generates_id_when_missing(self) -> None:
        mock_conn = MagicMock()
        now = datetime.datetime.now(datetime.UTC)
        entry = CachedInvestigation(
            id="",
            cache_key="key",
            finding_type="OOMKill",
            root_cause="cause",
            recommendation="fix",
            severity="high",
            cluster_name="prod",
            namespace="default",
            resource_name="pod",
            resource_kind="Deployment",
            pod_status_at_cache_time="Running",
            pod_restart_count_at_cache=0,
            tool_name="describe_pod",
            created_at=now,
            expires_at=now + datetime.timedelta(hours=6),
        )

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            adapter.set(entry)
            assert entry.id != ""

    def test_set_suppresses_exceptions(self) -> None:
        mock_conn = MagicMock()
        entry = CachedInvestigation(
            id="uuid-1",
            cache_key="key",
            finding_type="OOMKill",
            root_cause="cause",
            recommendation="fix",
            severity="high",
            cluster_name="prod",
            namespace="default",
            resource_name="pod",
            resource_kind="Deployment",
            pod_status_at_cache_time="Running",
            pod_restart_count_at_cache=0,
            tool_name="tool",
        )

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            mock_conn.execute.side_effect = RuntimeError("db error")
            adapter.set(entry)

    def test_invalidate_deletes_by_key(self) -> None:
        mock_conn = MagicMock()

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            adapter.invalidate("some-key")
            mock_conn.execute.assert_called()

    def test_invalidate_suppresses_exceptions(self) -> None:
        mock_conn = MagicMock()

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            mock_conn.execute.side_effect = RuntimeError("db error")
            adapter.invalidate("key")

    def test_invalidate_by_resource(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = [5]

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            result = adapter.invalidate_by_resource("prod", "default", "my-pod")
            assert result == 5  # noqa: PLR2004

    def test_invalidate_by_resource_suppresses_exceptions(self) -> None:
        mock_conn = MagicMock()

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            mock_conn.execute.side_effect = RuntimeError("db error")
            result = adapter.invalidate_by_resource("prod", "default", "pod")
            assert result == 0

    def test_clear(self) -> None:
        mock_conn = MagicMock()

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            adapter.clear()
            mock_conn.execute.assert_called()

    def test_clear_suppresses_exceptions(self) -> None:
        mock_conn = MagicMock()

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            mock_conn.execute.side_effect = RuntimeError("db error")
            adapter.clear()

    def test_stats(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.side_effect = [[10], [3]]

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            result = adapter.stats()
            assert result["total"] == 10  # noqa: PLR2004
            assert result["expired"] == 3  # noqa: PLR2004
            assert result["valid"] == 7  # noqa: PLR2004

    def test_stats_count_error_returns_zero(self) -> None:
        mock_conn = MagicMock()

        with patch(
            "hexawyn.infrastructure.memory.duckdb_cache_adapter._load_sql",
            return_value="SQL",
        ):
            adapter = DuckDBCacheAdapter(conn=mock_conn)
            mock_conn.execute.side_effect = RuntimeError("db error")
            result = adapter.stats()
            assert result["total"] == 0
            assert result["expired"] == 0
