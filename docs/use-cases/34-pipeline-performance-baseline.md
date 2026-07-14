# Use Case 34 — Pipeline Performance Baseline

## Sample Questions

- "Establish a CI/CD performance baseline for the payment-service pipeline — what is the average build time, test time, and deploy time over the last 30 runs?"
- "Has the checkout pipeline been getting slower over the last week? Show me the trend."
- "Which pipeline runs are outliers — taking more than double the average build time?"
- "Give me the p50 and p95 durations for each stage of the deploy-api pipeline"
- "Is the CI pipeline performance improving, stable, or degrading compared to last month?"

---

Fetches the last N PipelineRuns for a given pipeline name (default: 30), extracts per-stage durations (build/test/deploy) from child TaskRuns, computes statistical baselines (average, p50, p95, max), identifies outlier runs (>2x average), determines trend direction (improving/stable/degrading), and returns a structured baseline report.

---

## Flow 1 — Happy Path (payment-service: 30 runs, stable ~4m build time)

```mermaid
sequenceDiagram
    actor SRE
    participant MCP as MCP Tool<br/>(pipeline_performance_baseline)
    participant UC as PipelineBaselineUseCase
    participant Svc as PipelineBaselineService
    participant Port as PipelineBaselinePort (ABC)
    participant Adapter as TektonPipelineBaselineAdapter
    participant K8s as Kubernetes API (CRDs)
    participant Domain as CICDPerformanceBaselineService

    SRE->>MCP: pipeline_performance_baseline("payment-service",<br/>"ci", limit=30)
    MCP->>UC: execute(PipelineBaselineCommand)
    UC->>Svc: compute_baseline(command)

    Svc->>Port: list_pipeline_runs("ci", limit=30)
    Port->>Adapter: list_pipeline_runs("ci", limit=30)
    Adapter->>K8s: CustomObjectsApi.list_namespaced_custom_object<br/>(tekton.dev/v1/pipelineruns?labelSelector=pipeline=payment-service)
    K8s-->>Adapter: PipelineRunList (30 items, all with completionTime)
    Adapter-->>Svc: [PipelineRunRecord × 30]

    Note over Svc: Filter: only succeeded runs with completionTime<br/>Exclude: still-running + failed runs

    loop For each PipelineRun
        Svc->>Port: list_task_runs_for_pipeline("ci", pipeline_run_name)
        Port->>Adapter: list_task_runs_for_pipeline("ci", name)
        Adapter->>K8s: CustomObjectsApi.list_namespaced_custom_object<br/>(taskruns?labelSelector=tekton.dev/pipelineRun=name)
        K8s-->>Adapter: TaskRunList (build, test, deploy)
        Adapter-->>Svc: [TaskRunRecord × 3]
    end

    Svc->>Domain: compute_baseline(pipeline_runs=[30], task_runs=[90])
    Note over Domain: Stage extraction: group by task name pattern<br/>compute per-stage: avg, p50, p95, max durations<br/>detect outliers: >2x avg flagged<br/>compute trend: compare last 5 vs first 5 runs

    Domain-->>Svc: PipelineBaselineResult(build={avg:2m15s,p95:3m40s,max:5m10s},<br/>test={avg:1m30s,p95:2m,p95:4m20s},<br/>deploy={avg:45s,p95:1m10s,max:2m},<br/>trend=stable, outliers=[run-17,run-28])

    Svc-->>UC: PipelineBaselineResponse
    UC-->>MCP: response
    MCP-->>SRE: {pipeline:"payment-service", runs_analyzed:30, stages:{build:{...},test:{...},deploy:{...}}, trend:"stable", outliers:["run-17","run-28"]}
```

---

## Flow 2 — Error Flows (Pipeline not found, Tekton not installed, RBAC denied, cluster unreachable)

