# Use Case — List Kubernetes Ingresses (vanilla)

## Sample Questions

- "List all ingress resources and their hosts"
- "Which ingresses are missing TLS?"
- "Show all ingress resources and their backend services"
- "Are there duplicate ingress hosts?"
- "Which production ingresses are exposed without TLS?"

---

The user asks an AI agent (via MCP) to inventory vanilla Kubernetes Ingress
resources. The flow goes through: MCP Tool → ListIngressesUseCase → IngressPort
(driven port) → VanillaK8sAdapter → NetworkingV1Api. One Ingress can expose
several hosts (rules) and services; each (host, backend-service) pair becomes
one `IngressInfo`, and duplicate hosts across Ingresses remain visible for the
reporter to flag as routing conflicts.

### Flow 1 — Happy Path: Tool Execution

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as list_ingresses()
    participant UseCase as ListIngressesUseCase
    participant Port as IngressPort (ABC)
    participant Adapter as VanillaK8sAdapter
    participant API as Kubernetes NetworkingV1Api

    AI->>MCP: Call tool "list_ingresses" (namespace="default")
    MCP->>Tool: @mcp.tool() dispatch
    Tool->>UseCase: ListIngressesUseCase(port=build_ingress_adapter())<br/>execute(ListIngressesCommand(namespace))
    UseCase->>Port: port.list_ingresses(namespace)
    Port->>Adapter: VanillaK8sAdapter.list_ingresses(namespace)
    Adapter->>API: list_namespaced_ingress(namespace, timeout_seconds=5)
    API-->>Adapter: IngressList { items: [...] }

    Note over Adapter: spec.rules[].host → host<br/>spec.rules[].http.paths[].backend.service.name → target_service<br/>spec.tls present → tls_enabled=True

    Adapter-->>Port: list[IngressInfo] (name, namespace, host, target_service, tls_enabled)
    Port-->>UseCase: list[IngressInfo]
    UseCase-->>Tool: ListIngressesResponse { items, count, error }
    Tool-->>MCP: { items: [...], count: N, error: None }
    MCP-->>AI: ingresses with hosts, services, TLS
```

### Flow 2 — Multi-rule Ingress: one entry per (host, service)

```mermaid
sequenceDiagram
    participant Adapter as VanillaK8sAdapter
    participant API as NetworkingV1Api

    Adapter->>API: list_namespaced_ingress("production")
    API-->>Adapter: Ingress "api" with 2 rules (a.example.com → a-svc, b.example.com → b-svc)

    Note over Adapter: no information lost — 1 entry per (rule.host, backend.service)
    Adapter-->>Adapter: IngressInfo(a.example.com, a-svc)<br/>IngressInfo(b.example.com, b-svc)
```

### Flow 3 — Errors

```mermaid
sequenceDiagram
    participant Tool as list_ingresses()
    participant Adapter as VanillaK8sAdapter
    participant API as NetworkingV1Api

    Tool->>Adapter: list_ingresses("production")
    alt RBAC 403
        Adapter->>API: list_namespaced_ingress("production")
        API-->>Adapter: ApiException(status=403)
        Adapter-->>Tool: InsufficientPermissionsError
    else API down / kubeconfig missing
        Adapter->>API: list_namespaced_ingress("production")
        API-->>Adapter: ApiException / ConnectionError
        Adapter-->>Tool: ClusterUnreachableError
    end

    Note over Tool: Primary adapter (MCP tool) is the only layer that catches<br/>UseCase/Port never catch — errors propagate as HexawynError
    Tool-->>Tool: { items: [], count: 0, error: "..." }
```

### Flow 4 — Duplicate hosts exposed for the reporter

```mermaid
sequenceDiagram
    participant Adapter as VanillaK8sAdapter
    participant Reporter as Reporter (upper layer)

    Adapter->>Adapter: payments-api → api.payments.example.com<br/>payments-api-v2 → api.payments.example.com

    Note over Adapter: two Ingresses claim the same host — both returned, no heuristic
    Adapter-->>Reporter: [IngressInfo(payments-api, api.payments.example.com),<br/>IngressInfo(payments-api-v2, api.payments.example.com)]

    Note over Reporter: detects the routing conflict from the data
```

## Key Points

- **No server to run**: configured via stdio (`python -m hexawyn.mcp.stdio`),
  the client spawns the server per session.
- **IngressInfo = {name, namespace, host, target_service, tls_enabled}** —
  TLS derived only from `spec.tls`, never invented.
- **Multi-rule Ingresses are flattened per (host, service)** — no silent loss.
- **Duplicate hosts stay visible** — the tool reports facts; conflict detection
  is left to the reporter (no benchmark-specific heuristic).
- **Primary adapter (MCP tool) is the only layer that catches exceptions.**
- Errors are translated: 403 → `InsufficientPermissionsError`, otherwise →
  `ClusterUnreachableError`.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_install_configures_server` | `tests/unit/cli/integrations/mcp/test_cli_mcp.py` | ✅ |
| `test_list_ingresses_extracts_host_service_and_tls` | `tests/unit/adapters/secondary/vanilla/test_k8s_adapter.py` | ✅ |
| `test_list_ingresses_multiple_rules_produce_multiple_entries` | `tests/unit/adapters/secondary/vanilla/test_k8s_adapter.py` | ✅ |
| `test_list_ingresses_rbac_error` | `tests/unit/adapters/secondary/vanilla/test_k8s_adapter.py` | ✅ |
| `test_list_ingresses_unreachable_error` | `tests/unit/adapters/secondary/vanilla/test_k8s_adapter.py` | ✅ |
| `test_execute_returns_response` | `tests/unit/application/use_case/ingress/test_list_ingresses_use_case.py` | ✅ |
| `test_execute_passes_namespace_to_port` | `tests/unit/application/use_case/ingress/test_list_ingresses_use_case.py` | ✅ |
| `test_full_chain_lists_hosts_services_and_tls` | `tests/unit/mcp/tools/test_list_ingresses_chain.py` | ✅ |
| `test_duplicate_host_claims_are_exposed_for_the_reporter` | `tests/unit/mcp/tools/test_list_ingresses_chain.py` | ✅ |
| `test_build_ingress_adapter` | `tests/unit/test_server.py` | ✅ |

## Related Files

- `src/hexawyn/mcp/tools/list_ingresses.py` — MCP tool
- `src/hexawyn/application/use_case/ingress/list_ingresses/` — command / use case / response
- `src/hexawyn/application/ports/driven/ingress_port.py` — IngressInfo TypedDict + IngressPort ABC
- `src/hexawyn/adapters/secondary/vanilla/adapters/k8s_adapter.py` — VanillaK8sAdapter.list_ingresses
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py` — IngressPort delegation
- `src/hexawyn/mcp/adapters/cluster_adapters.py` — build_ingress_adapter()
- `src/hexawyn/mcp/server.py` — registration + `__all__`
- `src/hexawyn/mcp/stdio.py` — stdio entrypoint spawned by coding agents
