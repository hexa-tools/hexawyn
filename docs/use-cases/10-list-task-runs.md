# Use Case 8 — List TaskRuns for a Pipeline

## Sample Questions

- "List all TaskRuns for the build-deploy pipeline — which step is failing?"
- "What's the status of each step in the payment-service pipeline?"
- "Which task step broke the checkout pipeline?"
- "Show me the TaskRuns for the ci/deploy-api pipeline"

---

An AI agent (SRE) asks "List all TaskRuns for the build-deploy pipeline — which task step is failing?". The flow goes through all hexagonal layers: MCP Tool → ListTaskRunsUseCase → ListTaskRunsService → TektonPort (driven port) → VanillaAdapter → Kubernetes CustomObjectsApi (Tekton CRD). TaskRuns are sorted by start time descending; failed runs expose the failing step name and error message.

### Flow 1 — Happy Path: Pipeline with 3 TaskRuns, 1 Failed

```mermaid
sequenceDiagram
    participant AI as AI Agent (SRE)
    participant MCP as FastMCP Server
    participant Tool as list_task_runs(pipeline_name, namespace)
    participant UseCase as ListTaskRunsUseCase
    participant Service as ListTaskRunsService
    participant Port as TektonPort (ABC)
    participant Adapter as VanillaAdapter
    participant API as Kubernetes CustomObjectsApi

    AI->>MCP: Call tool "list_task_runs" pipeline_name="build-deploy" namespace="ci"
    MCP->>Tool: @mcp.tool() dispatch

    Tool->>UseCase: ListTaskRunsService(tekton_port=adapter)<br/>use_case.execute(ListTaskRunsCommand(pipeline_name="build-deploy", namespace="ci"))
    UseCase->>Service: service.list_task_runs(command)
    Service->>Port: tekton_port.list_task_runs("build-deploy", "ci")

    Port->>Adapter: VanillaAdapter.list_task_runs("build-deploy", "ci")
    Adapter->>API: GET /apis/tekton.dev/v1/namespaces/ci/taskruns<br/>?labelSelector=tekton.dev/pipeline=build-deploy
    API-->>Adapter: TaskRunList { items: [clone-repo, unit-tests, build-image] }

    Note over Adapter: _task_run_status() → Succeeded / Failed / NotStarted<br/>_extract_failing_step() → "run-tests", "exit code 1"<br/>_task_run_duration() → "12s" / "30s" / None

    Adapter-->>Port: list[TaskRunInfo]
    Port-->>Service: [{clone-repo, Succeeded, 12s}, {unit-tests, Failed, run-tests, exit code 1}, {build-image, NotStarted}]

    Note over Service: _start_time_sort_key() → sorted desc by start_time<br/>NotStarted (None) → last

    Service-->>UseCase: ListTaskRunsResponse(task_runs=[unit-tests, clone-repo, build-image])
    UseCase-->>Tool: response
    Tool-->>MCP: { task_runs: [...], error: None }
    MCP-->>AI: "Step 'run-tests' in TaskRun 'unit-tests' failed: exit code 1"
```

### Flow 2 — Error: Pipeline Not Found

```mermaid
sequenceDiagram
    participant AI as AI Agent (SRE)
    participant Tool as list_task_runs(pipeline_name="ghost-pipeline")
    participant Adapter as VanillaAdapter
    participant API as Kubernetes CustomObjectsApi

    AI->>Tool: Call "list_task_runs" pipeline_name="ghost-pipeline"
    Tool->>Adapter: VanillaAdapter.list_task_runs("ghost-pipeline", "ci")
    Adapter->>API: GET taskruns?labelSelector=tekton.dev/pipeline=ghost-pipeline
    API-->>Adapter: TaskRunList { items: [] }

    Note over Adapter: Empty items list<br/>→ raise PipelineNotFoundError("ghost-pipeline")

    Note over Tool: MCP tool is the primary adapter<br/>Service and UseCase never catch

    Adapter-->>Tool: PipelineNotFoundError propagates
    Tool-->>AI: { task_runs: [], error: "Pipeline 'ghost-pipeline' not found or has no TaskRuns..." }
```

