# Use Case — List OpenShift Routes

## Sample Questions

- "Which routes are exposed in the payments namespace, and are they TLS-enabled?"
- "Show me all OpenShift routes for the web namespace with their target services."
- "Are there any routes serving traffic without TLS termination?"
- "What hostnames are exposed via routes in the frontend namespace?"

---

Lists OpenShift `route.openshift.io` Routes through the OpenShift adapter. For
vanilla Kubernetes, use `list_ingresses` instead — the two capabilities stay
distinct.

### Flow 1 — Happy Path

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as list_openshift_routes()
    participant UseCase as ListOpenshiftRoutesUseCase
    participant Port as OpenShiftResourcePort (ABC)
    participant Adapter as OpenShiftAdapter
    participant API as CustomObjectsApi

    AI->>Tool: Call "list_openshift_routes" (namespace="payments")
    Tool->>UseCase: execute(ListOpenshiftRoutesCommand(namespace))
    UseCase->>Port: list_routes(namespace)
    Port->>Adapter: _list_namespaced(route.openshift.io, v1, routes, namespace)
    Adapter->>API: list_namespaced_custom_object(...)
    API-->>Adapter: RouteList
    Adapter-->>Port: list[RouteInfo] (host, target_service, tls_enabled)
    Port-->>UseCase: list[RouteInfo]
    UseCase-->>Tool: ListOpenshiftRoutesResponse { items, count, error }
    Tool-->>AI: routes with hosts, target services, TLS
```

### Flow 2 — Errors

```mermaid
sequenceDiagram
    participant Tool as list_openshift_routes()
    participant Adapter as OpenShiftAdapter
    participant API as CustomObjectsApi

    Tool->>Adapter: list_routes("payments")
    alt RBAC 403
        API-->>Adapter: ApiException(status=403)
        Adapter-->>Tool: InsufficientPermissionsError
    else API down
        API-->>Adapter: ApiException(status=500)
        Adapter-->>Tool: ClusterUnreachableError
    end
```

## Key Points

- `RouteInfo = {name, namespace, host, target_service, tls_enabled}` — TLS from
  `spec.tls`, never invented.
- OpenShift-only: vanilla clusters use `list_ingresses`.
- Infra exceptions are translated by the adapter — never escape as raw `ApiException`.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_handle_list_routes` | `tests/unit/runtime/agents/strategies/test_openshift.py` | ✅ |
| `test_maps_routes` | `tests/unit/adapters/secondary/openshift/test_openshift_adapter.py` | ✅ |
| `test_execute_returns_response` | `tests/unit/application/use_case/openshift/test_uc_list_openshift_routes_use_case.py` | ✅ |
| `test_list_openshift_routes_returns_dict` | `tests/unit/mcp/tools/test_tool_list_openshift_routes.py` | ✅ |

## Related Files

- `src/hexawyn/mcp/tools/list_openshift_routes.py`
- `src/hexawyn/application/use_case/openshift/list_openshift_routes/`
- `src/hexawyn/application/ports/driven/openshift_resource_port.py`
- `src/hexawyn/adapters/secondary/openshift/openshift_adapter.py`
