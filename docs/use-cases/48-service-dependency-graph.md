# Use Case 48 — Service Dependency Graph

## Sample Questions

- "Draw the dependency graph between services for the last hour"
- "Show me the runtime service interactions derived from OTel traces"
- "What is the call graph between my microservices?"
- "Which service calls which based on actual trace data?"
- "Build a dependency map from spans showing caller-callee relationships"

---

One MCP tool: `service_dependency_graph`. Extracts service-to-service edges from OTel span parent/child relationships, builds a directed graph with call counts, avg latency, and error rate per edge.

### Flow 1 — Happy Path: Graph Built

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as service_dependency_graph
    participant Service as ServiceDependencyGraphService
    participant Port as ServiceDependencyGraphPort
    participant Adapter as OTelDependencyGraphAdapter
    participant OTel as OTel Trace API

    AI->>MCP: "Draw dependency graph for last hour"
    MCP->>Tool: service_dependency_graph(60)

    Tool->>Service: build(command)
    Service->>Port: fetch_edges(req)
    Port->>Adapter: OTelDependencyGraphAdapter
    Adapter->>OTel: query all spans with parent/child links
    OTel-->>Adapter: api-gateway→auth (12450 calls, 82ms), payment→postgres (24600 calls, 35ms)

    Note over Service: Merge edges by source→target<br/>4 nodes: api-gateway, auth-service, payment, postgres<br/>2 edges aggregated

    Service-->>Tool: DependencyGraph(nodes=[4 services], edges=[2 edges])
    Tool-->>MCP: {nodes: ["api-gateway", "auth-service", "payment-service", "postgres-db"], edges: [{...}]}
    MCP-->>AI: "4 services, 2 edges:<br/>api-gateway → auth-service: 12750 calls, avg 82ms, error 2%<br/>payment-service → postgres-db: 24600 calls, avg 35ms, error 0%"
```

### Flow 2 — Isolated Nodes

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as service_dependency_graph
    participant Service as ServiceDependencyGraphService

    AI->>Tool: service_dependency_graph(60)
    Tool->>Service: build()
    Note over Service: No parent/child edges found<br/>Only root spans = isolated services

    Service-->>Tool: nodes=[], edges=[]
    Tool-->>AI: "No inter-service calls detected in the last hour. All traces are single-service."
```

### Flow 3 — OTel Unreachable

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as service_dependency_graph
    participant Adapter as OTelDependencyGraphAdapter
    participant OTel as OTel Trace API

    AI->>Tool: service_dependency_graph(60)
    Tool->>Adapter: fetch_edges(...)
    Adapter->>OTel: query
    OTel-->>Adapter: ❌ ConnectionError

    Adapter-->>Tool: exception
    Tool-->>AI: {error: "OTel backend unreachable"}
```

### Flow 4 — Checker Node: New Service Detection

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate graph accuracy
    alt LLM shows only unidirectional edge when bidirectional exists
        Checker-->>LLM: ⚠️ FLAG — "A→B AND B→A both detected, show both directions"
    alt LLM rounds call count without caveat (sampled data)
        Checker-->>LLM: ⚠️ FLAG — "extrapolated from X% sampling"
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **Edge extraction** — `source→target` from span parent/child service.name attributes
- **Aggregation** — multiple raw edges merged into single edge with summed call_count
- **Error rate** — `total_errors / call_count` per edge

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_build_from_spans` | `tests/unit/test_service_dependency_graph.py` | ✅ |
| `test_no_edges` | `tests/unit/test_service_dependency_graph.py` | ✅ |
| `test_returns_graph` | `tests/unit/test_service_dependency_graph_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/service_dependency_graph.py` — ServiceNode, ServiceEdge, DependencyGraph
- `src/hexawyn/application/ports/driven/service_dependency_graph_port.py` — ServiceDependencyGraphPort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_dependency_graph_adapter.py` — OTelDependencyGraphAdapter
- `src/hexawyn/mcp/tools/service_dependency_graph.py` — MCP tool
