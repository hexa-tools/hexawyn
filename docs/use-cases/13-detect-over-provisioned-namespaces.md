# Use Case 13 — Detect Over-Provisioned Namespaces

## Sample Questions

- "Which namespaces are wasting the most CPU and memory?"
- "Where can we reduce resource costs in the cluster?"
- "Show me the top 5 over-provisioned namespaces over the last 7 days"
- "The dev namespace has 8 CPUs allocated — how much is it actually using?"
- "What's our total estimated waste in cores and GB across all namespaces?"

---

FinOps use case: identifies namespaces where resource requests far exceed actual usage over a configurable window (default 7 days).
Waste ratio is computed independently for CPU and memory: `(requested - actual) / requested * 100`.
Namespaces with `max(cpu_waste_pct, memory_waste_pct) > 50%` are flagged as over-provisioned candidates.

---

## Flow 1 — Happy Path (dev=94% waste flagged, production=12% healthy)

```mermaid
sequenceDiagram
    participant FinOps
    participant MCP as MCP Tool<br/>(detect_over_provisioned_namespaces)
    participant UC as DetectOverProvisionedNamespacesUseCase
    participant SVC as DetectOverProvisionedNamespacesService
    participant Adapter as VanillaAdapter<br/>(NamespaceWasteAnalysisPort)
    participant K8s as Kubernetes API
    participant Prom as Prometheus API

    FinOps->>MCP: detect_over_provisioned_namespaces(window_days=7, top_n=5)
    MCP->>UC: execute(DetectOverProvisionedNamespacesCommand)
    UC->>SVC: detect_over_provisioned_namespaces(command)
    SVC->>Adapter: get_all_namespace_waste_data(window_days=7)
    Adapter->>K8s: list_namespace() → ages
    K8s-->>Adapter: [dev (720h), production (2160h)]
    Adapter->>K8s: list_pod_for_all_namespaces() → resource requests
    K8s-->>Adapter: [dev: 8CPU/16Gi, prod: 4CPU/8Gi]
    Adapter->>Prom: avg(rate(cpu_usage[7d])) by namespace
    Prom-->>Adapter: [dev: 0.45 cores, prod: 3.5 cores]
    Adapter->>Prom: avg(memory_usage[7d]) by namespace
    Prom-->>Adapter: [dev: 1.2 GB, prod: 7.5 GB]
    Adapter-->>SVC: list[NamespaceRawData]
    SVC->>SVC: NamespaceOverProvisioningService.analyze()
    Note over SVC: dev: cpu_waste=(8-0.45)/8=94.4%, mem_waste=92.5% → flagged
    Note over SVC: prod: cpu_waste=12.5%, mem_waste=6.25% → healthy
    SVC->>SVC: rank by max_waste_pct desc → [dev, production]
    SVC-->>UC: DetectOverProvisionedNamespacesResponse(report, prometheus_available=True)
    UC-->>MCP: response
    MCP-->>FinOps: {namespaces: [{dev, 94.4%, flagged}, {prod, 12.5%}], total_wasted_cores: 7.55}
```

---

## Flow 2 — Exclusions (new namespace < 24h + BestEffort pods with no requests)

```mermaid
sequenceDiagram
    participant FinOps
    participant MCP as MCP Tool
    participant Domain as NamespaceOverProvisioningService

    FinOps->>MCP: detect_over_provisioned_namespaces()
    MCP->>Domain: analyze(raw_data, top_n=5, window=7)
    Domain->>Domain: _partition(raw_data)
    Note over Domain: new-ns: age=6h < 24h → ExcludedNamespace("age < 24h")
    Note over Domain: burstable: has_requests=False → ExcludedNamespace("no requests")
    Note over Domain: dev: age=720h, has_requests=True → eligible
    Domain-->>MCP: OverProvisioningReport(namespaces=[dev], excluded=[new-ns, burstable])
    MCP-->>FinOps: {namespaces: [dev], excluded: [{new-ns, "age < 24h"}, {burstable, "no requests"}]}
```

---

## Flow 3 — Prometheus Unavailable (K8s-only mode, waste ratio not computable)

