# Use Case 44 — Span Bottleneck Analysis (DB vs Redis)

## Sample Questions

- "Is the bottleneck in the database or in the Redis cache?"
- "Which is slower based on OTel traces — DB queries or Redis commands?"
- "Is my database the bottleneck in our request flow?"
- "What is the slowest DB query and Redis command in the last 30 minutes?"

---

One MCP tool: `span_bottleneck_analysis`. Retrieves OTel traces, categorizes DB vs Redis spans, computes avg/p95/max, and identifies the dominant bottleneck with confidence.

### Flow 1 — Happy Path: DB Bottleneck Detected

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as span_bottleneck_analysis
    participant Service as SpanBottleneckAnalysisService
    participant Port as SpanBottleneckPort
    participant Adapter as OTelSpanBreakdownAdapter
    participant OTel as OTel Trace API

    AI->>MCP: "Is the bottleneck in DB or Redis?"
    MCP->>Tool: span_bottleneck_analysis(30)

    Tool->>Service: analyze(command)
    Service->>Port: fetch_db_spans(req)
    Port->>Adapter: OTelSpanBreakdownAdapter
    Adapter->>OTel: query db.system=* spans, last 30min
    OTel-->>Adapter: avg=380ms, p95=650ms, max=1200ms

    Service->>Port: fetch_redis_spans(req)
    Port->>Adapter: OTelSpanBreakdownAdapter
    Adapter->>OTel: query db.system=redis spans
    OTel-->>Adapter: avg=6ms, p95=15ms, max=45ms

    Note over Service: DB 63.3x slower → HIGH confidence<br/>bottleneck_pct = 98.4% of trace time

    Service-->>Tool: SpanBottleneckAnalysisResponse(bottleneck=DB, confidence=HIGH)
    Tool-->>MCP: {bottleneck: "db", confidence: "high", db_avg_ms: 380, redis_avg_ms: 6}
    MCP-->>AI: "DB is the bottleneck (HIGH confidence, 98.4% of trace time). DB avg=380ms vs Redis avg=6ms. Slowest query: SELECT * FROM orders..."
```

### Flow 2 — Redis Bottleneck

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as span_bottleneck_analysis
    participant Service as SpanBottleneckAnalysisService

    AI->>Tool: span_bottleneck_analysis(30)
    Tool->>Service: analyze()
    Note over Service: DB avg=50ms, Redis avg=200ms<br/>Redis 4x slower → HIGH confidence

    Service-->>Tool: bottleneck=REDIS, confidence=HIGH
    Tool-->>AI: "Redis is the bottleneck. avg=200ms vs DB 50ms. Slowest: HGETALL big:key"
```

### Flow 3 — Neither / Both Fast

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as span_bottleneck_analysis
    participant Service as SpanBottleneckAnalysisService

    AI->>Tool: span_bottleneck_analysis(30)
    Tool->>Service: analyze()
    Note over Service: DB avg=5ms, Redis avg=3ms<br/>Both < 20ms threshold → NEITHER

    Service-->>Tool: bottleneck=NEITHER, confidence=LOW
    Tool-->>AI: "No clear bottleneck — both DB and Redis are fast (<20ms average). Check other spans."
```

### Flow 4 — No Redis Spans Found

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as span_bottleneck_analysis
    participant Service as SpanBottleneckAnalysisService

    AI->>Tool: span_bottleneck_analysis(30)
    Tool->>Service: analyze()
    Note over Service: DB spans found, Redis=None<br/>Only DB analysis returned

    Service-->>Tool: bottleneck=DB, confidence=MEDIUM
    Tool-->>AI: "Only DB spans found. No Redis spans in traces. DB avg=350ms. Slowest: SELECT * FROM items"
```

## Key Points

- **DB vs Redis ratio** — >= 4x → HIGH confidence, >= 2x → MEDIUM, otherwise LOW
- **Both fast** — if both < 20ms average, NEITHER flagged
- **Redis missing** — no Redis spans → DB only, MEDIUM confidence
- **Slowest operation** — surfaces the exact query/command causing the delay

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_db_bottleneck_high_confidence` | `tests/unit/test_span_bottleneck.py` | ✅ |
| `test_redis_bottleneck` | `tests/unit/test_span_bottleneck.py` | ✅ |
| `test_no_bottleneck_both_fast` | `tests/unit/test_span_bottleneck.py` | ✅ |
| `test_db_only_no_redis_spans` | `tests/unit/test_span_bottleneck.py` | ✅ |
| `test_returns_db_bottleneck` | `tests/unit/test_span_bottleneck_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/span_bottleneck.py` — SpanBreakdown, BottleneckResult
- `src/hexawyn/application/ports/driven/span_bottleneck_port.py` — SpanBottleneckPort ABC
- `src/hexawyn/application/service/span_bottleneck_analysis_service.py` — service
- `src/hexawyn/adapters/secondary/gitops/otel_span_breakdown_adapter.py` — OTel adapter
- `src/hexawyn/mcp/tools/span_bottleneck_analysis.py` — MCP tool
