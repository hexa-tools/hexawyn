# Full Investigation — Happy Path

User asks a question in the CLI. No cache hit (L1 or L2). Full 9-node LangGraph pipeline runs: quota check → cache miss → tool call → LLM → semantic checker → LLM judge → DuckDB store → quota increment → L1 cache populate → CLI response with chips.

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant parse_intent
    participant QM as QuotaManager
    participant check_cache
    participant CacheL1
    participant DuckDB
    participant retrieve_context
    participant execute_tool
    participant MCP as MCP Tool
    participant K8s as K8s API
    participant generate_response
    participant LLM as LLM (claude-sonnet-4-6)
    participant semantic_checker
    participant llm_judge as LLM Judge (claude-haiku-4-5)
    participant store_memory
    participant format_response

    User->>CLI: types question
    CLI->>parse_intent: query

    Note over parse_intent,QM: [FREE] 50 investigations/month
    parse_intent->>QM: check_quota()
    QM->>DuckDB: SELECT investigation_count FROM usage_quota
    DuckDB-->>QM: count=23, limit=50
    QM-->>parse_intent: OK
    parse_intent-->>CLI: intent + tool_name

    CLI->>check_cache: query + embedding

    Note over check_cache: L1 miss (hash not found)
    check_cache->>CacheL1: get(hash)
    CacheL1-->>check_cache: None

    Note over check_cache,DuckDB: L2 miss (no similar past incident)
    check_cache->>DuckDB: VSS search (cosine similarity)
    DuckDB-->>check_cache: no match (score < 0.80)
    check_cache-->>CLI: cache_hit = false

    CLI->>retrieve_context: cluster context
    retrieve_context-->>CLI: ClusterContext

    CLI->>execute_tool: tool_name + args
    execute_tool->>MCP: call tool
    MCP->>K8s: kubectl / API call
    K8s-->>MCP: pod data (CrashLoopBackOff, 8 restarts)
    MCP-->>execute_tool: tool output
    execute_tool-->>CLI: raw data

    CLI->>generate_response: context + tool output
    generate_response->>LLM: prompt + data
    LLM-->>generate_response: "payments-api CrashLoopBackOff — OOM: 380Mi used, limit 256Mi"
    generate_response-->>CLI: llm_response

    CLI->>semantic_checker: llm_response + tool_output

    Note over semantic_checker: deterministic check PASS
    semantic_checker-->>CLI: verdict = PASS

    CLI->>llm_judge: llm_response + checker result

    Note over llm_judge: semantic check PASS (claude-haiku-4-5)
    llm_judge-->>CLI: verdict = PASS

    CLI->>store_memory: result + embedding

    Note over store_memory: quota incremented + L1 populated
    store_memory->>DuckDB: INSERT INTO incidents
    DuckDB-->>store_memory: stored

    store_memory->>QM: increment_quota()
    QM->>DuckDB: UPDATE investigation_count = 24
    DuckDB-->>QM: OK

    store_memory->>CacheL1: set(hash, result)
    CacheL1-->>store_memory: stored

    store_memory-->>CLI: stored

    CLI->>format_response: result + suggestions
    format_response-->>CLI: formatted response + 4 chips

    CLI-->>User: response + [24/50 · 26 remaining]
```

## Key Points

- Quota is checked BEFORE any investigation starts — if exceeded, the entire pipeline is skipped
- Cache L1 (in-memory hash) checked first, then L2 (DuckDB VSS cosine >= 0.80)
- The LLM is only called for response generation (claude-sonnet-4-6) and semantic judging (claude-haiku-4-5)
- Quota is incremented AND L1 is populated AFTER a successful investigation in store_memory
- Demo mode bypasses both quota check and quota increment entirely

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_checks_quota_in_normal_mode` | `tests/unit/test_quota_langgraph.py` | ✅ |
| `test_increments_quota_after_successful_investigation` | `tests/unit/test_quota_langgraph.py` | ✅ |
| `test_l1_miss_falls_through_to_l2` | `tests/unit/test_check_cache_node.py` | ✅ |
| `test_both_miss_returns_cache_hit_false` | `tests/unit/test_check_cache_node.py` | ✅ |
| `test_stores_result_in_l1` | `tests/unit/test_store_memory_cache.py` | ✅ |
| `test_finds_similar_embedding` | `tests/unit/test_duckdb_client.py` | ✅ |
| `test_is_not_exceeded_when_under_limit` | `tests/unit/test_quota_model.py` | ✅ |

## Related Files

- `src/hexawyn/lang_graph/nodes/parse_intent.py` — quota check before investigation
- `src/hexawyn/lang_graph/nodes/check_cache.py` — L1 + L2 cache check
- `src/hexawyn/lang_graph/nodes/store_memory.py` — quota increment + L1 store
- `src/hexawyn/lang_graph/nodes/generate_response.py` — LLM response generation
- `src/hexawyn/lang_graph/nodes/semantic_checker.py` — deterministic validation
- `src/hexawyn/lang_graph/nodes/llm_judge.py` — LLM semantic validation
- `src/hexawyn/infrastructure/config/quota_manager.py` — quota orchestration
- `src/hexawyn/infrastructure/memory/duckdb_client.py` — VSS search
