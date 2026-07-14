# Use Case 18 — Get Pipeline Run Status

## Sample Questions

- "What is the current status of all Tekton PipelineRuns in the CI namespace?"
- "How many builds succeeded or failed in the last 24 hours?"
- "Which pipeline run took the longest to complete today?"
- "Show me the most recent failed build and why it failed"
- "Are there any stuck or pending pipeline runs in ci?"

---

## Happy Path

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant UC as GetPipelineRunStatusUseCase
    participant Svc as PipelineRunStatusService
    participant Port as TektonPipelineStatusPort (ABC)
    participant Adapter as KubernetesTektonAdapter
    participant K8s as Kubernetes API (CRD)

    User->>MCP: get_pipeline_run_status(namespace="ci", hours_window=24)
    MCP->>UC: execute(GetPipelineRunStatusCommand)
    UC->>Svc: get_pipeline_run_status(command)

    Svc->>Port: list_pipeline_runs(namespace="ci", limit=500)
    Port->>Adapter: list_pipeline_runs("ci", 500)
    Adapter->>K8s: CustomObjectsApi.list_namespaced_custom_object(group="tekton.dev", plural="pipelineruns")
    K8s-->>Adapter: {items: [PipelineRun CRD objects]}

    Note over Adapter: Per run: _extract_status() → (status, failure_reason)<br/>_compute_duration_seconds() → elapsed or completed<br/>_extract_pipeline_ref() → name or "inline"

    Adapter-->>Svc: list[PipelineRunRecord]

    Note over Svc: _filter_by_window() → keep runs started within 24h<br/>Count by status: Running / Succeeded / Failed / Cancelled / NotStarted<br/>_find_most_recent_failed() → most recent Failed + failure_reason<br/>_find_slowest_run() → max duration_seconds among completed

    Svc-->>UC: GetPipelineRunStatusResponse
    UC-->>MCP: response.report
    MCP-->>User: {namespace, total, running, succeeded, failed, cancelled, most_recent_failed, slowest_run}
```

---

## Error Flows

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant Adapter as KubernetesTektonAdapter
    participant K8s as Kubernetes API

    User->>MCP: get_pipeline_run_status(namespace="ci")

    alt RBAC denied (403 Forbidden)
        Adapter->>K8s: list_namespaced_custom_object(namespace="ci")
        K8s--xAdapter: ApiException(status=403)
        Adapter-->>MCP: InsufficientPermissionsError propagates
        MCP-->>User: {error: "RBAC denied access to PipelineRuns in namespace 'ci'", total: 0}

    else Tekton CRDs not installed (404)
        K8s--xAdapter: ApiException(status=404)
        Adapter-->>MCP: TektonNotInstalledError propagates
        MCP-->>User: {error: "Tekton is not installed in this cluster", total: 0}

    else Cluster unreachable (connection error or other API failure)
        K8s--xAdapter: ConnectionError / ApiException(5xx)
        Adapter-->>MCP: ClusterUnreachableError propagates
        MCP-->>User: {error: "Tekton API unreachable in namespace 'ci': ...", total: 0}

    else Namespace has no PipelineRuns
        K8s-->>Adapter: {items: []}
        Adapter-->>Svc: []
        Note over Svc: _filter_by_window([]) → []<br/>All counts = 0, most_recent_failed = None
        MCP-->>User: {total: 0, running: 0, succeeded: 0, failed: 0, ...}

    else All runs older than hours_window
        K8s-->>Adapter: {items: [old runs]}
        Note over Svc: _filter_by_window filters them all out
        MCP-->>User: {total: 0, ...}
    end
```

---

## Checker Node — Response Quality Validation

```mermaid
sequenceDiagram
    participant Tool as MCP Tool
    participant Gen as generate_response (LLM)
    participant CK as checker_node
    participant Mem as store_memory
    participant Fmt as format_response

    Tool-->>Gen: PipelineRunStatusReport (raw counts + most_recent_failed)
    Gen-->>CK: LLM-generated pipeline health summary

    alt PASS — counts coherent, failed runs highlighted with reason
        CK->>Mem: store_memory(query, result, cluster)
        Mem-->>Fmt: stored
        CK-->>Fmt: status=PASS
        Fmt-->>User: pipeline health summary

    else FAIL (attempt < 3) — counts don't add up or failure reason missing
        CK-->>Gen: retry with corrected prompt
        Note over CK,Gen: retry_count += 1<br/>checker hint: "total != running+succeeded+failed+cancelled"
        Gen-->>CK: revised summary

    else FAIL (attempt ≥ 3) — DEGRADED
        CK-->>Fmt: status=DEGRADED
        Fmt-->>User: raw report data + "summary generation failed"

    else BLOCKED — mutation keyword in response ("delete", "restart", "drain")
        Note over CK: Read-only tool — block any write suggestions
        CK-->>Fmt: status=BLOCKED
        Fmt-->>User: "Operation blocked — read-only tool"

    else FLAG — partial data (NotStarted runs or skipped due to window)
        Note over CK: not_started > 0 or total < limit → possibly incomplete
        CK->>Mem: store_memory(with flag metadata)
        CK-->>Fmt: status=FLAG, caveats=["some runs may be pending or outside window"]
        Fmt-->>User: summary + caveat banner
    end
```

