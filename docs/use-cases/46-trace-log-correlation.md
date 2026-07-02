# Use Case 46 — Trace-Log Correlation

## Sample Questions

- "What are the error logs associated with the failed trace for POST /order?"
- "Find the error logs for the most recent failed checkout request"
- "Correlate the failed trace abc-def-123 with the application error logs"
- "Show me the application errors that happened during the failed payments trace"
- "What went wrong in the last failed POST /order request — show logs and spans"

---

One MCP tool: `trace_log_correlation`. Retrieves OTel error spans, correlates trace_id with log system (Loki/ELK), returns matching ERROR/FATAL log lines in trace timeline order.

### Flow 1 — Happy Path: Logs Correlated

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as trace_log_correlation
    participant Service as TraceLogCorrelationService
    participant Port as TraceLogCorrelationPort
    participant Adapter as OTelTraceLogAdapter
    participant OTel as OTel Trace API
    participant Loki as Loki/ELK

    AI->>MCP: "Error logs for POST /order trace?"
    MCP->>Tool: trace_log_correlation("POST /order")

    Tool->>Service: correlate(command)
    Service->>Port: fetch_error_spans(req)
    Port->>Adapter: OTelTraceLogAdapter
    Adapter->>OTel: query error spans for POST /order
    OTel-->>Adapter: [inventory.checkStock: timeout, order.createOrder: ValidationException]

    Service->>Port: fetch_correlated_logs("abc-def-123")
    Port->>Adapter: OTelTraceLogAdapter
    Adapter->>Loki: {trace_id="abc-def-123"} level=ERROR
    Loki-->>Adapter: [inventory: timeout postgres, order: invalid SKU]

    Note over Service: Align logs with spans by timestamp<br/>2 error spans → 2 correlated logs

    Service-->>Tool: TraceLogCorrelationResponse(trace_id="abc-def-123", logs=[...])
    Tool-->>MCP: {trace_id: "abc-def-123", error_span_count: 2, correlated_log_count: 2}
    MCP-->>AI: "Trace abc-def-123: 2 error spans with 2 correlated logs.<br/>1. inventory-service: timeout connecting to postgres<br/>2. order-service: ValidationException: invalid SKU"
```

### Flow 2 — Spans But No Logs

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as trace_log_correlation
    participant Service as TraceLogCorrelationService

    AI->>Tool: trace_log_correlation("POST /x")
    Tool->>Service: correlate()
    Note over Service: error_spans found, logs=[]<br/>"Found 1 error span(s) but no correlated logs"

    Service-->>Tool: correlated_log_count=0
    Tool-->>AI: "Found 1 error span but no correlated logs. Check if log system is configured."
```

### Flow 3 — No Error Spans

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as trace_log_correlation
    participant Service as TraceLogCorrelationService

    AI->>Tool: trace_log_correlation("POST /ghost")
    Tool->>Service: correlate()
    Note over Service: error_spans=[], trace_id=None<br/>"No error spans found"

    Service-->>Tool: error_span_count=0
    Tool-->>AI: "No error spans found for POST /ghost in traces."
```

### Flow 4 — Checker Node: Log-Span Alignment

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate log-span correlation
    alt LLM cites a log not in correlated_logs list
        Checker-->>LLM: ❌ FAIL — log must be in returned data
    alt LLM reorders logs breaking chronological order
        Checker-->>LLM: ⚠️ FLAG — logs must be in timestamp order
    alt LLM says "error caused by DB" but no DB span in error_spans
        Checker-->>LLM: ❌ FAIL — attribution must match span data
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **Error span extraction** — OTel spans with error=true or status_code=ERROR
- **Log correlation** — matches trace_id in log system (Loki/ELK)
- **Chronological order** — logs sorted by timestamp, aligned with span timeline
- **Graceful degradation** — spans without logs still returned with context

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_correlation_found` | `tests/unit/test_trace_log_correlation.py` | ✅ |
| `test_spans_but_no_logs` | `tests/unit/test_trace_log_correlation.py` | ✅ |
| `test_no_error_spans_found` | `tests/unit/test_trace_log_correlation.py` | ✅ |
| `test_returns_correlation` | `tests/unit/test_trace_log_correlation_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/trace_log_correlation.py` — TraceLogSpan, CorrelatedLog, TraceLogResult
- `src/hexawyn/application/ports/driven/trace_log_correlation_port.py` — TraceLogCorrelationPort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_trace_log_adapter.py` — OTelTraceLogAdapter
- `src/hexawyn/mcp/tools/trace_log_correlation.py` — MCP tool
