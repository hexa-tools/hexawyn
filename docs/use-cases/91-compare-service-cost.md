# 91 — Compare Service Cost (Month-over-Month)

Compare the total infrastructure cost of a service between current month
and previous month, with pod-level breakdown and trend indication.

## Sample Questions

- "What is the total infrastructure cost of the payment-service this month vs last month?"
- "How has the cost of auth-service changed month-over-month?"
- "Show me the cost breakdown by pod for payment-service this month."
- "Did the checkout-service cost decrease after our optimization efforts?"

---

## 1. Happy Path

```mermaid
sequenceDiagram
    participant User
    participant MCP as MCP Tool
    participant UC as UseCase
    participant Svc as Service
    participant Engine as ServiceCostComparisonEngine
    participant Port as ServiceCostPort
    participant Adapter as ServiceCostPrometheusAdapter
    participant Prom as Prometheus

    User->>MCP: compare_service_cost("payment-service")
    MCP->>Svc: CompareServiceCostService(port)
    MCP->>UC: execute(command)
    UC->>Svc: compare(command)
    Svc->>Svc: compute current month (2026-07, 31 days)
    Svc->>Svc: compute previous month (2026-06, 30 days)
    Svc->>Port: fetch_pod_resources("payment-service", "2026-07")
    Svc->>Port: fetch_pod_resources("payment-service", "2026-06")
    Port->>Adapter: fetch_pod_resources()
    Adapter->>Prom: sum(rate(container_cpu_usage[...]))
    Prom-->>Adapter: pod resource data
    Adapter-->>Port: list[PodResourceSnapshotData]
    Svc->>Engine: compute(service, current_pods, previous_pods, pricing)
    Engine->>Engine: cost = cpu_cores×price×hours + mem_gb×price×hours
    Engine->>Engine: delta_pct = (current-prev)/prev×100
    Engine->>Engine: classify trend (stable/increasing/decreasing)
    Engine-->>Svc: ServiceCostComparison
    MCP-->>User: trend=stable, delta=+3.3%, pod breakdown
```

---

## Key Points

- Cost formula: `(cpu_cores × price_per_core_hour + memory_gb × price_per_gb_hour) × days × 24`
- Month lengths auto-detected (28/29/30/31 days)
- Trend classification: >10% delta = increasing, <-10% = decreasing, else stable
- No Prometheus data → no_data verdict with recommendation
- Pod-level breakdown shows per-pod CPU/memory cost

---

## Related Files

- `src/hexawyn/domain/models/service_cost_comparison.py`
- `src/hexawyn/domain/services/service_cost/service_cost_comparison_engine.py`
- `src/hexawyn/application/ports/driven/service_cost_port.py`
- `src/hexawyn/application/ports/driving/compare_service_cost/`
- `src/hexawyn/application/service/compare_service_cost_service.py`
- `src/hexawyn/mcp/tools/compare_service_cost.py`
