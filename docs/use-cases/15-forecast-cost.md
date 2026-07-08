# Use Case 15 — Forecast Cost (Cost Predictive Model)

## Sample Questions

- "Combien vais-je dépenser ce mois en tout sur mon cluster Kubernetes ?"
- "Est-ce que mon spend accélère par rapport aux semaines précédentes ?"
- "Quels sont les 3 namespaces qui coûtent le plus cher ce mois-ci ?"
- "Mon budget mensuel est $2,000 — est-ce que je vais le dépasser ?"
- "Quelle est la tendance de mon spend Cloud par rapport au mois dernier ?"

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

## Détection d'accélération (trend > 1.0)

```mermaid
sequenceDiagram
    actor User
    participant Engine as CostForecastEngine
    participant Adapter as VanillaAdapter

    Note over Adapter: J1-J4: $40/jour → J5-J7: $80/jour
    Adapter-->>Engine: daily_costs (7 points non-uniformes)
    Note over Engine: recent_avg (3j) = $80<br/>overall_avg (7j) = $57<br/>trend_factor = 80/57 = 1.40
    Note over Engine: projected_total × 1.40 → alerte dépassement
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

## Pro Tier — Billing Réel (ECA-115, post v1.0)

```mermaid
sequenceDiagram
    actor User
    participant Svc as ForecastCostService
    participant Adapter as AWSCostAdapter
    participant AWS as AWS Cost Explorer

    Note over Svc: même engine, adapter différent
    Svc->>Adapter: get_daily_costs(days=90)
    Adapter->>AWS: GetCostAndUsage(90j)
    AWS-->>Adapter: [DailyCostData réels]
    Note over Adapter: billing_events: spot expiry, savings plan renewal
    Adapter-->>Svc: 90 points réels + BillingEvent[]
    Note over Svc: forecast_confidence="high", data_source="aws"
    Svc-->>User: projection précise + événements billing
```

---

## Key Points

- **Formule Free** : `daily_rate = resource_requests × pricing_constants / 30` — même constantes que le rightsizing (`$21.6/core/month`, `$2.88/GiB/month`).
- **Tendance** : `trend_factor = avg(3 derniers jours) / avg(global)`. Fenêtre glissante de 3 jours.
- **Free tier** : 7 jours d'historique estimé, tous identiques → `trend_factor = 1.0`, `confidence = "low"`.
- **Projection** : `projected = current_spend + daily_avg × trend_factor × days_remaining`.
- **Top drivers** : namespaces triés par coût journalier agrégé, convertis en coût mensuel estimé.
- **`previous_month_usd`** : `None` en Free (pas d'historique réel). Delta MoM = 0% par défaut.
- **Même engine** pour Free et Pro — seule la qualité des données de l'adapter change.

## Test Coverage

| Layer | Fichier |
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
