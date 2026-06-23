# Cache L1 Hit — Exact Match (Sub-millisecond)

User asks the same question asked in the last 5 minutes. Cache L1 (in-memory SHA-256 hash) returns the result instantly. No DuckDB call, no K8s API call, no LLM call. Quota IS still incremented — cache hit = investigation consumed.

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant parse_intent
    participant QM as QuotaManager
    participant check_cache
    participant CacheL1
    participant store_memory
    participant format_response

    User->>CLI: same question as 3 minutes ago
    CLI->>parse_intent: query
    parse_intent->>QM: check_quota()
    QM-->>parse_intent: OK

    parse_intent-->>CLI: intent + tool_name

    CLI->>check_cache: query + cluster_name

    Note over check_cache: compute SHA-256 hash
    check_cache->>CacheL1: get(hash)

    Note over check_cache,CacheL1: L1 HIT — age=180s < TTL=300s
    CacheL1-->>check_cache: CacheEntry (age=180s, valid=true)

    Note over check_cache: K8s API skipped ✓
    Note over check_cache: LLM call skipped ✓
    Note over check_cache: DuckDB VSS skipped ✓

    check_cache-->>CLI: cache_hit=True, result="OOM detected"

    CLI->>store_memory: increment quota (cache hit counts)
    store_memory->>QM: increment_quota()
    QM-->>store_memory: OK

    CLI->>format_response: cached result + suggestions
    format_response-->>CLI: formatted response + chips

    Note over CLI: answered in <1ms

    CLI-->>User: response + [24/50 · 26 remaining]
```

## Key Points

- L1 hit skips 5 LangGraph nodes: retrieve_context, execute_tool, generate_response, semantic_checker, llm_judge
- TTL is 5 minutes — cluster state changes fast, older cached results are stale
- Hash is case-insensitive: "Why is Payments-API" == "why is payments-api"
- Different cluster = different hash (prod-eu ≠ prod-us)
- Demo mode results never stored in L1

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_l1_hit_returns_cache_hit_true` | `tests/unit/test_check_cache_node.py` | ✅ |
| `test_l1_hit_does_not_call_l2` | `tests/unit/test_check_cache_node.py` | ✅ |
| `test_set_and_get_returns_entry` | `tests/unit/test_cache_repository.py` | ✅ |
| `test_is_valid_when_fresh` | `tests/unit/test_cache_model.py` | ✅ |
| `test_is_expired_when_old` | `tests/unit/test_cache_model.py` | ✅ |
| `test_case_insensitive_query` | `tests/unit/test_cache_manager.py` | ✅ |
| `test_same_query_same_cluster_same_hash` | `tests/unit/test_cache_manager.py` | ✅ |

## Related Files

- `src/hexawyn/lang_graph/nodes/check_cache.py` — L1 check before L2 VSS
- `src/hexawyn/infrastructure/config/cache_manager.py` — compute_query_hash, get_l1, set_l1
- `src/hexawyn/infrastructure/memory/cache_l1_repository.py` — in-memory dict store
- `src/hexawyn/domain/models/cache.py` — CacheEntry model with 5min TTL
