# Use Case 14 — Estimate Rightsizing Savings

## Sample Questions

- "Which of my workloads are over-provisioned and what would I save by rightsizing them?"
- "How much money am I wasting on CPU and memory for my Kubernetes deployments?"
- "Show me the top 5 rightsizing recommendations ranked by monthly savings."
- "My ml-worker pod uses very little CPU — what should I request instead?"
- "Are any of my deployments under-provisioned and at risk of OOM kill?"

---

## Happy Path

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant UC as EstimateRightsizingSavingsUseCase
    participant Svc as EstimateRightsizingSavingsService
    participant Domain as RightsizingAnalysisService
    participant Adapter as VanillaAdapter
    participant K8s as K8s AppsV1API
    participant Metrics as metrics-server

    User->>MCP: estimate_rightsizing_savings(top_n=5)
    MCP->>UC: execute(command)
    UC->>Svc: estimate_rightsizing_savings(command)
    Svc->>Adapter: get_workload_rightsizing_data()
    Adapter->>K8s: list_deployment_for_all_namespaces()
    K8s-->>Adapter: [Deployment list]
    Adapter->>Metrics: list_cluster_custom_object(metrics.k8s.io/v1beta1/pods)
    Metrics-->>Adapter: [Pod metrics list]
    Adapter-->>Svc: [WorkloadRawData list]
    Svc->>Domain: analyze(raw_data, top_n=5)
    Domain-->>Svc: RightsizingReport
    Svc-->>UC: EstimateRightsizingSavingsResponse
    UC-->>MCP: response
    MCP-->>User: recommendations + total savings
```

---

## metrics-server Unavailable

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant Adapter as VanillaAdapter
    participant Metrics as metrics-server

    User->>MCP: estimate_rightsizing_savings()
    MCP->>Adapter: get_workload_rightsizing_data()
    Adapter->>Metrics: list_cluster_custom_object(...)
    Metrics--xAdapter: (no metrics-server installed)
    Note over Adapter: cpu_actual=None, memory_actual=None
    Adapter-->>MCP: WorkloadRawData with nulls
    Note over MCP: metrics_server_available=False
    MCP-->>User: metrics_server_available: false, recommendations: []
```

---

## Cluster Unreachable

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant Adapter as VanillaAdapter
    participant K8s as K8s API

    User->>MCP: estimate_rightsizing_savings()
    MCP->>Adapter: get_workload_rightsizing_data()
    Adapter->>K8s: list_deployment_for_all_namespaces()
    K8s--xAdapter: ConnectionError
    Adapter-->>MCP: ClusterUnreachableError
    MCP-->>User: error: "ClusterUnreachableError: ..."
```

---

## Under-Provisioned Detection (OOM Risk)

```mermaid
sequenceDiagram
    actor User
    participant Domain as RightsizingAnalysisService
    participant Adapter as VanillaAdapter

    Note over Adapter: cache pod → 972 MiB actual / 1024 MiB requested = 95%
    Adapter-->>Domain: memory_actual_mi=972, memory_requested_mi=1024
    Note over Domain: memory ratio > 85% → UNDER_PROVISIONED
    Note over Domain: recommended = actual × 2 = 1944 Mi
    Domain-->>User: type=under_provisioned, reason="RAM 95% of requests — OOM risk"
```

---

## Key Points

- **Workload data source**: K8s `AppsV1API` (deployments + stateful sets) crossed with metrics-server pod metrics.
- **Pod → workload matching**: Pod names follow `{deployment}-{rs-hash}-{pod-hash}` convention; workload name extracted via `rsplit("-", 2)[0]`.
- **Over-provisioned**: CPU < 30% of requests OR RAM < 40% of requests.
- **Under-provisioned**: RAM > 85% of requests (OOM risk). Always included — no $5 minimum filter.
- **Headroom**: 30% added for over-provisioned recommendations; ×2 for under-provisioned.
- **Pricing**: `$21.6/core/month` and `$2.88/GiB/month` (generic on-demand rates).
- **Priority**: high > $50/mo, medium > $20/mo, low > $5/mo.
- **Savings filter**: Only applied to over-provisioned; workloads below $5/mo savings are skipped and counted in `skipped_count`.

## Test Coverage

| Layer | File |
|-------|------|
| Domain models | `tests/unit/test_rightsizing.py` |
| Domain service | `tests/unit/test_rightsizing_analysis_service.py` |
| Application service + use case | `tests/unit/test_estimate_rightsizing_savings_use_case.py` |
| VanillaAdapter port | `tests/unit/test_vanilla_adapter.py::TestVanillaAdapterRightsizingPort` |
| Integration (real adapter) | `tests/integration/test_estimate_rightsizing_savings_integration.py` |

## Related Files

- `src/hexawyn/domain/models/rightsizing.py`
- `src/hexawyn/domain/services/rightsizing/rightsizing_analysis_service.py`
- `src/hexawyn/application/ports/driven/rightsizing_port.py`
- `src/hexawyn/application/ports/driving/estimate_rightsizing_savings/`
- `src/hexawyn/application/service/estimate_rightsizing_savings_service.py`
- `src/hexawyn/application/use_case/estimate_rightsizing_savings/estimate_rightsizing_savings_use_case.py`
- `src/hexawyn/mcp/tools/estimate_rightsizing_savings.py`
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py`
