# Use Case 185 — Cilium Policy Audit

## Sample Questions

- "Which workloads selected by Cilium policies have no ingress or egress restriction?"
- "Audit my Cilium network policy coverage and show me the exposure gaps"
- "Are there any workloads in the cluster not covered by a Cilium policy?"
- "Which namespaces have Cilium workloads lacking a default-deny or L7 rule?"
- "Show me the Cilium policy coverage gaps ranked by risk per namespace"

---

A security engineer wants to find Cilium-policy-selected workloads with no
ingress/egress restriction or no L7 rule so they can prioritize fixes. The tool
compares each workload's labels against the endpoint selectors of the
`cilium.io/v2` policies and flags coverage gaps (no policy, no default-deny,
partial restriction, L3/L4-only), ranked by risk and grouped per namespace. When
Cilium is absent the view degrades to "vanilla" and a NOT_INSTALLED marker is
returned. The flow crosses the hexagonal layers: MCP Tool →
CiliumPolicyAuditUseCase → CiliumPort (driven port) → CiliumAdapter (secondary)
→ VanillaAdapter → Kubernetes API.

### Flow 1 — Happy Path: Audit Coverage

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as cilium_policy_audit (MCP Tool)
    participant UseCase as CiliumPolicyAuditUseCase
    participant Port as CiliumPort (ABC)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    User->>Tool: "Audit Cilium policy coverage"
    Tool->>UseCase: execute(CiliumPolicyAuditCommand())
    UseCase->>Port: audit_policies()
    Port->>Adapter: policies + workload selectors

    Adapter->>API: list cilium.io policies
    API-->>Adapter: policies

    Adapter->>API: list pods (labels)
    API-->>Adapter: workloads

    Note over Adapter: match workloads to endpoint selectors<br/>flag no_policy / no_default_deny / partial / l7_gap

    Adapter-->>Port: CiliumPolicyAudit(gaps)
    Port-->>UseCase: CiliumPolicyAuditResult
    UseCase-->>Tool: CiliumPolicyAuditResponse(findings, risk)
    Tool-->>User: { status, uncovered_count, findings, summary, ... }
```

### Flow 2 — Errors: Not Installed (Vanilla fallback), RBAC, Unreachable

```mermaid
sequenceDiagram
    participant Tool as cilium_policy_audit (MCP Tool)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    alt No cilium.io CRD group (404)
        Adapter->>API: list cilium.io CRDs
        API-->>Adapter: status 404
        Adapter-->>Tool: CiliumPolicyAuditResult(installed=False, view="vanilla")
        Tool-->>Tool: { installed=False, status="not_installed", view="vanilla", note=... }
    else RBAC forbidden
        Adapter->>API: list policies / pods
        API-->>Adapter: status 403
        Adapter-->>Tool: InsufficientPermissionsError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    else Cluster unreachable / timeout
        Adapter->>API: list policies / pods
        API-->>Adapter: connection refused / timeout
        Adapter-->>Tool: ClusterUnreachableError / AdapterTimeoutError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    end
```

### Flow 3 — Checker Node: Honest Audit

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Result as CiliumPolicyAuditResult
    participant Store as Memory / Response

    Checker->>Result: cross-check selector coverage vs findings

    alt Gap invented
        Checker-->>Checker: FAIL (gap must be observed)
        Checker-->>Store: findings from actual selector coverage
    else Priority rank fabricated
        Checker-->>Checker: FLAG (risk from observed coverage only)
        Checker-->>Store: risk = critical/medium from observed coverage
    else Default-deny omitted
        Checker-->>Checker: FAIL (default-deny must be stated)
        Checker-->>Store: coverage includes no_default_deny
    else Observed and valid
        Checker-->>Store: PASS (store audit)
    end
```

### Flow 4 — DuckDB Memory: Query-Before, Store-After, Offline Fallback

```mermaid
sequenceDiagram
    participant Tool as cilium_policy_audit (MCP Tool)
    participant Cache as Cache / DuckDB
    participant Adapter as CiliumAdapter (secondary)

    Note over Tool: VSS search before (semantic cache hit)
    Tool->>Cache: search_similar("cilium policy coverage gaps")
    Cache-->>Tool: similar prior audit (optional shortcut)

    Tool->>Adapter: audit_policies()
    Adapter-->>Tool: CiliumPolicyAuditResult

    Note over Tool: store after (observed, not invented)
    Tool->>Cache: store audit + note

    Note over Tool: offline fallback (no cluster)
    Cache-->>Tool: degraded answer with explicit note
```

## Key Points

- `CiliumPolicyAuditUseCase` depends only on `CiliumPort`.
- Compares workload labels against Cilium policy endpoint selectors; a workload
  is matched when the policy's `matchLabels` is a subset of its labels.
- Coverage states: `no_policy`, `no_default_deny`, `partial`, `l7_gap`, and
  `covered` (excluded from findings).
- Risk (critical / medium) is derived only from observed coverage; findings are
  deduplicated per workload.
- When Cilium is absent the result reports `view="vanilla"` and
  NOT_INSTALLED — never a fabricated Cilium audit.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_audit_flags_workload_without_policy` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_audit_fully_covered` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_audit_not_installed_returns_vanilla_view` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_no_policy_gap` | `tests/unit/domain/services/test_policy_audit.py` | ✅ |
| `test_fully_covered_no_gaps` | `tests/unit/domain/services/test_policy_audit.py` | ✅ |
| `test_l7_gap` | `tests/unit/domain/services/test_policy_audit.py` | ✅ |
| `test_overlapping_selectors_deduplicated` | `tests/unit/domain/services/test_policy_audit.py` | ✅ |
| `test_execute_returns_findings` | `tests/unit/application/use_case/cilium/test_uc_cilium_policy_audit_use_case.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/cilium.py` — `CiliumWorkload`, `CiliumAuditFinding`, `CiliumPolicyAuditResult`
- `src/hexawyn/domain/services/cilium/policy_audit.py` — pure coverage matching + risk
- `src/hexawyn/application/ports/driven/cilium_port.py` — `CiliumPort.audit_policies()`
- `src/hexawyn/application/use_case/cilium/cilium_policy_audit/` — Command, Response, UseCase
- `src/hexawyn/adapters/secondary/gitops/cilium_adapter.py` — `CiliumAdapter.audit_policies()`
- `src/hexawyn/mcp/tools/cilium_policy_audit.py` — MCP tool
