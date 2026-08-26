# Use Case — List OpenShift Projects

## Sample Questions

- "List all OpenShift projects and their current status."
- "What projects exist in my OpenShift cluster and how are they doing?"
- "Show me every project on this OCP cluster with its display name."
- "How many projects do we have running in production OpenShift?"

---

Lists OpenShift `project.openshift.io` Projects (the OpenShift form of
Namespaces) through the OpenShift adapter. `status.phase` drives the status;
`spec.displayName` is the human-readable name.

### Flow 1 — Happy Path

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as list_openshift_projects()
    participant UseCase as ListOpenshiftProjectsUseCase
    participant Port as OpenShiftResourcePort (ABC)
    participant Adapter as OpenShiftAdapter
    participant API as CustomObjectsApi

    AI->>Tool: Call "list_openshift_projects"
    Tool->>UseCase: execute(ListOpenshiftProjectsCommand())
    UseCase->>Port: list_projects()
    Port->>Adapter: _list_cluster(project.openshift.io, v1, projects)
    Adapter->>API: list_cluster_custom_object(...)
    API-->>Adapter: ProjectList

    Note over Adapter: status.phase → status<br/>spec.displayName → display_name

    Adapter-->>Port: list[ProjectInfo] (name, status, display_name)
    Port-->>UseCase: list[ProjectInfo]
    UseCase-->>Tool: ListOpenshiftProjectsResponse { items, count, error }
    Tool-->>AI: projects with status and display names
```

### Flow 2 — Errors

```mermaid
sequenceDiagram
    participant Tool as list_openshift_projects()
    participant Adapter as OpenShiftAdapter
    participant API as CustomObjectsApi

    Tool->>Adapter: list_projects()
    alt RBAC 403
        API-->>Adapter: ApiException(status=403)
        Adapter-->>Tool: InsufficientPermissionsError
    else API down
        API-->>Adapter: ApiException(status=500)
        Adapter-->>Tool: ClusterUnreachableError
    end
```

## Key Points

- `ProjectInfo = {name, status, display_name}` — status derived from
  `status.phase`, never from a `status` string.
- OpenShift-only: vanilla clusters use `list_namespaces`.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_projects_expose_phase_and_display_name` | `tests/unit/runtime/agents/strategies/test_openshift.py` | ✅ |
| `test_maps_projects` | `tests/unit/adapters/secondary/openshift/test_openshift_adapter.py` | ✅ |
| `test_execute_returns_response` | `tests/unit/application/use_case/openshift/test_uc_list_openshift_projects_use_case.py` | ✅ |
| `test_list_openshift_projects_returns_dict` | `tests/unit/mcp/tools/test_tool_list_openshift_projects.py` | ✅ |

## Related Files

- `src/hexawyn/mcp/tools/list_openshift_projects.py`
- `src/hexawyn/application/use_case/openshift/list_openshift_projects/`
- `src/hexawyn/application/ports/driven/openshift_resource_port.py`
- `src/hexawyn/adapters/secondary/openshift/openshift_adapter.py`