```mermaid
sequenceDiagram
    actor SRE
    participant MCP as MCP Tool
    participant Adapter as TektonPipelineBaselineAdapter
    participant K8s as Kubernetes API

    SRE->>MCP: pipeline_performance_baseline("unknown-pipeline", "ci")

    alt Pipeline not found (404)
        MCP->>Adapter: list_pipeline_runs("ci", limit=30)
        Adapter->>K8s: list_namespaced_custom_object(pipelineruns)
        K8s-->>Adapter: ApiException(status=404)
        Adapter->>Adapter: raise PipelineNotFoundError("unknown-pipeline")
        Adapter-->>MCP: PipelineNotFoundError
        MCP-->>SRE: {error: "Pipeline 'unknown-pipeline' not found in namespace 'ci'"}
    else RBAC denied (403)
        MCP->>Adapter: list_pipeline_runs("ci", limit=30)
        Adapter->>K8s: list_namespaced_custom_object()
        K8s-->>Adapter: ApiException(status=403)
        Adapter->>Adapter: raise InsufficientPermissionsError
        Adapter-->>MCP: InsufficientPermissionsError
        MCP-->>SRE: {error: "RBAC denied — cannot read PipelineRun resources"}
    else Tekton not installed (404 on CRD)
        MCP->>Adapter: list_pipeline_runs("ci", limit=30)
        Adapter->>K8s: list_namespaced_custom_object()
        K8s-->>Adapter: ApiException(status=404)
        Adapter->>Adapter: raise TektonNotInstalledError
        Adapter-->>MCP: TektonNotInstalledError
        MCP-->>SRE: {error: "Tekton is not installed — no PipelineRun CRDs found"}
    else Cluster unreachable
        MCP->>Adapter: list_pipeline_runs("ci", limit=30)
        Adapter->>K8s: list_namespaced_custom_object()
        K8s-->>Adapter: RuntimeError("connection refused")
        Adapter->>Adapter: raise ClusterUnreachableError
        Adapter-->>MCP: ClusterUnreachableError
        MCP-->>SRE: {error: "Cannot fetch PipelineRun data — cluster unreachable"}
    end
```

---

## Flow 3 — Edge Cases (fewer than N runs, outlier exclusion, no stage separation, in-progress runs)

```mermaid
sequenceDiagram
    actor SRE
    participant MCP as MCP Tool
    participant Svc as PipelineBaselineService
    participant Domain as CICDPerformanceBaselineService

    SRE->>MCP: pipeline_performance_baseline("new-pipeline", "ci", limit=30)

    Note over Svc: Only 5 runs available (< 30 requested)

    alt Runs < N (only 5 available)
        Svc->>Domain: compute_baseline(pipeline_runs=[5])
        Domain->>Domain: Baseline computed on available data<br/>includes note: "runs_available=5, requested=30"
        Domain-->>Svc: PipelineBaselineResult(runs_analyzed=5, note="Only 5 runs available")
    else One run is outlier (45m vs avg 4m)
        Svc->>Domain: compute_baseline(pipeline_runs=[30])
        Domain->>Domain: Detects run-23: 45m > 2× avg (4m)<br/>Flags as outlier, excludes from baseline
        Domain-->>Svc: PipelineBaselineResult(outliers=["run-23"], excluded_count=1)
    else No TaskRun stage separation
        Svc->>Domain: compute_baseline(pipeline_runs=[30], task_runs=[])
        Domain->>Domain: No child TaskRuns found<br/>Returns total PipelineRun duration only<br/>stages={}, total_duration={avg:..., p95:...}
        Domain-->>Svc: PipelineBaselineResult(stages={}, total_duration={...})
    else Runs without completionTime (still running)
        Svc->>Domain: compute_baseline(pipeline_runs=[30])
        Domain->>Domain: 3 runs have completionTime=None<br/>Excluded from baseline, counted in excluded_running
        Domain-->>Svc: PipelineBaselineResult(runs_analyzed=27, excluded_running=3)
    end

    Svc-->>MCP: PipelineBaselineResponse
    MCP-->>SRE: {runs_analyzed:5, note:"Only 5 runs available", stages:{...}, trend:"insufficient_data"}
```

---

## Flow 4 — Checker Node (validation)

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Domain as CICDPerformanceBaselineService
    participant LLM as LLM

    Checker->>Domain: validate_baseline(result)

    alt PASS — all validations green
        Domain->>Domain: runs_analyzed >= 5 ✓<br/>stages have meaningful durations ✓<br/>no all-failed scenario ✓

        Checker-->>MCP: PASS — format_response with baseline report
    else FLAG — outliers detected (>2x avg)
        Domain->>Domain: 2 runs flagged as outliers

        Checker-->>MCP: FLAG — format_response with caveats<br/>"Baseline computed, 2 outliers excluded"
    else DEGRADED — insufficient data (< 5 runs)
        Domain->>Domain: Only 3 runs — trend cannot be determined

        Checker-->>MCP: DEGRADED — format_response<br/>"Baseline computed on 3 runs — trend unavailable"
    else BLOCKED — all runs failed
        Domain->>Domain: 0 succeeded runs — no baseline computable

        Checker-->>MCP: BLOCKED — format_response<br/>"Cannot compute baseline: all 30 pipeline runs failed"
    end
