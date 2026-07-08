# Use Case 46 — Canary vs Stable OTel Comparison

## Sample Questions

- "Does the canary version of the order service have higher latency or error rate?"
- "Is the canary safe to promote based on OTel metrics?"
- "Compare p99 latency between the canary and stable deployments"
- "What is the error rate delta for the payments canary vs stable?"
- "Should I promote or rollback the current canary based on real-time telemetry?"

---

One MCP tool for canary comparison: `canary_comparison`. Compares OTel metrics (p50/p95/p99, error rate) between canary and stable versions, computes deltas, adjusts confidence based on traffic split, and returns a verdict.

### Flow 1 — Happy Path: Canary Regression Detected

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as canary_comparison
    participant Service as CanaryComparisonService
    participant Port as CanaryComparisonPort
    participant Adapter as OTelCanaryComparisonAdapter
    participant OTel as OTel API

    AI->>MCP: "Does the canary of order-service have higher latency?"
    MCP->>Tool: canary_comparison("order-service", 30m, 5%)

    Tool->>Service: compare(command)
    Service->>Port: fetch_stable_metrics(req)
    Port->>Adapter: OTelCanaryComparisonAdapter
    Adapter->>OTel: trace query: version=v2.3, last 30m
    OTel-->>Adapter: p99=210ms, count=9500, error=0.1%

    Service->>Port: fetch_canary_metrics(req)
    Port->>Adapter: OTelCanaryComparisonAdapter
    Adapter->>OTel: trace query: version=v2.4, last 30m
    OTel-->>Adapter: p99=480ms, count=500, error=2.1%

    Note over Service: ComparisonResult.compute()<br/>p99_delta = (480-210)/210*100 = +128.6%<br/>confidence = MEDIUM (canary count < 500, split < 20%)

    Service-->>Tool: CanaryComparisonResponse(verdict=REGRESSION, confidence=MEDIUM)
    Tool-->>MCP: {verdict: "regression", p99_delta_pct: 128.6}
    MCP-->>AI: "REGRESSION detected. p99: 480ms vs 210ms (+128.6%).<br/>Error rate: 2.1% vs 0.1% (+2.0%).<br/>Confidence: MEDIUM (low canary traffic at 5% split).<br/>Do NOT promote."
```

### Flow 2 — Canary Safe

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as canary_comparison
    participant Service as CanaryComparisonService

    AI->>Tool: canary_comparison("order-service", 30m, 50%)

    Tool->>Service: compare()
    Note over Service: stable p99=210ms, canary p99=205ms (-2.4%)<br/>error rate unchanged (0.1%)<br/>counts: canary=8000, stable=9500<br/>confidence=HIGH

    Service-->>Tool: CanaryComparisonResponse(verdict=SAFE)
    Tool-->>AI: "SAFE to promote. p99: 205ms vs 210ms (-2.4%).<br/>Confidence: HIGH."
```

### Flow 3 — Insufficient Data

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as canary_comparison
    participant Service as CanaryComparisonService

    AI->>Tool: canary_comparison("new-service", 10m, 5%)
    Tool->>Service: compare()
    Note over Service: canary count=0, stable count=0<br/>INSUFFICIENT_DATA

    Service-->>Tool: verdict=INSUFFICIENT_DATA
    Tool-->>AI: "INSUFFICIENT DATA — no traces found for either version.<br/>Ensure canary is deployed and receiving traffic."
```

## Key Points

- **Metric deltas** — computes `(canary - stable) / stable * 100` for p99 and error rate
- **Confidence adjustment** — LOW if canary count < `min_sample` (500), MEDIUM if traffic split < 20%, HIGH otherwise
- **Regression threshold** — p99 increase > 10% OR error rate increase > 0.5pp → REGRESSION
- **Read-only** — never triggers promote or rollback; operators decide

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_canary_regression` | `tests/unit/test_canary_comparison.py` | ✅ |
| `test_canary_safe` | `tests/unit/test_canary_comparison.py` | ✅ |
| `test_low_confidence` | `tests/unit/test_canary_comparison.py` | ✅ |
| `test_insufficient_data` | `tests/unit/test_canary_comparison.py` | ✅ |
| `test_returns_regression` | `tests/unit/test_canary_comparison_tool.py` | ✅ |
| `test_returns_safe` | `tests/unit/test_canary_comparison_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/canary_comparison.py` — VersionMetrics, ComparisonResult, CanaryComparisonRequest
- `src/hexawyn/application/ports/driven/canary_comparison_port.py` — CanaryComparisonPort ABC
- `src/hexawyn/application/service/canary_comparison_service.py` — service
- `src/hexawyn/adapters/secondary/gitops/otel_canary_comparison_adapter.py` — OTel adapter
- `src/hexawyn/mcp/tools/canary_comparison.py` — MCP tool
