"""Integration tests: MCP tools → DuckDB cache + memory full cycle.

Simulates hexa-control-plane's LangGraph flow (check_cache → execute_tool → store_memory)
by calling the real MCP tool, storing the result in DuckDB via CachePort/IncidentMemoryPort,
then verifying cache hit and VSS retrieval.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

import duckdb
import pytest
from hexawyn.domain.models.cache import CachedInvestigation
from hexawyn.domain.models.incident_memory import IncidentMemoryRecord
from hexawyn.infrastructure.memory.duckdb_cache_adapter import (
    DuckDBCacheAdapter,
    compute_cache_key,
)
from hexawyn.infrastructure.memory.incident_memory_repository import (
    IncidentMemoryRepository,
)

SCHEMA_PATH = (
    Path(__file__).parent.parent.parent / "src/hexawyn/infrastructure/memory/sql/schema.sql"
)
INDEXES_PATH = (
    Path(__file__).parent.parent.parent / "src/hexawyn/infrastructure/memory/sql/indexes.sql"
)


@pytest.fixture
def cycle_conn() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(":memory:")
    conn.execute("INSTALL vss;")
    conn.execute("LOAD vss;")
    conn.execute(SCHEMA_PATH.read_text(encoding="utf-8"))
    conn.execute(INDEXES_PATH.read_text(encoding="utf-8"))
    yield conn
    conn.close()


@pytest.fixture
def cache(cycle_conn: duckdb.DuckDBPyConnection) -> DuckDBCacheAdapter:
    return DuckDBCacheAdapter(conn=cycle_conn)


@pytest.fixture
def memory_repo(cycle_conn: duckdb.DuckDBPyConnection) -> IncidentMemoryRepository:
    return IncidentMemoryRepository(conn=cycle_conn)


def _fake_embedding() -> list[float]:
    random.seed(123)
    return [round(random.uniform(-1.0, 1.0), 6) for _ in range(768)]


def _store_in_cache(  # noqa: PLR0913
    cache: DuckDBCacheAdapter,
    tool_name: str,
    result: dict[str, object],
    cluster: str = "prod-eu",
    namespace: str = "",
    resource: str = "",
    query: str = "",
) -> str:
    cache_key = compute_cache_key(cluster, tool_name, namespace, resource, query)
    cache.set(
        CachedInvestigation(
            id="",
            cache_key=cache_key,
            finding_type=tool_name,
            root_cause=json.dumps(result),
            recommendation="",
            severity="info",
            cluster_name=cluster,
            namespace=namespace,
            resource_name=resource,
            resource_kind="Namespace",
            pod_status_at_cache_time="Running",
            pod_restart_count_at_cache=0,
            tool_name=tool_name,
            sanitized=True,
        )
    )
    return cache_key


def _store_in_memory(
    memory_repo: IncidentMemoryRepository,
    tool_name: str,
    cluster: str = "prod-eu",
    namespace: str = "",
    cause: str = "",
) -> None:
    memory_repo.store_incident(
        IncidentMemoryRecord(
            cluster_name=cluster,
            tool_name=tool_name,
            cause=cause or f"Investigation by {tool_name}",
            solution="Automated analysis",
            severity="info",
            namespace=namespace or None,
            embedding=_fake_embedding(),
        )
    )


@pytest.mark.integration
class TestGetResourceUsageCacheCycle:
    def test_full_cycle_cache_miss_then_hit(
        self,
        cache: DuckDBCacheAdapter,
        memory_repo: IncidentMemoryRepository,
        cycle_conn: duckdb.DuckDBPyConnection,
    ) -> None:
        from unittest.mock import MagicMock, patch

        tool_name = "get_resource_usage"
        cluster = "prod-eu"
        query = "how much CPU is dev namespace actually using?"

        cache_key = compute_cache_key(cluster, tool_name, "dev", "", query)

        miss = cache.get(cache_key)
        assert miss is None

        mock_response = MagicMock()
        mock_response.pods = []
        mock_response.namespace_summary = []
        mock_response.metrics_server_available = True
        mock_response.source = "metrics-server"
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pod_metrics_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_resource_usage.GetResourceUsageUseCase",
                return_value=mock_uc,
            ),
        ):
            result = _execute_get_resource_usage(namespace="dev")

        assert result.get("error") is None

        _store_in_cache(cache, tool_name, result, cluster=cluster, namespace="dev", query=query)
        _store_in_memory(
            memory_repo,
            tool_name,
            cluster=cluster,
            namespace="dev",
            cause="CPU usage analysis for namespace dev",
        )

        hit = cache.get(cache_key)
        assert hit is not None
        assert hit.tool_name == tool_name
        assert hit.cluster_name == cluster

    def test_full_cycle_vss_retrieves_stored_incident(
        self,
        cache: DuckDBCacheAdapter,
        memory_repo: IncidentMemoryRepository,
        cycle_conn: duckdb.DuckDBPyConnection,
    ) -> None:
        from hexawyn.infrastructure.memory.duckdb_client import search_similar

        tool_name = "get_resource_usage"
        cluster = "prod-eu"
        namespace = "staging"

        _store_in_cache(
            cache,
            tool_name,
            {"pods": []},
            cluster=cluster,
            namespace=namespace,
            query="cpu usage staging",
        )  # noqa: E501
        _store_in_memory(
            memory_repo,
            tool_name,
            cluster=cluster,
            namespace=namespace,
            cause="CPU usage investigation for staging namespace",
        )

        emb = _fake_embedding()
        results = search_similar(
            cycle_conn,
            embedding=emb,
            cluster_name=cluster,
            namespace=namespace,
            limit=5,
            min_score=0.0,
        )

        assert len(results) >= 1
        assert results[0]["tool_name"] == tool_name
        assert results[0]["namespace"] == namespace

    def test_cache_miss_different_cluster(
        self,
        cache: DuckDBCacheAdapter,
        memory_repo: IncidentMemoryRepository,
    ) -> None:
        tool_name = "get_resource_usage"

        _store_in_cache(cache, tool_name, {}, cluster="prod-eu", query="cpu dev")
        _store_in_memory(memory_repo, tool_name, cluster="prod-eu")

        cache_key_us = compute_cache_key("prod-us", tool_name, "", "", "cpu dev")

        miss = cache.get(cache_key_us)
        assert miss is None


def _execute_get_resource_usage(namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.tools.get_resource_usage import get_resource_usage

    return get_resource_usage(namespace=namespace)


@pytest.mark.integration
class TestGetNamespaceResourceAllocationCacheCycle:
    def test_full_cycle_cache_miss_then_hit(
        self,
        cache: DuckDBCacheAdapter,
        memory_repo: IncidentMemoryRepository,
        cycle_conn: duckdb.DuckDBPyConnection,
    ) -> None:
        from unittest.mock import MagicMock, patch

        tool_name = "get_namespace_resource_allocation"
        cluster = "prod-eu"
        query = "rank namespaces by CPU requests"

        cache_key = compute_cache_key(cluster, tool_name, "", "", query)

        miss = cache.get(cache_key)
        assert miss is None

        mock_response = MagicMock()
        mock_response.allocations = []
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_namespace_resource_allocation.GetNamespaceResourceAllocationUseCase",
                return_value=mock_uc,
            ),
        ):
            result = _execute_get_namespace_resource_allocation()

        assert result.get("error") is None

        _store_in_cache(cache, tool_name, result, cluster=cluster, query=query)
        _store_in_memory(
            memory_repo,
            tool_name,
            cluster=cluster,
            cause="Resource allocation ranking across namespaces",
        )

        hit = cache.get(cache_key)
        assert hit is not None
        assert hit.tool_name == tool_name

    def test_full_cycle_vss_retrieves_stored_incident(
        self,
        cache: DuckDBCacheAdapter,
        memory_repo: IncidentMemoryRepository,
        cycle_conn: duckdb.DuckDBPyConnection,
    ) -> None:
        from hexawyn.infrastructure.memory.duckdb_client import search_similar

        tool_name = "get_namespace_resource_allocation"
        cluster = "prod-eu"

        _store_in_cache(
            cache, tool_name, {"allocations": []}, cluster=cluster, query="resource allocation"
        )  # noqa: E501
        _store_in_memory(
            memory_repo, tool_name, cluster=cluster, cause="Namespace resource footprint analysis"
        )

        emb = _fake_embedding()
        results = search_similar(
            cycle_conn,
            embedding=emb,
            cluster_name=cluster,
            limit=5,
            min_score=0.0,
        )

        assert len(results) >= 1
        assert results[0]["tool_name"] == tool_name

    def test_ttl_expiry_on_cache(
        self,
        cache: DuckDBCacheAdapter,
        memory_repo: IncidentMemoryRepository,
    ) -> None:
        from datetime import UTC, datetime, timedelta

        tool_name = "get_namespace_resource_allocation"
        cluster = "prod-eu"
        query = "which namespace has most pods"

        cache_key = compute_cache_key(cluster, tool_name, "", "", query)

        expired = datetime.now(UTC) - timedelta(hours=1)
        cache.set(
            CachedInvestigation(
                id="",
                cache_key=cache_key,
                finding_type=tool_name,
                root_cause="{}",
                recommendation="",
                severity="info",
                cluster_name=cluster,
                namespace="",
                resource_name="",
                resource_kind="Namespace",
                pod_status_at_cache_time="Running",
                pod_restart_count_at_cache=0,
                tool_name=tool_name,
                expires_at=expired,
                sanitized=True,
            )
        )

        miss = cache.get(cache_key)
        assert miss is None


def _execute_get_namespace_resource_allocation() -> dict[str, object]:
    from hexawyn.mcp.tools.get_namespace_resource_allocation import (
        get_namespace_resource_allocation,
    )

    return get_namespace_resource_allocation()
