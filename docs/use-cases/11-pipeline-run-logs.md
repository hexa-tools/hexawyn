# Use Case 11 — Pipeline Run Logs

## Sample Questions

- "Show me the full logs of the failed PipelineRun deploy-payment-v2"
- "At which step did the build pipeline break and why?"
- "Get the logs for the last failed Tekton pipeline run"
- "Show me all TaskRun logs for PipelineRun deploy-v3 in the ci namespace"
- "What caused the checkout pipeline to fail — show the error logs"

---

One MCP tool: `pipeline_run_logs`. Retrieves logs from all TaskRuns in a PipelineRun, highlights failed steps with error output, truncates large logs to last 500 lines.

### Flow 1 — Happy Path: Failed Step Highlighted

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as pipeline_run_logs
    participant Service as PipelineRunLogsService
    participant Port as PipelineRunLogsPort
    participant Adapter as KubernetesPipelineRunLogsAdapter
    participant K8s as Kubernetes API

    AI->>MCP: "Show logs of deploy-payment-v2"
    MCP->>Tool: pipeline_run_logs("deploy-payment-v2", "ci")

    Tool->>Service: get_logs(command)
    Service->>Port: fetch_step_logs(req)
    Port->>Adapter: KubernetesPipelineRunLogsAdapter
    Adapter->>K8s: GET PipelineRun + TaskRuns + logs per pod
    K8s-->>Adapter: clone-repo: succeeded, build-image: FAILED

    Note over Service: 3 steps: clone-repo OK, build-image FAILED, deploy SKIPPED<br/>Truncate if > 500 lines per step

    Service-->>Tool: PipelineRunLogsResponse(failed_step_count=1, steps=[...])
    Tool-->>MCP: {failed_step_count: 1, steps: [{name: "build-image", status: "failed", log_lines: ["ERROR: no space left on device"]}]}
    MCP-->>AI: "deploy-payment-v2: build-image FAILED. Error: docker build failed — no space left on device. 1 of 3 steps failed."
```

### Flow 2 — Still Running

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as pipeline_run_logs
    participant Service as PipelineRunLogsService

    AI->>Tool: pipeline_run_logs("deploy-v3", "ci")
    Tool->>Service: get_logs()
    Note over Service: clone-repo RUNNING, other steps not started<br/>is_still_running=True

    Service-->>Tool: is_still_running=True
    Tool-->>AI: "deploy-v3 is still running. clone-repo step in progress. Logs displayed so far."
```

### Flow 3 — PipelineRun Not Found

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as pipeline_run_logs
    participant Service as PipelineRunLogsService

    AI->>Tool: pipeline_run_logs("ghost", "ci")
    Tool->>Service: get_logs()
    Note over Service: steps=[], pipeline_run_found=False

    Service-->>Tool: pipeline_run_found=False
    Tool-->>AI: "PipelineRun 'ghost' not found in namespace 'ci'."
```

### Flow 4 — Truncation Warning

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as pipeline_run_logs
    participant Service as PipelineRunLogsService

    AI->>Tool: pipeline_run_logs("verbose-build", "ci")
    Tool->>Service: get_logs()
    Note over Service: build-image step has 1200 log lines<br/>truncated to last 500 with warning

    Service-->>Tool: steps: [{truncated: true, log_lines: 500, status: SUCCEEDED}]
    Tool-->>AI: "build-image succeeded (logs truncated to last 500 lines — 1200 total). clone-repo succeeded."
```

## Key Points

- **Failed step highlighting** — FAILED steps returned first with full error output
- **Truncation** — logs > 500 lines truncated to last 500 with `truncated=True` flag
- **Still running** — steps in RUNNING status flagged, logs returned so far
- **Not found** — empty steps → `pipeline_run_found=False`

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_failed_step_highlighted` | `tests/unit/test_pipeline_run_logs.py` | ✅ |
| `test_not_found` | `tests/unit/test_pipeline_run_logs.py` | ✅ |
| `test_still_running` | `tests/unit/test_pipeline_run_logs.py` | ✅ |
| `test_returns_logs_with_failed` | `tests/unit/test_pipeline_run_logs_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/pipeline_run_logs.py` — StepLog, PipelineRunLogsResult
- `src/hexawyn/application/ports/driven/pipeline_run_logs_port.py` — PipelineRunLogsPort ABC
- `src/hexawyn/adapters/secondary/gitops/kubernetes_pipeline_run_logs_adapter.py` — adapter
- `src/hexawyn/mcp/tools/pipeline_run_logs.py` — MCP tool