```mermaid
sequenceDiagram
    participant FinOps
    participant MCP as MCP Tool
    participant Adapter as VanillaAdapter
    participant K8s as Kubernetes API

    FinOps->>MCP: detect_over_provisioned_namespaces()
    MCP->>Adapter: get_all_namespace_waste_data(window_days=7)
    Adapter->>K8s: list_namespace() + list_pod_for_all_namespaces()
    K8s-->>Adapter: namespace ages + resource requests OK
    Note over Adapter: PROMETHEUS_URL="" → skip Prometheus queries
    Adapter-->>MCP: NamespaceRawData[cpu_actual=None, mem_actual=None]
    MCP->>MCP: NamespaceOverProvisioningService.analyze()
    Note over MCP: actual=None → waste_pct=0.0, is_over_provisioned=False
    MCP-->>FinOps: {namespaces: [dev, prod, ...], prometheus_available: false, error: null}
    Note over FinOps: Requests visible, but no waste ratio without Prometheus
```

---

## Flow 4 — Error Flows (Cluster RBAC denied / Prometheus down)

```mermaid
sequenceDiagram
    participant FinOps
    participant MCP as MCP Tool
    participant Adapter as VanillaAdapter
    participant K8s as Kubernetes API
    participant Prom as Prometheus API

    FinOps->>MCP: detect_over_provisioned_namespaces()

    alt Cluster unreachable or RBAC denied
        MCP->>Adapter: get_all_namespace_waste_data()
        Adapter->>K8s: list_namespace()
        K8s-->>Adapter: Exception (timeout / 403 Forbidden)
        Adapter->>Adapter: raise ClusterUnreachableError(...)
        Adapter-->>MCP: ClusterUnreachableError
        MCP-->>FinOps: {error: "Cannot reach K8s API: ...", namespaces: [], prometheus_available: false}
    else Prometheus down or unreachable
        MCP->>Adapter: get_all_namespace_waste_data()
        Adapter->>K8s: list_namespace() + pods — OK
        Adapter->>Prom: httpx.get(/api/v1/query)
        Prom-->>Adapter: HTTPError (connection refused / timeout)
        Adapter->>Adapter: raise PrometheusUnavailableError(url)
        Adapter-->>MCP: PrometheusUnavailableError
        MCP-->>FinOps: {error: "Prometheus unavailable at http://...", namespaces: []}
    end
```

---

## Key Points

- CPU and memory waste computed **independently** — `max(cpu_waste_pct, memory_waste_pct)` determines if a namespace is over-provisioned
- Over-provisioned threshold: **> 50%** waste on either resource
- Namespaces younger than 24h or with no resource requests are **excluded**, never errored
- Prometheus is **optional** — without it, requests are listed but `waste_pct = 0.0`
- Results ranked by `max_waste_pct` descending; `top_n` (default 5) caps output

## Test Coverage

| Test | File | Scenario |
|---|---|---|
| `test_dev_namespace_94_pct_cpu_waste` | `test_namespace_over_provisioning_service.py` | Formula: (8-0.45)/8×100 = 94.4% |
| `test_dev_94pct_waste_is_flagged` | `test_namespace_over_provisioning_service.py` | Flagging threshold > 50% |
| `test_no_resource_requests_excluded` | `test_namespace_over_provisioning_service.py` | BestEffort exclusion |
| `test_recently_created_namespace_excluded` | `test_namespace_over_provisioning_service.py` | Age < 24h exclusion |
| `test_ranking_dev_before_staging_before_prod` | `test_namespace_over_provisioning_service.py` | Ranking by max_waste_pct |
| `test_namespace_included_when_no_prometheus_data` | `test_namespace_over_provisioning_service.py` | Prometheus unavailable — no flagging |
| `test_tc1_dev_flagged_production_healthy` | `test_detect_over_provisioned_namespaces_integration.py` | Integration TC1 |
| `test_tc2_recently_created_namespace_excluded` | `test_detect_over_provisioned_namespaces_integration.py` | Integration TC2 |
| `test_prometheus_unavailable_raises_error` | `test_detect_over_provisioned_namespaces_integration.py` | Prometheus down → error |
| `test_waste_ratio_formula_correct` | `test_detect_over_provisioned_namespaces_integration.py` | Formula end-to-end |

## Related Files

- `src/hexawyn/domain/models/namespace_waste.py` — `NamespaceWaste`, `ExcludedNamespace`, `OverProvisioningReport`
- `src/hexawyn/domain/services/namespace_waste/namespace_over_provisioning_service.py` — pure waste computation
- `src/hexawyn/application/ports/driven/namespace_waste_port.py` — `NamespaceRawData`, `NamespaceWasteAnalysisPort`
- `src/hexawyn/application/service/detect_over_provisioned_namespaces_service.py` — orchestration
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py` — K8s + Prometheus data fetch
- `src/hexawyn/mcp/tools/detect_over_provisioned_namespaces.py` — MCP entry point
