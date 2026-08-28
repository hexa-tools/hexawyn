# Use Case 190 — Cilium Encryption Status

## Sample Questions

- "Is Cilium wire-level encryption (WireGuard or IPsec) enabled on my cluster?"
- "What encryption mode is Cilium using, and how many nodes are covered?"
- "Are my east-west workloads encrypted on the dataplane right now?"
- "Which Cilium encryption mode is configured, wireguard or ipsec?"
- "Show me the Cilium encryption status and node coverage"

---

A security engineer wants to verify that east-west traffic is encrypted on the
dataplane. The tool reads the observed Cilium configuration (`cilium-config`)
to report the encryption mode (none / wireguard / ipsec) and the node coverage
(encrypted nodes / total). When Cilium is absent it returns NOT_INSTALLED —
never a fabricated mode. The flow crosses the hexagonal layers: MCP Tool →
CiliumEncryptionStatusUseCase → CiliumPort (driven port) → CiliumAdapter
(secondary) → VanillaAdapter → Kubernetes API.

### Flow 1 — Happy Path: Read Encryption State

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as cilium_encryption_status (MCP Tool)
    participant UseCase as CiliumEncryptionStatusUseCase
    participant Port as CiliumPort (ABC)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    User->>Tool: "Is Cilium encryption enabled?"
    Tool->>UseCase: execute(CiliumEncryptionStatusCommand())
    UseCase->>Port: encryption_status()
    Port->>Adapter: read config + daemonset

    Adapter->>API: list daemon-sets (find "cilium")
    API-->>Adapter: DaemonSet (status)

    Adapter->>API: read configmap "cilium-config"
    API-->>Adapter: data { "encryption-type": "wireguard" }

    Note over Adapter: deduce mode (none/wireguard/ipsec)<br/>node coverage from daemonset status

    Adapter-->>Port: CiliumEncryptionStatusResult(mode, coverage)
    Port-->>UseCase: CiliumEncryptionStatusResult
    UseCase-->>Tool: CiliumEncryptionStatusResponse(mode, coverage)
    Tool-->>User: { installed, mode, encrypted_nodes, coverage, ... }
```

### Flow 2 — Errors: Not Installed, RBAC, Unreachable

```mermaid
sequenceDiagram
    participant Tool as cilium_encryption_status (MCP Tool)
    participant Adapter as CiliumAdapter (secondary)
    participant API as Kubernetes API

    alt No cilium.io CRD group (404)
        Adapter->>API: list cilium.io CRDs
        API-->>Adapter: status 404
        Adapter-->>Tool: CiliumEncryptionStatusResult(installed=False)
        Tool-->>Tool: { installed=False, status="not_installed", note=... }
    else RBAC forbidden
        Adapter->>API: list daemon-sets
        API-->>Adapter: status 403
        Adapter-->>Tool: InsufficientPermissionsError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    else Cluster unreachable / timeout
        Adapter->>API: list daemon-sets
        API-->>Adapter: connection refused / timeout
        Adapter-->>Tool: ClusterUnreachableError / AdapterTimeoutError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    end
```

### Flow 3 — Checker Node: Honest Encryption

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Result as CiliumEncryptionStatusResult
    participant Store as Memory / Response

    Checker->>Result: cross-check config vs mode

    alt Encryption invented
        Checker-->>Checker: FAIL (mode must be observed from config)
        Checker-->>Store: mode from cilium-config
    else Mode fabricated
        Checker-->>Checker: FLAG (observed only)
        Checker-->>Store: mode = none/wireguard/ipsec/UNKNOWN
    else Coverage omitted
        Checker-->>Checker: FAIL (coverage required)
        Checker-->>Store: encrypted_nodes/total_nodes from daemonset status
    else Observed and valid
        Checker-->>Store: PASS (store encryption status)
    end
```

### Flow 4 — DuckDB Memory: Query-Before, Store-After, Offline Fallback

```mermaid
sequenceDiagram
    participant Tool as cilium_encryption_status (MCP Tool)
    participant Cache as Cache / DuckDB
    participant Adapter as CiliumAdapter (secondary)

    Note over Tool: VSS search before (semantic cache hit)
    Tool->>Cache: search_similar("is cilium encryption enabled")
    Cache-->>Tool: similar prior status (optional shortcut)

    Tool->>Adapter: encryption_status()
    Adapter-->>Tool: CiliumEncryptionStatusResult

    Note over Tool: store after (observed, not invented)
    Tool->>Cache: store status + note

    Note over Tool: offline fallback (no cluster)
    Cache-->>Tool: degraded answer with explicit note
```

## Key Points

- `CiliumEncryptionStatusUseCase` depends only on `CiliumPort`.
- `mode` comes from the observed `cilium-config` keys (`encryption-type`,
  `encryption-enabled`) — never inferred; an unreadable config yields `UNKNOWN`.
- `coverage` is `encrypted_nodes/total_nodes` from the Cilium DaemonSet status;
  a disabled mode reports `0/...`.
- NOT_INSTALLED is returned when the `cilium.io` CRD group is absent.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_wireguard_enabled` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_ipsec_enabled` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_none_when_disabled` | `tests/unit/adapters/secondary/gitops/test_cilium_adapter.py` | ✅ |
| `test_wireguard_enabled_with_coverage` | `tests/unit/domain/services/test_encryption_status_builder.py` | ✅ |
| `test_deduce_wireguard` | `tests/unit/domain/services/test_encryption_status_builder.py` | ✅ |
| `test_execute_returns_status` | `tests/unit/application/use_case/cilium/test_uc_cilium_encryption_status_use_case.py` | ✅ |
| `test_cilium_encryption_status_returns_dict` | `tests/unit/mcp/tools/test_tool_cilium_encryption_status.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/cilium.py` — `CiliumEncryptionStatusResult`
- `src/hexawyn/domain/services/cilium/encryption_status_builder.py` — pure mode/coverage building
- `src/hexawyn/application/ports/driven/cilium_port.py` — `CiliumPort.encryption_status()`
- `src/hexawyn/application/use_case/cilium/cilium_encryption_status/` — Command, Response, UseCase
- `src/hexawyn/adapters/secondary/gitops/cilium_adapter.py` — `CiliumAdapter.encryption_status()`
- `src/hexawyn/mcp/tools/cilium_encryption_status.py` — MCP tool
