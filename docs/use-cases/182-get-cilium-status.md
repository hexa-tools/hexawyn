# Use Case 182 — Get Cilium Status

## Sample Questions

- "Are the Cilium agents healthy and is the datapath functional on my cluster?"
- "How many Cilium agents are ready out of the total scheduled across nodes?"
- "Show me the per-node Cilium agent status and whether connectivity is OK"
- "Are there any Cilium controller errors or unhealthy agents right now?"
- "Is any node's dataplane degraded, and which nodes are affected?"

---

A platform/SRE engineer asks whether the Cilium agents and the datapath are
healthy before trusting a network diagnosis. The tool aggregates per-node agent
health into a ready/total summary, surfaces controller errors and a connectivity
probe result, and reports a global degraded summary. When Cilium is absent it
returns NOT_INSTALLED — never a fabricated value. The flow crosses the
hexagonal layers: MCP Tool → GetCiliumStatusUseCase → CiliumPort (driven port)
→ CiliumAdapter (secondary) → VanillaAdapter → Kubernetes API.

### Flow 1 — Happy Path: Read Datapath Health

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as get_cilium_status (MCP Tool)
    participant UseCase as GetCiliumStatusUseCase
    participant Port as CiliumPort (ABC)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    User->>Tool: "Are the Cilium agents healthy?"
    Tool->>UseCase: execute(GetCiliumStatusCommand())
    UseCase->>Port: status()
    Port->>Adapter: read agent pods + endpoints

    Adapter->>API: list daemon-sets (find "cilium")
    API-->>Adapter: DaemonSet list (found)

    Adapter->>API: list pods label k8s-app=cilium
    API-->>Adapter: PodList (agent states)

    Note over Adapter: ready / total per node<br/>controller errors<br/>connectivity ok|degraded

    Adapter-->>Port: CiliumStatusResult(agents, degraded)
    Port-->>UseCase: CiliumStatusResult
    UseCase-->>Tool: GetCiliumStatusResponse(nodes=[...])
    Tool-->>User: { status, ready_agents, controller_errors, connectivity, ... }
```

### Flow 2 — Errors: Not Installed, Unreachable, RBAC

```mermaid
sequenceDiagram
    participant Tool as get_cilium_status (MCP Tool)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    alt No Cilium (CRD 404)
        Adapter->>API: list cilium.io CRDs
        API-->>Adapter: status 404
        Adapter-->>Tool: CiliumStatusResult(installed=False)
        Tool-->>Tool: { installed=False, status="not_installed", note=... }
    else RBAC forbidden
        Adapter->>API: list daemon-sets
        API-->>Adapter: status 403
        Adapter-->>Tool: InsufficientPermissionsError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    else Cluster unreachable
        Adapter->>API: list daemon-sets
        API-->>Adapter: connection refused
        Adapter-->>Tool: ClusterUnreachableError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    end
```

### Flow 3 — Checker Node: Honest Status

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Result as CiliumStatusResult
    participant Store as Memory / Response

    Checker->>Result: cross-check agent counts vs ready

    alt Agents 0 but "healthy"
        Checker-->>Checker: FAIL (healthy must be observed)
        Checker-->>Store: status="unknown", note="no agents observed"
    else Degraded omitted
        Checker-->>Checker: FLAG (degraded must be reported)
        Checker-->>Store: status="degraded", degraded_summary="{ready}/{total} agents ready"
    else Health value fabricated
        Checker-->>Checker: FLAG (observed counts only)
        Checker-->>Store: ready_agents/total_agents from observed pods
    else Observed and valid
        Checker-->>Store: PASS (store result)
    end
```

### Flow 4 — DuckDB Memory: Query-Before, Store-After, Offline Fallback

```mermaid
sequenceDiagram
    participant Tool as get_cilium_status (MCP Tool)
    participant Cache as Cache / DuckDB
    participant Adapter as CiliumAdapter (secondary)

    Note over Tool: VSS search before (semantic cache hit)
    Tool->>Cache: search_similar("are cilium agents healthy?")
    Cache-->>Tool: similar prior answer (optional shortcut)

    Tool->>Adapter: status()
    Adapter-->>Tool: CiliumStatusResult

    Note over Tool: store after (observed, not invented)
    Tool->>Cache: store result + note

    Note over Tool: offline fallback (no cluster)
    Cache-->>Tool: degraded answer with explicit note
```

## Key Points

- `GetCiliumStatusUseCase` depends only on `CiliumPort` — never on a k8s client.
- `status` is `healthy` only when every observed agent is ready; an empty agent
  list is reported as `unknown`, never `healthy`.
- `ready_agents`/`total_agents` come from observed pods; `controller_errors`
  counts non-ready or restarted agents.
- `connectivity` is `ok`/`degraded` derived from readiness; `degraded_summary`
  is a `{ready}/{total} agents ready` string when any agent is down.
- NOT_INSTALLED is returned when the `cilium.io` CRD group is absent — never a
  fabricated value.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_status_healthy_when_all_ready` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_status_degraded_when_some_down` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_status_not_installed` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_status_unreachable_raises_cluster_unreachable` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_healthy_when_all_ready` | `tests/unit/domain/services/test_cilium_status_report_builder.py` | ✅ |
| `test_execute_returns_healthy_response` | `tests/unit/application/use_case/cilium/test_uc_get_cilium_status_use_case.py` | ✅ |
| `test_get_cilium_status_returns_dict` | `tests/unit/mcp/tools/test_tool_get_cilium_status.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/cilium.py` — `CiliumStatusResult`, `CiliumAgentHealth`
- `src/hexawyn/domain/services/cilium/status_report_builder.py` — pure status logic
- `src/hexawyn/application/ports/driven/cilium_port.py` — `CiliumPort` (`status()`)
- `src/hexawyn/application/use_case/cilium/get_cilium_status/` — Command, Response, UseCase
- `src/hexawyn/adapters/secondary/gitops/cilium_adapter.py` — `CiliumAdapter.status()`
- `src/hexawyn/mcp/tools/get_cilium_status.py` — MCP tool
- `src/hexawyn/mcp/adapters/cilium_adapters.py` — `build_cilium_adapter()` wiring
