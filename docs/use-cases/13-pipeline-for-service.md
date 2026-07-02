# Use Case 13 — Pipeline for Service

## Sample Questions

- "Find the pipeline responsible for deploying the checkout service"
- "Which repository and branch does the payment-service pipeline use?"
- "What pipeline builds the auth-service and what is its trigger?"
- "Are there multiple pipelines for the order service?"
- "Show me the last run status of the deployment pipeline for checkout-service"

---

One MCP tool: `pipeline_for_service`. Finds Tekton/ArgoCD pipelines associated with a service, returns repo URL, branch, trigger config, last run status.

### Flow 1 — Happy Path: Pipeline Found

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as pipeline_for_service
    participant Service as PipelineForServiceService
    participant Port as PipelineForServicePort
    participant Adapter as KubernetesPipelineForServiceAdapter
    participant K8s as Kubernetes API

    AI->>MCP: "Which pipeline deploys checkout?"
    MCP->>Tool: pipeline_for_service("checkout-service")

    Tool->>Service: find(command)
    Service->>Port: find_pipelines(req)
    Port->>Adapter: KubernetesPipelineForServiceAdapter
    Adapter->>K8s: search PipelineRuns with label service=checkout-service
    K8s-->>Adapter: deploy-checkout found

    Note over Service: pipeline: deploy-checkout, repo: github.com/org/checkout, branch: main, trigger: webhook

    Service-->>Tool: PipelineForServiceResponse(pipelines_found=1)
    Tool-->>MCP: {pipelines_found: 1, pipelines: [{name: "deploy-checkout", repo_url: "...", branch: "main"}]}
    MCP-->>AI: "checkout-service deployed by 'deploy-checkout' (ci namespace). Repo: github.com/org/checkout, branch: main. Trigger: webhook. Last run: succeeded at 10:00."
```

### Flow 2 — Multiple Pipelines

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as pipeline_for_service
    participant Service as PipelineForServiceService

    AI->>Tool: pipeline_for_service("payment-service")
    Tool->>Service: find()
    Note over Service: 2 pipelines found: build-payment (webhook) + release-payment (manual)

    Service-->>Tool: pipelines_found=2
    Tool-->>AI: "2 pipelines for payment-service:<br/>1. build-payment — webhook — main<br/>2. release-payment — manual — release"
```

### Flow 3 — Not Found

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as pipeline_for_service
    participant Service as PipelineForServiceService

    AI->>Tool: pipeline_for_service("ghost-service")
    Tool->>Service: find()
    Note over Service: pipelines=[], pipelines_found=0

    Service-->>Tool: pipelines_found=0
    Tool-->>AI: "No pipeline found for 'ghost-service'."
```

### Flow 4 — Checker Node: Monorepo Detection

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate pipeline attribution
    alt Pipeline uses monorepo but subdirectory not mentioned
        Checker-->>LLM: ⚠️ FLAG — monorepo subdirectory path must be shown
    alt LLM confuses webhook trigger with cron schedule
        Checker-->>LLM: ❌ FAIL — trigger type must match actual config
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **Service→Pipeline mapping** — searches by label/annotation matching service name
- **Trigger types** — webhook, schedule (cron), manual
- **Multi-pipeline** — all pipelines returned if service has build + release
- **Last run** — most recent PipelineRun status + timestamp

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_pipeline_found` | `tests/unit/test_pipeline_for_service.py` | ✅ |
| `test_multiple_pipelines` | `tests/unit/test_pipeline_for_service.py` | ✅ |
| `test_not_found` | `tests/unit/test_pipeline_for_service.py` | ✅ |
| `test_finds_pipeline` | `tests/unit/test_pipeline_for_service_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/pipeline_for_service.py` — ServicePipeline, PipelineForServiceResult
- `src/hexawyn/application/ports/driven/pipeline_for_service_port.py` — PipelineForServicePort ABC
- `src/hexawyn/adapters/secondary/gitops/kubernetes_pipeline_for_service_adapter.py` — adapter
- `src/hexawyn/mcp/tools/pipeline_for_service.py` — MCP tool
