# Use Case — Retrieval Gate (ECA-177)

Lightweight heuristic classifier that decides whether a user query needs VSS memory retrieval BEFORE the cache/VSS pipeline runs. Uses regex patterns (no LLM, no embeddings, < 1ms per query) to classify queries as `needs_memory=True` (investigation, diagnostic) or `needs_memory=False` (list, count, describe).

Saves 30-40% of DuckDB VSS lookups for simple queries like "list namespaces" or "show me pods".

## Sample Questions

- "Why is my pod crashing?" → needs_memory=True
- "List all namespaces in production" → needs_memory=False
- "Debug the OOM in auth-service" → needs_memory=True
- "What is the version of nginx?" → needs_memory=False

---

### Flow 1 — Cache Bypass for Simple Queries

```mermaid
sequenceDiagram
    participant CLI as ChatCLIService
    participant RG as RetrievalGate
    participant C1 as CacheL1
    participant VSS as DuckDB VSS
    participant RT as RuntimeAdapter

    CLI->>RG: should_retrieve(query)

    Note over RG: Classification heuristique (< 1ms)
    RG->>RG: SKIP patterns: "^list, ^show, ^count..."
    RG->>RG: NEEDS patterns: "why, crash, error, debug..."

    alt needs_memory=False (simple query)
        RG-->>CLI: False — skip cache/VSS
        Note over CLI,C1: Cache/VSS SKIPPED
        CLI->>RT: run_investigation(query, memory_context=None)
        RT-->>CLI: InvestigationOutput
    else needs_memory=True (investigation)
        RG-->>CLI: True — proceed with cache/VSS
        CLI->>C1: get(hash)
        alt L1 hit
            C1-->>CLI: CacheEntry
        else L1 miss
            CLI->>VSS: search_similar(embedding)
            VSS-->>CLI: results
        end
        CLI->>RT: run_investigation(query, memory_context)
        RT-->>CLI: InvestigationOutput
    end
```

### Flow 2 — Pattern Classification Logic

```mermaid
sequenceDiagram
    participant RG as RetrievalGate
    participant P1 as NEEDS_MEMORY_PATTERNS
    participant P2 as SKIP_MEMORY_PATTERNS

    RG->>RG: lower(query), strip, truncate to 500 chars

    loop For each NEEDS pattern
        RG->>P1: re.search(pattern, query)
        alt match found
            P1-->>RG: True
            RG-->>RG: return True
        end
    end

    loop For each SKIP pattern
        RG->>P2: re.search(pattern, query)
        alt match found
            P2-->>RG: True
            RG-->>RG: return False
        end
    end

    RG->>RG: len(words) >= 4 → True (needs context)
    RG-->>RG: return False (short, no patterns)
```

## Key Points

- Classification < 1ms per query — regex only, no LLM/embeddings
- NEEDS wins over SKIP (conservative: better to search unnecessarily than miss)
- Query truncated to 500 chars for ReDoS protection
- French patterns need to be added (currently English-only)
- Integration: inject RetrievalGate into ChatCLIService (optional, backward-compatible)

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_why_crashing` | `tests/unit/domain/services/test_retrieval_gate.py` | ✅ |
| `test_list_namespaces` | `tests/unit/domain/services/test_retrieval_gate.py` | ✅ |
| `test_needs_wins_over_skip` | `tests/unit/domain/services/test_retrieval_gate.py` | ✅ |
| `test_french_query_defaults_to_needs_memory` | `tests/unit/domain/services/test_retrieval_gate.py` | ✅ |
| `test_very_long_query` | `tests/unit/domain/services/test_retrieval_gate.py` | ✅ |
| `test_retrieval_gate_skip_clears_history` | `tests/unit/application/service/test_chat_cli_service.py` | ✅ |

## Related Files

- `src/hexawyn/domain/services/retrieval_gate.py` — RetrievalGate classifier
- `src/hexawyn/application/service/chat_cli_service.py` — Injection point
- `tests/unit/domain/services/test_retrieval_gate.py` — 38 tests
- `tests/unit/application/service/test_chat_cli_service.py` — Integration tests
