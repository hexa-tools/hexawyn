# Use Case 40 — Query KubeArchive for Historical Resource State

## Sample Questions

- "Query KubeArchive for the historical state of all pods in the payment namespace from last Tuesday — what was the pod count and which ones were restarting?"
- "What was the state of pods in the production namespace at 2026-06-09T10:00:00Z?"
- "How many pods were running in staging last Monday and which ones were crashing?"
- "Compare the pods in the payment namespace now vs last week — what changed?"
- "Show me which deployments existed in the ci namespace on June 1st"
- "Were there any pods in CrashLoopBackOff in production last Tuesday?"
- "Give me a historical snapshot of all pods in the payment namespace and compare with the live state"

---

An AI agent asks to query KubeArchive for the historical state of Kubernetes resources at a specific point in time. The flow goes through: MCP Tool → QueryKubeArchiveUseCase → HistoricalStateQueryService → KubeArchivePort (driven port) → KubeArchiveHTTPAdapter → KubeArchive REST API. The service maps KubeArchive API responses to domain models, runs restart detection and failing pod filtering, and optionally compares historical vs current state via K8sPort.

### Flow 1 — Happy Path: Query Historical Pod State

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as query_kubearchive(namespace, resource_type, timestamp)
    participant UseCase as QueryKubeArchiveUseCase
    participant Service as HistoricalStateQueryService
    participant KAPort as KubeArchivePort (ABC)
    participant KAAdapter as KubeArchiveHTTPAdapter
    participant KAAPI as KubeArchive REST API

    AI->>MCP: Call tool "query_kubearchive"<br/>namespace="payment" resource_type="pods"<br/>timestamp="2026-06-09T10:00:00Z"
    MCP->>Tool: @mcp.tool() dispatch

    Tool->>UseCase: use_case.execute(QueryKubeArchiveCommand(...))
    UseCase->>Service: service.query(command)
    Service->>KAPort: kubearchive_port.query_historical_state(query)

    KAPort->>KAAdapter: KubeArchiveHTTPAdapter(endpoint)
    KAAdapter->>KAAPI: GET /api/v1/resources<br/>?namespace=payment&kind=pods&timestamp=2026-06-09T10:00:00Z
    KAAPI-->>KAAdapter: {total_resources: 8, items: [...]}

    Note over KAAdapter: Map API response →<br/>HistoricalPodInfo TypedDicts

    KAAdapter-->>KAPort: KubeArchiveResponse(pods=[...])
    KAPort-->>Service: response

    Note over Service: Map to domain models<br/>HistoricalPod, create snapshot

    Service-->>UseCase: QueryKubeArchiveResponse(total_resources=8, pods=[...])
    UseCase-->>Tool: response
    Tool-->>MCP: {pods: [...], total_resources: 8, error: null}
    MCP-->>AI: "payment namespace had 8 pods at 2026-06-09T10:00:00Z.<br/>payment-pod-def had 8 restarts — flagged.<br/>payment-worker-xyz was in CrashLoopBackOff with 23 restarts.<br/>5 other pods were healthy with 0 restarts."
```

### Flow 2 — Error: KubeArchive Unreachable / Not Installed

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as query_kubearchive
    participant Adapter as KubeArchiveHTTPAdapter
    participant KAAPI as KubeArchive REST API

    AI->>Tool: Call "query_kubearchive" namespace="payment"
    Tool->>Adapter: query_historical_state(...)
    Adapter->>KAAPI: GET /api/v1/resources
    KAAPI-->>Adapter: ❌ ConnectError (Connection refused)

    Note over Adapter: catch httpx.ConnectError<br/>→ raise KubeArchiveUnavailableError<br/>"Install KubeArchive first: https://kubearchive.org/docs/installation"

    Adapter-->>Tool: KubeArchiveUnavailableError propagates
    Tool-->>AI: {error: "KubeArchive not available. Install: https://..."}
```

### Flow 3 — Comparison Mode: Historical vs Current State

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as query_kubearchive(compare_with_current=true)
    participant Service as HistoricalStateQueryService
    participant KAPort as KubeArchivePort
    participant K8sPort as K8sPort
    participant Domain as StateComparison (domain)

    AI->>Tool: Call with compare_with_current=true

    Tool->>Service: service.query(command)
    Service->>KAPort: query_historical_state(query)
    KAPort-->>Service: 8 historical pods

    alt compare_with_current is True
        Service->>K8sPort: list_pods(namespace="payment")
        K8sPort-->>Service: 3 current pods

        Note over Service: Map both to HistoricalPod models<br/>Mark currently_exists=False for deleted pods

        Service->>Domain: StateComparison.compare(historical, current)
        Domain-->>Service: StateComparison(removed=5, pods_removed_names=[...])

        Note over Service: Build HistoricalComparisonResult<br/>delta_message: "−5 pods removed since 2026-06-09T10:00:00Z"
    end

    Service-->>Tool: QueryKubeArchiveResponse(comparison=...)
    Tool-->>AI: "8 pods at queried time, 3 currently running.<br/>−5 pods removed: pod-a, pod-b, ..."