```

---

## Key Points

- Fetches last N PipelineRuns via **label selector** `pipeline=<name>` from Tekton CRDs
- Extracts per-stage durations by grouping child TaskRuns by **task name pattern** (build/test/deploy) with best-effort matching when stage names vary
- Filters out runs with `completionTime=None` (still running) and **failed runs** — baseline computed only on succeeded runs
- Detects **outliers**: any run whose duration exceeds **2× the stage average** is flagged and excluded from the baseline
- Computes **trend**: compares average duration of last 5 runs vs first 5 runs → improving (faster), stable (±10%), degrading (slower)
- When fewer than N runs are available, baseline is computed on available data with `runs_available` note

## Test Coverage

| Test | File | Scenario |
|---|---|---|
| `test_stable_30_runs_returns_correct_baseline` | `test_pipeline_performance_baseline.py` | 30 runs, stable ~4m build → avg=4m, trend=stable |
| `test_last_5_runs_degrading_flags_outliers` | `test_pipeline_performance_baseline.py` | Last 5 runs avg 8m (double) → trend=degrading, outliers flagged |
| `test_only_5_runs_computes_with_note` | `test_pipeline_performance_baseline.py` | 5 runs available → baseline on available data, note added |
| `test_single_45m_run_flagged_as_outlier` | `test_pipeline_performance_baseline.py` | One run 45m vs avg 4m → flagged outlier, excluded |
| `test_no_taskrun_stages_returns_total_only` | `test_pipeline_performance_baseline.py` | No TaskRun stage separation → total duration returned |
| `test_pipeline_not_found_raises_error` | `test_pipeline_performance_baseline.py` | Pipeline name not found → PipelineNotFoundError |
| `test_runs_without_completion_time_excluded` | `test_pipeline_performance_baseline.py` | Runs with completionTime=None → excluded from baseline |
| `test_all_failed_runs_returns_empty_baseline` | `test_pipeline_performance_baseline.py` | All runs failed → baseline only on succeeded (0) |
| `test_stage_names_vary_best_effort_matching` | `test_pipeline_performance_baseline.py` | Stage names vary between runs → best-effort matching |
| `test_parallel_tasks_noted` | `test_pipeline_performance_baseline.py` | TaskRun durations don't add up to total (parallel) → noted |
| `test_trend_computation_improving` | `test_pipeline_performance_baseline.py` | First 5 avg 5m, last 5 avg 3m → trend=improving |
| `test_trend_computation_stable` | `test_pipeline_performance_baseline.py` | First 5 avg 4m, last 5 avg 4.2m (within ±10%) → stable |
| `test_p50_p95_max_computed_correctly` | `test_pipeline_performance_baseline.py` | 30 durations → p50 and p95 computed via statistics module |
| `test_happy_path_returns_expected_json_keys` | `test_pipeline_performance_baseline.py` | MCP tool JSON structure validation |

## Related Files

- `src/hexawyn/domain/models/pipeline_baseline.py` — `PipelineBaselineResult`, `StageStats`, `OutlierRecord`
- `src/hexawyn/domain/services/pipeline_baseline/cicd_performance_baseline_service.py` — Stats computation, outlier detection, trend analysis
- `src/hexawyn/application/ports/driven/pipeline_baseline_port.py` — `PipelineBaselineRecord`, `TaskRunStageRecord`, `PipelineBaselinePort`
- `src/hexawyn/application/ports/driving/pipeline_performance_baseline/` — Command, Response, ServicePort
- `src/hexawyn/application/use_case/pipeline_performance_baseline/` — UseCase
- `src/hexawyn/application/service/pipeline_performance_baseline_service.py` — Application service
- `src/hexawyn/adapters/secondary/tekton_pipeline_baseline_adapter.py` — K8s CRD adapter
- `src/hexawyn/mcp/tools/pipeline_performance_baseline.py` — MCP entry point