---

## Key Points

- **Time-window filtering** — only runs started within `hours_window` (default 24h) are counted; runs with no `start_time` (NotStarted/Pending) are always included.
- **Elapsed time for running** — `duration_seconds` is computed as `now - start_time` for in-progress runs, giving live elapsed time without waiting for completion.
- **Failure reason surfacing** — the adapter extracts the Tekton condition `reason` field (e.g., `TaskRunTimeout`, `TaskRunImagePullFailed`) so engineers can act immediately without browsing the Tekton dashboard.
- **Slowest run** — computed across all completed (Succeeded + Failed) runs within the window; useful for detecting regressions in build time.
- **Graceful Tekton-absent handling** — `TektonNotInstalledError` on 404 gives a clear message instead of a raw API error.

## Test Coverage

| Test | Scenario |
|------|----------|
| `TestPipelineRunStatusService::test_happy_path_mixed_statuses` | 2 Succeeded, 1 Running, 2 Failed → correct counts |
| `TestPipelineRunStatusService::test_no_pipeline_runs_returns_empty_summary` | No runs → all zeros |
| `TestPipelineRunStatusService::test_all_runs_older_than_window_returns_empty` | 30h old runs excluded from 24h window |
| `TestPipelineRunStatusService::test_failed_run_failure_reason_surfaced` | TaskRunTimeout reason returned |
| `TestPipelineRunStatusService::test_slowest_run_identified` | Longest duration_seconds selected |
| `TestPipelineRunStatusService::test_cancelled_runs_counted` | Cancelled counted separately |
| `TestPipelineRunStatusService::test_custom_hours_window_applied` | 2h window excludes 3h old run |
| `TestPipelineRunStatusService::test_rbac_error_propagates` | InsufficientPermissionsError bubbles |
| `TestKubernetesTektonAdapter::test_list_pipeline_runs_403_raises_insufficient_permissions` | 403 → InsufficientPermissionsError |
| `TestKubernetesTektonAdapter::test_list_pipeline_runs_404_raises_tekton_not_installed` | 404 → TektonNotInstalledError |
| `TestKubernetesTektonAdapter::test_failure_reason_extracted_for_failed_run` | reason="TaskRunTimeout" extracted |
| `TestKubernetesTektonAdapter::test_running_run_has_elapsed_duration` | duration_seconds ≥ 0 for running |
| `TestFilterByWindow::test_includes_pending_run_with_no_start_time` | None start_time → included |
| `TestFilterByWindow::test_invalid_timestamp_excluded` | Malformed timestamp → excluded |
| `TestGetPipelineRunStatusMCPTool::test_tool_error_returns_error_key` | Exception → error key in result |

## Related Files

- `src/hexawyn/domain/models/pipeline.py` — `PipelineRunSummary`, `PipelineRunStatusReport`
- `src/hexawyn/application/ports/driven/tekton_pipeline_status_port.py` — `PipelineRunRecord` TypedDict + `TektonPipelineStatusPort` ABC
- `src/hexawyn/application/ports/driving/get_pipeline_run_status/` — command, response, service port ABC
- `src/hexawyn/application/service/pipeline_run_status_service.py` — window filter, aggregation, most_recent_failed, slowest
- `src/hexawyn/application/use_case/get_pipeline_run_status/get_pipeline_run_status_use_case.py` — thin use case
- `src/hexawyn/adapters/secondary/kubernetes_tekton_adapter.py` — K8s CRD fetch, status/failure_reason/duration extraction
- `src/hexawyn/mcp/tools/get_pipeline_run_status.py` — MCP tool registration + serialization
- `tests/unit/test_get_pipeline_run_status.py` — 59 unit tests
