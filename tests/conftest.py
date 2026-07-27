from __future__ import annotations

import os
from pathlib import Path

import duckdb
import pytest

_SQL_DIR = Path(__file__).parent.parent / "src" / "hexawyn" / "infrastructure" / "memory" / "sql"


@pytest.fixture
def in_memory_db() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(":memory:")
    try:
        conn.execute("INSTALL vss;")
        conn.execute("LOAD vss;")
    except Exception:
        pass
    schema_path = _SQL_DIR / "schema.sql"
    if schema_path.exists():
        conn.execute(schema_path.read_text(encoding="utf-8"))
    yield conn
    conn.close()


@pytest.fixture
def demo_adapter_aws():
    from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

    return DemoAdapter(scenario="aws_eks")


@pytest.fixture
def demo_adapter_gcp():
    from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

    return DemoAdapter(scenario="gcp_gke")


@pytest.fixture
def demo_adapter_openshift():
    from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

    return DemoAdapter(scenario="openshift")


@pytest.fixture
def demo_mode_env() -> None:
    os.environ["HEXAWYN_DEMO_MODE"] = "true"
    os.environ["HEXAWYN_DEMO_SCENARIO"] = "aws_eks"
    yield
    os.environ.pop("HEXAWYN_DEMO_MODE", None)
    os.environ.pop("HEXAWYN_DEMO_SCENARIO", None)
