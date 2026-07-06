# 87 — Compute SLO Error Budget Burn Rate

Compute the SLO error budget burn rate for a service by querying Prometheus
for actual success rate, then calculating total error budget, consumed budget,
remaining budget, burn rate multiplier, and time-to-exhaustion.

## Sample Questions

- "What is the current error budget burn rate for the payment-service SLO — are we on track to exhaust the error budget before end of month?"
- "How much error budget remains for auth-service with an SLO of 99.9%?"
- "Is the payment-service at risk of breaching its 30-day SLO?"
- "Show me the burn rate and time-to-exhaustion for all production services"
- "Has the checkout-service already exhausted its error budget this month?"

---

## 1. Happy Path — Full Hexagonal Chain

```mermaid
sequenceDiagram
    participant User
    participant MCP as MCP Tool
    participant UC as ComputeSLOErrorBudgetUseCase
    participant Svc as ComputeSLOErrorBudgetService
    participant Engine as SLOErrorBudgetBurnRateEngine
    participant Port as ErrorBudgetPort
    participant Adapter as PrometheusErrorBudgetAdapter
    participant Prom as Prometheus

    User->>MCP: compute_slo_error_budget("payment-service", 0.999, 30)
    MCP->>MCP: build_error_budget_adapter()
    MCP->>Svc: ComputeSLOErrorBudgetService(port=adapter)
    MCP->>UC: ComputeSLOErrorBudgetUseCase(service=svc)
    MCP->>UC: execute(command)
    UC->>Svc: compute_slo_error_budget(command)
    Svc->>Port: fetch_success_rate("payment-service", 30)
    Port->>Adapter: fetch_success_rate("payment-service", 30)

    Note over Adapter: build PromQL: rate(5xx)/rate(all)
    Adapter->>Prom: instant_query(promql, 15s)
    Prom-->>Adapter: [{success_rate: 0.995}]
    Adapter-->>Port: ServiceSuccessRateRawData

    Port-->>Svc: raw data
    Svc->>Engine: compute(slo=0.999, window=30d, raw)
    Engine->>Engine: budget = (1-0.999)*43200 = 43.2 min
    Engine->>Engine: burn_rate = 0.005/0.001 = 5.0x
    Engine->>Engine: consumed = 0.005*43200 = 216 min
    Engine->>Engine: remaining = (43.2-216)/43.2*100 = -400%
    Engine->>Engine: verdict = budget_exhausted
    Engine-->>Svc: SLOErrorBudgetResult
    Svc-->>UC: ComputeSLOErrorBudgetResponse
    UC-->>MCP: response

    Note over MCP: serialize to dict
    MCP-->>User: burn_rate=5.0, verdict=budget_exhausted
```

## 2. Error Flows

```mermaid
sequenceDiagram
    participant MCP as MCP Tool
    participant Svc as Service
    participant Adapter as PrometheusErrorBudgetAdapter
    participant Prom as Prometheus

    alt Prometheus Unreachable
        Adapter->>Prom: instant_query()
        Prom-->>Adapter: HTTPError / Timeout
        Adapter->>Adapter: catch Exception
        Adapter-->>Svc: ServiceSuccessRateRawData(has_data=False)
        Svc->>Svc: Engine returns no_data verdict
        MCP-->>User: {"verdict": "no_data"}
    else PromQL Error (HTTP 400)
        Adapter->>Prom: instant_query()
        Prom-->>Adapter: 400 Bad Request
        Adapter->>Adapter: catch Exception
        Adapter-->>Svc: ServiceSuccessRateRawData(has_data=False)
        MCP-->>User: {"verdict": "no_data"}
    else No Traffic (empty response)
        Adapter->>Prom: instant_query()
        Prom-->>Adapter: [] (empty)
        Adapter-->>Svc: ServiceSuccessRateRawData(has_data=False, total_requests=0)
        Engine-->>Svc: verdict = no_data
        MCP-->>User: {"verdict": "no_data", "recommendation": "No traffic data available"}
    end
```

