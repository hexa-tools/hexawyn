# Use Case 11 — List Pipeline Runs

## Sample Questions

- "Show me the last 10 pipeline runs for the payment-service — what is the success rate?"
- "How often does the checkout pipeline fail?"
- "What's the average build time for the auth-service?"
- "Are there any abnormally slow runs in the payment pipeline recently?"

---

## Happy Path — 10 runs, stats computed

```mermaid
sequenceDiagram
    participant EM as Engineering Manager
    participant MCP as MCP Tool<br/>(list_pipeline_runs)
    participant UC as ListPipelineRunsUseCase
    participant SVC as ListPipelineRunsService
    participant PORT as TektonPort
    participant K8S as VanillaAdapter<br/>(Tekton CRD API)

    EM->>MCP: list_pipeline_runs("payment-service", namespace="ci", limit=10)
    MCP->>UC: execute(ListPipelineRunsCommand)
    UC->>SVC: list_pipeline_runs(command)
    SVC->>PORT: list_pipeline_runs("payment-service", "ci")
    PORT->>K8S: list_namespaced_custom_object(pipelineruns, label=payment-service)
    K8S-->>PORT: [{name, status, startTime, completionTime, annotations}...]
    PORT-->>SVC: list[PipelineRunInfo] (10 runs)
    SVC->>SVC: sort by start_time desc
    SVC->>SVC: compute stats (success_rate=80%, avg=4m30s)
    SVC->>SVC: detect outliers (duration > 2x average)
    SVC-->>UC: ListPipelineRunsResponse(runs, stats, outliers=[], note=None)
    UC-->>MCP: ListPipelineRunsResponse
    MCP-->>EM: {runs: [...], stats: {success_rate: 80.0, avg: 270s}, outliers: [], note: null}
```

---

## TC2 — Outlier detected (run took 22min vs average 5min)

```mermaid
sequenceDiagram
    participant EM as Engineering Manager
    participant MCP as MCP Tool
    participant SVC as ListPipelineRunsService

    EM->>MCP: list_pipeline_runs("payment-service")
    MCP->>SVC: list_pipeline_runs(command)
    SVC->>SVC: average_duration = 300s (5min)
    SVC->>SVC: outlier_threshold = 600s (2x)
    SVC->>SVC: run "payment-run-outlier" = 1320s (22min) > 600s → OUTLIER
    SVC-->>MCP: ListPipelineRunsResponse(outliers=["payment-run-outlier"])
    MCP-->>EM: {outliers: ["payment-run-outlier"], stats: {average_duration_seconds: 300}}
```

---

## TC3 — Fewer than 10 runs available

```mermaid
sequenceDiagram
    participant EM as Engineering Manager
    participant MCP as MCP Tool
    participant SVC as ListPipelineRunsService
    participant PORT as TektonPort

    EM->>MCP: list_pipeline_runs("payment-service", limit=10)
    MCP->>SVC: list_pipeline_runs(command)
    SVC->>PORT: list_pipeline_runs("payment-service", "ci")
    PORT-->>SVC: list[PipelineRunInfo] (3 runs only)
    SVC->>SVC: len(runs)=3 < limit=10 → note = "Only 3 run(s) available."
    SVC-->>MCP: ListPipelineRunsResponse(runs=[...3 runs...], note="Only 3 run(s) available.")
    MCP-->>EM: {runs: [...], note: "Only 3 run(s) available.", error: null}
```

---

## TC4 — Service not found

```mermaid
sequenceDiagram
    participant EM as Engineering Manager
    participant MCP as MCP Tool<br/>(final catch)
    participant SVC as ListPipelineRunsService
    participant PORT as TektonPort
    participant K8S as VanillaAdapter

    EM->>MCP: list_pipeline_runs("unknown-service")
    MCP->>SVC: list_pipeline_runs(command)
    SVC->>PORT: list_pipeline_runs("unknown-service", "ci")
    PORT->>K8S: list_namespaced_custom_object(label=unknown-service)
    K8S-->>PORT: {items: []} (empty)
    PORT->>PORT: items empty → raise ServiceNotFoundError("unknown-service")
    PORT-->>SVC: ServiceNotFoundError
    SVC-->>MCP: ServiceNotFoundError (never caught — propagates)
    MCP->>MCP: except Exception → capture error message
    MCP-->>EM: {runs: [], stats: {}, error: "No pipelines found for service 'unknown-service'."}
```
