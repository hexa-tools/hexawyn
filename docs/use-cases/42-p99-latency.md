# Use Case 42 — P99 Latency Percentile

## Sample Questions

- "What is the 99th percentile latency of /v1/checkout over the last 2 hours?"
- "Is the checkout endpoint meeting its 500ms SLO?"
- "Compute p50, p95, and p99 latency for the payments API"
- "What is the tail latency for the search endpoint in the last hour?"
- "Show me the SLO compliance status for /v1/orders"

---

One MCP tool: `p99_latency`. Queries OTel Prometheus histogram metrics, computes p50/p95/p99, compares against SLO threshold, returns pass/fail status.

### Flow 1 — Happy Path: SLO Pass

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as p99_latency
    participant Service as P99LatencyService
    participant Port as LatencyPercentilePort
    participant Adapter as OTelLatencyAdapter
    participant Prom as Prometheus/OTel

    AI->>MCP: "p99 of /v1/checkout over 2h?"
    MCP->>Tool: p99_latency("/v1/checkout", 120, 500)

    Tool->>Service: compute_p99(command)
    Service->>Port: fetch_percentiles(req)
    Port->>Adapter: OTelPrometheusLatencyAdapter
    Adapter->>Prom: histogram_quantile(0.99, http_server_duration_ms_bucket{endpoint="/v1/checkout"})
    Prom-->>Adapter: p50=85, p95=210, p99=480, count=14200

    Note over Service: P99Result.compute()<br/>p99=480ms < SLO=500ms → PASS<br/>margin=20ms

    Service-->>Tool: P99LatencyResponse(slo_status=pass)
    Tool-->>MCP: {p99_ms: 480, slo_status: "pass", sample_count: 14200}
    MCP-->>AI: "/v1/checkout p99=480ms, SLO=500ms → PASS. p50=85ms, p95=210ms.<br/>14,200 requests in the window."
```

### Flow 2 — SLO Fail

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as p99_latency
    participant Service as P99LatencyService

    AI->>Tool: p99_latency("/v1/checkout")
    Tool->>Service: compute_p99()
    Note over Service: p99=820ms > SLO=500ms → FAIL<br/>delta=+320ms

    Service-->>Tool: SLO FAIL
    Tool-->>AI: "FAIL: p99=820ms exceeds SLO of 500ms by +320ms."
```

### Flow 3 — No Data

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as p99_latency
    participant Service as P99LatencyService

    AI->>Tool: p99_latency("/v1/ghost")
    Tool->>Service: compute_p99()
    Note over Service: sample_count=0 → NO_DATA

    Service-->>Tool: NO_DATA
    Tool-->>AI: "No data found for /v1/ghost in the time window."
```

### Flow 4 — Checker Node: SLO Validation

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate SLO computation
    alt LLM says "SLO failed" for p99=480ms, SLO=500ms
        Checker-->>LLM: ❌ FAIL — p99 < threshold must be PASS
    alt LLM cites wrong percentile (p95=480 instead of p99=480)
        Checker-->>LLM: ❌ FAIL — check each percentile against result
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **p50, p95, p99** — full latency profile for the endpoint
- **SLO comparison** — `slo_delta_ms = p99 - slo_threshold`, pass if ≤ 0
- **NO_DATA** — when sample_count=0 (endpoint not instrumented or no traffic)
- **Histogram-based** — uses Prometheus histogram buckets via OTel

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_slo_pass` | `tests/unit/test_p99_latency.py` | ✅ |
| `test_slo_fail` | `tests/unit/test_p99_latency.py` | ✅ |
| `test_no_data` | `tests/unit/test_p99_latency.py` | ✅ |
| `test_returns_percentiles` | `tests/unit/test_p99_latency_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/p99_latency.py` — LatencyPercentiles, P99Result
- `src/hexawyn/application/ports/driven/latency_percentile_port.py` — LatencyPercentilePort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_latency_adapter.py` — OTel adapter
- `src/hexawyn/mcp/tools/p99_latency.py` — MCP tool
