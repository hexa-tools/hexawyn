import datetime
import threading
from pathlib import Path
from typing import TypedDict

import duckdb

from hexawyn.domain.errors import DuckDBUnavailableError, EncryptionError
from hexawyn.domain.models.quota import UNLIMITED
from hexawyn.infrastructure.memory.encryption import (
    derive_key,
    is_encryption_disabled,
    prepare_db,
)

SQL_DIR = Path(__file__).parent / "sql"

_DB_SIZE_WARNING_THRESHOLD: int = 1_073_741_824


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


class SimilarInvestigationDict(TypedDict):
    id: str
    timestamp: str
    age_days: int
    cluster_name: str
    namespace: str | None
    tool_name: str
    resource_name: str | None
    resource_kind: str | None
    cause: str | None
    solution: str | None
    severity: str
    weight: float
    score: float


HEXAWYN_DIR = Path.home() / ".hexawyn"
DB_PATH = HEXAWYN_DIR / "memory.duckdb"

_conn_lock = threading.RLock()
_singleton_conn: duckdb.DuckDBPyConnection | None = None
_singleton_init_done = False
mutants_x_reset_connection_state__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_reset_connection_state__mutmut)
def reset_connection_state() -> None:
    """Drop the cached connection so a fresh one is created (test isolation)."""
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        _singleton_conn = None
        _singleton_init_done = False


def x_reset_connection_state__mutmut_orig() -> None:
    """Drop the cached connection so a fresh one is created (test isolation)."""
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        _singleton_conn = None
        _singleton_init_done = False


def x_reset_connection_state__mutmut_1() -> None:
    """Drop the cached connection so a fresh one is created (test isolation)."""
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        _singleton_conn = ""
        _singleton_init_done = False


def x_reset_connection_state__mutmut_2() -> None:
    """Drop the cached connection so a fresh one is created (test isolation)."""
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        _singleton_conn = None
        _singleton_init_done = None


def x_reset_connection_state__mutmut_3() -> None:
    """Drop the cached connection so a fresh one is created (test isolation)."""
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        _singleton_conn = None
        _singleton_init_done = True

mutants_x_reset_connection_state__mutmut['_mutmut_orig'] = x_reset_connection_state__mutmut_orig # type: ignore # mutmut generated
mutants_x_reset_connection_state__mutmut['x_reset_connection_state__mutmut_1'] = x_reset_connection_state__mutmut_1 # type: ignore # mutmut generated
mutants_x_reset_connection_state__mutmut['x_reset_connection_state__mutmut_2'] = x_reset_connection_state__mutmut_2 # type: ignore # mutmut generated
mutants_x_reset_connection_state__mutmut['x_reset_connection_state__mutmut_3'] = x_reset_connection_state__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_connection__mutmut)
def get_connection() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_orig() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_1() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_2() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=None, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_3() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=None)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_4() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_5() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, )

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_6() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=False, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_7() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=False)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_8() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_9() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = None
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_10() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(None)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_11() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = None

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_12() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(None)

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_13() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(None))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_14() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute(None)
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_15() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("XXINSTALL vss;XX")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_16() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("install vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_17() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL VSS;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_18() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute(None)

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_19() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("XXLOAD vss;XX")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_20() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("load vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_21() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD VSS;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_22() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(None)

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_23() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql(None))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_24() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("XXschema.sqlXX"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_25() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("SCHEMA.SQL"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_26() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute(None)

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_27() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("XXSET hnsw_enable_experimental_persistence = true;XX")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_28() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("set hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_29() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET HNSW_ENABLE_EXPERIMENTAL_PERSISTENCE = TRUE;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_30() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(None)

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_31() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql(None))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_32() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("XXindexes.sqlXX"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_33() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("INDEXES.SQL"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_34() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = None
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_35() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = None
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_36() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = False
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_37() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                None,
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_38() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context=None,
            ) from e


def x_get_connection__mutmut_39() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                context={"path": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_40() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                ) from e


def x_get_connection__mutmut_41() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"XXpathXX": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_42() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"PATH": str(DB_PATH), "error": str(e)},
            ) from e


def x_get_connection__mutmut_43() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(None), "error": str(e)},
            ) from e


