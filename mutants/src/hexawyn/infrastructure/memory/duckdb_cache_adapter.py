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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__load_sql__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__load_sql__mutmut)
def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


def x__load_sql__mutmut_orig(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


def x__load_sql__mutmut_1(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding=None)


def x__load_sql__mutmut_2(filename: str) -> str:
    return (SQL_DIR * filename).read_text(encoding="utf-8")


def x__load_sql__mutmut_3(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="XXutf-8XX")


def x__load_sql__mutmut_4(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="UTF-8")

mutants_x__load_sql__mutmut['_mutmut_orig'] = x__load_sql__mutmut_orig # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_1'] = x__load_sql__mutmut_1 # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_2'] = x__load_sql__mutmut_2 # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_3'] = x__load_sql__mutmut_3 # type: ignore # mutmut generated
mutants_x__load_sql__mutmut['x__load_sql__mutmut_4'] = x__load_sql__mutmut_4 # type: ignore # mutmut generated


class CacheStatsDict(TypedDict):
    total: int
    expired: int
    valid: int
    invalidated: int
mutants_x_compute_cache_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_cache_key__mutmut)
def compute_cache_key(
    cluster_name: str,
    tool_name: str,
    namespace: str,
    resource_name: str,
    query: str,
) -> str:
    raw = f"{cluster_name}|{tool_name}|{namespace}|{resource_name}|{query}".lower()
    return hashlib.sha256(raw.encode()).hexdigest()


def x_compute_cache_key__mutmut_orig(
    cluster_name: str,
    tool_name: str,
    namespace: str,
    resource_name: str,
    query: str,
) -> str:
    raw = f"{cluster_name}|{tool_name}|{namespace}|{resource_name}|{query}".lower()
    return hashlib.sha256(raw.encode()).hexdigest()


def x_compute_cache_key__mutmut_1(
    cluster_name: str,
    tool_name: str,
    namespace: str,
    resource_name: str,
    query: str,
) -> str:
    raw = None
    return hashlib.sha256(raw.encode()).hexdigest()


def x_compute_cache_key__mutmut_2(
    cluster_name: str,
    tool_name: str,
    namespace: str,
    resource_name: str,
    query: str,
) -> str:
    raw = f"{cluster_name}|{tool_name}|{namespace}|{resource_name}|{query}".upper()
    return hashlib.sha256(raw.encode()).hexdigest()


def x_compute_cache_key__mutmut_3(
    cluster_name: str,
    tool_name: str,
    namespace: str,
    resource_name: str,
    query: str,
) -> str:
    raw = f"{cluster_name}|{tool_name}|{namespace}|{resource_name}|{query}".lower()
    return hashlib.sha256(None).hexdigest()

mutants_x_compute_cache_key__mutmut['_mutmut_orig'] = x_compute_cache_key__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_cache_key__mutmut['x_compute_cache_key__mutmut_1'] = x_compute_cache_key__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_cache_key__mutmut['x_compute_cache_key__mutmut_2'] = x_compute_cache_key__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_cache_key__mutmut['x_compute_cache_key__mutmut_3'] = x_compute_cache_key__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁget__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁset__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁclear__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁstats__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut: MutantDict = {}  # type: ignore


