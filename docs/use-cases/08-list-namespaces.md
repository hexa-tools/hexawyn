# Use Case 5 — List All Namespaces with Age Overview

## Sample Questions

- "List all Kubernetes namespaces in the cluster"
- "What namespaces exist and how old are they?"
- "Which namespaces were created recently?"
- "Show me the full namespace inventory for this cluster"

---

The user asks an AI agent (via MCP) to list all Kubernetes namespaces with their age. The flow goes through: MCP Tool → ListNamespacesUseCase (ABC) → ListNamespacesService → K8sPort (driven port) → VanillaAdapter/DemoAdapter → Kubernetes API. Tools are discovered at CLI startup and synced once to the control-plane (Valkey cache). The PlannerAgent reads tools from cache — not from the investigation payload.

### Flow 1 — Startup: Tool Discovery + Sync to Control-Plane

```mermaid
sequenceDiagram
    participant CLI as hexa start (CLI)
    participant Discovery as MCPDiscoveryAdapter
    participant MCP as FastMCP (in-process)
    participant Client as RuntimeClient
    participant CP as Control-Plane API
    participant Valkey

    CLI->>Discovery: discover()
    Discovery->>MCP: asyncio.run(mcp.list_tools())
    MCP-->>Discovery: [Tool(name="list_namespaces", ...), ...]
    Discovery-->>CLI: MCPToolRegistry (cached in-memory)

    CLI->>Client: post_tools(registry.to_payload())
    Client->>CP: POST /api/v1/tools/sync {tools: [...]}
    CP->>Valkey: cache_set("hexawyn:available_tools", json, ttl=86400)
    Valkey-->>CP: OK
    CP-->>Client: {status: "ok", count: 2}
```

### Flow 2 — Investigation: Agent Routes to list_namespaces via BM25

```mermaid
sequenceDiagram
    participant User as AI Agent
    participant CP as Control-Plane
    participant Valkey as Valkey Cache
    participant Node as parse_intent (LangGraph)
    participant BM25 as BM25ToolRanker
    participant Planner as PlannerAgent (LLM)
    participant MCP as MCP Server (CLI)

    User->>CP: "list namespaces"

    Note over CP: investigation request — NO available_tools in payload

    CP->>Node: parse_intent(query="list namespaces")

    Node->>Valkey: cache_get("hexawyn:available_tools")
    Valkey-->>Node: [{name:"list_namespaces", ...}, ...]

    Node->>BM25: rank(query="list namespaces", tools=[...])
    Note over BM25: tokenize → "list" + "namespaces"<br/>list_namespaces: high score (match name+desc)<br/>get_pod_logs: low score
    BM25-->>Node: [RankedTool(name="list_namespaces", score=0.95), ...]

    Node->>Planner: invoke(state, ranked_tools)
    Planner-->>Node: {tool_name: "list_namespaces"}

    Node-->>CP: ParseIntentOutput(tool_name="list_namespaces")

    CP->>MCP: Call tool "list_namespaces"
    MCP-->>CP: [{name:"default", status:"Active", age:"30d"}, ...]

    CP-->>User: [{name, status, age}, ...]
```

### Flow 3 — Happy Path: Tool Execution (CLI Side)

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as list_namespaces()
    participant UseCase as ListNamespacesUseCase (ABC)
    participant Service as ListNamespacesService
    participant Port as K8sPort (ABC)
    participant Adapter as VanillaAdapter
    participant API as Kubernetes API

    AI->>MCP: Call tool "list_namespaces"
    MCP->>Tool: @mcp.tool() dispatch

    Tool->>UseCase: ListNamespacesService(k8s_port=adapter)<br/>use_case.execute(ListNamespacesCommand())
    UseCase->>Service: service.list_namespaces(command)
    Service->>Port: k8s_port.list_namespaces()
    Port->>Adapter: VanillaAdapter.list_namespaces()

    Adapter->>API: GET /api/v1/namespaces (timeout=5s)
    API-->>Adapter: NamespaceList { items: [...] }

    Note over Adapter: metadata.creation_timestamp → age:<br/>30d, 2h, 5m

    Adapter-->>Port: list[NamespaceInfo]
    Port-->>Service: [{name, status, age}, ...]
    Service-->>UseCase: ListNamespacesResponse
    UseCase-->>Tool: response
    Tool-->>MCP: { namespaces: [...], error: None }
    MCP-->>AI: [{name:"default", status:"Active", age:"30d"}, ...]