def x_get_connection__mutmut_44() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "XXerrorXX": str(e)},
            ) from e


def x_get_connection__mutmut_45() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "ERROR": str(e)},
            ) from e


def x_get_connection__mutmut_46() -> duckdb.DuckDBPyConnection:
    """
    Initialize DuckDB, install VSS, create schema, create HNSW index.
    Called once at startup by the MCP server and CLI.

    Database encryption is enabled by default. The AES-256-GCM encryption key
    is derived from the installation's machine identity (via get_machine_id)
    using PBKDF2-HMAC-SHA256 with 600k iterations. It is stable across
    kubeconfig / context / cluster changes.

    The DB file at ~/.hexawyn/memory.duckdb.enc is encrypted at rest.
    During the application lifetime, the decrypted memory.duckdb is used.
    On clean shutdown (atexit), the file is re-encrypted and the plaintext
    copy is deleted. An undecryptable .enc (e.g. from a previous key scheme)
    is quarantined and a fresh database is created instead of failing.

    Set HEXAWYN_DISABLE_ENCRYPTION=true to skip encryption (demo/testing only).

    A single connection is shared across callers (thread-safe) so concurrent
    startup work never opens multiple writers on the same DuckDB file, which
    would raise a lock conflict.

    Raises:
        EncryptionError: if the wrong kubeconfig is used (key mismatch).
        DuckDBUnavailableError: if DuckDB fails to initialize.
    """
    global _singleton_conn, _singleton_init_done
    with _conn_lock:
        if _singleton_conn is not None:
            return _singleton_conn
        try:
            HEXAWYN_DIR.mkdir(parents=True, exist_ok=True)

            if not is_encryption_disabled():
                key = derive_key()
                prepare_db(key)

            conn = duckdb.connect(str(DB_PATH))

            conn.execute("INSTALL vss;")
            conn.execute("LOAD vss;")

            conn.execute(_load_sql("schema.sql"))

            conn.execute("SET hnsw_enable_experimental_persistence = true;")

            conn.execute(_load_sql("indexes.sql"))

            _singleton_conn = conn
            _singleton_init_done = True
            return conn
        except EncryptionError:
            raise
        except Exception as e:
            raise DuckDBUnavailableError(
                f"Failed to initialize DuckDB at {DB_PATH}: {e}",
                context={"path": str(DB_PATH), "error": str(None)},
            ) from e

mutants_x_get_connection__mutmut['_mutmut_orig'] = x_get_connection__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_1'] = x_get_connection__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_2'] = x_get_connection__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_3'] = x_get_connection__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_4'] = x_get_connection__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_5'] = x_get_connection__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_6'] = x_get_connection__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_7'] = x_get_connection__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_8'] = x_get_connection__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_9'] = x_get_connection__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_10'] = x_get_connection__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_11'] = x_get_connection__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_12'] = x_get_connection__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_13'] = x_get_connection__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_14'] = x_get_connection__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_15'] = x_get_connection__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_16'] = x_get_connection__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_17'] = x_get_connection__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_18'] = x_get_connection__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_19'] = x_get_connection__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_20'] = x_get_connection__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_21'] = x_get_connection__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_22'] = x_get_connection__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_23'] = x_get_connection__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_24'] = x_get_connection__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_25'] = x_get_connection__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_26'] = x_get_connection__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_27'] = x_get_connection__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_28'] = x_get_connection__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_29'] = x_get_connection__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_30'] = x_get_connection__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_31'] = x_get_connection__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_32'] = x_get_connection__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_33'] = x_get_connection__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_34'] = x_get_connection__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_35'] = x_get_connection__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_36'] = x_get_connection__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_37'] = x_get_connection__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_38'] = x_get_connection__mutmut_38 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_39'] = x_get_connection__mutmut_39 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_40'] = x_get_connection__mutmut_40 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_41'] = x_get_connection__mutmut_41 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_42'] = x_get_connection__mutmut_42 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_43'] = x_get_connection__mutmut_43 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_44'] = x_get_connection__mutmut_44 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_45'] = x_get_connection__mutmut_45 # type: ignore # mutmut generated
mutants_x_get_connection__mutmut['x_get_connection__mutmut_46'] = x_get_connection__mutmut_46 # type: ignore # mutmut generated