```

### Flow 4 — Checker Node: Semantic Validation (LangGraph)

```mermaid
sequenceDiagram
    participant LLM as LLM Response
    participant Checker as Checker Node
    participant KB as KubeArchive Results
    participant Live as Live Cluster State

    Checker->>LLM: Validate response against KubeArchive results

    alt LLM mixes historical and live data without source tags
        Checker-->>LLM: ❌ FAIL — each datum must be tagged with source (historical/live)
    else LLM omits queried timestamp in answer
        Checker-->>LLM: ⚠️ FLAG — timestamp must appear in response
    else LLM invents pod names not in KubeArchive results
        Checker-->>LLM: ❌ FAIL — cross-check pod names against KubeArchive results
    else LLM miscalculates delta (e.g. "+2 added" instead of "−5 removed")
        Checker-->>LLM: ❌ FAIL — verify historical_count - current_count math
    else LLM invents state for null/expired timestamp
        Checker-->>LLM: ❌ FAIL — null result → "data not available" (no invention)
    else LLM misinterprets restart count (says "restarted since Tuesday" when restarts predate query)
        Checker-->>LLM: ⚠️ LOW CONFIDENCE — causal interpretation unverifiable
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **Historical state query** — queries KubeArchive REST API for pod state at a specific ISO 8601 timestamp
- **Restart detection** — flags pods with restart_count > 5 and pods in failing phases (CrashLoopBackOff, Error, ImagePullBackOff, Evicted)
- **Comparison mode** — compares historical vs current state, shows delta (pods added/removed), marks pods that no longer exist as `currently_exists=False`
- **Error translation** — HTTP errors (ConnectError, HTTPStatusError, TimeoutException) translated to `KubeArchiveUnavailableError`; expired timestamps handled gracefully
- **KubeArchive not installed** — returns installation hint URL instead of crashing

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_is_frozen_dataclass` | `tests/unit/test_historical_pod.py` | ✅ |
| `test_restarting_pods_filtered` | `tests/unit/test_historical_pod.py` | ✅ |
| `test_failing_pods_filtered` | `tests/unit/test_historical_pod.py` | ✅ |
| `test_delta_shows_added_pods` | `tests/unit/test_historical_pod.py` | ✅ |
| `test_delta_shows_removed_pods` | `tests/unit/test_historical_pod.py` | ✅ |
| `test_inherits_from_hexawyn_error` | `tests/unit/test_kubearchive_errors.py` | ✅ |
| `test_message_includes_timestamp_and_retention` | `tests/unit/test_kubearchive_errors.py` | ✅ |
| `test_has_query_historical_state_method` | `tests/unit/test_kubearchive_port.py` | ✅ |
| `test_is_frozen` | `tests/unit/test_query_kubearchive_command.py` | ✅ |
| `test_delegates_to_service_port` | `tests/unit/test_query_kubearchive_use_case.py` | ✅ |
| `test_query_returns_pods_from_kubearchive` | `tests/unit/test_historical_state_query_service.py` | ✅ |
| `test_compare_with_current_mode` | `tests/unit/test_historical_state_query_service.py` | ✅ |
| `test_kubearchive_unavailable` | `tests/unit/test_historical_state_query_service.py` | ✅ |
| `test_implements_kubearchive_port` | `tests/unit/test_kubearchive_http_adapter.py` | ✅ |
| `test_query_historical_state_happy_path` | `tests/unit/test_kubearchive_http_adapter.py` | ✅ |
| `test_kubearchive_unreachable` | `tests/unit/test_kubearchive_http_adapter.py` | ✅ |
| `test_http_error_translated` | `tests/unit/test_kubearchive_http_adapter.py` | ✅ |
| `test_returns_pods_for_namespace` | `tests/unit/test_query_kubearchive.py` | ✅ |
| `test_handles_error_gracefully` | `tests/unit/test_query_kubearchive.py` | ✅ |
| `test_with_comparison_mode` | `tests/unit/test_query_kubearchive.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/historical_pod.py` — HistoricalPod, HistoricalStateSnapshot, StateComparison, PodRestartStatus
- `src/hexawyn/domain/errors.py` — KubeArchiveUnavailableError, HistoricalDataWindowExpiredError
- `src/hexawyn/application/ports/driven/kubearchive_port.py` — KubeArchivePort ABC + TypedDicts
- `src/hexawyn/application/ports/driving/query_kubearchive/` — Command, Response, ServicePort ABC
- `src/hexawyn/application/service/historical_state_query_service.py` — service implementation
- `src/hexawyn/application/use_case/query_kubearchive/` — QueryKubeArchiveUseCase
- `src/hexawyn/adapters/secondary/kubearchive_http_adapter.py` — KubeArchiveHTTPAdapter
- `src/hexawyn/mcp/tools/query_kubearchive.py` — MCP tool
