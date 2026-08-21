# Use Case — List OpenShift SecurityContextConstraints

## Sample Questions

- "Show me the SecurityContextConstraints that allow privileged containers."
- "Which SCCs run as RunAsAny?"
- "Audit the OpenShift SCCs for allow_privileged_container=true."

---

Lists OpenShift `security.openshift.io` SecurityContextConstraints (the
OpenShift form of PodSecurityPolicies) through the OpenShift adapter.
`allowPrivilegedContainer` and `runAsUser.type` are read at the root of the
SCC.

### Flow 1 — Happy Path

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as list_openshift_sccs()
    participant UseCase as ListOpenshiftSccsUseCase
    participant Port as OpenShiftResourcePort (ABC)
    participant Adapter as OpenShiftAdapter
    participant API as CustomObjectsApi

    AI->>Tool: Call "list_openshift_sccs"
    Tool->>UseCase: execute(ListOpenshiftSccsCommand())
    UseCase->>Port: list_security_context_constraints()
    Port->>Adapter: _list_cluster(security.openshift.io, v1, securitycontextconstraints)
    Adapter->>API: list_cluster_custom_object(...)
    API-->>Adapter: SCCList

    Note over Adapter: allowPrivilegedContainer (root)<br/>runAsUser.type (root)

    Adapter-->>Port: list[SecurityContextConstraintInfo]
    Port-->>UseCase: list[SecurityContextConstraintInfo]
    UseCase-->>Tool: ListOpenshiftSccsResponse { items, count, error }
    Tool-->>AI: SCCs with privileged and run-as-user settings
```

### Flow 2 — Errors

```mermaid
sequenceDiagram
    participant Tool as list_openshift_sccs()
    participant Adapter as OpenShiftAdapter
    participant API as CustomObjectsApi

    Tool->>Adapter: list_security_context_constraints()
    alt RBAC 403
        API-->>Adapter: ApiException(status=403)
        Adapter-->>Tool: InsufficientPermissionsError
    else API down
        API-->>Adapter: ApiException(status=500)
        Adapter-->>Tool: ClusterUnreachableError
    end
```

## Key Points

- `SecurityContextConstraintInfo = {name, allow_privileged_container, run_as_user_type}`
  — read at the SCC root, matching the real CRD shape.
- Cluster-wide resource (no namespace scope).

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_sccs_expose_allow_privileged_and_run_as` | `tests/unit/runtime/agents/strategies/test_openshift.py` | ✅ |
| `test_maps_sccs` | `tests/unit/adapters/secondary/openshift/test_openshift_adapter.py` | ✅ |
| `test_execute_returns_response` | `tests/unit/application/use_case/openshift/test_uc_list_openshift_sccs_use_case.py` | ✅ |
| `test_list_openshift_sccs_returns_dict` | `tests/unit/mcp/tools/test_tool_list_openshift_sccs.py` | ✅ |

## Related Files

- `src/hexawyn/mcp/tools/list_openshift_sccs.py`
- `src/hexawyn/application/use_case/openshift/list_openshift_sccs/`
- `src/hexawyn/application/ports/driven/openshift_resource_port.py`
- `src/hexawyn/adapters/secondary/openshift/openshift_adapter.py`
