# Use Case 192 — Cilium Service Graph

## Sample Questions

- "Draw the service dependency graph from the Cilium flow logs in the payments namespace"
- "Which services talk to each other according to observed Cilium flows?"
- "Show me the Cilium-based service graph with edge traffic and dropped flows"
- "What is the actual connectivity between my workloads from Hubble flows?"
- "Build a service-to-service graph from the last hour of Cilium flows"

---

A platform/observability engineer wants to build a service↔service graph from
Cilium flows (Hubble) to visualize actual connectivity between workloads in a
namespace. The tool aggregates observed flows into graph edges (reusing the
`DependencyGraph.compute` logic from `service_dependency_graph`), so the result
is built from real observed traffic rather than an inferred topology. When
Hubble is unavailable it builds an empty graph (graceful fallback). The flow
crosses the hexagonal layers: MCP Tool → CiliumServiceGraphUseCase →
ServiceDependencyGraphPort (driven port) → HubbleDependencyGraphAdapter
(secondary) → CiliumHubblePort → Hubble Relay.

### Flow 1 — Happy Path: Build the Graph from Flows

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as cilium_service_graph (MCP Tool)
    participant UseCase as CiliumServiceGraphUseCase
    participant Port as ServiceDependencyGraphPort (ABC)
    participant Adapter as HubbleDependencyGraphAdapter
    participant Hubble as Hubble Relay

    User->>Tool: "Draw the service graph from flows"
    Tool->>UseCase: execute(CiliumServiceGraphCommand(time_window))
    UseCase->>Port: fetch_edges(DependencyGraphRequest)
    Port->>Adapter: query flow aggregation

    Adapter->>Hubble: GetFlows(window)
    Hubble-->>Adapter: flows

    Note over Adapter: aggregate to from/to/count/avg_ms/errors
    Adapter-->>Port: raw edges
    Port-->>UseCase: raw edges
    UseCase->>UseCase: DependencyGraph.compute(request, edges)
    UseCase-->>Tool: CiliumServiceGraphResponse(nodes, edges)
    Tool-->>User: { nodes, edges, error, ... }
```

### Flow 2 — Errors: Not Installed (Empty), Unreachable, Timeout

```mermaid
sequenceDiagram
    participant Tool as cilium_service_graph (MCP Tool)
    participant Adapter as HubbleDependencyGraphAdapter
    participant Client as Hubble HTTP client

    alt No Hubble Relay configured
        Adapter->>Client: get_flows()
        Client-->>Adapter: not installed
        Adapter-->>Tool: [] edges -> empty graph
        Tool-->>Tool: { nodes=[], edges=[], note="no flow data" }
    else Unreachable / timeout
        Adapter->>Client: get_flows()
        Client-->>Adapter: connection refused / timeout
        Adapter-->>Tool: ClusterUnreachableError / AdapterTimeoutError
        Tool-->>Tool: { nodes=[], edges=[], error=... }
    end
```

### Flow 3 — Checker Node: Honest Graph

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Graph as DependencyGraph
    participant Store as Memory / Response

    Checker->>Graph: cross-check edges against flows

    alt Edge invented
        Checker-->>Checker: FAIL (edge must come from observed flows)
        Checker-->>Store: edges from flow aggregation
    else Traffic fabricated
        Checker-->>Checker: FLAG (call_count observed only)
        Checker-->>Store: count/errors from observed flows
    else Direction omitted
        Checker-->>Checker: FAIL (direction required)
        Checker-->>Store: from/to on every edge
    else Observed and valid
        Checker-->>Store: PASS (store graph)
    end
```

### Flow 4 — DuckDB Memory: Query-Before, Store-After, Offline Fallback

```mermaid
sequenceDiagram
    participant Tool as cilium_service_graph (MCP Tool)
    participant Cache as Cache / DuckDB
    participant Adapter as HubbleDependencyGraphAdapter

    Note over Tool: VSS search before (semantic cache hit)
    Tool->>Cache: search_similar("service graph from cilium flows")
    Cache-->>Tool: similar prior graph (optional shortcut)

    Tool->>Adapter: fetch_edges(request)
    Adapter-->>Tool: raw edges -> graph

    Note over Tool: store after (observed, not invented)
    Tool->>Cache: store graph + note

    Note over Tool: offline fallback (no Hubble)
    Cache-->>Tool: empty graph with explicit note
```

## Key Points

- `CiliumServiceGraphUseCase` depends only on `ServiceDependencyGraphPort`.
- Reuses `DependencyGraph.compute` (from `service_dependency_graph`) — the only
  difference is the adapter (Hubble flows vs inferred topology).
- Edges are aggregated per `(source, target)` pair with observed flow count,
  average latency (`0` when not reported) and dropped count (error rate).
- An empty graph is returned when Hubble is unavailable or no flows are seen
  (graceful fallback); traffic is never fabricated.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_builds_edges_from_flows` | `tests/unit/adapters/secondary/cilium/test_cilium_hubble_graph_adapter.py` | ✅ |
| `test_empty_when_hubble_not_installed` | `tests/unit/adapters/secondary/cilium/test_cilium_hubble_graph_adapter.py` | ✅ |
| `test_aggregates_by_pair` | `tests/unit/domain/services/test_graph_builder.py` | ✅ |
| `test_counts_dropped_as_errors` | `tests/unit/domain/services/test_graph_builder.py` | ✅ |
| `test_includes_self_loop` | `tests/unit/domain/services/test_graph_builder.py` | ✅ |
| `test_execute_builds_graph` | `tests/unit/application/use_case/cilium/test_uc_cilium_service_graph_use_case.py` | ✅ |
| `test_cilium_service_graph_returns_dict` | `tests/unit/mcp/tools/test_tool_cilium_service_graph.py` | ✅ |

## Related Files

- `src/hexawyn/domain/services/cilium/graph_builder.py` — pure flow→edge aggregation
- `src/hexawyn/adapters/secondary/cilium/cilium_hubble_graph_adapter.py` — `HubbleDependencyGraphAdapter`
- `src/hexawyn/application/ports/driven/service_dependency_graph_port.py` — `ServiceDependencyGraphPort` (reused)
- `src/hexawyn/domain/models/service_dependency_graph.py` — `DependencyGraph.compute` (reused)
- `src/hexawyn/application/use_case/cilium/cilium_service_graph/` — Command, Response, UseCase
- `src/hexawyn/mcp/tools/cilium_service_graph.py` — MCP tool
- `src/hexawyn/mcp/adapters/cilium_adapters.py` — `build_cilium_service_graph_adapter()`
