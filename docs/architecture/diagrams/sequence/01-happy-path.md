# Full Investigation — Happy Path

User asks a question, no cache hit, the full 9-node LangGraph pipeline runs, result is stored in DuckDB, and quota is incremented.

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant parse_intent
    participant QM as QuotaManager
    participant DuckDB
    participant check_cache
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

    Note over parse_intent,QM: [FREE] quota check
    parse_intent->>QM: check_quota()
    QM->>DuckDB: SELECT investigation_count FROM usage_quota
    DuckDB-->>QM: count=23, limit=50
    QM-->>parse_intent: OK
    parse_intent-->>CLI: intent + tool_name

    CLI->>check_cache: query + embedding
    check_cache->>DuckDB: VSS search (cosine similarity)
    DuckDB-->>check_cache: no match (score < 0.80)
    check_cache-->>CLI: cache_hit = false

    CLI->>retrieve_context: cluster context
    retrieve_context-->>CLI: ClusterContext

    CLI->>execute_tool: tool_name + args
    execute_tool->>MCP: call tool
    MCP->>K8s: kubectl / API call
    K8s-->>MCP: pod data
    MCP-->>execute_tool: tool output
    execute_tool-->>CLI: raw data

    CLI->>generate_response: context + tool output
    generate_response->>LLM: prompt + data
    LLM-->>generate_response: investigation response
    generate_response-->>CLI: llm_response

    CLI->>semantic_checker: llm_response + tool_output
    semantic_checker-->>CLI: verdict = PASS

    CLI->>llm_judge: llm_response + checker result
    llm_judge-->>CLI: verdict = PASS

    CLI->>store_memory: result + embedding
    store_memory->>DuckDB: INSERT INTO incidents
    DuckDB-->>store_memory: stored

    Note over store_memory,QM: [FREE] increment quota
    store_memory->>QM: increment_quota()
    QM->>DuckDB: UPDATE investigation_count = 24
    DuckDB-->>QM: OK

    store_memory-->>CLI: stored

    CLI->>format_response: result + suggestions
    format_response-->>CLI: formatted response + chips

    CLI-->>User: response + [24/50 · 26 remaining]
```

## Key Points

- Quota is checked BEFORE any investigation starts — if exceeded, the entire pipeline is skipped
- Cache hit/miss is determined by cosine similarity threshold (0.80) against DuckDB VSS
- The LLM is only called for response generation (claude-sonnet-4-6) and semantic judging (claude-haiku-4-5)
- Quota is incremented AFTER a successful investigation in store_memory
- Demo mode bypasses both quota check and quota increment entirely
