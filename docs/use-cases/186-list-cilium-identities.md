# Use Case 186 — List Cilium Identities

## Sample Questions

- "List all the Cilium security identities in my cluster"
- "Which pods share the same Cilium identity labels so I can gauge policy effect?"
- "Show me the Cilium identities in the payments namespace with their endpoint counts"
- "What are the numeric IDs and label sets of the Cilium security identities?"
- "How many endpoints are associated with each Cilium identity right now?"

---

A platform/security engineer wants to list the Cilium security identities
(endpoint ↔ labels mapping) to understand which set of pods share an identity
before interpreting policy effect. The tool reads the `cilium.io/v2`
`ciliumidentities` CRD and, when available, counts the associated
`ciliumendpoints` per identity. When the `cilium.io` CRD group is absent it
returns NOT_INSTALLED. The flow crosses the hexagonal layers: MCP Tool →
ListCiliumIdentitiesUseCase → CiliumPort (driven port) → CiliumAdapter
(secondary) → VanillaAdapter → Kubernetes API.

### Flow 1 — Happy Path: List Identities

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as list_cilium_identities (MCP Tool)
    participant UseCase as ListCiliumIdentitiesUseCase
    participant Port as CiliumPort (ABC)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    User->>Tool: "List the Cilium security identities"
    Tool->>UseCase: execute(ListCiliumIdentitiesCommand())
    UseCase->>Port: list_identities()
    Port->>Adapter: read cilium.io identities

    Adapter->>API: list ciliumidentities (v2)
    API-->>Adapter: identities

    Adapter->>API: list ciliumendpoints (v2, optional)
    API-->>Adapter: endpoints

    Note over Adapter: id from metadata.name<br/>labels from spec/metadata<br/>endpoint_count from matching endpoints

    Adapter-->>Port: CiliumIdentitiesResult(identities)
    Port-->>UseCase: CiliumIdentitiesResult
    UseCase-->>Tool: ListCiliumIdentitiesResponse(identities=[...])
    Tool-->>User: { installed, total_identities, identities, ... }
```

### Flow 2 — Errors: Not Installed, RBAC, Unreachable

```mermaid
sequenceDiagram
    participant Tool as list_cilium_identities (MCP Tool)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    alt No cilium.io CRD group (404)
        Adapter->>API: list ciliumidentities
        API-->>Adapter: status 404
        Adapter-->>Tool: CiliumIdentitiesResult(installed=False)
        Tool-->>Tool: { installed=False, status="not_installed", note=... }
    else RBAC forbidden
        Adapter->>API: list ciliumidentities
        API-->>Adapter: status 403
        Adapter-->>Tool: InsufficientPermissionsError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    else Cluster unreachable / timeout
        Adapter->>API: list ciliumidentities
        API-->>Adapter: connection refused / timeout
        Adapter-->>Tool: ClusterUnreachableError / AdapterTimeoutError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    end
```

### Flow 3 — Checker Node: Honest Identities

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Result as CiliumIdentitiesResult
    participant Store as Memory / Response

    Checker->>Result: cross-check identities against the raw list

    alt Identity invented
        Checker-->>Checker: FAIL (identity must come from CRD list)
        Checker-->>Store: identities from observed ciliumidentities
    else Endpoint count fabricated
        Checker-->>Checker: FLAG (counts observed only)
        Checker-->>Store: endpoint_count from matching ciliumendpoints
    else Vanilla labels mixed in
        Checker-->>Checker: FAIL (Cilium identities only)
        Checker-->>Store: labels from cilium.io identities only
    else Observed and valid
        Checker-->>Store: PASS (store identities)
    end
```

### Flow 4 — DuckDB Memory: Query-Before, Store-After, Offline Fallback

```mermaid
sequenceDiagram
    participant Tool as list_cilium_identities (MCP Tool)
    participant Cache as Cache / DuckDB
    participant Adapter as CiliumAdapter (secondary)

    Note over Tool: VSS search before (semantic cache hit)
    Tool->>Cache: search_similar("list cilium identities")
    Cache-->>Tool: similar prior list (optional shortcut)

    Tool->>Adapter: list_identities()
    Adapter-->>Tool: CiliumIdentitiesResult

    Note over Tool: store after (observed, not invented)
    Tool->>Cache: store identities + note

    Note over Tool: offline fallback (no cluster)
    Cache-->>Tool: degraded answer with explicit note
```

## Key Points

- `ListCiliumIdentitiesUseCase` depends only on `CiliumPort`.
- Reads the `cilium.io/v2` `ciliumidentities` CRD — never vanilla labels.
- Each identity reports its numeric `id` (from `metadata.name`), its label set,
  and the count of matching `ciliumendpoints` (0 when the endpoints CRD is not
  available).
- NOT_INSTALLED is returned when the `cilium.io` CRD group is absent.
- A workload/label set is never invented — values come only from observed CRDs.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_list_identities_with_endpoint_counts` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_list_identities_not_installed` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_lists_identities_with_endpoint_counts` | `tests/unit/domain/services/test_identity_builder.py` | ✅ |
| `test_identity_without_labels_reported_empty` | `tests/unit/domain/services/test_identity_builder.py` | ✅ |
| `test_malformed_id_preserved_raw` | `tests/unit/domain/services/test_identity_builder.py` | ✅ |
| `test_execute_returns_identities` | `tests/unit/application/use_case/cilium/test_uc_list_cilium_identities_use_case.py` | ✅ |
| `test_list_cilium_identities_returns_dict` | `tests/unit/mcp/tools/test_tool_list_cilium_identities.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/cilium.py` — `CiliumIdentityInfo`, `CiliumIdentitiesResult`
- `src/hexawyn/domain/services/cilium/identity_builder.py` — pure identity listing
- `src/hexawyn/application/ports/driven/cilium_port.py` — `CiliumPort.list_identities()`
- `src/hexawyn/application/use_case/cilium/list_cilium_identities/` — Command, Response, UseCase
- `src/hexawyn/adapters/secondary/gitops/cilium_adapter.py` — `CiliumAdapter.list_identities()`
- `src/hexawyn/mcp/tools/list_cilium_identities.py` — MCP tool