### Flow 3 — Error: Tekton API Unreachable

```mermaid
sequenceDiagram
    participant AI as AI Agent (SRE)
    participant Tool as list_task_runs()
    participant Adapter as VanillaAdapter
    participant API as Kubernetes CustomObjectsApi

    AI->>Tool: Call "list_task_runs" pipeline_name="build-deploy"
    Tool->>Adapter: VanillaAdapter.list_task_runs("build-deploy", "ci")
    Adapter->>API: GET /apis/tekton.dev/v1/namespaces/ci/taskruns
    API-->>Adapter: ❌ ApiException (connection refused / timeout)

    Note over Adapter: _fetch_task_runs() catches ApiException<br/>→ raise ClusterUnreachableError("Cannot reach Tekton API: ...")
    Note over Tool: Primary adapter catches all HexawynError subclasses

    Adapter-->>Tool: ClusterUnreachableError propagates
    Tool-->>AI: { task_runs: [], error: "Cannot reach Tekton API: ..." }
```

### Flow 4 — Edge Case: Timeout Step

```mermaid
sequenceDiagram
    participant AI as AI Agent (SRE)
    participant Tool as list_task_runs()
    participant Adapter as VanillaAdapter
    participant API as Kubernetes CustomObjectsApi

    AI->>Tool: Call "list_task_runs" pipeline_name="build-deploy"
    Tool->>Adapter: list_task_runs("build-deploy", "ci")
    Adapter->>API: GET taskruns?labelSelector=tekton.dev/pipeline=build-deploy
    API-->>Adapter: TaskRunList { items: [run with DeadlineExceeded step] }

    Note over Adapter: _extract_failing_step():<br/>terminated.reason == "DeadlineExceeded"<br/>→ failing_step_error = "Timeout" (not "Error")

    Adapter-->>Tool: [{ status: "Failed", failing_step: "run-tests", failing_step_error: "Timeout" }]
    Tool-->>AI: { task_runs: [...], error: None }
    AI-->>AI: "Step 'run-tests' timed out"
```

## Key Points

- **TektonPort is separate from K8sPort** — ISP: Tekton CRD operations do not belong in the core K8s port
- **Error translation in the secondary adapter** — `ApiException` → `ClusterUnreachableError`; empty result → `PipelineNotFoundError`. Domain errors never escape the adapter.
- **Service never catches** — `ListTaskRunsService` lets `PipelineNotFoundError` propagate naturally
- **Timeout shown as "Timeout" not "Error"** — `terminated.reason == "DeadlineExceeded"` is mapped explicitly
- **Sorted desc by start_time** — `NotStarted` (null start_time) always last

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_is_frozen` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_fields` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_default_task_runs_is_empty` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_accepts_task_runs_list` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_is_abstract` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_cannot_instantiate_directly` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_delegates_to_service_port` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_passes_command_to_service` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_implements_service_port` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_failed_task_run_exposes_failing_step_and_error` (TC1) | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_all_succeeded_no_failing_step` (TC2) | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_running_task_run_has_start_time_and_no_duration` (TC3) | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_pipeline_not_found_propagates` (TC4) | `tests/unit/test_list_task_runs_use_case.py` | ✅ |
| `test_sorted_by_start_time_descending` | `tests/unit/test_list_task_runs_use_case.py` | ✅ |

## Related Files

- `src/hexawyn/application/ports/driven/tekton_port.py` — `TaskRunInfo` TypedDict + `TektonPort` ABC
- `src/hexawyn/application/ports/driving/list_task_runs/` — Command, Response, ServicePort
- `src/hexawyn/application/service/list_task_runs_service.py` — `ListTaskRunsService` (sorting)
- `src/hexawyn/application/use_case/list_task_runs/list_task_runs_use_case.py` — `ListTaskRunsUseCase`
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py` — Tekton CRD parsing + error translation
- `src/hexawyn/domain/errors.py` — `PipelineNotFoundError`
- `src/hexawyn/mcp/tools/list_task_runs.py` — MCP tool (primary adapter, final catch)
- `src/hexawyn/mcp/server.py` — `build_tekton_adapter()`
