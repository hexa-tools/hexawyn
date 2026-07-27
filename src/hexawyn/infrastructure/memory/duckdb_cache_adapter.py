import hashlib
import logging
import uuid
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import TypedDict

import duckdb

from hexawyn.application.ports.driven.cache_port import CachePort
from hexawyn.domain.models.cache import CachedInvestigation, CacheValidationResult

logger = logging.getLogger(__name__)

SQL_DIR = Path(__file__).parent / "sql"


def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


class CacheStatsDict(TypedDict):
    total: int
    expired: int
    valid: int
    invalidated: int


def compute_cache_key(
    cluster_name: str,
    tool_name: str,
    namespace: str,
    resource_name: str,
    query: str,
) -> str:
    raw = f"{cluster_name}|{tool_name}|{namespace}|{resource_name}|{query}".lower()
    return hashlib.sha256(raw.encode()).hexdigest()


class DuckDBCacheAdapter(CachePort):
    """Investigation cache backed by DuckDB. Lives in ~/.hexawyn/cache.db."""

    def __init__(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" / "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def close(self) -> None:
        if self._owns_connection:
            self._conn.close()

    def _ensure_schema(self) -> None:
        self._conn.execute(_load_sql("cache_schema.sql"))

    def get(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def get_with_validation(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(is_valid=False, reason="CACHE_MISS")

        if cached.pod_status_at_cache_time != current_pod_status:
            self.invalidate(cache_key)
            reason = f"POD_STATUS_CHANGED: {cached.pod_status_at_cache_time} → {current_pod_status}"
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if current_restart_count > cached.pod_restart_count_at_cache:
            self.invalidate(cache_key)
            reason = f"RESTART_COUNT_CHANGED: {cached.pod_restart_count_at_cache} → {current_restart_count}"  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def set(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (id) DO UPDATE SET "
                "cache_key=excluded.cache_key, "
                "finding_type=excluded.finding_type, "
                "root_cause=excluded.root_cause, "
                "recommendation=excluded.recommendation, "
                "severity=excluded.severity, "
                "cluster_name=excluded.cluster_name, "
                "namespace=excluded.namespace, "
                "resource_name=excluded.resource_name, "
                "resource_kind=excluded.resource_kind, "
                "pod_status_at_cache_time=excluded.pod_status_at_cache_time, "
                "pod_restart_count_at_cache=excluded.pod_restart_count_at_cache, "
                "tool_name=excluded.tool_name, "
                "created_at=excluded.created_at, "
                "expires_at=excluded.expires_at, "
                "sanitized=excluded.sanitized",
                [
                    result.id,
                    result.cache_key,
                    result.finding_type,
                    result.root_cause,
                    result.recommendation,
                    result.severity,
                    result.cluster_name,
                    result.namespace,
                    result.resource_name,
                    result.resource_kind,
                    result.pod_status_at_cache_time,
                    result.pod_restart_count_at_cache,
                    result.tool_name,
                    result.created_at or datetime.now(UTC),
                    result.expires_at or (datetime.now(UTC) + timedelta(hours=6)),
                    result.sanitized,
                ],
            )
        except Exception as exc:
            logger.warning(
                "Cache set failed for key %s: %s",
                result.cache_key[:16],
                exc,
            )

    def invalidate(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def invalidate_by_resource(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                [cluster, namespace, resource],
            )
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                [cluster, namespace, resource],
            )
            return before
        except Exception:
            logger.warning(
                "Cache invalidate_by_resource failed: %s/%s/%s",
                cluster,
                namespace,
                resource,
            )
            return 0

    def clear(self) -> None:
        try:
            self._conn.execute("DELETE FROM cache_investigations")
        except Exception:
            logger.warning("Cache clear failed")

    def stats(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def _count(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, params or []).fetchone()
            return int(row[0]) if row else 0
        except Exception:
            return 0

    def _row_to_model(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(str(row[14]))
        )
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=UTC)
        return CachedInvestigation(
            id=str(row[0]),
            cache_key=str(row[1]),
            finding_type=str(row[2]),
            root_cause=str(row[3]),
            recommendation=str(row[4]),
            severity=str(row[5]),
            cluster_name=str(row[6]),
            namespace=str(row[7]),
            resource_name=str(row[8]),
            resource_kind=str(row[9]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )
