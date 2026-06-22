# LangGraph Flow — 9-Node Investigation Pipeline

The full LangGraph pipeline showing all 9 nodes, conditional routing, and integration points with DuckDB and QuotaManager.

```mermaid
graph TD
    Start([User Query]) --> parse_intent

    parse_intent --> |quota OK| check_cache
    parse_intent --> |quota exceeded| Error([QuotaExceededError])

    check_cache --> |cache_hit| format_response
    check_cache --> |miss| retrieve_context

    retrieve_context --> execute_tool
    execute_tool --> generate_response

    generate_response --> semantic_checker

    semantic_checker --> |PASS| llm_judge
    semantic_checker --> |FAIL & retry<3| generate_response
    semantic_checker --> |FAIL & retry>=3| format_response_degraded([DEGRADED])
    semantic_checker --> |BLOCKED| format_response_blocked([BLOCKED])

    llm_judge --> |PASS| store_memory
    llm_judge --> |FAIL| generate_response
    llm_judge --> |FLAG| store_memory

    store_memory --> format_response

    format_response --> End([User Response])

    subgraph "External Integrations"
        DuckDB[(DuckDB)]
        QM[QuotaManager]
        LLM1[claude-sonnet-4-6]
        LLM2[claude-haiku-4-5]
    end

    parse_intent -.-> QM
    check_cache -.-> DuckDB
    generate_response -.-> LLM1
    llm_judge -.-> LLM2
    store_memory -.-> DuckDB
    store_memory -.-> QM
```

## Key Points

- **9 nodes**: parse_intent, check_cache, retrieve_context, execute_tool, generate_response, semantic_checker, llm_judge, store_memory, format_response
- **Check cache first**: DuckDB VSS is queried BEFORE any LLM call — cache hits skip 5 expensive nodes
- **Max 3 retries**: generate_response can retry up to 3 times if checker fails — after 3 failures, format_response returns DEGRADED status
- **BLOCKED is a hard stop**: mutation guard violations immediately route to format_response
- **FLAG goes to store_memory**: results with caveats are stored but marked for review
