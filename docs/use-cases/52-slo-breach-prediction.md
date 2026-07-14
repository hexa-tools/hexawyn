# Use Case 52 — SLO Breach Prediction

## Sample Questions

- "Which services are at risk of violating their latency SLO in the next hour?"
- "Will any service breach its p99 SLO within the next 60 minutes?"
- "Predict which services need attention before they breach their SLO"
- "Is the auth-service trending toward an SLO violation?"
- "Show me services with degrading p99 latency and projected breach times"

---

One MCP tool: `slo_breach_prediction`. Computes trend slope from recent metrics, extrapolates p99, compares against SLO, returns ranked risk list with time-to-breach.

### Flow 1 — Happy Path: Risk Detected

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as slo_breach_prediction
    participant Service as SLOBreachPredictionService
    participant Port as SLOBreachPredictionPort
    participant Adapter as OTelSLOPredictionAdapter
    participant Prom as Prometheus/OTel

    AI->>MCP: "Which services will breach SLO?"
    MCP->>Tool: slo_breach_prediction(60)

    Tool->>Service: predict(command)
    Service->>Port: fetch_trend_metrics(req)
    Port->>Adapter: OTelSLOPredictionAdapter
    Adapter->>Prom: p99 trends for all services, last 30min
    Prom-->>Adapter: auth: +8.2ms/min, payment: stable, checkout: +2.1ms/min

    Note over Service: auth: (500-320)/8.2 = 22min → HIGH<br/>checkout: (300-180)/2.1 = 57min → MEDIUM<br/>payment: slope=0 → safe

    Service-->>Tool: SLOBreachPredictionResult(at_risk=[auth, checkout], safe_count=1)
    Tool-->>MCP: {at_risk: [{service: "auth-service", breach_in_minutes: 22, risk: "high"}, ...], safe_count: 1}
    MCP-->>AI: "2 services at risk:<br/>⚠️ auth-service: breach in 22 min (slope +8.2ms/min)<br/>⚡ checkout-service: breach in 57 min (slope +2.1ms/min)<br/>1 service stable."
```

### Flow 2 — All Stable

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as slo_breach_prediction
    participant Service as SLOBreachPredictionService

    AI->>Tool: slo_breach_prediction(60)
    Tool->>Service: predict()
    Note over Service: All services have slope ≤ 0 or projected < SLO

    Service-->>Tool: at_risk=[], safe_count=5
    Tool-->>AI: "All 5 services stable — no SLO breaches projected."
```

### Flow 3 — Already Breached

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as slo_breach_prediction
    participant Service as SLOBreachPredictionService

    AI->>Tool: slo_breach_prediction(60)
    Tool->>Service: predict()
    Note over Service: auth-service current p99=820ms > SLO=500ms<br/>already breached — not a prediction

    Service-->>Tool: auth in at_risk with risk=HIGH
    Tool-->>AI: "auth-service SLO already breached (p99=820ms > 500ms). Not projected."
```

### Flow 4 — Checker Node: Math Validation

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate prediction math
    alt breach_in_minutes calculation wrong
        Checker-->>LLM: ❌ FAIL — (slo-current)/slope
    alt LLM presents prediction as certainty
        Checker-->>LLM: ⚠️ FLAG — must use "projected IF current trend continues"
    alt Stale data used (>2 min old)
        Checker-->>LLM: ⚠️ FLAG — flag data staleness in response
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **Trend slope** — linear regression on last 30 min p99 values
- **Breach time** — `(slo - current_p99) / slope` if slope > 0
- **Risk levels** — HIGH (breach ≤ 30min), MEDIUM (≤ 60min), LOW (>60min)
- **Already breached** — services above SLO flagged separately from predictions

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_ranked_risks` | `tests/unit/test_slo_breach_prediction.py` | ✅ |
| `test_no_risk` | `tests/unit/test_slo_breach_prediction.py` | ✅ |
| `test_returns_risks` | `tests/unit/test_slo_breach_prediction_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/slo_breach_prediction.py` — ServiceRisk, SLOBreachPredictionResult
- `src/hexawyn/application/ports/driven/slo_breach_prediction_port.py` — SLOBreachPredictionPort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_slo_prediction_adapter.py` — adapter
- `src/hexawyn/mcp/tools/slo_breach_prediction.py` — MCP tool
