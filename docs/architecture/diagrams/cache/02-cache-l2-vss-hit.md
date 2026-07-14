# Cache L2 — DuckDB VSS Semantic Match

Cache L2 uses vector similarity search (HNSW index, cosine >= 0.80) on DuckDB incidents table. Finds semantically similar past investigations. History window enforced by tier: 7 days Free, 90 days Pro. On L2 hit, result is automatically stored in L1 for next time.

```mermaid
sequenceDiagram
    participant check_cache
    participant CacheL1
    participant ES as embedding_service
    participant DuckDB
    participant QM as QuotaManager
    participant store_memory

    check_cache->>CacheL1: get(hash)
    Note over CacheL1: L1 miss (no hash match)
    CacheL1-->>check_cache: None

    check_cache->>QM: get_history_days()
    QM-->>check_cache: 7 (Free) or 90 (Pro)

    check_cache->>ES: embed(query)
    ES-->>check_cache: float[768] embedding

    check_cache->>DuckDB: search_similar(embedding, history_days)

    Note over DuckDB: HNSW index — approximate nearest neighbor

    DuckDB-->>check_cache: score=0.92, age=2days<br/>cause="OOM", solution="increase limit"

    Note over DuckDB: score / ln(age_days + 2) — recency weighting
    Note over DuckDB: history filter: 7 days Free / 90 days Pro

    alt score >= 0.80
        Note over check_cache: L2 HIT — skip LLM + K8s

        check_cache->>CacheL1: set(hash, result)
        Note over CacheL1: populated after L2 hit for next time
        CacheL1-->>check_cache: stored

        check_cache-->>store_memory: result + quota increment
    end
```

## Key Points

- Cosine similarity threshold: 0.80 — lower scores are treated as cache miss
- Recency weighting: score divided by ln(age_days + 2) — recent matches ranked higher
- HNSW index enables fast approximate nearest neighbor search on 768-dimensional embeddings
- L2 hit automatically populates L1 — next identical query returns in <1ms
- Free tier sees 7 days of history, Pro tier sees 90 days (via history_days parameter)

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_l2_hit_stores_in_l1` | `tests/unit/test_check_cache_node.py` | ✅ |
| `test_l1_miss_falls_through_to_l2` | `tests/unit/test_check_cache_node.py` | ✅ |
| `test_finds_similar_embedding` | `tests/unit/test_duckdb_client.py` | ✅ |
| `test_default_history_days_is_free` | `tests/unit/test_duckdb_search.py` | ✅ |
| `test_pro_history_days_is_90` | `tests/unit/test_duckdb_search.py` | ✅ |
| `test_returns_entry_when_cached` | `tests/unit/test_cache_manager.py` | ✅ |

## Related Files

- `src/hexawyn/lang_graph/nodes/check_cache.py` — L2 fallback after L1 miss
- `src/hexawyn/infrastructure/memory/duckdb_client.py` — search_similar VSS function
- `src/hexawyn/infrastructure/memory/sql/search_similar.sql` — VSS query with recency
- `src/hexawyn/infrastructure/config/cache_manager.py` — set_l1 populates L1 on L2 hit
- `src/hexawyn/infrastructure/config/quota_manager.py` — get_history_days per tier
