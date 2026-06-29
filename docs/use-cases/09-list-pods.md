# Use Case 6 — List Pods in Namespace

An AI agent asks to list all pods in a given namespace with health status. The flow goes through: MCP Tool → ListPodsUseCase (ABC) → ListPodsService → K8sPort (driven port) → VanillaAdapter/DemoAdapter → Kubernetes API. Pods are sorted unhealthy first (CrashLoop → Pending → Running), then alphabetically. Tools are auto-discovered at startup and synced to the control-plane.

### Flow 1 — Happy Path: List Pods in a Namespace

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as list_pods(namespace)
    participant UseCase as ListPodsUseCase (ABC)
    participant Service as ListPodsService
    participant Port as K8sPort (ABC)
    participant Adapter as VanillaAdapter
    participant API as Kubernetes API

    AI->>MCP: Call tool "list_pods" namespace="production"
    MCP->>Tool: @mcp.tool() dispatch

    Tool->>UseCase: ListPodsService(k8s_port)<br/>use_case.execute(ListPodsCommand(namespace="production"))
    UseCase->>Service: service.execute(command)
    Service->>Port: k8s_port.list_pods(namespace="production")

    Port->>Adapter: VanillaAdapter.list_pods(namespace="production")
    Adapter->>API: GET /api/v1/namespaces/production/pods (timeout=5s)
    API-->>Adapter: PodList { items: [...] }

    Note over Adapter: _to_pod_info():<br/>name, namespace, status, restarts<br/>age (creation_timestamp), node (spec.node_name)

    Adapter-->>Port: list[PodInfo]
    Port-->>Service: [{name, namespace, status, restarts, age, node}, ...]

    Note over Service: _sort_key():<br/>CrashLoop=0, Pending=2, Running=99<br/>then by name alphabetically

    Service-->>UseCase: ListPodsResponse(pods=[unhealthy_first...])
    UseCase-->>Tool: response
    Tool-->>MCP: { pods: [...], error: None }
    MCP-->>AI: [{name:"payments-api", status:"CrashLoop", restarts:5, age:"2d", node:"node-1"}, ...]
```

### Flow 2 — Error: Namespace Not Found

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as list_pods(namespace="ghost")
    participant Adapter as VanillaAdapter
    participant API as Kubernetes API

    AI->>Tool: Call "list_pods" namespace="ghost"
    Tool->>Adapter: VanillaAdapter.list_pods(namespace="ghost")
    Adapter->>API: GET /api/v1/namespaces/ghost/pods
    API-->>Adapter: ❌ 404 NotFound

    Note over Tool: Primary adapter catches<br/>Service/UseCase never catch

    Adapter-->>Tool: error propagates
    Tool-->>AI: { pods: [], error: "namespace not found" }
```

### Flow 3 — Error: RBAC Access Denied

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as list_pods(namespace="secure")
    participant Adapter as VanillaAdapter
    participant API as Kubernetes API

    AI->>Tool: Call "list_pods" namespace="secure"
    Tool->>Adapter: VanillaAdapter.list_pods(namespace="secure")
    Adapter->>API: GET /api/v1/namespaces/secure/pods
    API-->>Adapter: ❌ 403 Forbidden

    Note over Tool: Primary adapter catches

    Adapter-->>Tool: ApiException("forbidden")
    Tool-->>AI: { pods: [], error: "access denied" }
```

### Flow 4 — Startup: Tool Auto-Discovery + Sync

```mermaid
sequenceDiagram
    participant CLI as hexa start
    participant Discovery as MCPDiscoveryAdapter
    participant MCP as FastMCP (in-process)
    participant Client as RuntimeClient
    participant CP as Control-Plane
    participant Valkey

    CLI->>Discovery: discover()
    Discovery->>MCP: asyncio.run(mcp.list_tools())
    MCP-->>Discovery: [Tool(name="list_pods", ...), Tool(name="list_namespaces", ...)]
    Discovery-->>CLI: MCPToolRegistry (cached)

    CLI->>Client: post_tools(registry.to_payload())
    Client->>CP: POST /api/v1/tools/sync {tools: [...]}
    CP->>Valkey: cache_set("hexawyn:available_tools", ...)
    Valkey-->>CP: OK
```

## Key Points

- **Auto-discovery** — `register_tools()` scans `mcp/tools/*.py`, no manual imports needed
- **Sorting** — unhealthy first (CrashLoop=0, Pending=2, Running=99), then alphabetically
- **PodInfo = {name, namespace, status, restarts, age, node}** — age from creation_timestamp, node from spec.node_name
- **UseCase = ABC, Service = impl** — same pattern as all other use cases
- **Primary adapter catches** — MCP tool handles ClusterUnreachable, RBAC, NotFound

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_execute_sorts_unhealthy_first` | `tests/unit/test_list_pods_service.py` | ✅ |
| `test_crashloop_before_running` | `tests/unit/test_list_pods_service.py` | ✅ |
| `test_list_pods_tool_is_registered` | `tests/unit/test_server.py` | ✅ |
| `test_list_pods_returns_pods_for_namespace` | `tests/unit/test_server.py` | ✅ |
| `test_list_pods_empty_namespace` | `tests/unit/test_server.py` | ✅ |
| `test_list_pods_handles_error` | `tests/unit/test_server.py` | ✅ |
| `test_list_pods_returns_real_kubernetes_pods` | `tests/unit/test_vanilla_adapter.py` | ✅ |

## Related Files

- `src/hexawyn/application/ports/driven/k8s_port.py` — PodInfo TypedDict + K8sPort ABC
- `src/hexawyn/application/ports/driving/list_pods/` — Command, Response
- `src/hexawyn/application/use_case/list_pods/` — ListPodsUseCase (ABC)
- `src/hexawyn/application/service/list_pods_service.py` — ListPodsService (sorting)
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py` — VanillaAdapter
- `src/hexawyn/adapters/secondary/mock/demo_adapter.py` — DemoAdapter
- `src/hexawyn/mcp/tools/list_pods.py` — MCP tool
