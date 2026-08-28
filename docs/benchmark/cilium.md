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
| `cilium/301-cilium-netpol-get` | full spec + endpoint selector + ingress/egress/L7 rules returned | AC2 |
| `cilium/302-cilium-netpol-get-not-found` | upstream `ResourceNotFoundError` (not a raw K8s 404) | AC4 |
| `cilium/303-cilium-netpol-get-not-installed` | `installed=false`, `status="not_installed"` | AC3 |
| `cilium/304-cilium-netpol-get-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/401-cilium-policy-audit-gap` | uncovered workload flagged, `risk` observed | AC2, AC3 |
| `cilium/402-cilium-policy-audit-covered` | `status="covered"`, no findings | AC2 |
| `cilium/403-cilium-policy-audit-l7-gap` | L3/L4 restricted but no L7 → flagged | AC3 |
| `cilium/404-cilium-policy-audit-not-installed` | `installed=false`, `view="vanilla"`, NOT_INSTALLED | AC4 |
| `cilium/405-cilium-policy-audit-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/501-cilium-identities-list` | identities with numeric id, labels, endpoint count | AC2 |
| `cilium/502-cilium-identities-empty` | `status="empty"`, empty list, no crash | AC2 |
| `cilium/503-cilium-identities-not-installed` | `installed=false`, `status="not_installed"` | AC3 |
| `cilium/504-cilium-identities-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/601-cilium-segmentation-reachable` | allowed-but-unrestricted path flagged, source/destination tagged | AC2 |
| `cilium/602-cilium-segmentation-isolated` | policy blocks path → not flagged | AC2 |
| `cilium/603-cilium-segmentation-not-installed` | `installed=false`, `view="vanilla"`, NOT_INSTALLED | AC4 |
| `cilium/604-cilium-segmentation-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/701-cilium-flows-query` | flows filtered by ns/pod/verdict with identities, verdict, protocol, ports | AC2 |
| `cilium/702-cilium-flows-window-limit` | window filtering (last 15m) and limit respected | AC3 |
| `cilium/703-cilium-flows-not-installed` | `installed=false`, NOT_INSTALLED when Hubble absent, no fabricated flows | AC4 |
| `cilium/704-cilium-flows-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/801-cilium-denials-detect` | dropped flows grouped by policy/source/dest with counts and reason | AC2 |
| `cilium/802-cilium-denials-none` | `status="none"`, zero counts, no crash | AC2 |
| `cilium/803-cilium-denials-not-installed` | `installed=false`, NOT_INSTALLED when Hubble absent, no fabricated denials | AC4 |
| `cilium/804-cilium-denials-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/901-cilium-encryption-status` | mode (none/wireguard/ipsec) + node coverage from Cilium config | AC2 |
| `cilium/902-cilium-encryption-disabled` | `mode="none"`, `status="disabled"`, coverage zero | AC2 |
| `cilium/903-cilium-encryption-not-installed` | `installed=false`, NOT_INSTALLED, no fabricated mode | AC3 |
| `cilium/904-cilium-encryption-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/1001-cilium-bandwidth-throttled` | throttled pod flagged with quota | AC2 |
| `cilium/1002-cilium-bandwidth-near-limit` | near-limit pod flagged, impact-ranked | AC2 |
| `cilium/1003-cilium-bandwidth-not-available` | `status="not_available"` when no bandwidth annotations | AC3 |
| `cilium/1004-cilium-bandwidth-not-installed` | `installed=false`, NOT_INSTALLED, no fabricated data | AC3 |
| `cilium/1005-cilium-bandwidth-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |
| `cilium/1101-cilium-service-graph` | nodes + edges from observed Hubble flows (call_count, error_rate) | AC2 |
| `cilium/1102-cilium-service-graph-empty` | empty graph when Hubble unavailable/no traffic | AC4 |
| `cilium/1103-cilium-service-graph-rbac-denied` | upstream `InsufficientPermissionsError` | AC6 |

## Expected coverage

- **Classified categories:** reading mode mapping (tunnel / native-routing / cluster / ipvlan / UNKNOWN); health/connectivity aggregation (healthy / degraded / unknown / not_installed); network-policy rule summarisation (L3/L4/L7, endpoint selector, kind breakdown); policy detail retrieval (full spec, L7 protocols, not-installed vs not-found); policy coverage audit (no_policy / no_default_deny / partial / l7_gap, risk ranking); identity listing (numeric id, label set, endpoint count); east-west segmentation audit (allowed-but-unrestricted reachability matrix, Cilium vs vanilla view); Hubble flow querying (verdict, identities, protocol/ports, window/limit, NOT_INSTALLED when Hubble absent); Cilium denial detection (dropped-flow grouping by policy/source/destination/reason, NOT_INSTALLED when Hubble absent); wire-encryption status (mode none/wireguard/ipsec, node coverage, NOT_INSTALLED when Cilium absent); bandwidth-manager audit (per-pod quota, throttled/near-limit classification, NOT_AVAILABLE/NOT_INSTALLED); service graph from Cilium flows (nodes + edges with call count and error rate, empty graceful fallback).
- **Guardrails:** `installed=true` and `status="healthy"` are never invented without a cilium DaemonSet or `cilium.io` CRD; a version is never fabricated; degraded state is never omitted; Cilium is never confused with Calico or Istio; policies, rule counts, detail, audit findings, identities, reachability paths, flow entries, denial counts, the encryption mode, bandwidth states and graph edges come only from observed sources; a missing policy is reported via `ResourceNotFoundError`, absent Cilium yields a `view="vanilla"` NOT_INSTALLED marker, and absent Hubble yields NOT_INSTALLED flow/denial results and an empty service graph — never a fabricated audit, identity, reachability path, flow, denial, encryption mode, bandwidth state or graph edge.
