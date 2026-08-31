# Use Case 42 — Argo Rollouts (Progressive Delivery)

## Sample Questions

- "Is my canary rollout for payments-api healthy?"
- "Why is my blue-green deployment blocked?"
- "Are there any rollouts in progress in my cluster?"
- "What is the error rate of the canary version of my service?"
- "Has the automated analysis passed for my rollout?"
- "Are there any failed AnalysisRuns linked to my rollout?"
- "Should I promote or abort the auth-service rollout?"

---

Five MCP tools for Argo Rollouts: `rollouts_detect` (detects installation + version), `rollouts_list` (lists all Rollouts with strategy and phase), `rollout_get` (detailed status with step info and canary weight), `rollout_status` (real-time phase + canary weight), `analysis_runs_list` (AnalysisRuns with failed metrics). All tools are read-only — promote, abort, and retry are NEVER available.

### Flow 1 — Happy Path: Canary Rollout Progression

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as rollout_get(name, namespace)
    participant UseCase as RolloutGetUseCase
    participant Service as RolloutGetService
    participant Port as RolloutsPort (ABC)
    participant Adapter as ArgoRolloutsDetector
    participant K8s as Kubernetes API

    AI->>MCP: Call "rollout_get" name="payments-api" namespace="production"
    MCP->>Tool: @mcp.tool() dispatch

    Tool->>UseCase: execute(RolloutGetCommand(...))
    UseCase->>Service: get_rollout(command)
    Service->>Port: get_rollout("payments-api", "production")

    Port->>Adapter: ArgoRolloutsDetector
    Adapter->>K8s: GET /apis/argoproj.io/v1alpha1/namespaces/production/rollouts/payments-api
    K8s-->>Adapter: Rollout status

    Note over Adapter: Map CRD → Rollout domain model<br/>strategy=CANARY, phase=PROGRESSING<br/>step 2/5: setWeight 20%<br/>canary=v2.1.0, stable=v2.0.0

    Adapter-->>Port: Rollout(phase=PROGRESSING, canary_weight=20)
    Port-->>Service: rollout
    Service-->>UseCase: RolloutGetResponse(phase="progressing", canary_weight=20)
    UseCase-->>Tool: response
    Tool-->>MCP: {phase: "progressing", canary_weight: 20, step_index: 2, total_steps: 5}
    MCP-->>AI: "payments-api canary: step 2/5 — 20% traffic to v2.1.0<br/>3 of 5 replicas ready, progressing normally."
```

### Flow 2 — Paused Rollout with Manual Approval

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as rollout_status
    participant Adapter as ArgoRolloutsDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "rollout_status" name="auth-service"
    Tool->>Adapter: get_rollout("auth-service", "staging")
    Adapter->>K8s: GET .../rollouts/auth-service
    K8s-->>Adapter: Rollout PAUSED at step 3/5

    Note over Adapter: phase=PAUSED<br/>pause_reason="manual"<br/>paused_at="2026-07-01T10:00:00Z"<br/>canary_weight=40%

    Adapter-->>Tool: Rollout(paused, reason=manual)
    Tool-->>AI: "auth-service ROLLOUT PAUSED at step 3/5 — 40% canary.<br/>Paused manually for approval.<br/>Use `kubectl argo rollouts promote auth-service -n staging` to proceed."
```

### Flow 3 — AnalysisRun Failed, Rollout Degraded

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as analysis_runs_list + rollout_get
    participant Adapter as ArgoRolloutsDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "rollout_get" name="payments-api"
    Tool->>Adapter: get_rollout("payments-api", "production")
    Adapter->>K8s: GET .../rollouts/payments-api
    K8s-->>Adapter: phase=DEGRADED, analysis_run="payments-api-analysis-abc"

    Note over Adapter: AnalysisRun FAILED → Rollout DEGRADED

    AI->>Tool: Call "analysis_runs_list" rollout_name="payments-api"
    Tool->>Adapter: list_analysis_runs(rollout_name="payments-api")
    Adapter->>K8s: GET .../analysisruns?labelSelector=rollout=payments-api
    K8s-->>Adapter: AnalysisRun FAILED

    Note over Adapter: metrics_count=3<br/>failed_metrics=["error-rate", "latency-p99"]<br/>message="Metric error-rate exceeded threshold: 5.2% > 2%"

    Tool-->>AI: "payments-api is DEGRADED.<br/>AnalysisRun FAILED: error-rate at 5.2% (threshold 2%).<br/>Also: latency-p99 exceeded threshold.<br/>Recommendation: abort rollout manually via `kubectl argo rollouts abort payments-api`"
```

### Flow 4 — Argo Rollouts Not Installed

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as rollouts_detect
    participant Detector as ArgoRolloutsDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "rollouts_detect"
    Tool->>Detector: detect_rollouts()
    Detector->>K8s: Check argo-rollouts CRDs (argoproj.io/v1alpha1)
    K8s-->>Detector: ❌ CRD not found

    Note over Detector: ComponentNotInstalledError<br/>"Argo Rollouts is not installed"

    Detector-->>Tool: RolloutsDetectionResult(installed=False)
    Tool-->>AI: "Argo Rollouts not detected.<br/>Install: https://argo-rollouts.readthedocs.io/en/stable/installation/"
```

## Key Points

- **Read-only only** — `rollout_promote`, `rollout_abort`, `rollout_retry` are NEVER exposed; operators must use `kubectl argo rollouts` or the dashboard
- **Canary weight tracking** — every Rollout reports `canary_weight` (0-100%) per step
- **Pause reasons** — `manual`, `duration`, or `analysis` captured in `pause_reason`
- **AnalysisRun linking** — `analysis_run_name` field connects Rollout to its active AnalysisRun
- **Failed metrics** — AnalysisRun lists every failed metric with threshold-violation message

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_tool_returns_detection` | `tests/unit/test_rollouts_tools.py` | ✅ |
| `test_tool_returns_rollouts` | `tests/unit/test_rollouts_tools.py` | ✅ |
| `test_tool_returns_detail` | `tests/unit/test_rollouts_tools.py` | ✅ |
| `test_tool_returns_status` | `tests/unit/test_rollouts_tools.py` | ✅ |
| `test_tool_returns_analysis_runs` | `tests/unit/test_rollouts_tools.py` | ✅ |
| `test_all_rollouts_tools_have_register` | `tests/unit/test_rollouts_tools.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/rollouts.py` — Rollout, AnalysisRun, RolloutsDetectionResult, RolloutStepStatus
- `src/hexawyn/domain/errors.py` — ComponentNotInstalledError
- `src/hexawyn/application/ports/driven/rollouts_port.py` — RolloutsPort ABC
- `src/hexawyn/adapters/secondary/gitops/argo_rollouts_detector.py` — ArgoRolloutsDetector
- `src/hexawyn/mcp/tools/rollouts_detect.py` — detect tool
- `src/hexawyn/mcp/tools/rollouts_list.py` — list tool
- `src/hexawyn/mcp/tools/rollout_get.py` — get tool
- `src/hexawyn/mcp/tools/rollout_status.py` — status tool
- `src/hexawyn/mcp/tools/analysis_runs_list.py` — analysis runs tool
