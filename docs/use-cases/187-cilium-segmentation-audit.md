# Use Case 187 — Cilium Segmentation Audit

## Sample Questions

- "Which workloads can reach each other through Cilium identities without a policy?"
- "Audit my east-west segmentation and show me the allowed-but-unrestricted paths"
- "Which Cilium identities can talk to each other freely across tiers?"
- "Show me the reachability matrix between Cilium identities and where policies block traffic"
- "Are there any paths between Cilium identities that no policy restricts?"

---

A security engineer wants to audit east-west segmentation based on Cilium
identities and policies to confirm workloads in one tier cannot reach another
without a policy. The tool builds a reachability matrix from Cilium security
identities and their network policies, flagging allowed-but-unrestricted paths
(no source egress nor destination ingress policy). It explicitly distinguishes
the Cilium view from the vanilla NetworkPolicy view and returns NOT_INSTALLED
when Cilium is absent. The flow crosses the hexagonal layers: MCP Tool →
CiliumSegmentationAuditUseCase → CiliumPort (driven port) → CiliumAdapter
(secondary) → VanillaAdapter → Kubernetes API.

### Flow 1 — Happy Path: Build the Reachability Matrix

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as cilium_segmentation_audit (MCP Tool)
    participant UseCase as CiliumSegmentationAuditUseCase
    participant Port as CiliumPort (ABC)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    User->>Tool: "Audit east-west segmentation"
    Tool->>UseCase: execute(CiliumSegmentationAuditCommand())
    UseCase->>Port: segmentation_audit()
    Port->>Adapter: identities + policies

    Adapter->>API: list ciliumidentities
    API-->>Adapter: identities
    Adapter->>API: list cilium network policies
    API-->>Adapter: policies

    Note over Adapter: source egress / destination ingress per pair<br/>flag allowed-but-unrestricted paths

    Adapter-->>Port: CiliumSegmentationAudit(view="cilium")
    Port-->>UseCase: CiliumSegmentationAuditResult
    UseCase-->>Tool: CiliumSegmentationAuditResponse(findings, matrix)
    Tool-->>User: { view, total_paths, uncovered_paths, findings, ... }
```

### Flow 2 — Errors: Not Installed (Vanilla fallback), RBAC, Unreachable

```mermaid
sequenceDiagram
    participant Tool as cilium_segmentation_audit (MCP Tool)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    alt No cilium.io CRD group (404)
        Adapter->>API: list ciliumidentities
        API-->>Adapter: status 404
        Adapter-->>Tool: CiliumSegmentationAudit(installed=False, view="vanilla")
        Tool-->>Tool: { installed=False, status="not_installed", view="vanilla", note=... }
    else RBAC forbidden
        Adapter->>API: list identities / policies
        API-->>Adapter: status 403
        Adapter-->>Tool: InsufficientPermissionsError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    else Cluster unreachable / timeout
        Adapter->>API: list identities / policies
        API-->>Adapter: connection refused / timeout
        Adapter-->>Tool: ClusterUnreachableError / AdapterTimeoutError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    end
```

### Flow 3 — Checker Node: Honest Matrix

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Result as CiliumSegmentationAuditResult
    participant Store as Memory / Response

    Checker->>Result: cross-check paths against identities/policies

    alt Path invented
        Checker-->>Checker: FAIL (path must come from identity matrix)
        Checker-->>Store: findings from observed identities/policies
    else Severity fabricated
        Checker-->>Checker: FLAG (derived from observed coverage only)
        Checker-->>Store: severity observed (unrestricted = high)
    else Source omitted
        Checker-->>Checker: FAIL (each path tagged source)
        Checker-->>Store: source_id + destination_id on every finding
    else Observed and valid
        Checker-->>Store: PASS (store matrix)
    end
```

### Flow 4 — DuckDB Memory: Query-Before, Store-After, Offline Fallback

```mermaid
sequenceDiagram
    participant Tool as cilium_segmentation_audit (MCP Tool)
    participant Cache as Cache / DuckDB
    participant Adapter as CiliumAdapter (secondary)

    Note over Tool: VSS search before (semantic cache hit)
    Tool->>Cache: search_similar("cilium east-west segmentation")
    Cache-->>Tool: similar prior audit (optional shortcut)

    Tool->>Adapter: segmentation_audit()
    Adapter-->>Tool: CiliumSegmentationAuditResult

    Note over Tool: store after (observed, not invented)
    Tool->>Cache: store matrix + note

    Note over Tool: offline fallback (no cluster)
    Cache-->>Tool: degraded answer with explicit note
```

## Key Points

- `CiliumSegmentationAuditUseCase` depends only on `CiliumPort`.
- Reachability is computed purely from Cilium identities and policies; a path
  is flagged when neither the source egress nor the destination ingress is
  restricted by a Cilium policy.
- Each finding carries a source and destination identity and an observed
  severity; paths are deduplicated per identity pair.
- The `view` field explicitly distinguishes "cilium" from the "vanilla"
  NetworkPolicy fallback (used only when Cilium is absent).
- NOT_INSTALLED is returned when the `cilium.io` CRD group is absent — never a
  fabricated matrix.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_flags_unrestricted_paths` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_isolated_when_policy_restricts` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_not_installed_returns_vanilla_view` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_flags_unrestricted_path` | `tests/unit/domain/services/test_segmentation_audit_builder.py` | ✅ |
| `test_isolated_when_policy_blocks_paths` | `tests/unit/domain/services/test_segmentation_audit_builder.py` | ✅ |
| `test_single_identity_trivial_matrix` | `tests/unit/domain/services/test_segmentation_audit_builder.py` | ✅ |
| `test_large_matrix_compact_report` | `tests/unit/domain/services/test_segmentation_audit_builder.py` | ✅ |
| `test_execute_returns_findings` | `tests/unit/application/use_case/cilium/test_uc_cilium_segmentation_audit_use_case.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/cilium.py` — `CiliumPathFinding`, `CiliumSegmentationAuditResult`
- `src/hexawyn/domain/services/cilium/segmentation_audit_builder.py` — pure reachability matrix
- `src/hexawyn/application/ports/driven/cilium_port.py` — `CiliumPort.segmentation_audit()`
- `src/hexawyn/application/use_case/cilium/cilium_segmentation_audit/` — Command, Response, UseCase
- `src/hexawyn/adapters/secondary/gitops/cilium_adapter.py` — `CiliumAdapter.segmentation_audit()`
- `src/hexawyn/mcp/tools/cilium_segmentation_audit.py` — MCP tool
