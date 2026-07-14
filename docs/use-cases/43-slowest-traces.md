# Use Case 43 — Slowest Traces per Pod

## Sample Questions

- "Show me the 5 slowest traces for pod checkout-7d in the last hour"
- "What are the slowest requests for the payments pod?"
- "Rank the top 5 traces by duration for pod auth-service-abc"
- "Find the worst-performing traces for the checkout pod this hour"
- "List the longest running spans for pod frontend-deploy"

---

One MCP tool: `slowest_traces`. Queries OTel traces filtered by pod name (k8s.pod.name), ranks by total duration descending, returns top N.

### Flow 1 — Happy Path: Top 5 Returned

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as slowest_traces
    participant Service as SlowestTracesService
    participant Port as SlowTraceSearchPort
    participant Adapter as OTelPodTraceAdapter
    participant OTel as OTel Trace API

    AI->>MCP: "5 slowest traces for checkout-7d?"
    MCP->>Tool: slowest_traces("checkout-7d", 60, 5)

    Tool->>Service: find_slowest(command)
    Service->>Port: search_pod_traces(req)
    Port->>Adapter: OTelPodTraceAdapter
    Adapter->>OTel: query k8s.pod.name=checkout-7d, last 60min
    OTel-->>Adapter: 50 traces returned

    Note over Service: sort by duration descending<br/>top 5: tr001=4200ms, tr002=3800ms, tr003=2100ms

    Service-->>Tool: SlowestTracesResponse(slowest_traces=[...], total=50)
    Tool-->>MCP: {slowest_traces: [{trace_id: "tr001", duration_ms: 4200, operation: "POST /checkout", span_count: 42}, ...]}
    MCP-->>AI: "Top 5 of 50 traces for checkout-7d:<br/>1. tr001 — 4200ms — POST /checkout — 42 spans<br/>2. tr002 — 3800ms — POST /checkout — 38 spans..."
```

### Flow 2 — Fewer Than Requested

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as slowest_traces
    participant Service as SlowestTracesService

    AI->>Tool: slowest_traces("quiet-pod", 60, 5)
    Tool->>Service: find_slowest()
    Note over Service: Only 2 traces found<br/>note: "Only 2 trace(s) found (fewer than requested 5)"

    Service-->>Tool: total=2, slowest_traces=[trX, trY]
    Tool-->>AI: "Only 2 traces found for quiet-pod:<br/>trX — 800ms, trY — 600ms"
```

### Flow 3 — Pod Not Found

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as slowest_traces
    participant Service as SlowestTracesService

    AI->>Tool: slowest_traces("ghost-pod", 60, 5)
    Tool->>Service: find_slowest()
    Note over Service: traces=[]<br/>note: "No traces found for pod 'ghost-pod'"

    Service-->>Tool: slowest_traces=[], note="No traces found"
    Tool-->>AI: "No traces found for pod 'ghost-pod' in the last hour."
```

### Flow 4 — Checker Node: Sample Bias

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate trace ranking
    alt OTel uses 10% sampling, LLM presents count as absolute
        Checker-->>LLM: ⚠️ FLAG — extrapolate: "~500 traces estimated (10% sampling)"
    alt LLM omits span count from trace summary
        Checker-->>LLM: ⚠️ FLAG — span_count must be included per trace
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **Ranking** — traces sorted by total duration descending, top N returned
- **Pod filter** — uses `k8s.pod.name` attribute for exact match
- **Truncation** — if fewer traces than top_n, all returned with note
- **Span count** — each trace includes span_count for complexity assessment

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_ranked` | `tests/unit/test_slowest_traces.py` | ✅ |
| `test_top_n_truncation` | `tests/unit/test_slowest_traces.py` | ✅ |
| `test_empty` | `tests/unit/test_slowest_traces.py` | ✅ |
| `test_returns_top_n` | `tests/unit/test_slowest_traces_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/slowest_traces.py` — SlowTrace, SlowestTracesResult
- `src/hexawyn/application/ports/driven/slow_trace_search_port.py` — SlowTraceSearchPort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_pod_trace_adapter.py` — OTelPodTraceAdapter
- `src/hexawyn/mcp/tools/slowest_traces.py` — MCP tool
