# Cache Hit — DuckDB VSS Match

User asks a question that matches a past investigation in DuckDB (cosine similarity >= 0.80). The LLM is never called — the cached result is returned instantly. Quota IS still incremented: a cache hit counts as an investigation consumed.

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant parse_intent
    participant QM as QuotaManager
    participant DuckDB
    participant check_cache
    participant store_memory
    participant format_response

    User->>CLI: "why did payments-api crash?"
    CLI->>parse_intent: query

    Note over parse_intent,QM: [FREE] quota check
    parse_intent->>QM: check_quota()
    QM->>DuckDB: investigation_count < 50?
    DuckDB-->>QM: OK
    parse_intent-->>CLI: intent + tool_name

    CLI->>check_cache: query embedding
    check_cache->>DuckDB: VSS search / ln(age_days+2)
    Note over DuckDB: cosine similarity = 0.92<br/>score >= 0.80 → MATCH
    DuckDB-->>check_cache: cached result (cause, solution, severity)

    alt cache_hit = true
        Note over check_cache,execute_tool: LLM + K8s skipped entirely
        check_cache-->>CLI: cached_result + cache_hit = true

        CLI->>format_response: cached result
        format_response-->>CLI: formatted + suggestions

        CLI->>store_memory: update weight
        store_memory->>DuckDB: UPDATE incidents SET weight = weight + 0.1

        Note over store_memory,QM: [FREE] cache hit still counts
        store_memory->>QM: increment_quota()
        QM->>DuckDB: UPDATE investigation_count

        store_memory-->>CLI: OK

        CLI-->>User: "This happened 3 days ago:<br/>Cause: OOM kill — Increase memory limit<br/>(cache hit) [24/50 · 26 remaining]"
    end
```

## Key Points

- Cache hits skip retrieve_context, execute_tool, generate_response, semantic_checker, and llm_judge — saving 5 nodes
- Cache hits still consume 1 investigation from the monthly quota (same pool as full investigations)
- The cached result's weight is incremented by 0.1, reinforcing popular investigations
- Results show "this happened X days ago" using age_days from DuckDB
- Recency scoring (`/ ln(age_days + 2)`) ensures older incidents are ranked lower
