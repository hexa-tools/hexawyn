# Use Case 45 — Metric Correlation (5xx ↔ Latency)

## Sample Questions

- "Is the spike in 5xx error rate on api-gateway correlated with latency on auth-service?"
- "Are the payment-service errors caused by database latency?"
- "Correlate the latency spike on auth-service with the error spike on the gateway"
- "Is there a causal relationship between the checkout errors and Redis slowness?"
- "Overlay 5xx rate and p99 latency for the last 30 minutes and check correlation"

---

One MCP tool: `metric_correlation`. Fetches two time series from OTel/Prometheus, computes Pearson correlation coefficient, determines correlated/uncorrelated/inconclusive, generates causal hypothesis.

### Flow 1 — Happy Path: Correlated

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as metric_correlation
    participant Service as MetricCorrelationService
    participant Port as MetricCorrelationPort
    participant Adapter as OTelCorrelationAdapter
    participant Prom as Prometheus/OTel

    AI->>MCP: "Is api-gateway 5xx correlated with auth latency?"
    MCP->>Tool: metric_correlation("api-gateway", "auth-service", 30)

    Tool->>Service: correlate(command)
    Service->>Port: fetch_primary_series(req)
    Port->>Adapter: OTelPrometheusCorrelationAdapter
    Adapter->>Prom: rate(http_requests_total{status=~"5.."}[30m])
    Prom-->>Adapter: [0.01, 0.45, 0.82, 0.91, 0.30]

    Service->>Port: fetch_correlated_series(req)
    Port->>Adapter: histogram_quantile(0.99, http_duration_ms)
    Prom-->>Adapter: [80, 320, 750, 820, 410]

    Note over Service: Pearson r = 0.97 → CORRELATED<br/>hypothesis: "auth latency spike likely contributing"

    Service-->>Tool: CORRELATED, r=0.97
    Tool-->>MCP: {status: "correlated", coefficient: 0.97, hypothesis: "..."}
    MCP-->>AI: "CORRELATED (r=0.97): auth-service latency spike likely causing api-gateway 5xx timeouts."
```

### Flow 2 — Uncorrelated

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as metric_correlation
    participant Service as MetricCorrelationService

    AI->>Tool: metric_correlation("api-gateway", "auth-service", 30)
    Tool->>Service: correlate()
    Note over Service: r = 0.12 → UNCORRELATED

    Service-->>Tool: UNCORRELATED
    Tool-->>AI: "UNCORRELATED (r=0.12): no significant relationship between 5xx and auth latency."
```

### Flow 3 — Insufficient Data

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as metric_correlation
    participant Service as MetricCorrelationService

    AI->>Tool: metric_correlation(...)
    Tool->>Service: correlate()
    Note over Service: data_point_count=2 < MIN_DATA_POINTS=3

    Service-->>Tool: INCONCLUSIVE
    Tool-->>AI: "INCONCLUSIVE: only 2 data points — need at least 3 for correlation."
```

### Flow 4 — Negative Correlation (Inverse)

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as metric_correlation
    participant Service as MetricCorrelationService

    AI->>Tool: metric_correlation(...)
    Tool->>Service: correlate()
    Note over Service: r = -0.85 → UNCORRELATED + "inverse relationship"

    Service-->>Tool: coefficient=-0.85, "inverse relationship"
    Tool-->>AI: "Inverse correlation (r=-0.85): 5xx drops when latency rises — likely independent."
```

## Key Points

- **Pearson coefficient** — linear correlation between two time series
- **Threshold** — |r| ≥ 0.7 → correlated, |r| < 0.3 → uncorrelated, between → inconclusive
- **Minimum 3 data points** — avoids spurious correlation on tiny samples
- **Negative correlation** — detected and reported as inverse relationship

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_correlated` | `tests/unit/test_metric_correlation.py` | ✅ |
| `test_uncorrelated` | `tests/unit/test_metric_correlation.py` | ✅ |
| `test_insufficient_data` | `tests/unit/test_metric_correlation.py` | ✅ |
| `test_negative_correlation` | `tests/unit/test_metric_correlation.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/metric_correlation.py` — CorrelationResult
- `src/hexawyn/application/ports/driven/metric_correlation_port.py` — MetricCorrelationPort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_correlation_adapter.py` — OTel adapter
- `src/hexawyn/mcp/tools/metric_correlation.py` — MCP tool