## 3. Checker Node Flow

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Engine as SLOErrorBudgetBurnRateEngine

    Checker->>Engine: compute(slo=0.999, raw)

    alt PASS — budget_safe (0 errors)
        Engine-->>Checker: burn_rate=0, verdict=budget_safe
        Checker-->>User: "No errors — budget fully intact"
    else FLAG — better than SLO but not mentioned
        Engine-->>Checker: burn_rate=0.5, verdict=budget_accumulating
        Checker->>Checker: verify recommendation mentions "accumulating"
        Checker-->>User: "Budget accumulating ✓"
    else FAIL — burn rate math incorrect
        Engine-->>Checker: burn_rate=5.0, LLM says "4x"
        Checker->>Checker: error_rate/error_budget_rate = 5.0 ≠ 4.0
        Checker-->>User: "FAIL: burn rate mismatch — recalculating"
    else BLOCKED — budget remaining sign wrong
        Engine-->>Checker: remaining=-400%, LLM says "budget at risk"
        Checker->>Checker: remaining < 0 → must be budget_exhausted
        Checker-->>User: "FAIL: incorrect verdict for negative remaining"
    end
```

## 4. Verdict Classification Logic

```mermaid
sequenceDiagram
    participant Engine as Engine
    participant Classify as _classify_verdict

    Engine->>Classify: classify(burn_rate=5.0, remaining_pct=-400%)
    alt remaining_pct <= 0
        Classify-->>Engine: budget_exhausted
    else burn_rate >= 1.0 AND remaining > 0
        Classify-->>Engine: budget_at_risk
    else burn_rate == 0.0
        Classify-->>Engine: budget_safe
    else burn_rate < 1.0
        Classify-->>Engine: budget_accumulating
    end
```

---

## Key Points

- Queries Prometheus for actual success rate via `MetricsQueryPort` (PromQL aggregation on HTTP codes)
- Computes error budget as `(1 - SLO_target) × window_minutes` — deterministic domain math
- Burn rate multiplier = `error_rate / (1 - SLO_target)` — how many times faster than allowed
- Budget consumption uses observation window (e.g. 7-day partial window into 30-day SLO) — partial windows can have remaining budget even with burn_rate > 1
- Default SLO of 99.5% when none is configured for the service
- Prometheus errors (unreachable, bad query, empty result) are caught in the adapter and translate to `no_data` verdict — never crash

---

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_burn_rate_5x_when_burning_fast` | `tests/unit/test_slo_error_budget_engine.py` | ✅ |
| `test_burn_rate_zero_when_no_errors` | `tests/unit/test_slo_error_budget_engine.py` | ✅ |
| `test_budget_already_exhausted_negative_remaining` | `tests/unit/test_slo_error_budget_engine.py` | ✅ |
| `test_at_risk_with_partial_window_observation` | `tests/unit/test_slo_error_budget_engine.py` | ✅ |
| `test_budget_barely_below_slo_at_risk` | `tests/unit/test_slo_error_budget_engine.py` | ✅ |
| `test_no_data_verdict` | `tests/unit/test_slo_error_budget_engine.py` | ✅ |
| `test_default_slo_995_when_not_configured` | `tests/unit/test_slo_error_budget_engine.py` | ✅ |
| `test_zero_requests_in_window_budget_not_consumed` | `tests/unit/test_slo_error_budget_engine.py` | ✅ |
| `test_calls_port_with_correct_args` | `tests/unit/test_error_budget_port_and_service.py` | ✅ |
| `test_burn_rate_5x_returns_exhausted_verdict` | `tests/unit/test_error_budget_port_and_service.py` | ✅ |
| `test_delegates_to_service` | `tests/unit/test_error_budget_port_and_service.py` | ✅ |
| `test_delegates_and_returns_dict` | `tests/unit/test_compute_slo_error_budget_mcp.py` | ✅ |
| `test_build_error_budget_adapter_returns_error_budget_port` | `tests/unit/test_server.py` | ✅ |

---

## Related Files

- `src/hexawyn/domain/models/error_budget.py` — SLOErrorBudgetRequest, SLOErrorBudgetResult
- `src/hexawyn/domain/services/error_budget/slo_error_budget_engine.py` — pure domain computation
- `src/hexawyn/application/ports/driven/error_budget_port.py` — driven port ABC + TypedDict
- `src/hexawyn/application/ports/driving/compute_slo_error_budget/` — command, response, service port
- `src/hexawyn/application/service/compute_slo_error_budget_service.py` — application service
- `src/hexawyn/application/use_case/compute_slo_error_budget/` — use case orchestrator
- `src/hexawyn/adapters/secondary/gitops/prometheus_error_budget_adapter.py` — Prometheus adapter
- `src/hexawyn/mcp/server.py` — build_error_budget_adapter()
- `src/hexawyn/mcp/tools/compute_slo_error_budget.py` — MCP tool