_UNLIMITED_HISTORY_DAYS = 36500  # 100 years — effectively no date filter
mutants_x_search_similar__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_search_similar__mutmut)
def search_similar(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_orig(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_1(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 6,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_2(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 1.8,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_3(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = None

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_4(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days != UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_5(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = None
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_6(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = None

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_7(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace(None, f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_8(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", None)

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_9(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace(f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_10(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", )

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_11(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql(None).replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_12(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("XXsearch_similar.sqlXX").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_13(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("SEARCH_SIMILAR.SQL").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_14(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("XXFLOAT[?]XX", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_15(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("float[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_16(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = None

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_17(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_18(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = None
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_19(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace(None, "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_20(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", None)
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_21(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_22(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", )
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_23(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("XXAND sanitized = falseXX", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_24(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("and sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_25(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND SANITIZED = FALSE", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_26(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "XXAND namespace = ?\n  AND sanitized = falseXX")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_27(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "and namespace = ?\n  and sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_28(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND NAMESPACE = ?\n  AND SANITIZED = FALSE")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_29(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(None)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_30(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_31(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = None
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_32(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace(None, "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_33(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", None)
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_34(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_35(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", )
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_36(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("XXAND sanitized = falseXX", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_37(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("and sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_38(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND SANITIZED = FALSE", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_39(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "XXAND resource_name = ?\n  AND sanitized = falseXX")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_40(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "and resource_name = ?\n  and sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_41(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND RESOURCE_NAME = ?\n  AND SANITIZED = FALSE")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_42(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(None)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_43(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(None)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_44(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = None

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_45(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(None, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_46(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, None).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_47(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_48(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, ).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_49(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = None
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_50(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None or row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_51(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[13] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_52(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_53(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[13] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_54(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] > min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_55(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                None
            )
    return output


def x_search_similar__mutmut_56(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=None,
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_57(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=None,
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_58(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=None,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_59(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=None,
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_60(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_61(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_62(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_63(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=None,
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_64(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_65(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_66(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=None,
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_67(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=None,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_68(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=None,
                )
            )
    return output


def x_search_similar__mutmut_69(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_70(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_71(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_72(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_73(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_74(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_75(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_76(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_77(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_78(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_79(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_80(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_81(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    )
            )
    return output


def x_search_similar__mutmut_82(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(None),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_83(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[1]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_84(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(None) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_85(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[2]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_86(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[2] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_87(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "XXXX",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_88(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(None) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_89(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[3]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_90(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[3] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_91(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_92(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 1,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_93(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(None) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_94(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[4]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_95(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[4] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_96(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "XXXX",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_97(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(None) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_98(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[5]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_99(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[5] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_100(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(None) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_101(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[6]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_102(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[6] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_103(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(None) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_104(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[7]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_105(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[7] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_106(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(None) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_107(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[8]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_108(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[8] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_109(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "XXXX",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_110(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(None) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_111(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[9]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_112(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[9] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_113(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(None) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_114(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[10]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_115(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[10] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_116(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(None) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_117(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[11]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_118(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[11] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_119(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "XXlowXX",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_120(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "LOW",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_121(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(None) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_122(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[12]) if row[11] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_123(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[12] else 1.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_124(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 2.0,
                    score=float(row[12]),
                )
            )
    return output


def x_search_similar__mutmut_125(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(None),
                )
            )
    return output


def x_search_similar__mutmut_126(  # noqa: PLR0913
    conn: duckdb.DuckDBPyConnection,
    embedding: list[float],
    cluster_name: str,
    history_days: int = UNLIMITED,
    namespace: str | None = None,
    resource_name: str | None = None,
    limit: int = 5,
    min_score: float = 0.80,
) -> list[SimilarInvestigationDict]:
    """
    VSS search with a history window.

    Neutral by design: no hardcoded tiered retention figure. ``UNLIMITED``
    (``-1``) uses the 36500-days proxy (no effective filter).

    Uses HNSW index for fast approximate nearest neighbor search.
    Explicit columns only — no wildcard select (enforced by hexa_guard.py R8).
    """
    effective_days = _UNLIMITED_HISTORY_DAYS if history_days == UNLIMITED else history_days

    embedding_dim = len(embedding)
    sql = _load_sql("search_similar.sql").replace("FLOAT[?]", f"FLOAT[{embedding_dim}]")

    params: list[str | int | float | list[float] | None] = [
        embedding,
        cluster_name,
        effective_days,
    ]

    if namespace is not None:
        sql = sql.replace("AND sanitized = false", "AND namespace = ?\n  AND sanitized = false")
        params.append(namespace)

    if resource_name is not None:
        sql = sql.replace("AND sanitized = false", "AND resource_name = ?\n  AND sanitized = false")
        params.append(resource_name)

    params.append(limit)

    results = conn.execute(sql, params).fetchall()

    output: list[SimilarInvestigationDict] = []
    for row in results:
        if row[12] is not None and row[12] >= min_score:
            output.append(
                SimilarInvestigationDict(
                    id=str(row[0]),
                    timestamp=str(row[1]) if row[1] else "",
                    age_days=int(row[2]) if row[2] is not None else 0,
                    cluster_name=str(row[3]) if row[3] else "",
                    namespace=str(row[4]) if row[4] else None,
                    resource_name=str(row[5]) if row[5] else None,
                    resource_kind=str(row[6]) if row[6] else None,
                    tool_name=str(row[7]) if row[7] else "",
                    cause=str(row[8]) if row[8] else None,
                    solution=str(row[9]) if row[9] else None,
                    severity=str(row[10]) if row[10] else "low",
                    weight=float(row[11]) if row[11] else 1.0,
                    score=float(row[13]),
                )
            )
    return output

mutants_x_search_similar__mutmut['_mutmut_orig'] = x_search_similar__mutmut_orig # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_1'] = x_search_similar__mutmut_1 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_2'] = x_search_similar__mutmut_2 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_3'] = x_search_similar__mutmut_3 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_4'] = x_search_similar__mutmut_4 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_5'] = x_search_similar__mutmut_5 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_6'] = x_search_similar__mutmut_6 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_7'] = x_search_similar__mutmut_7 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_8'] = x_search_similar__mutmut_8 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_9'] = x_search_similar__mutmut_9 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_10'] = x_search_similar__mutmut_10 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_11'] = x_search_similar__mutmut_11 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_12'] = x_search_similar__mutmut_12 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_13'] = x_search_similar__mutmut_13 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_14'] = x_search_similar__mutmut_14 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_15'] = x_search_similar__mutmut_15 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_16'] = x_search_similar__mutmut_16 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_17'] = x_search_similar__mutmut_17 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_18'] = x_search_similar__mutmut_18 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_19'] = x_search_similar__mutmut_19 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_20'] = x_search_similar__mutmut_20 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_21'] = x_search_similar__mutmut_21 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_22'] = x_search_similar__mutmut_22 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_23'] = x_search_similar__mutmut_23 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_24'] = x_search_similar__mutmut_24 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_25'] = x_search_similar__mutmut_25 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_26'] = x_search_similar__mutmut_26 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_27'] = x_search_similar__mutmut_27 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_28'] = x_search_similar__mutmut_28 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_29'] = x_search_similar__mutmut_29 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_30'] = x_search_similar__mutmut_30 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_31'] = x_search_similar__mutmut_31 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_32'] = x_search_similar__mutmut_32 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_33'] = x_search_similar__mutmut_33 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_34'] = x_search_similar__mutmut_34 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_35'] = x_search_similar__mutmut_35 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_36'] = x_search_similar__mutmut_36 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_37'] = x_search_similar__mutmut_37 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_38'] = x_search_similar__mutmut_38 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_39'] = x_search_similar__mutmut_39 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_40'] = x_search_similar__mutmut_40 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_41'] = x_search_similar__mutmut_41 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_42'] = x_search_similar__mutmut_42 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_43'] = x_search_similar__mutmut_43 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_44'] = x_search_similar__mutmut_44 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_45'] = x_search_similar__mutmut_45 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_46'] = x_search_similar__mutmut_46 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_47'] = x_search_similar__mutmut_47 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_48'] = x_search_similar__mutmut_48 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_49'] = x_search_similar__mutmut_49 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_50'] = x_search_similar__mutmut_50 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_51'] = x_search_similar__mutmut_51 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_52'] = x_search_similar__mutmut_52 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_53'] = x_search_similar__mutmut_53 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_54'] = x_search_similar__mutmut_54 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_55'] = x_search_similar__mutmut_55 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_56'] = x_search_similar__mutmut_56 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_57'] = x_search_similar__mutmut_57 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_58'] = x_search_similar__mutmut_58 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_59'] = x_search_similar__mutmut_59 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_60'] = x_search_similar__mutmut_60 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_61'] = x_search_similar__mutmut_61 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_62'] = x_search_similar__mutmut_62 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_63'] = x_search_similar__mutmut_63 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_64'] = x_search_similar__mutmut_64 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_65'] = x_search_similar__mutmut_65 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_66'] = x_search_similar__mutmut_66 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_67'] = x_search_similar__mutmut_67 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_68'] = x_search_similar__mutmut_68 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_69'] = x_search_similar__mutmut_69 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_70'] = x_search_similar__mutmut_70 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_71'] = x_search_similar__mutmut_71 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_72'] = x_search_similar__mutmut_72 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_73'] = x_search_similar__mutmut_73 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_74'] = x_search_similar__mutmut_74 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_75'] = x_search_similar__mutmut_75 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_76'] = x_search_similar__mutmut_76 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_77'] = x_search_similar__mutmut_77 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_78'] = x_search_similar__mutmut_78 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_79'] = x_search_similar__mutmut_79 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_80'] = x_search_similar__mutmut_80 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_81'] = x_search_similar__mutmut_81 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_82'] = x_search_similar__mutmut_82 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_83'] = x_search_similar__mutmut_83 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_84'] = x_search_similar__mutmut_84 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_85'] = x_search_similar__mutmut_85 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_86'] = x_search_similar__mutmut_86 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_87'] = x_search_similar__mutmut_87 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_88'] = x_search_similar__mutmut_88 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_89'] = x_search_similar__mutmut_89 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_90'] = x_search_similar__mutmut_90 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_91'] = x_search_similar__mutmut_91 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_92'] = x_search_similar__mutmut_92 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_93'] = x_search_similar__mutmut_93 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_94'] = x_search_similar__mutmut_94 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_95'] = x_search_similar__mutmut_95 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_96'] = x_search_similar__mutmut_96 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_97'] = x_search_similar__mutmut_97 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_98'] = x_search_similar__mutmut_98 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_99'] = x_search_similar__mutmut_99 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_100'] = x_search_similar__mutmut_100 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_101'] = x_search_similar__mutmut_101 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_102'] = x_search_similar__mutmut_102 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_103'] = x_search_similar__mutmut_103 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_104'] = x_search_similar__mutmut_104 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_105'] = x_search_similar__mutmut_105 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_106'] = x_search_similar__mutmut_106 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_107'] = x_search_similar__mutmut_107 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_108'] = x_search_similar__mutmut_108 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_109'] = x_search_similar__mutmut_109 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_110'] = x_search_similar__mutmut_110 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_111'] = x_search_similar__mutmut_111 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_112'] = x_search_similar__mutmut_112 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_113'] = x_search_similar__mutmut_113 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_114'] = x_search_similar__mutmut_114 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_115'] = x_search_similar__mutmut_115 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_116'] = x_search_similar__mutmut_116 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_117'] = x_search_similar__mutmut_117 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_118'] = x_search_similar__mutmut_118 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_119'] = x_search_similar__mutmut_119 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_120'] = x_search_similar__mutmut_120 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_121'] = x_search_similar__mutmut_121 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_122'] = x_search_similar__mutmut_122 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_123'] = x_search_similar__mutmut_123 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_124'] = x_search_similar__mutmut_124 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_125'] = x_search_similar__mutmut_125 # type: ignore # mutmut generated
mutants_x_search_similar__mutmut['x_search_similar__mutmut_126'] = x_search_similar__mutmut_126 # type: ignore # mutmut generated
mutants_x_get_db_size_bytes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_db_size_bytes__mutmut)
def get_db_size_bytes(db_path: Path | None = None) -> int:
    target = db_path if db_path is not None else DB_PATH
    if not target.exists():
        return 0
    return target.stat().st_size


def x_get_db_size_bytes__mutmut_orig(db_path: Path | None = None) -> int:
    target = db_path if db_path is not None else DB_PATH
    if not target.exists():
        return 0
    return target.stat().st_size


def x_get_db_size_bytes__mutmut_1(db_path: Path | None = None) -> int:
    target = None
    if not target.exists():
        return 0
    return target.stat().st_size


def x_get_db_size_bytes__mutmut_2(db_path: Path | None = None) -> int:
    target = db_path if db_path is None else DB_PATH
    if not target.exists():
        return 0
    return target.stat().st_size


def x_get_db_size_bytes__mutmut_3(db_path: Path | None = None) -> int:
    target = db_path if db_path is not None else DB_PATH
    if target.exists():
        return 0
    return target.stat().st_size


def x_get_db_size_bytes__mutmut_4(db_path: Path | None = None) -> int:
    target = db_path if db_path is not None else DB_PATH
    if not target.exists():
        return 1
    return target.stat().st_size

mutants_x_get_db_size_bytes__mutmut['_mutmut_orig'] = x_get_db_size_bytes__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_db_size_bytes__mutmut['x_get_db_size_bytes__mutmut_1'] = x_get_db_size_bytes__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_db_size_bytes__mutmut['x_get_db_size_bytes__mutmut_2'] = x_get_db_size_bytes__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_db_size_bytes__mutmut['x_get_db_size_bytes__mutmut_3'] = x_get_db_size_bytes__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_db_size_bytes__mutmut['x_get_db_size_bytes__mutmut_4'] = x_get_db_size_bytes__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_db_over_threshold__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_db_over_threshold__mutmut)
def is_db_over_threshold(
    db_path: Path | None = None,
    threshold_bytes: int | None = None,
) -> bool:
    threshold = threshold_bytes if threshold_bytes is not None else _DB_SIZE_WARNING_THRESHOLD
    return get_db_size_bytes(db_path) > threshold


def x_is_db_over_threshold__mutmut_orig(
    db_path: Path | None = None,
    threshold_bytes: int | None = None,
) -> bool:
    threshold = threshold_bytes if threshold_bytes is not None else _DB_SIZE_WARNING_THRESHOLD
    return get_db_size_bytes(db_path) > threshold


def x_is_db_over_threshold__mutmut_1(
    db_path: Path | None = None,
    threshold_bytes: int | None = None,
) -> bool:
    threshold = None
    return get_db_size_bytes(db_path) > threshold


def x_is_db_over_threshold__mutmut_2(
    db_path: Path | None = None,
    threshold_bytes: int | None = None,
) -> bool:
    threshold = threshold_bytes if threshold_bytes is None else _DB_SIZE_WARNING_THRESHOLD
    return get_db_size_bytes(db_path) > threshold


def x_is_db_over_threshold__mutmut_3(
    db_path: Path | None = None,
    threshold_bytes: int | None = None,
) -> bool:
    threshold = threshold_bytes if threshold_bytes is not None else _DB_SIZE_WARNING_THRESHOLD
    return get_db_size_bytes(None) > threshold


def x_is_db_over_threshold__mutmut_4(
    db_path: Path | None = None,
    threshold_bytes: int | None = None,
) -> bool:
    threshold = threshold_bytes if threshold_bytes is not None else _DB_SIZE_WARNING_THRESHOLD
    return get_db_size_bytes(db_path) >= threshold

mutants_x_is_db_over_threshold__mutmut['_mutmut_orig'] = x_is_db_over_threshold__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_db_over_threshold__mutmut['x_is_db_over_threshold__mutmut_1'] = x_is_db_over_threshold__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_db_over_threshold__mutmut['x_is_db_over_threshold__mutmut_2'] = x_is_db_over_threshold__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_db_over_threshold__mutmut['x_is_db_over_threshold__mutmut_3'] = x_is_db_over_threshold__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_db_over_threshold__mutmut['x_is_db_over_threshold__mutmut_4'] = x_is_db_over_threshold__mutmut_4 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_purge_expired_incidents__mutmut)
def purge_expired_incidents(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_orig(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_1(conn: duckdb.DuckDBPyConnection) -> int:
    before = None
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_2(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(None).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_3(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql(None)).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_4(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("XXcount_incidents.sqlXX")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_5(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("COUNT_INCIDENTS.SQL")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_6(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(None)
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_7(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql(None))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_8(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("XXpurge_expired.sqlXX"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_9(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("PURGE_EXPIRED.SQL"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_10(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = None
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_11(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(None).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_12(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql(None)).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_13(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("XXcount_incidents.sqlXX")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_14(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("COUNT_INCIDENTS.SQL")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_15(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = None
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_16(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[1] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_17(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 1
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_18(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = None
    return before_count - after_count


def x_purge_expired_incidents__mutmut_19(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[1] if after else 0
    return before_count - after_count


def x_purge_expired_incidents__mutmut_20(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 1
    return before_count - after_count


def x_purge_expired_incidents__mutmut_21(conn: duckdb.DuckDBPyConnection) -> int:
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_expired.sql"))
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count + after_count

mutants_x_purge_expired_incidents__mutmut['_mutmut_orig'] = x_purge_expired_incidents__mutmut_orig # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_1'] = x_purge_expired_incidents__mutmut_1 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_2'] = x_purge_expired_incidents__mutmut_2 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_3'] = x_purge_expired_incidents__mutmut_3 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_4'] = x_purge_expired_incidents__mutmut_4 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_5'] = x_purge_expired_incidents__mutmut_5 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_6'] = x_purge_expired_incidents__mutmut_6 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_7'] = x_purge_expired_incidents__mutmut_7 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_8'] = x_purge_expired_incidents__mutmut_8 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_9'] = x_purge_expired_incidents__mutmut_9 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_10'] = x_purge_expired_incidents__mutmut_10 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_11'] = x_purge_expired_incidents__mutmut_11 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_12'] = x_purge_expired_incidents__mutmut_12 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_13'] = x_purge_expired_incidents__mutmut_13 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_14'] = x_purge_expired_incidents__mutmut_14 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_15'] = x_purge_expired_incidents__mutmut_15 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_16'] = x_purge_expired_incidents__mutmut_16 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_17'] = x_purge_expired_incidents__mutmut_17 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_18'] = x_purge_expired_incidents__mutmut_18 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_19'] = x_purge_expired_incidents__mutmut_19 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_20'] = x_purge_expired_incidents__mutmut_20 # type: ignore # mutmut generated
mutants_x_purge_expired_incidents__mutmut['x_purge_expired_incidents__mutmut_21'] = x_purge_expired_incidents__mutmut_21 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_purge_older_than__mutmut)
def purge_older_than(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_orig(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_1(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is not None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_2(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = None
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_3(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_4(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(None) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_5(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=None)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_6(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = None
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_7(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(None).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_8(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql(None)).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_9(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("XXcount_incidents.sqlXX")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_10(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("COUNT_INCIDENTS.SQL")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_11(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(None, [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_12(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), None)
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_13(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute([cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_14(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), )
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_15(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql(None), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_16(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("XXpurge_older_than.sqlXX"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_17(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("PURGE_OLDER_THAN.SQL"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_18(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = None
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_19(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(None).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_20(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql(None)).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_21(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("XXcount_incidents.sqlXX")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_22(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("COUNT_INCIDENTS.SQL")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_23(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = None
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_24(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[1] if before else 0
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_25(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 1
    after_count: int = after[0] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_26(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = None
    return before_count - after_count


def x_purge_older_than__mutmut_27(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[1] if after else 0
    return before_count - after_count


def x_purge_older_than__mutmut_28(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 1
    return before_count - after_count


def x_purge_older_than__mutmut_29(
    conn: duckdb.DuckDBPyConnection,
    days: int,
    cutoff: datetime.datetime | None = None,
) -> int:
    if cutoff is None:
        cutoff = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    before = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    conn.execute(_load_sql("purge_older_than.sql"), [cutoff.isoformat()])
    after = conn.execute(_load_sql("count_incidents.sql")).fetchone()
    before_count: int = before[0] if before else 0
    after_count: int = after[0] if after else 0
    return before_count + after_count

mutants_x_purge_older_than__mutmut['_mutmut_orig'] = x_purge_older_than__mutmut_orig # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_1'] = x_purge_older_than__mutmut_1 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_2'] = x_purge_older_than__mutmut_2 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_3'] = x_purge_older_than__mutmut_3 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_4'] = x_purge_older_than__mutmut_4 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_5'] = x_purge_older_than__mutmut_5 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_6'] = x_purge_older_than__mutmut_6 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_7'] = x_purge_older_than__mutmut_7 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_8'] = x_purge_older_than__mutmut_8 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_9'] = x_purge_older_than__mutmut_9 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_10'] = x_purge_older_than__mutmut_10 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_11'] = x_purge_older_than__mutmut_11 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_12'] = x_purge_older_than__mutmut_12 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_13'] = x_purge_older_than__mutmut_13 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_14'] = x_purge_older_than__mutmut_14 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_15'] = x_purge_older_than__mutmut_15 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_16'] = x_purge_older_than__mutmut_16 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_17'] = x_purge_older_than__mutmut_17 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_18'] = x_purge_older_than__mutmut_18 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_19'] = x_purge_older_than__mutmut_19 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_20'] = x_purge_older_than__mutmut_20 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_21'] = x_purge_older_than__mutmut_21 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_22'] = x_purge_older_than__mutmut_22 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_23'] = x_purge_older_than__mutmut_23 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_24'] = x_purge_older_than__mutmut_24 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_25'] = x_purge_older_than__mutmut_25 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_26'] = x_purge_older_than__mutmut_26 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_27'] = x_purge_older_than__mutmut_27 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_28'] = x_purge_older_than__mutmut_28 # type: ignore # mutmut generated
mutants_x_purge_older_than__mutmut['x_purge_older_than__mutmut_29'] = x_purge_older_than__mutmut_29 # type: ignore # mutmut generated