```

### Flow 4 — Error: Cluster Unreachable

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as list_namespaces() @mcp.tool()
    participant Adapter as VanillaAdapter
    participant API as Kubernetes API

    AI->>Tool: Call "list_namespaces"
    Tool->>Adapter: VanillaAdapter("prod-eu")
    Adapter->>API: load_kubeconfig(context="prod-eu")
    API-->>Adapter: ❌ ClusterUnreachableError("no kubeconfig")

    Note over Tool: Primary adapter catches<br/>Service/UseCase never catch

    Adapter-->>Tool: ClusterUnreachableError propagates
    Tool-->>AI: { namespaces: [], error: "no kubeconfig" }
```

## Key Points

- **Tools synced once at startup** → `POST /api/v1/tools/sync` → Valkey. Not sent with every investigation.
- **parse_intent reads from Valkey** → `cache_get("hexawyn:available_tools")`. No `available_tools` in payload.
- **NamespaceInfo = {name, status, age}** — age derived from `metadata.creation_timestamp`.
- **UseCase = ABC, Service = impl** — same pattern as `ChatCliUseCase`/`ChatCliService`.
- **Primary adapter (MCP tool) is the only layer that catches exceptions.**

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_creates_namespace_info_with_all_fields` | `tests/unit/test_k8s_port.py` | ✅ |
| `test_list_namespaces_is_abstract` | `tests/unit/test_k8s_port.py` | ✅ |
| `test_implements_use_case` | `tests/unit/test_list_namespaces_use_case.py` | ✅ |
| `test_delegates_to_port` | `tests/unit/test_list_namespaces_use_case.py` | ✅ |
| `test_list_namespaces_returns_namespace_info_list` | `tests/unit/test_vanilla_adapter.py` | ✅ |
| `test_list_namespaces_terminating_status` | `tests/unit/test_vanilla_adapter.py` | ✅ |
| `test_list_namespaces_returns_list` | `tests/unit/test_demo_adapter.py` | ✅ |
| `test_list_namespaces_tool_is_registered` | `tests/unit/test_server.py` | ✅ |
| `test_sync_tools_returns_ok` | `tests/unit/test_api.py` (control-plane) | ✅ |
| `test_run_with_available_tools_ranks_and_returns` | `tests/unit/test_planner_integration.py` (control-plane) | ✅ |

## Related Files

- `src/hexawyn/application/ports/driven/k8s_port.py` — NamespaceInfo TypedDict + K8sPort ABC
- `src/hexawyn/application/use_case/list_namespaces/` — ListNamespacesUseCase (ABC)
- `src/hexawyn/application/service/list_namespaces_service.py` — ListNamespacesService (impl)
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py` — VanillaAdapter
- `src/hexawyn/adapters/secondary/mock/demo_adapter.py` — DemoAdapter
- `src/hexawyn/adapters/secondary/mcp/mcp_discovery_adapter.py` — Tool discovery at startup
- `src/hexawyn/mcp/server.py` — MCP tool registration + build_k8s_adapter()
- `src/hexawyn/mcp/tools/list_namespaces.py` — MCP tool
- `src/hexawyn/cli/app.py` — _sync_tools_to_control_plane()
- `src/hexawyn/api/routers/tools.py` (control-plane) — POST /api/v1/tools/sync
- `src/hexawyn/lang_graph/nodes/parse_intent.py` (control-plane) — _load_tools_from_cache()
