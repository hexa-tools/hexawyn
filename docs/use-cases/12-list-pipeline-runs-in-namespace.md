# Use Case 12 — List PipelineRuns in Namespace

**Actor:** SRE / On-call engineer  
**Goal:** Get an operational overview of all PipelineRuns in a given namespace, sorted by urgency (Failed first, then Running, then Succeeded), with stuck detection for Running pipelines that have been running for more than 1 hour.

---

## TC1 — Happy Path (5 runs: 2 Failed, 1 Running, 2 Succeeded)

```mermaid
sequenceDiagram
    participant SRE
    participant MCP as MCP Tool<br/>(list_pipeline_runs_in_namespace)
    participant UC as ListPipelineRunsInNamespaceUseCase
    participant SVC as ListPipelineRunsInNamespaceService
    participant TektonPort
    participant VanillaAdapter

    SRE->>MCP: list_pipeline_runs_in_namespace(namespace="tekton")
    MCP->>UC: execute(command)
    UC->>SVC: list_pipeline_runs_in_namespace(command)
    SVC->>TektonPort: list_pipeline_runs_in_namespace("tekton", limit=100)
    TektonPort->>VanillaAdapter: list_namespaced_custom_object(group, version, namespace, plural)
    VanillaAdapter-->>TektonPort: [{name: "deploy-payment-v3", status: Failed, ...}, ...]
    TektonPort-->>SVC: [5 NamespacedPipelineRunInfo items]
    SVC->>SVC: _sort_by_status_then_time(runs)
    SVC->>SVC: _find_stuck_runs(sorted_runs)
    SVC-->>UC: ListPipelineRunsInNamespaceResponse(runs=[Failed×2, Running×1, Succeeded×2], stuck_runs=[], note=None)
    UC-->>MCP: response
    MCP-->>SRE: {runs: [{...is_stuck: false}, ...], stuck_runs: [], note: null, error: null}
```

---

## TC2 — Empty Namespace (returns informative note, not an error)

```mermaid
sequenceDiagram
    participant SRE
    participant MCP as MCP Tool
    participant UC as ListPipelineRunsInNamespaceUseCase
    participant SVC as ListPipelineRunsInNamespaceService
    participant VanillaAdapter

    SRE->>MCP: list_pipeline_runs_in_namespace(namespace="staging")
    MCP->>UC: execute(command)
    UC->>SVC: list_pipeline_runs_in_namespace(command)
    SVC->>VanillaAdapter: list_pipeline_runs_in_namespace("staging", limit=100)
    VanillaAdapter-->>SVC: [] (empty list — no CRD items)
    SVC->>SVC: note = "No PipelineRuns found in namespace 'staging'."
    SVC-->>UC: ListPipelineRunsInNamespaceResponse(runs=[], stuck_runs=[], note="No PipelineRuns found...")
    UC-->>MCP: response
    MCP-->>SRE: {runs: [], stuck_runs: [], note: "No PipelineRuns found in namespace 'staging'.", error: null}
```

---

## TC3 — Stuck Detection (Running > 1 hour)

```mermaid
sequenceDiagram
    participant SRE
    participant MCP as MCP Tool
    participant SVC as ListPipelineRunsInNamespaceService

    SRE->>MCP: list_pipeline_runs_in_namespace(namespace="ci")
    MCP->>SVC: list_pipeline_runs_in_namespace(command)
    SVC->>SVC: fetch all runs from adapter
    SVC->>SVC: _find_stuck_runs(runs)
    note right of SVC: run "deploy-checkout-v5" is Running<br/>start_time = 2h ago → elapsed > 3600s → STUCK
    SVC-->>MCP: ListPipelineRunsInNamespaceResponse(stuck_runs=["deploy-checkout-v5"])
    MCP-->>SRE: {runs: [{name: "deploy-checkout-v5", is_stuck: true, ...}], stuck_runs: ["deploy-checkout-v5"], error: null}
```

---

## TC4 — RBAC Denied (InsufficientPermissionsError)

```mermaid
sequenceDiagram
    participant SRE
    participant MCP as MCP Tool
    participant VanillaAdapter
    participant K8sAPI as Kubernetes API

    SRE->>MCP: list_pipeline_runs_in_namespace(namespace="prod")
    MCP->>VanillaAdapter: list_pipeline_runs_in_namespace("prod", limit=100)
    VanillaAdapter->>K8sAPI: list_namespaced_custom_object(...)
    K8sAPI-->>VanillaAdapter: ApiException(status=403, reason="Forbidden")
    VanillaAdapter->>VanillaAdapter: raise InsufficientPermissionsError(...)
    VanillaAdapter-->>MCP: InsufficientPermissionsError
    MCP-->>SRE: {runs: [], stuck_runs: [], note: null, error: "Access denied to namespace 'prod': Forbidden"}
```

---

## TC5 — Tekton Not Installed (TektonNotInstalledError)

```mermaid
sequenceDiagram
    participant SRE
    participant MCP as MCP Tool
    participant VanillaAdapter
    participant K8sAPI as Kubernetes API

    SRE->>MCP: list_pipeline_runs_in_namespace(namespace="tekton")
    MCP->>VanillaAdapter: list_pipeline_runs_in_namespace("tekton", limit=100)
    VanillaAdapter->>K8sAPI: list_namespaced_custom_object(group="tekton.dev", ...)
    K8sAPI-->>VanillaAdapter: ApiException(status=404, reason="Not Found")
    VanillaAdapter->>VanillaAdapter: raise TektonNotInstalledError()
    VanillaAdapter-->>MCP: TektonNotInstalledError
    MCP-->>SRE: {runs: [], stuck_runs: [], note: null, error: "Tekton is not installed in this cluster. Install Tekton Pipelines first."}
```
