# Use Case 50 — Redundant Call Detection

## Sample Questions

- "Are there any redundant or unnecessary calls in the web -> api -> db -> api flow?"
- "Does this trace have N+1 query patterns?"
- "Detect duplicate DB queries and round-trips in the checkout flow"
- "Show me wasted calls in the payments trace"
- "Are there N+1 patterns or circular calls in the last trace?"

---

One MCP tool: `redundant_calls`. Analyses span operations in a trace flow, detects N+1 patterns (≥5 identical calls), duplicates (≥2), and round-trips. Returns optimisation suggestions.

### Flow 1 — Happy Path: N+1 Detected

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as redundant_calls
    participant Service as RedundantCallsService
    participant Port as RedundantCallDetectionPort
    participant Adapter as OTelRedundantCallAdapter
    participant OTel as OTel Trace API

    AI->>MCP: "Redundant calls in web -> api -> db?"
    MCP->>Tool: redundant_calls("web -> api -> db")

    Tool->>Service: detect(command)
    Service->>Port: fetch_spans(req)
    Port->>Adapter: OTelRedundantCallAdapter
    Adapter->>OTel: query spans for flow
    OTel-->>Adapter: 47x SELECT * FROM products WHERE id = ?

    Note over Service: 47 identical queries → N+1 pattern<br/>calculate waste = 47 * 15ms = ~690ms

    Service-->>Tool: RedundantCallResult(patterns=[N+1], waste=680ms)
    Tool-->>MCP: {patterns: [{type: "n_plus_one", occurrences: 47, wasted_ms: 680}], total_redundant_calls: 47}
    MCP-->>AI: "N+1 detected: SELECT * FROM products called 47 times (~680ms wasted). Suggestion: Use IN clause or batch fetch."
```

### Flow 2 — No Redundancy

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as redundant_calls
    participant Service as RedundantCallsService

    AI->>Tool: redundant_calls("web -> api -> db")
    Tool->>Service: detect()
    Note over Service: 3 different queries, 1 call each<br/>no patterns detected

    Service-->>Tool: patterns=[], waste=0
    Tool-->>AI: "No redundant calls detected. All span operations are unique."
```

### Flow 3 — Round-Trip

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as redundant_calls
    participant Service as RedundantCallsService

    AI->>Tool: redundant_calls("web -> api -> db -> api")
    Tool->>Service: detect()
    Note over Service: api→db→api callback detected<br/>round-trip latency: 145ms

    Service-->>Tool: patterns=[{type: "round_trip", wasted_ms: 145}]
    Tool-->>AI: "Round-trip detected: api→db→api adds 145ms. Refactor to avoid callback."
```

### Flow 4 — Checker Node: Pattern Validation

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate redundancy claims
    alt LLM says "N+1 detected" for 3 identical calls (threshold=5)
        Checker-->>LLM: ❌ FAIL — N+1 needs ≥5 identical calls
    alt LLM suggests batching but pattern is intentional polling
        Checker-->>LLM: ⚠️ FLAG — verify if repeated calls are intentional
    alt LLM calculates waste incorrectly
        Checker-->>LLM: ❌ FAIL — waste = sum(duration) - avg(duration)
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **N+1 detection** — ≥5 identical span operations → suggest batching/caching
- **Duplicate detection** — ≥2 identical calls → suggest result caching
- **Round-trip** — A→B→A callback paths detected
- **Waste calculation** — `sum(durations) - avg(duration)` per redundant group

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_n_plus_one` | `tests/unit/test_redundant_calls.py` | ✅ |
| `test_duplicate` | `tests/unit/test_redundant_calls.py` | ✅ |
| `test_no_redundancy` | `tests/unit/test_redundant_calls.py` | ✅ |
| `test_returns_n_plus_one` | `tests/unit/test_redundant_calls_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/redundant_calls.py` — SpanInfo, RedundancyPattern, RedundantCallResult
- `src/hexawyn/application/ports/driven/redundant_call_detection_port.py` — RedundantCallDetectionPort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_redundant_call_adapter.py` — adapter
- `src/hexawyn/mcp/tools/redundant_calls.py` — MCP tool
