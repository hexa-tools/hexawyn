# Use Case 191 — Cilium Bandwidth Audit

## Sample Questions

- "Which pods are hitting their Cilium bandwidth limits and being throttled?"
- "Audit my Cilium bandwidth manager quotas and show me near-limit workloads"
- "Are any pods throttled by the Cilium bandwidth manager right now?"
- "Show me per-pod bandwidth quotas and anomalies across my cluster"
- "Which namespaces have workloads close to or over their egress bandwidth limit?"

---

A platform/FinOps engineer wants to audit Cilium bandwidth-manager quotas
(per-pod/auth) and usage to detect throttled workloads or unplanned bandwidth
spikes. The tool reads per-pod bandwidth annotations and flags throttled or
near-limit workloads, ranked by impact. When Cilium is absent it returns
NOT_INSTALLED; when the bandwidth manager is enabled but no bandwidth
annotations are found it reports NOT_AVAILABLE — never fabricated data. The
flow crosses the hexagonal layers: MCP Tool → CiliumBandwidthAuditUseCase →
CiliumPort (driven port) → CiliumAdapter (secondary) → VanillaAdapter →
Kubernetes API.

### Flow 1 — Happy Path: Audit Bandwidth Quotas

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as cilium_bandwidth_audit (MCP Tool)
    participant UseCase as CiliumBandwidthAuditUseCase
    participant Port as CiliumPort (ABC)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    User->>Tool: "Which pods are hitting bandwidth limits?"
    Tool->>UseCase: execute(CiliumBandwidthAuditCommand())
    UseCase->>Port: bandwidth_audit()
    Port->>Adapter: read annotations + flow stats

    Adapter->>API: list daemon-sets (find "cilium")
    API-->>Adapter: DaemonSet (found)
    Adapter->>API: list pods (annotations)
    API-->>Adapter: pods

    Note over Adapter: per-pod quota + usage<br/>state = throttled / near_limit / ok / UNKNOWN

    Adapter-->>Port: CiliumBandwidthAudit(entries)
    Port-->>UseCase: CiliumBandwidthAuditResult
    UseCase-->>Tool: CiliumBandwidthAuditResponse(entries)
    Tool-->>User: { installed, status, total_pods, entries, ... }
```

### Flow 2 — Errors: Not Installed, Not Available, RBAC, Unreachable

```mermaid
sequenceDiagram
    participant Tool as cilium_bandwidth_audit (MCP Tool)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    alt No cilium.io CRD group (404)
        Adapter->>API: list cilium.io CRDs
        API-->>Adapter: status 404
        Adapter-->>Tool: CiliumBandwidthAudit(installed=False)
        Tool-->>Tool: { installed=False, status="not_installed", note=... }
    else No bandwidth annotations
        Adapter-->>Tool: CiliumBandwidthAudit(status="not_available")
        Tool-->>Tool: { installed=True, status="not_available", note=... }
    else RBAC forbidden
        Adapter->>API: list daemon-sets / pods
        API-->>Adapter: status 403
        Adapter-->>Tool: InsufficientPermissionsError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    else Cluster unreachable / timeout
        Adapter->>API: list daemon-sets / pods
        API-->>Adapter: connection refused / timeout
        Adapter-->>Tool: ClusterUnreachableError / AdapterTimeoutError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    end
```

### Flow 3 — Checker Node: Honest Bandwidth

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Result as CiliumBandwidthAuditResult
    participant Store as Memory / Response

    Checker->>Result: cross-check quota vs annotations

    alt Throttle invented
        Checker-->>Checker: FAIL (state must come from observed data)
        Checker-->>Store: state from annotations/usage
    else Ratio fabricated
        Checker-->>Checker: FLAG (usage_ratio observed only)
        Checker-->>Store: usage_ratio from observed stat
    else Limit omitted
        Checker-->>Checker: FAIL (limit required)
        Checker-->>Store: ingress_limit / egress_limit from annotation
    else Observed and valid
        Checker-->>Store: PASS (store bandwidth audit)
    end
```

### Flow 4 — DuckDB Memory: Query-Before, Store-After, Offline Fallback

```mermaid
sequenceDiagram
    participant Tool as cilium_bandwidth_audit (MCP Tool)
    participant Cache as Cache / DuckDB
    participant Adapter as CiliumAdapter (secondary)

    Note over Tool: VSS search before (semantic cache hit)
    Tool->>Cache: search_similar("pods hitting bandwidth limits")
    Cache-->>Tool: similar prior audit (optional shortcut)

    Tool->>Adapter: bandwidth_audit()
    Adapter-->>Tool: CiliumBandwidthAuditResult

    Note over Tool: store after (observed, not invented)
    Tool->>Cache: store audit + note

    Note over Tool: offline fallback (no cluster)
    Cache-->>Tool: degraded answer with explicit note
```

## Key Points

- `CiliumBandwidthAuditUseCase` depends only on `CiliumPort`.
- Reads per-pod bandwidth annotations and flags throttled (`throttled`) or
  near-limit (`near_limit`) workloads; a missing usage stat yields `UNKNOWN`.
- Anomalies are reported first (impact-ranked), not per-pod in arbitrary order.
- NOT_INSTALLED when Cilium is absent; NOT_AVAILABLE when the bandwidth manager
  is enabled but no bandwidth annotations are found.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_flags_throttled_pod` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_flags_near_limit` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_no_annotations_returns_not_available` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_throttled_wins` | `tests/unit/domain/services/test_bandwidth_builder.py` | ✅ |
| `test_near_limit` | `tests/unit/domain/services/test_bandwidth_builder.py` | ✅ |
| `test_flags_throttled_first` | `tests/unit/domain/services/test_bandwidth_builder.py` | ✅ |
| `test_execute_returns_entries` | `tests/unit/application/use_case/cilium/test_uc_cilium_bandwidth_audit_use_case.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/cilium.py` — `CiliumBandwidthEntry`, `CiliumBandwidthAuditResult`
- `src/hexawyn/domain/services/cilium/bandwidth_builder.py` — pure bandwidth classification
- `src/hexawyn/application/ports/driven/cilium_port.py` — `CiliumPort.bandwidth_audit()`
- `src/hexawyn/application/use_case/cilium/cilium_bandwidth_audit/` — Command, Response, UseCase
- `src/hexawyn/adapters/secondary/gitops/cilium_adapter.py` — `CiliumAdapter.bandwidth_audit()`
- `src/hexawyn/mcp/tools/cilium_bandwidth_audit.py` — MCP tool
