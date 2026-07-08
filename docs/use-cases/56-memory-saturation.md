# Use Case 56 — Memory Saturation Prediction

## Sample Questions

- "Which pod is going to OOM in the next 30 minutes?"
- "Predict which pods are at risk of memory saturation"
- "Is there a memory leak in the checkout service right now?"
- "Show me pods with growing memory and their projected saturation time"
- "Why is the checkout pod consuming more memory?"

---

One MCP tool for memory saturation prediction: `memory_saturation`. Queries Prometheus for memory trends, extrapolates time-to-saturation, and correlates with OTel traces for root cause.

### Flow 1 — Happy Path: Critical Pod Detected

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as memory_saturation
    participant Service as MemorySaturationService
    participant Port as MemorySaturationPort
    participant Adapter as PrometheusMemoryAdapter
    participant Prom as Prometheus
    participant OTel as OTel API

    AI->>MCP: "Which pod is about to OOM?"
    MCP->>Tool: memory_saturation(30)

    Tool->>Service: predict(command)
    Service->>Port: fetch_memory_metrics(req)
    Port->>Adapter: PrometheusMemoryAdapter
    Adapter->>Prom: rate(container_memory_usage) for 30min
    Prom-->>Adapter: checkout-pod: 850MB/1024MB, +8.5MB/min

    Note over Service: MemorySaturationResult.compute()<br/>(1024-850)/8.5 = 20.5 min<br/>→ CRITICAL

    Service->>Port: correlate_with_otel("checkout-pod-abc")
    Port->>Adapter: check traces
    Adapter->>OTel: span analysis for checkout-pod-abc
    OTel-->>Adapter: DB query returning 15MB/request

    Service-->>Tool: MemorySaturationResponse(critical_pods=[...], safe_pod_count=1)
    Tool-->>MCP: {critical_pods: [{pod_name: "checkout-pod-abc", saturation_in_minutes: 20.5, otel_root_cause: "..."}]}
    MCP-->>AI: "checkout-pod-abc: 850/1024MB, +8.5MB/min → OOM in ~20 min. Root cause: DB query returning 15MB per /checkout call."
```

### Flow 2 — All Stable

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as memory_saturation
    participant Service as MemorySaturationService

    AI->>Tool: memory_saturation(30)
    Tool->>Service: predict()
    Note over Service: All pods have stable memory<br/>critical_pods=[], safe_pod_count=5

    Service-->>Tool: no critical pods
    Tool-->>AI: "All 5 pods stable — no OOM risk in next 30 minutes."
```

## Key Points

- **saturation_in_minutes** = `(limit - current) / growth_rate` — linear extrapolation
- **CRITICAL** if saturation < 15 min, **AT_RISK** if < 30 min, otherwise **STABLE**
- **No limit** → node capacity (32GB default) used as ceiling
- **OTel correlation** — identifies the downstream call causing memory growth

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_compute_critical` | `tests/unit/test_memory_saturation.py` | ✅ |
| `test_no_risk` | `tests/unit/test_memory_saturation.py` | ✅ |
| `test_returns_critical_pods` | `tests/unit/test_memory_saturation_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/memory_saturation.py` — MemoryPrediction, MemorySaturationResult
- `src/hexawyn/application/ports/driven/memory_saturation_port.py` — MemorySaturationPort ABC
- `src/hexawyn/adapters/secondary/gitops/prometheus_memory_adapter.py` — Prometheus adapter
- `src/hexawyn/mcp/tools/memory_saturation.py` — MCP tool