class DuckDBCacheAdapter(CachePort):
    """Investigation cache backed by DuckDB. Lives in ~/.hexawyn/cache.db."""

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁ__init____mutmut)
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

    def xǁDuckDBCacheAdapterǁ__init____mutmut_orig(
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

    def xǁDuckDBCacheAdapterǁ__init____mutmut_1(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" / "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_2(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = None
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" / "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_3(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = None
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" / "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_4(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = True
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" / "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_5(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = None
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_6(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path and str(Path.home() / ".hexawyn" / "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_7(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(None)
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_8(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" * "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_9(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() * ".hexawyn" / "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_10(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / "XX.hexawynXX" / "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_11(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / ".HEXAWYN" / "cache.db")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_12(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" / "XXcache.dbXX")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_13(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" / "CACHE.DB")
            self._conn = duckdb.connect(resolved)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_14(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" / "cache.db")
            self._conn = None
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_15(
        self,
        db_path: str | None = None,
        conn: duckdb.DuckDBPyConnection | None = None,
    ) -> None:
        if conn is not None:
            self._conn = conn
            self._owns_connection = False
        else:
            resolved = db_path or str(Path.home() / ".hexawyn" / "cache.db")
            self._conn = duckdb.connect(None)
            self._owns_connection = True
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_16(
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
            self._owns_connection = None
        self._ensure_schema()

    def xǁDuckDBCacheAdapterǁ__init____mutmut_17(
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
            self._owns_connection = False
        self._ensure_schema()

    def close(self) -> None:
        if self._owns_connection:
            self._conn.close()

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut)
    def _ensure_schema(self) -> None:
        self._conn.execute(_load_sql("cache_schema.sql"))

    def xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_orig(self) -> None:
        self._conn.execute(_load_sql("cache_schema.sql"))

    def xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_1(self) -> None:
        self._conn.execute(None)

    def xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_2(self) -> None:
        self._conn.execute(_load_sql(None))

    def xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_3(self) -> None:
        self._conn.execute(_load_sql("XXcache_schema.sqlXX"))

    def xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_4(self) -> None:
        self._conn.execute(_load_sql("CACHE_SCHEMA.SQL"))

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁget__mutmut)
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

    def xǁDuckDBCacheAdapterǁget__mutmut_orig(self, cache_key: str) -> CachedInvestigation | None:
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

    def xǁDuckDBCacheAdapterǁget__mutmut_1(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = None
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_2(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                None,
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_3(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                None,
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_4(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_5(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_6(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "XXSELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?XX",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_7(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "select * from cache_investigations where cache_key = ? and expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_8(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM CACHE_INVESTIGATIONS WHERE CACHE_KEY = ? AND EXPIRES_AT > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_9(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(None)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_10(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is not None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_11(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(None)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_12(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning(None, cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_13(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", None)
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_14(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning(cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_15(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", )
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_16(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("XXCache get failed for key %sXX", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_17(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("cache get failed for key %s", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_18(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("CACHE GET FAILED FOR KEY %S", cache_key[:16])
            return None

    def xǁDuckDBCacheAdapterǁget__mutmut_19(self, cache_key: str) -> CachedInvestigation | None:
        try:
            row = self._conn.execute(
                "SELECT * FROM cache_investigations WHERE cache_key = ? AND expires_at > ?",
                [cache_key, datetime.now(UTC)],
            ).fetchone()
            if row is None:
                return None
            return self._row_to_model(row)
        except Exception:
            logger.warning("Cache get failed for key %s", cache_key[:17])
            return None

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut)
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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_orig(
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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_1(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = None
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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_2(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(None)
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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_3(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is not None:
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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_4(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(is_valid=None, reason="CACHE_MISS")

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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_5(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(is_valid=False, reason=None)

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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_6(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(reason="CACHE_MISS")

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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_7(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(is_valid=False, )

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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_8(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(is_valid=True, reason="CACHE_MISS")

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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_9(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(is_valid=False, reason="XXCACHE_MISSXX")

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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_10(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(is_valid=False, reason="cache_miss")

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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_11(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(is_valid=False, reason="CACHE_MISS")

        if cached.pod_status_at_cache_time == current_pod_status:
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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_12(
        self,
        cache_key: str,
        current_pod_status: str,
        current_restart_count: int,
    ) -> tuple[CachedInvestigation | None, CacheValidationResult]:
        cached = self.get(cache_key)
        if cached is None:
            return None, CacheValidationResult(is_valid=False, reason="CACHE_MISS")

        if cached.pod_status_at_cache_time != current_pod_status:
            self.invalidate(None)
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

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_13(
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
            reason = None
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if current_restart_count > cached.pod_restart_count_at_cache:
            self.invalidate(cache_key)
            reason = f"RESTART_COUNT_CHANGED: {cached.pod_restart_count_at_cache} → {current_restart_count}"  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_14(
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
            return None, CacheValidationResult(is_valid=None, reason=reason)

        if current_restart_count > cached.pod_restart_count_at_cache:
            self.invalidate(cache_key)
            reason = f"RESTART_COUNT_CHANGED: {cached.pod_restart_count_at_cache} → {current_restart_count}"  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_15(
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
            return None, CacheValidationResult(is_valid=False, reason=None)

        if current_restart_count > cached.pod_restart_count_at_cache:
            self.invalidate(cache_key)
            reason = f"RESTART_COUNT_CHANGED: {cached.pod_restart_count_at_cache} → {current_restart_count}"  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_16(
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
            return None, CacheValidationResult(reason=reason)

        if current_restart_count > cached.pod_restart_count_at_cache:
            self.invalidate(cache_key)
            reason = f"RESTART_COUNT_CHANGED: {cached.pod_restart_count_at_cache} → {current_restart_count}"  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_17(
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
            return None, CacheValidationResult(is_valid=False, )

        if current_restart_count > cached.pod_restart_count_at_cache:
            self.invalidate(cache_key)
            reason = f"RESTART_COUNT_CHANGED: {cached.pod_restart_count_at_cache} → {current_restart_count}"  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_18(
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
            return None, CacheValidationResult(is_valid=True, reason=reason)

        if current_restart_count > cached.pod_restart_count_at_cache:
            self.invalidate(cache_key)
            reason = f"RESTART_COUNT_CHANGED: {cached.pod_restart_count_at_cache} → {current_restart_count}"  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_19(
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

        if current_restart_count >= cached.pod_restart_count_at_cache:
            self.invalidate(cache_key)
            reason = f"RESTART_COUNT_CHANGED: {cached.pod_restart_count_at_cache} → {current_restart_count}"  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_20(
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
            self.invalidate(None)
            reason = f"RESTART_COUNT_CHANGED: {cached.pod_restart_count_at_cache} → {current_restart_count}"  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_21(
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
            reason = None  # noqa: E501
            return None, CacheValidationResult(is_valid=False, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_22(
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
            return None, CacheValidationResult(is_valid=None, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_23(
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
            return None, CacheValidationResult(is_valid=False, reason=None)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_24(
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
            return None, CacheValidationResult(reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_25(
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
            return None, CacheValidationResult(is_valid=False, )

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_26(
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
            return None, CacheValidationResult(is_valid=True, reason=reason)

        if cached.is_expired:
            self.invalidate(cache_key)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_27(
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
            self.invalidate(None)
            return None, CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_28(
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
            return None, CacheValidationResult(is_valid=None, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_29(
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
            return None, CacheValidationResult(is_valid=False, reason=None)

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_30(
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
            return None, CacheValidationResult(reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_31(
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
            return None, CacheValidationResult(is_valid=False, )

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_32(
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
            return None, CacheValidationResult(is_valid=True, reason="TTL_EXPIRED")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_33(
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
            return None, CacheValidationResult(is_valid=False, reason="XXTTL_EXPIREDXX")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_34(
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
            return None, CacheValidationResult(is_valid=False, reason="ttl_expired")

        return cached, CacheValidationResult(is_valid=True, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_35(
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

        return cached, CacheValidationResult(is_valid=None, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_36(
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

        return cached, CacheValidationResult(is_valid=True, reason=None)

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_37(
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

        return cached, CacheValidationResult(reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_38(
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

        return cached, CacheValidationResult(is_valid=True, )

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_39(
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

        return cached, CacheValidationResult(is_valid=False, reason="VALID")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_40(
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

        return cached, CacheValidationResult(is_valid=True, reason="XXVALIDXX")

    def xǁDuckDBCacheAdapterǁget_with_validation__mutmut_41(
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

        return cached, CacheValidationResult(is_valid=True, reason="valid")

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁset__mutmut)
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

    def xǁDuckDBCacheAdapterǁset__mutmut_orig(self, result: CachedInvestigation) -> None:
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

    def xǁDuckDBCacheAdapterǁset__mutmut_1(self, result: CachedInvestigation) -> None:
        if result.id is None and result.id == "":
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

    def xǁDuckDBCacheAdapterǁset__mutmut_2(self, result: CachedInvestigation) -> None:
        if result.id is not None or result.id == "":
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

    def xǁDuckDBCacheAdapterǁset__mutmut_3(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id != "":
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

    def xǁDuckDBCacheAdapterǁset__mutmut_4(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "XXXX":
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

    def xǁDuckDBCacheAdapterǁset__mutmut_5(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = None

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

    def xǁDuckDBCacheAdapterǁset__mutmut_6(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(None)

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

    def xǁDuckDBCacheAdapterǁset__mutmut_7(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                None,
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

    def xǁDuckDBCacheAdapterǁset__mutmut_8(self, result: CachedInvestigation) -> None:
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
                None,
            )
        except Exception as exc:
            logger.warning(
                "Cache set failed for key %s: %s",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_9(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
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

    def xǁDuckDBCacheAdapterǁset__mutmut_10(self, result: CachedInvestigation) -> None:
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
                )
        except Exception as exc:
            logger.warning(
                "Cache set failed for key %s: %s",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_11(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "XXINSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) XX"  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁset__mutmut_12(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "insert into cache_investigations values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁset__mutmut_13(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO CACHE_INVESTIGATIONS VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁset__mutmut_14(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "XXON CONFLICT (id) DO UPDATE SET XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_15(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "on conflict (id) do update set "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_16(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (ID) DO UPDATE SET "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_17(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (id) DO UPDATE SET "
                "XXcache_key=excluded.cache_key, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_18(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (id) DO UPDATE SET "
                "CACHE_KEY=EXCLUDED.CACHE_KEY, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_19(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (id) DO UPDATE SET "
                "cache_key=excluded.cache_key, "
                "XXfinding_type=excluded.finding_type, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_20(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (id) DO UPDATE SET "
                "cache_key=excluded.cache_key, "
                "FINDING_TYPE=EXCLUDED.FINDING_TYPE, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_21(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (id) DO UPDATE SET "
                "cache_key=excluded.cache_key, "
                "finding_type=excluded.finding_type, "
                "XXroot_cause=excluded.root_cause, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_22(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (id) DO UPDATE SET "
                "cache_key=excluded.cache_key, "
                "finding_type=excluded.finding_type, "
                "ROOT_CAUSE=EXCLUDED.ROOT_CAUSE, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_23(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (id) DO UPDATE SET "
                "cache_key=excluded.cache_key, "
                "finding_type=excluded.finding_type, "
                "root_cause=excluded.root_cause, "
                "XXrecommendation=excluded.recommendation, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_24(self, result: CachedInvestigation) -> None:
        if result.id is None or result.id == "":
            result.id = str(uuid.uuid4())

        try:
            self._conn.execute(
                "INSERT INTO cache_investigations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "  # noqa: E501
                "ON CONFLICT (id) DO UPDATE SET "
                "cache_key=excluded.cache_key, "
                "finding_type=excluded.finding_type, "
                "root_cause=excluded.root_cause, "
                "RECOMMENDATION=EXCLUDED.RECOMMENDATION, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_25(self, result: CachedInvestigation) -> None:
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
                "XXseverity=excluded.severity, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_26(self, result: CachedInvestigation) -> None:
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
                "SEVERITY=EXCLUDED.SEVERITY, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_27(self, result: CachedInvestigation) -> None:
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
                "XXcluster_name=excluded.cluster_name, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_28(self, result: CachedInvestigation) -> None:
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
                "CLUSTER_NAME=EXCLUDED.CLUSTER_NAME, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_29(self, result: CachedInvestigation) -> None:
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
                "XXnamespace=excluded.namespace, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_30(self, result: CachedInvestigation) -> None:
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
                "NAMESPACE=EXCLUDED.NAMESPACE, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_31(self, result: CachedInvestigation) -> None:
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
                "XXresource_name=excluded.resource_name, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_32(self, result: CachedInvestigation) -> None:
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
                "RESOURCE_NAME=EXCLUDED.RESOURCE_NAME, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_33(self, result: CachedInvestigation) -> None:
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
                "XXresource_kind=excluded.resource_kind, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_34(self, result: CachedInvestigation) -> None:
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
                "RESOURCE_KIND=EXCLUDED.RESOURCE_KIND, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_35(self, result: CachedInvestigation) -> None:
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
                "XXpod_status_at_cache_time=excluded.pod_status_at_cache_time, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_36(self, result: CachedInvestigation) -> None:
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
                "POD_STATUS_AT_CACHE_TIME=EXCLUDED.POD_STATUS_AT_CACHE_TIME, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_37(self, result: CachedInvestigation) -> None:
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
                "XXpod_restart_count_at_cache=excluded.pod_restart_count_at_cache, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_38(self, result: CachedInvestigation) -> None:
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
                "POD_RESTART_COUNT_AT_CACHE=EXCLUDED.POD_RESTART_COUNT_AT_CACHE, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_39(self, result: CachedInvestigation) -> None:
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
                "XXtool_name=excluded.tool_name, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_40(self, result: CachedInvestigation) -> None:
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
                "TOOL_NAME=EXCLUDED.TOOL_NAME, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_41(self, result: CachedInvestigation) -> None:
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
                "XXcreated_at=excluded.created_at, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_42(self, result: CachedInvestigation) -> None:
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
                "CREATED_AT=EXCLUDED.CREATED_AT, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_43(self, result: CachedInvestigation) -> None:
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
                "XXexpires_at=excluded.expires_at, XX"
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

    def xǁDuckDBCacheAdapterǁset__mutmut_44(self, result: CachedInvestigation) -> None:
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
                "EXPIRES_AT=EXCLUDED.EXPIRES_AT, "
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

    def xǁDuckDBCacheAdapterǁset__mutmut_45(self, result: CachedInvestigation) -> None:
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
                "XXsanitized=excluded.sanitizedXX",
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

    def xǁDuckDBCacheAdapterǁset__mutmut_46(self, result: CachedInvestigation) -> None:
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
                "SANITIZED=EXCLUDED.SANITIZED",
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

    def xǁDuckDBCacheAdapterǁset__mutmut_47(self, result: CachedInvestigation) -> None:
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
                    result.created_at and datetime.now(UTC),
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

    def xǁDuckDBCacheAdapterǁset__mutmut_48(self, result: CachedInvestigation) -> None:
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
                    result.created_at or datetime.now(None),
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

    def xǁDuckDBCacheAdapterǁset__mutmut_49(self, result: CachedInvestigation) -> None:
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
                    result.expires_at and (datetime.now(UTC) + timedelta(hours=6)),
                    result.sanitized,
                ],
            )
        except Exception as exc:
            logger.warning(
                "Cache set failed for key %s: %s",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_50(self, result: CachedInvestigation) -> None:
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
                    result.expires_at or (datetime.now(UTC) - timedelta(hours=6)),
                    result.sanitized,
                ],
            )
        except Exception as exc:
            logger.warning(
                "Cache set failed for key %s: %s",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_51(self, result: CachedInvestigation) -> None:
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
                    result.expires_at or (datetime.now(None) + timedelta(hours=6)),
                    result.sanitized,
                ],
            )
        except Exception as exc:
            logger.warning(
                "Cache set failed for key %s: %s",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_52(self, result: CachedInvestigation) -> None:
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
                    result.expires_at or (datetime.now(UTC) + timedelta(hours=None)),
                    result.sanitized,
                ],
            )
        except Exception as exc:
            logger.warning(
                "Cache set failed for key %s: %s",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_53(self, result: CachedInvestigation) -> None:
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
                    result.expires_at or (datetime.now(UTC) + timedelta(hours=7)),
                    result.sanitized,
                ],
            )
        except Exception as exc:
            logger.warning(
                "Cache set failed for key %s: %s",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_54(self, result: CachedInvestigation) -> None:
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
                None,
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_55(self, result: CachedInvestigation) -> None:
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
                None,
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_56(self, result: CachedInvestigation) -> None:
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
                None,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_57(self, result: CachedInvestigation) -> None:
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
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_58(self, result: CachedInvestigation) -> None:
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
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_59(self, result: CachedInvestigation) -> None:
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
                )

    def xǁDuckDBCacheAdapterǁset__mutmut_60(self, result: CachedInvestigation) -> None:
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
                "XXCache set failed for key %s: %sXX",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_61(self, result: CachedInvestigation) -> None:
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
                "cache set failed for key %s: %s",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_62(self, result: CachedInvestigation) -> None:
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
                "CACHE SET FAILED FOR KEY %S: %S",
                result.cache_key[:16],
                exc,
            )

    def xǁDuckDBCacheAdapterǁset__mutmut_63(self, result: CachedInvestigation) -> None:
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
                result.cache_key[:17],
                exc,
            )

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut)
    def invalidate(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_orig(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_1(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                None,
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_2(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                None,
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_3(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_4(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_5(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "XXDELETE FROM cache_investigations WHERE cache_key = ?XX",
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_6(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "delete from cache_investigations where cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_7(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM CACHE_INVESTIGATIONS WHERE CACHE_KEY = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_8(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning(None, cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_9(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", None)

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_10(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning(cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_11(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", )

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_12(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("XXCache invalidate failed for key %sXX", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_13(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("cache invalidate failed for key %s", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_14(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("CACHE INVALIDATE FAILED FOR KEY %S", cache_key[:16])

    def xǁDuckDBCacheAdapterǁinvalidate__mutmut_15(self, cache_key: str) -> None:
        try:
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cache_key = ?",
                [cache_key],
            )
        except Exception:
            logger.warning("Cache invalidate failed for key %s", cache_key[:17])

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut)
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_orig(self, cluster: str, namespace: str, resource: str) -> int:
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_1(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = None
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_2(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                None,  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_3(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                None,
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_4(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_5(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_6(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "XXSELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?XX",  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_7(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "select count(*) from cache_investigations where cluster_name = ? and namespace = ? and resource_name = ?",  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_8(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM CACHE_INVESTIGATIONS WHERE CLUSTER_NAME = ? AND NAMESPACE = ? AND RESOURCE_NAME = ?",  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_9(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                [cluster, namespace, resource],
            )
            self._conn.execute(
                None,  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_10(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                [cluster, namespace, resource],
            )
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                None,
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_11(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                [cluster, namespace, resource],
            )
            self._conn.execute(
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_12(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                [cluster, namespace, resource],
            )
            self._conn.execute(
                "DELETE FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_13(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                [cluster, namespace, resource],
            )
            self._conn.execute(
                "XXDELETE FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?XX",  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_14(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                [cluster, namespace, resource],
            )
            self._conn.execute(
                "delete from cache_investigations where cluster_name = ? and namespace = ? and resource_name = ?",  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_15(self, cluster: str, namespace: str, resource: str) -> int:
        try:
            before = self._count(
                "SELECT COUNT(*) FROM cache_investigations WHERE cluster_name = ? AND namespace = ? AND resource_name = ?",  # noqa: E501
                [cluster, namespace, resource],
            )
            self._conn.execute(
                "DELETE FROM CACHE_INVESTIGATIONS WHERE CLUSTER_NAME = ? AND NAMESPACE = ? AND RESOURCE_NAME = ?",  # noqa: E501
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

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_16(self, cluster: str, namespace: str, resource: str) -> int:
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
                None,
                cluster,
                namespace,
                resource,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_17(self, cluster: str, namespace: str, resource: str) -> int:
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
                None,
                namespace,
                resource,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_18(self, cluster: str, namespace: str, resource: str) -> int:
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
                None,
                resource,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_19(self, cluster: str, namespace: str, resource: str) -> int:
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
                None,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_20(self, cluster: str, namespace: str, resource: str) -> int:
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
                cluster,
                namespace,
                resource,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_21(self, cluster: str, namespace: str, resource: str) -> int:
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
                namespace,
                resource,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_22(self, cluster: str, namespace: str, resource: str) -> int:
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
                resource,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_23(self, cluster: str, namespace: str, resource: str) -> int:
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
                )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_24(self, cluster: str, namespace: str, resource: str) -> int:
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
                "XXCache invalidate_by_resource failed: %s/%s/%sXX",
                cluster,
                namespace,
                resource,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_25(self, cluster: str, namespace: str, resource: str) -> int:
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
                "cache invalidate_by_resource failed: %s/%s/%s",
                cluster,
                namespace,
                resource,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_26(self, cluster: str, namespace: str, resource: str) -> int:
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
                "CACHE INVALIDATE_BY_RESOURCE FAILED: %S/%S/%S",
                cluster,
                namespace,
                resource,
            )
            return 0

    def xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_27(self, cluster: str, namespace: str, resource: str) -> int:
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
            return 1

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁclear__mutmut)
    def clear(self) -> None:
        try:
            self._conn.execute("DELETE FROM cache_investigations")
        except Exception:
            logger.warning("Cache clear failed")

    def xǁDuckDBCacheAdapterǁclear__mutmut_orig(self) -> None:
        try:
            self._conn.execute("DELETE FROM cache_investigations")
        except Exception:
            logger.warning("Cache clear failed")

    def xǁDuckDBCacheAdapterǁclear__mutmut_1(self) -> None:
        try:
            self._conn.execute(None)
        except Exception:
            logger.warning("Cache clear failed")

    def xǁDuckDBCacheAdapterǁclear__mutmut_2(self) -> None:
        try:
            self._conn.execute("XXDELETE FROM cache_investigationsXX")
        except Exception:
            logger.warning("Cache clear failed")

    def xǁDuckDBCacheAdapterǁclear__mutmut_3(self) -> None:
        try:
            self._conn.execute("delete from cache_investigations")
        except Exception:
            logger.warning("Cache clear failed")

    def xǁDuckDBCacheAdapterǁclear__mutmut_4(self) -> None:
        try:
            self._conn.execute("DELETE FROM CACHE_INVESTIGATIONS")
        except Exception:
            logger.warning("Cache clear failed")

    def xǁDuckDBCacheAdapterǁclear__mutmut_5(self) -> None:
        try:
            self._conn.execute("DELETE FROM cache_investigations")
        except Exception:
            logger.warning(None)

    def xǁDuckDBCacheAdapterǁclear__mutmut_6(self) -> None:
        try:
            self._conn.execute("DELETE FROM cache_investigations")
        except Exception:
            logger.warning("XXCache clear failedXX")

    def xǁDuckDBCacheAdapterǁclear__mutmut_7(self) -> None:
        try:
            self._conn.execute("DELETE FROM cache_investigations")
        except Exception:
            logger.warning("cache clear failed")

    def xǁDuckDBCacheAdapterǁclear__mutmut_8(self) -> None:
        try:
            self._conn.execute("DELETE FROM cache_investigations")
        except Exception:
            logger.warning("CACHE CLEAR FAILED")

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁstats__mutmut)
    def stats(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_orig(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_1(self) -> CacheStatsDict:  # type: ignore[override]
        now = None
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_2(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(None)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_3(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = None
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_4(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count(None)
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_5(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("XXSELECT COUNT(*) FROM cache_investigationsXX")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_6(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("select count(*) from cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_7(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM CACHE_INVESTIGATIONS")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_8(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = None
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_9(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            None, [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_10(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", None
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_11(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_12(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_13(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "XXSELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?XX", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_14(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "select count(*) from cache_investigations where expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_15(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM CACHE_INVESTIGATIONS WHERE EXPIRES_AT <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_16(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = None
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_17(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total + expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_18(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=None, expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_19(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=None, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_20(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=None, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_21(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=None)

    def xǁDuckDBCacheAdapterǁstats__mutmut_22(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(expired=expired, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_23(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, valid=valid, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_24(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, invalidated=0)

    def xǁDuckDBCacheAdapterǁstats__mutmut_25(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, )

    def xǁDuckDBCacheAdapterǁstats__mutmut_26(self) -> CacheStatsDict:  # type: ignore[override]
        now = datetime.now(UTC)
        total = self._count("SELECT COUNT(*) FROM cache_investigations")
        expired = self._count(
            "SELECT COUNT(*) FROM cache_investigations WHERE expires_at <= ?", [now]
        )
        valid = total - expired
        return CacheStatsDict(total=total, expired=expired, valid=valid, invalidated=1)

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁ_count__mutmut)
    def _count(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, params or []).fetchone()
            return int(row[0]) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_orig(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, params or []).fetchone()
            return int(row[0]) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_1(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = None
            return int(row[0]) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_2(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(None, params or []).fetchone()
            return int(row[0]) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_3(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, None).fetchone()
            return int(row[0]) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_4(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(params or []).fetchone()
            return int(row[0]) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_5(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, ).fetchone()
            return int(row[0]) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_6(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, params and []).fetchone()
            return int(row[0]) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_7(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, params or []).fetchone()
            return int(None) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_8(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, params or []).fetchone()
            return int(row[1]) if row else 0
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_9(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, params or []).fetchone()
            return int(row[0]) if row else 1
        except Exception:
            return 0

    def xǁDuckDBCacheAdapterǁ_count__mutmut_10(self, query: str, params: list[object] | None = None) -> int:
        try:
            row = self._conn.execute(query, params or []).fetchone()
            return int(row[0]) if row else 0
        except Exception:
            return 1

    @_mutmut_mutated(mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut)
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_orig(self, row: tuple[object, ...]) -> CachedInvestigation:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_1(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = None
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_2(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[14] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_3(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(None)
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_4(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(None))
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_5(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[14]))
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_6(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = None
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_7(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[15] if isinstance(row[14], datetime) else datetime.fromisoformat(str(row[14]))
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_8(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(None)
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_9(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(str(None))
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_10(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(str(row[15]))
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_11(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(str(row[14]))
        )
        if created_at.tzinfo is not None:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_12(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(str(row[14]))
        )
        if created_at.tzinfo is None:
            created_at = None
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_13(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(str(row[14]))
        )
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=None)
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_14(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(str(row[14]))
        )
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        if expires_at.tzinfo is not None:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_15(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(str(row[14]))
        )
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        if expires_at.tzinfo is None:
            expires_at = None
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_16(self, row: tuple[object, ...]) -> CachedInvestigation:
        created_at = (
            row[13] if isinstance(row[13], datetime) else datetime.fromisoformat(str(row[13]))
        )
        expires_at = (
            row[14] if isinstance(row[14], datetime) else datetime.fromisoformat(str(row[14]))
        )
        if created_at.tzinfo is None:
            created_at = created_at.replace(tzinfo=UTC)
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=None)
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_17(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            id=None,
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_18(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            cache_key=None,
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_19(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            finding_type=None,
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_20(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            root_cause=None,
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_21(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            recommendation=None,
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_22(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            severity=None,
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_23(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            cluster_name=None,
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_24(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            namespace=None,
            resource_name=str(row[8]),
            resource_kind=str(row[9]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_25(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            resource_name=None,
            resource_kind=str(row[9]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_26(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            resource_kind=None,
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_27(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            pod_status_at_cache_time=None,
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_28(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            pod_restart_count_at_cache=None,  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_29(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            tool_name=None,
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_30(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            created_at=None,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_31(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            expires_at=None,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_32(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            sanitized=None,
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_33(self, row: tuple[object, ...]) -> CachedInvestigation:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_34(self, row: tuple[object, ...]) -> CachedInvestigation:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_35(self, row: tuple[object, ...]) -> CachedInvestigation:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_36(self, row: tuple[object, ...]) -> CachedInvestigation:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_37(self, row: tuple[object, ...]) -> CachedInvestigation:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_38(self, row: tuple[object, ...]) -> CachedInvestigation:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_39(self, row: tuple[object, ...]) -> CachedInvestigation:
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_40(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            resource_name=str(row[8]),
            resource_kind=str(row[9]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_41(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            resource_kind=str(row[9]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_42(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_43(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_44(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_45(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_46(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_47(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_48(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_49(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            id=str(None),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_50(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            id=str(row[1]),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_51(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            cache_key=str(None),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_52(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            cache_key=str(row[2]),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_53(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            finding_type=str(None),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_54(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            finding_type=str(row[3]),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_55(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            root_cause=str(None),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_56(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            root_cause=str(row[4]),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_57(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            recommendation=str(None),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_58(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            recommendation=str(row[5]),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_59(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            severity=str(None),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_60(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            severity=str(row[6]),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_61(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            cluster_name=str(None),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_62(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            cluster_name=str(row[7]),
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

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_63(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            namespace=str(None),
            resource_name=str(row[8]),
            resource_kind=str(row[9]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_64(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            namespace=str(row[8]),
            resource_name=str(row[8]),
            resource_kind=str(row[9]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_65(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            resource_name=str(None),
            resource_kind=str(row[9]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_66(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            resource_name=str(row[9]),
            resource_kind=str(row[9]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_67(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            resource_kind=str(None),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_68(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            resource_kind=str(row[10]),
            pod_status_at_cache_time=str(row[10]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_69(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            pod_status_at_cache_time=str(None),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_70(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            pod_status_at_cache_time=str(row[11]),
            pod_restart_count_at_cache=int(row[11]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_71(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            pod_restart_count_at_cache=int(None),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_72(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            pod_restart_count_at_cache=int(row[12]),  # type: ignore[call-overload]
            tool_name=str(row[12]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_73(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            tool_name=str(None),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_74(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            tool_name=str(row[13]),
            created_at=created_at,
            expires_at=expires_at,
            sanitized=bool(row[15]),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_75(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            sanitized=bool(None),
        )

    def xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_76(self, row: tuple[object, ...]) -> CachedInvestigation:
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
            sanitized=bool(row[16]),
        )

mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_9'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_10'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_11'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_12'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_13'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_14'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_15'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_16'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ__init____mutmut['xǁDuckDBCacheAdapterǁ__init____mutmut_17'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ__init____mutmut_17 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut['xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut['xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut['xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut['xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_ensure_schema__mutmut_4 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁget__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_9'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_10'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_11'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_12'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_13'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_14'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_15'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_16'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_17'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_18'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget__mutmut['xǁDuckDBCacheAdapterǁget__mutmut_19'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget__mutmut_19 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_9'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_10'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_11'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_12'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_13'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_14'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_15'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_16'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_17'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_18'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_19'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_20'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_21'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_22'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_23'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_24'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_25'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_26'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_27'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_28'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_29'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_30'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_31'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_32'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_33'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_34'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_35'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_36'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_37'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_38'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_39'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_40'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁget_with_validation__mutmut['xǁDuckDBCacheAdapterǁget_with_validation__mutmut_41'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁget_with_validation__mutmut_41 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁset__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_9'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_10'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_11'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_12'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_13'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_14'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_15'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_16'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_17'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_18'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_19'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_20'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_21'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_22'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_23'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_24'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_25'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_26'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_27'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_28'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_29'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_30'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_31'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_32'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_33'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_34'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_35'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_36'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_37'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_38'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_39'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_40'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_41'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_42'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_43'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_44'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_45'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_46'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_47'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_48'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_49'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_50'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_51'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_52'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_53'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_54'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_55'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_56'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_57'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_57 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_58'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_58 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_59'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_59 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_60'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_60 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_61'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_61 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_62'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_62 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁset__mutmut['xǁDuckDBCacheAdapterǁset__mutmut_63'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁset__mutmut_63 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_9'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_10'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_11'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_12'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_13'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_14'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate__mutmut['xǁDuckDBCacheAdapterǁinvalidate__mutmut_15'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate__mutmut_15 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_9'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_10'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_11'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_12'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_13'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_14'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_15'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_16'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_17'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_18'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_19'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_20'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_21'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_22'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_23'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_24'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_25'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_26'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut['xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_27'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁinvalidate_by_resource__mutmut_27 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁclear__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁclear__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁclear__mutmut['xǁDuckDBCacheAdapterǁclear__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁclear__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁclear__mutmut['xǁDuckDBCacheAdapterǁclear__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁclear__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁclear__mutmut['xǁDuckDBCacheAdapterǁclear__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁclear__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁclear__mutmut['xǁDuckDBCacheAdapterǁclear__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁclear__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁclear__mutmut['xǁDuckDBCacheAdapterǁclear__mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁclear__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁclear__mutmut['xǁDuckDBCacheAdapterǁclear__mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁclear__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁclear__mutmut['xǁDuckDBCacheAdapterǁclear__mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁclear__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁclear__mutmut['xǁDuckDBCacheAdapterǁclear__mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁclear__mutmut_8 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁstats__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_9'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_10'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_11'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_12'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_13'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_14'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_15'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_16'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_17'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_18'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_19'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_20'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_21'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_22'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_23'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_24'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_25'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁstats__mutmut['xǁDuckDBCacheAdapterǁstats__mutmut_26'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁstats__mutmut_26 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_9'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_count__mutmut['xǁDuckDBCacheAdapterǁ_count__mutmut_10'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_count__mutmut_10 # type: ignore # mutmut generated

mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['_mutmut_orig'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_1'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_2'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_3'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_4'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_5'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_6'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_7'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_8'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_9'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_10'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_11'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_12'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_13'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_14'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_15'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_16'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_17'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_18'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_19'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_20'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_21'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_22'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_23'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_24'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_25'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_26'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_27'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_28'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_29'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_30'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_31'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_32'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_33'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_34'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_35'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_35 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_36'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_36 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_37'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_37 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_38'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_38 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_39'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_39 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_40'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_40 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_41'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_41 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_42'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_42 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_43'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_43 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_44'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_44 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_45'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_45 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_46'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_46 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_47'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_47 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_48'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_48 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_49'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_49 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_50'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_50 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_51'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_51 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_52'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_52 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_53'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_53 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_54'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_54 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_55'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_55 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_56'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_56 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_57'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_57 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_58'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_58 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_59'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_59 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_60'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_60 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_61'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_61 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_62'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_62 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_63'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_63 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_64'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_64 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_65'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_65 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_66'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_66 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_67'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_67 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_68'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_68 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_69'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_69 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_70'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_70 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_71'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_71 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_72'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_72 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_73'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_73 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_74'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_74 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_75'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_75 # type: ignore # mutmut generated
mutants_xǁDuckDBCacheAdapterǁ_row_to_model__mutmut['xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_76'] = DuckDBCacheAdapter.xǁDuckDBCacheAdapterǁ_row_to_model__mutmut_76 # type: ignore # mutmut generated
