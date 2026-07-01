# Use Case 41 — GitOps Detection (Flux CD / Argo CD)

## Sample Questions

- "Does my cluster use Flux or Argo CD?"
- "Which GitOps engine is installed and show me its apps"
- "Montre-moi le statut de toutes mes apps Argo CD"
- "Why is my payments-api HelmRelease not synced with Git?"
- "What is the latest commit deployed to my cluster via GitOps?"

---

Seven MCP tools for GitOps detection: `gitops_detect` (auto-detects Flux vs Argo CD), `gitops_apps_list` (lists all HelmReleases/Kustomizations/Applications), `gitops_app_get` (detail with sync message), `gitops_app_status` (sync + health), `gitops_app_sync` (read-only sync status), `gitops_sources_list` (GitRepositories, HelmRepositories), `gitops_source_get` (source connection status). All tools are read-only — no sync triggered.

### Flow 1 — Happy Path: Auto-Detect + List Apps

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as gitops_detect / gitops_apps_list
    participant UseCase as GitOpsDetectUseCase
    participant Service as GitOpsDetectService
    participant Port as GitOpsPort (ABC)
    participant Detector as GitOpsDetector
    participant K8s as Kubernetes API

    AI->>MCP: Call "gitops_detect"
    MCP->>Tool: @mcp.tool() dispatch

    Tool->>UseCase: execute(GitOpsDetectCommand())
    UseCase->>Service: detect(command)
    Service->>Port: detect_engine()

    Port->>Detector: GitOpsDetector()
    Detector->>K8s: Check Flux CRDs (helm.toolkit.fluxcd.io)
    K8s-->>Detector: ✅ CRD found

    Note over Detector: FluxAdapter instantiated<br/>helm.toolkit.fluxcd.io/v2

    Detector-->>Port: GitOpsDetectionResult(engine=FLUX, version=v2.4.0,<br/>apps_count=12, out_of_sync_count=2)

    Port-->>Service: result
    Service-->>UseCase: GitOpsDetectResponse(engine="flux", apps_count=12)
    UseCase-->>Tool: response
    Tool-->>MCP: {engine: "flux", apps_count: 12, error: null}
    MCP-->>AI: "Flux CD v2.4.0 detected.<br/>12 apps managed, 2 out-of-sync, 1 failed."
```

### Flow 2 — Error: No GitOps Engine Found

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as gitops_detect
    participant Detector as GitOpsDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "gitops_detect"
    Tool->>Detector: detect_engine()

    Detector->>K8s: Check Flux CRDs
    K8s-->>Detector: ❌ Not found
    Detector->>K8s: Check Argo CD CRDs
    K8s-->>Detector: ❌ Not found

    Note over Detector: GitOpsEngineNotFoundError<br/>"No GitOps engine detected"

    Detector-->>Tool: GitOpsDetectionResult(engine=NONE, apps_count=0)
    Tool-->>AI: {engine: "none", error: null}
```

### Flow 3 — App Out-of-Sync with Detailed Cause

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as gitops_app_get(name, namespace)
    participant Service as GitOpsAppGetService
    participant Port as GitOpsPort
    participant Adapter as FluxAdapter
    participant K8s as Kubernetes API

    AI->>Tool: Call "gitops_app_get" name="payments-api" namespace="flux-system"
    Tool->>Service: get_app(command)
    Service->>Port: get_app("payments-api", "flux-system")
    Port->>Adapter: get_app(...)
    Adapter->>K8s: GET /apis/helm.toolkit.fluxcd.io/v2/namespaces/flux-system/helmreleases/payments-api
    K8s-->>Adapter: HelmRelease status

    Note over Adapter: Map CRD → GitOpsApp domain model<br/>sync_status=OUT_OF_SYNC<br/>message="HelmRelease reconciliation failed: values mismatch"

    Adapter-->>Port: GitOpsApp(sync=OUT_OF_SYNC, message=...)
    Port-->>Service: app
    Service-->>Tool: GitOpsAppGetResponse(sync_status="out_of_sync", message=...)
    Tool-->>AI: "payments-api is OUT_OF_SYNC.<br/>Cause: HelmRelease reconciliation failed — values mismatch."
```

### Flow 4 — Source Connection Failure

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as gitops_source_get
    participant Adapter as FluxAdapter
    participant K8s as Kubernetes API

    AI->>Tool: Call "gitops_source_get" name="prod-repo" namespace="flux-system"
    Tool->>Adapter: get_source("prod-repo", "flux-system")
    Adapter->>K8s: GET .../gitrepositories/prod-repo
    K8s-->>Adapter: GitRepository status

    Note over Adapter: ready=False<br/>message="authentication failed: SSH key invalid"

    Adapter-->>Tool: GitOpsSource(ready=False, message=...)
    Tool-->>AI: "prod-repo: NOT READY.<br/>Authentication failed — SSH key invalid."
```

## Key Points

- **Auto-detection** — checks Flux CRDs first (`helm.toolkit.fluxcd.io`), then Argo CD CRDs (`argoproj.io`), returns `NONE` if neither found
- **7 tools, read-only** — no sync/trigger operations; operators retain full control via `flux reconcile` or Argo CD UI
- **Out-of-sync causes** — `message` field in GitOpsApp captures the exact reconciliation error
- **Source health** — GitRepository/HelmRepository `ready` status with connection error details
- **Engine-agnostic** — FluxAdapter handles HelmRelease, Kustomization; ArgoCDAdapter handles Application, AppProject

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_flux_detected` | `tests/unit/test_gitops_detect.py` | ✅ |
| `test_none_detected` | `tests/unit/test_gitops_detect.py` | ✅ |
| `test_tool_returns_detection` | `tests/unit/test_gitops_detect.py` | ✅ |
| `test_tool_returns_apps` | `tests/unit/test_gitops_tools.py` | ✅ |
| `test_tool_returns_app_detail` | `tests/unit/test_gitops_tools.py` | ✅ |
| `test_tool_returns_status` | `tests/unit/test_gitops_tools.py` | ✅ |
| `test_tool_returns_sync_status_read_only` | `tests/unit/test_gitops_tools.py` | ✅ |
| `test_tool_returns_sources` | `tests/unit/test_gitops_tools.py` | ✅ |
| `test_tool_returns_source_detail` | `tests/unit/test_gitops_tools.py` | ✅ |
| `test_all_gitops_tools_have_register` | `tests/unit/test_gitops_tools.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/gitops.py` — GitOpsApp, GitOpsSource, GitOpsDetectionResult
- `src/hexawyn/domain/errors.py` — GitOpsEngineNotFoundError
- `src/hexawyn/application/ports/driven/gitops_port.py` — GitOpsPort ABC
- `src/hexawyn/adapters/secondary/gitops/gitops_detector.py` — GitOpsDetector
- `src/hexawyn/adapters/secondary/gitops/flux_adapter.py` — FluxAdapter
- `src/hexawyn/adapters/secondary/gitops/argocd_adapter.py` — ArgoCDAdapter
- `src/hexawyn/mcp/tools/gitops_detect.py` — detect tool
- `src/hexawyn/mcp/tools/gitops_apps_list.py` — list tool
- `src/hexawyn/mcp/tools/gitops_app_get.py` — get tool
- `src/hexawyn/mcp/tools/gitops_app_status.py` — status tool
- `src/hexawyn/mcp/tools/gitops_app_sync.py` — sync status tool
- `src/hexawyn/mcp/tools/gitops_sources_list.py` — sources list tool
- `src/hexawyn/mcp/tools/gitops_source_get.py` — source get tool
