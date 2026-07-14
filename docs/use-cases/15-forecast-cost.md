# Use Case 15 — Forecast Cost (Cost Predictive Model)

## Sample Questions

- "How much will I spend this month in total on my Kubernetes cluster?"
- "Is my spend accelerating compared to previous weeks?"
- "Which are the 3 most expensive namespaces this month?"
- "My monthly budget is $2,000 — am I going to exceed it?"
- "What is my Cloud spend trend compared to last month?"

---

## Happy Path

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant UC as ForecastCostUseCase
    participant Svc as ForecastCostService
    participant Engine as CostForecastEngine
    participant Adapter as VanillaAdapter
    participant K8s as K8s AppsV1 API

    User->>MCP: forecast_cost(historical_days=7)
    MCP->>UC: execute(command)
    UC->>Svc: forecast_cost(command)
    Svc->>Adapter: get_daily_costs(days=7)
    Adapter->>K8s: list_deployment_for_all_namespaces()
    K8s-->>Adapter: [Deployment list]
    Note over Adapter: cpu × $21.6/core/month + mem × $2.88/GiB/month ÷ 30
    Adapter-->>Svc: [DailyCostData × 7 jours]
    Svc->>Engine: forecast(daily_costs, days_elapsed, days_in_month, ...)
    Note over Engine: current_spend = daily_rate × days_elapsed<br/>trend_factor = recent_avg / overall_avg<br/>projected = current + daily_avg × trend × days_remaining
    Engine-->>Svc: CostForecast
    Svc-->>UC: ForecastCostResponse
    UC-->>MCP: response
    MCP-->>User: projected_total, trend_factor, top_cost_drivers
```

---

## Acceleration Detection (trend > 1.0)

```mermaid
sequenceDiagram
    actor User
    participant Engine as CostForecastEngine
    participant Adapter as VanillaAdapter

    Note over Adapter: D1-D4: $40/day → D5-D7: $80/day
    Adapter-->>Engine: daily_costs (7 non-uniform points)
    Note over Engine: recent_avg (3d) = $80<br/>overall_avg (7d) = $57<br/>trend_factor = 80/57 = 1.40
    Note over Engine: projected_total × 1.40 → overrun alert
    Engine-->>User: trend_factor: 1.40, forecast_confidence: "low"
```

---

## Cluster Unreachable

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant Adapter as VanillaAdapter
    participant K8s as K8s API

    User->>MCP: forecast_cost()
    MCP->>Adapter: get_daily_costs(7)
    Adapter->>K8s: list_deployment_for_all_namespaces()
    K8s--xAdapter: ConnectionError / Forbidden
    Adapter-->>MCP: ClusterUnreachableError
    MCP-->>User: error: "ClusterUnreachableError: ..."
```

---

## Pro Tier — Real Billing (ECA-115, post v1.0)

```mermaid
sequenceDiagram
    actor User
    participant Svc as ForecastCostService
    participant Adapter as AWSCostAdapter
    participant AWS as AWS Cost Explorer

    Note over Svc: same engine, different adapter
    Svc->>Adapter: get_daily_costs(days=90)
    Adapter->>AWS: GetCostAndUsage(90d)
    AWS-->>Adapter: [real DailyCostData]
    Note over Adapter: billing_events: spot expiry, savings plan renewal
    Adapter-->>Svc: 90 real points + BillingEvent[]
    Note over Svc: forecast_confidence="high", data_source="aws"
    Svc-->>User: precise projection + billing events
```

---

## Key Points

- **Free formula**: `daily_rate = resource_requests × pricing_constants / 30` — same constants as rightsizing (`$21.6/core/month`, `$2.88/GiB/month`).
- **Trend**: `trend_factor = avg(last 3 days) / avg(overall)`. 3-day sliding window.
- **Free tier**: 7 days of estimated history, all identical → `trend_factor = 1.0`, `confidence = "low"`.
- **Projection**: `projected = current_spend + daily_avg × trend_factor × days_remaining`.
- **Top drivers**: namespaces sorted by aggregated daily cost, converted to estimated monthly cost.
- **`previous_month_usd`**: `None` on Free (no real history). MoM delta = 0% by default.
- **Same engine** for Free and Pro — only the adapter's data quality changes.

## Test Coverage

| Layer | File |
|-------|---------|
| Domain models | `tests/unit/test_cost_forecast_models.py` |
| Domain service | `tests/unit/test_cost_forecast_engine.py` |
| Port + app service + use case | `tests/unit/test_forecast_cost_port_and_service.py` |
| MCP tool + VanillaAdapter | `tests/unit/test_forecast_cost_mcp_and_adapter.py` |
| Integration (real adapter) | `tests/integration/test_forecast_cost_integration.py` |

## Related Files

- `src/hexawyn/domain/models/cost_forecast.py`
- `src/hexawyn/domain/services/cost_forecast/cost_forecast_engine.py`
- `src/hexawyn/application/ports/driven/cost_forecast_port.py`
- `src/hexawyn/application/ports/driving/forecast_cost/`
- `src/hexawyn/application/service/forecast_cost_service.py`
- `src/hexawyn/application/use_case/forecast_cost/forecast_cost_use_case.py`
- `src/hexawyn/mcp/tools/forecast_cost.py`
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py`
