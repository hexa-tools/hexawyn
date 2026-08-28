# cilium — pending

**0** scenarios · **pending** — no benchmark run yet (awaiting hexa-benchmark scenarios for `cilium_detect`).

> Legend /100: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

## Scenarios to benchmark

The `cilium_detect` tool must satisfy the scenarios below once the hexa-benchmark cases land. Each maps to an acceptance criterion of the feature ticket.

| Scenario | Expected | AC |
|---|---|---|
| `cilium/001-cilium-installed` | `installed=true`, observed version from image tag, agent pod health | AC2, AC3 |
| `cilium/002-cilium-not-installed` | `installed=false`, `status="not_installed"`, no invented values | AC4 |
| `cilium/003-cilium-degraded` | `status="degraded"`, `degraded_summary="{ready}/{total} agents ready"` | AC3 |
| `cilium/004-cilium-routing-mode` | `mode` = tunnel / native-routing read from `cilium-config`; unknown → `UNKNOWN` | AC2 |
| `cilium/005-cilium-rbac-denied` | upstream `InsufficientPermissionsError` (not a fabricated answer) | AC6 |
| `cilium/006-cilium-cluster-unreachable` | upstream `ClusterUnreachableError` (not a fabricated answer) | AC6 |
| `cilium/101-cilium-status-healthy` | `status="healthy"`, `ready=total`, `connectivity="ok"` | AC2, AC3 |
| `cilium/102-cilium-status-degraded` | `status="degraded"`, `degraded_summary="{ready}/{total} agents ready"`, per-node status | AC3 |
| `cilium/103-cilium-status-not-installed` | `installed=false`, `status="not_installed"`, no invented values | AC4 |
| `cilium/104-cilium-status-unreachable` | upstream `ClusterUnreachableError` | AC6 |
| `cilium/105-cilium-status-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/201-cilium-netpol-list` | both kinds listed, endpoint selector + ingress/egress/L7 summary | AC2 |
| `cilium/202-cilium-netpol-empty` | `status="empty"`, empty list, no crash | AC2 |
| `cilium/203-cilium-netpol-not-installed` | `installed=false`, `status="not_installed"`, no invented policies | AC3 |
| `cilium/204-cilium-netpol-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/205-cilium-netpol-kinds-separated` | `CiliumNetworkPolicy` vs `CiliumClusterwideNetworkPolicy` kept distinct | AC2 |

## Expected coverage

- **Classified categories:** reading mode mapping (tunnel / native-routing / cluster / ipvlan / UNKNOWN); health/connectivity aggregation (healthy / degraded / unknown / not_installed); network-policy rule summarisation (L3/L4/L7, endpoint selector, kind breakdown).
- **Guardrails:** `installed=true` and `status="healthy"` are never invented without a cilium DaemonSet or `cilium.io` CRD; a version is never fabricated; degraded state is never omitted; Cilium is never confused with Calico or Istio; policies and rule counts come only from observed CRDs.
