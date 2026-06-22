import json

from hexawyn.infrastructure.config.cache_manager import get_l1, set_l1
from hexawyn.infrastructure.config.quota_manager import get_history_days
from hexawyn.infrastructure.memory.duckdb_client import get_connection, search_similar
from hexawyn.lang_graph.typing.agent_state import AgentState
from hexawyn.lang_graph.typing.node_outputs import CheckCacheOutput


def run(state: AgentState) -> CheckCacheOutput:
    """
    Check cache before running the full investigation pipeline.

    Two-level cache strategy:
    L1 — Exact match (in-memory, sub-ms, 5min TTL)
         Hash of (query + cluster_name) → CacheEntry
    L2 — Semantic match (DuckDB VSS, cosine >= 0.80)
         Embedding similarity → SimilarInvestigationDict

    If L1 hit  → return immediately, skip L2 + full pipeline
    If L1 miss → check L2
    If L2 hit  → populate L1, return result, skip full pipeline
    If L2 miss → cache_hit=False, full pipeline runs
    """
    query = state["query"]
    cluster_name = state["cluster_context"].name

    # ── L1: exact match (in-memory) ───────────────────────
    l1_entry = get_l1(query=query, cluster_name=cluster_name)
    if l1_entry is not None:
        return CheckCacheOutput(
            cache_hit=True,
            cached_result=l1_entry.result,
        )

    # ── L2: semantic match (DuckDB VSS) ───────────────────
    history_days = get_history_days()

    stub_embedding: list[float] = [0.0] * 1536

    l2_results = search_similar(
        conn=get_connection(),
        embedding=stub_embedding,
        cluster_name=cluster_name,
        history_days=history_days,
    )

    if l2_results:
        best = l2_results[0]
        result_str = json.dumps(best)

        set_l1(
            query=query,
            cluster_name=cluster_name,
            result=result_str,
        )

        return CheckCacheOutput(
            cache_hit=True,
            cached_result=result_str,
        )

    # ── Both miss → full pipeline ──────────────────────────
    return CheckCacheOutput(
        cache_hit=False,
        cached_result=None,
    )
