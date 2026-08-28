# Use Case 183 — List Cilium Network Policies

## Sample Questions

- "List all the Cilium network policies defined in my cluster"
- "What CiliumNetworkPolicy rules exist in the payments namespace?"
- "Are there any Cilium cluster-wide network policies applying to the whole cluster?"
- "Show me all Cilium L7 network policies with their ingress and egress rules"
- "Which Cilium policies apply to the database endpoints via their selectors?"

---

A security/platform engineer asks to see every Cilium L3/L4/L7 rule before
auditing connectivity. The tool enumerates both `CiliumNetworkPolicy` and
`CiliumClusterwideNetworkPolicy` custom resources, extracting the endpoint
selector and a per-policy ingress/egress + L7 rule summary — never the vanilla
`NetworkPolicy`. When the `cilium.io` CRD group is absent it returns
NOT_INSTALLED. The flow crosses the hexagonal layers: MCP Tool →
ListCiliumNetworkPoliciesUseCase → CiliumPort (driven port) → CiliumAdapter
(secondary) → VanillaAdapter → Kubernetes API.

### Flow 1 — Happy Path: List Policies Across Kinds

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as list_cilium_network_policies (MCP Tool)
    participant UseCase as ListCiliumNetworkPoliciesUseCase
    participant Port as CiliumPort (ABC)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    User->>Tool: "List the Cilium network policies"
    Tool->>UseCase: execute(ListCiliumNetworkPoliciesCommand())
    UseCase->>Port: list_network_policies()
    Port->>Adapter: list cilium.io custom objects

    Adapter->>API: list ciliumnetworkpolicies (v2)
    API-->>Adapter: namespaced policies

    Adapter->>API: list ciliumclusterwidenetworkpolicies (v2)
    API-->>Adapter: cluster-wide policies

    Note over Adapter: endpoint selector + ingress/egress + L7 summary

    Adapter-->>Port: CiliumNetworkPoliciesResult(policies)
    Port-->>UseCase: CiliumNetworkPoliciesResult
    UseCase-->>Tool: ListCiliumNetworkPoliciesResponse(policies=[...])
    Tool-->>User: { installed, total_policies, namespaced_count, clusterwide_count, ... }
```

### Flow 2 — Errors: Not Installed, Unreachable, RBAC

```mermaid
sequenceDiagram
    participant Tool as list_cilium_network_policies (MCP Tool)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    alt No cilium.io CRD group (404)
        Adapter->>API: list ciliumnetworkpolicies
        API-->>Adapter: status 404
        Adapter-->>Tool: CiliumNetworkPoliciesResult(installed=False)
        Tool-->>Tool: { installed=False, status="not_installed", note=... }
    else RBAC forbidden
        Adapter->>API: list ciliumnetworkpolicies
        API-->>Adapter: status 403
        Adapter-->>Tool: InsufficientPermissionsError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    else Cluster unreachable
        Adapter->>API: list ciliumnetworkpolicies
        API-->>Adapter: connection refused
        Adapter-->>Tool: ClusterUnreachableError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    end
```

### Flow 3 — Checker Node: Honest Inventory

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Result as CiliumNetworkPoliciesResult
    participant Store as Memory / Response

    Checker->>Result: cross-check against raw list

    alt Policy invented
        Checker-->>Checker: FAIL (policy must come from CRD list)
        Checker-->>Store: status="not_installed" or empty
    else Rule counts fabricated
        Checker-->>Checker: FLAG (observed counts only)
        Checker-->>Store: ingress_rule_count/egress_rule_count from observed spec
    else Kinds mixed up
        Checker-->>Checker: FAIL (CiliumNetworkPolicy vs Clusterwide distinct)
        Checker-->>Store: namespaced_count / clusterwide_count separated
    else Observed and valid
        Checker-->>Store: PASS (store result)
    end
```

### Flow 4 — DuckDB Memory: Query-Before, Store-After, Offline Fallback

```mermaid
sequenceDiagram
    participant Tool as list_cilium_network_policies (MCP Tool)
    participant Cache as Cache / DuckDB
    participant Adapter as CiliumAdapter (secondary)

    Note over Tool: VSS search before (semantic cache hit)
    Tool->>Cache: search_similar("list cilium network policies")
    Cache-->>Tool: similar prior answer (optional shortcut)

    Tool->>Adapter: list_network_policies()
    Adapter-->>Tool: CiliumNetworkPoliciesResult

    Note over Tool: store after (observed, not invented)
    Tool->>Cache: store result + note

    Note over Tool: offline fallback (no cluster)
    Cache-->>Tool: degraded answer with explicit note
```

## Key Points

- `ListCiliumNetworkPoliciesUseCase` depends only on `CiliumPort`.
- Reads the `cilium.io/v2` `ciliumnetworkpolicies` and
  `ciliumclusterwidenetworkpolicies` CRDs — never the vanilla `NetworkPolicy`.
- Each policy exposes its `endpointSelector` (rendered, or reported as-is when
  malformed) plus ingress/egress/L7 rule counts and raw L7 protocol names.
- NOT_INSTALLED is returned only when the CRD group is absent (both kinds 404).
- Kind breakdown (`namespaced_count` / `clusterwide_count`) is kept distinct.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_lists_both_kinds_with_summary` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_not_installed_when_group_absent` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_rbac_403_raises_insufficient_permissions` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_extracts_selector_and_rules` | `tests/unit/domain/services/test_cilium_network_policy_summary.py` | ✅ |
| `test_counts_l7_rules_and_protocols` | `tests/unit/domain/services/test_cilium_network_policy_summary.py` | ✅ |
| `test_execute_returns_policy_list` | `tests/unit/application/use_case/cilium/test_uc_list_cilium_network_policies_use_case.py` | ✅ |
| `test_list_cilium_network_policies_returns_dict` | `tests/unit/mcp/tools/test_tool_list_cilium_network_policies.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/cilium.py` — `CiliumNetworkPolicyInfo`, `CiliumNetworkPoliciesResult`
- `src/hexawyn/domain/services/cilium/network_policy_summary.py` — L3/L4/L7 pure rule summary
- `src/hexawyn/application/ports/driven/cilium_port.py` — `CiliumPort.list_network_policies()`
- `src/hexawyn/application/use_case/cilium/list_cilium_network_policies/` — Command, Response, UseCase
- `src/hexawyn/adapters/secondary/gitops/cilium_adapter.py` — `CiliumAdapter.list_network_policies()`
- `src/hexawyn/mcp/tools/list_cilium_network_policies.py` — MCP tool
