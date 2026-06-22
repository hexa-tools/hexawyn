import os

from fastmcp import FastMCP

from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.config.config_manager import get_api_key
from hexawyn.infrastructure.config.kubeconfig_reader import (
    get_active_context,
    load_kubeconfig,
    validate_connection,
)
from hexawyn.infrastructure.memory.duckdb_client import get_connection

# Initialize FastMCP server
mcp = FastMCP(
    name="hexawyn",
    version="0.1.0b0",
    instructions="AI-powered Kubernetes diagnostic agent",
)

# ── Startup kubeconfig validation ─────────────────────────
_k8s_api = None
_cluster_status: dict[str, str] = {"status": "not_initialized"}

try:
    _k8s_api = load_kubeconfig()
    active_ctx = get_active_context()
    context_name = str(active_ctx["name"]) if active_ctx else "unknown"
    _cluster_status = validate_connection(_k8s_api, context_name)
except ClusterUnreachableError as e:
    _cluster_status = {
        "status": "no_kubeconfig",
        "error": str(e),
    }
    print("[hexawyn] \u26a0\ufe0f  No kubeconfig found — starting in degraded mode")


@mcp.tool()
def health() -> dict[str, str]:
    """
    Health check endpoint — used by Docker, CI, and Marketplace readiness probes.
    Returns status, version, DuckDB connectivity, API key status, and cluster connectivity.
    """
    db_ok = False
    try:
        conn = get_connection()
        conn.execute("SELECT 1").fetchone()
        db_ok = True
    except Exception:
        db_ok = False

    api_key_ok = get_api_key() is not None

    return {
        "status": "ok" if db_ok else "degraded",
        "version": "0.1.0b0",
        "duckdb": "connected" if db_ok else "unavailable",
        "api_key": "configured" if api_key_ok else "missing",
        "cluster": _cluster_status.get("status", "unknown"),
        "context": _cluster_status.get("context", "none"),
    }


if __name__ == "__main__":
    port = int(os.environ.get("HEXAWYN_PORT", "8000"))
    mcp.run(host="0.0.0.0", port=port)
