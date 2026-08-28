# Use Case 188 — Get Cilium Flows

## Sample Questions

- "Show me recent Hubble network flows for the payments namespace"
- "Which flows were dropped by Cilium in the last 15 minutes?"
- "What traffic is flowing between web and db pods, with verdicts and ports?"
- "Are there any forwarded flows hitting payment-api from outside the namespace?"
- "List the last 50 Cilium flows for pod web-0 with their source and destination identities"

---

A platform/observability engineer wants to query Cilium flow logs (Hubble) to
see the actual network flows between workloads and reason about traffic. The
tool queries a Hubble Relay HTTP endpoint, filtering by namespace/pod/direction
and window/limit, and returns each flow's source/destination identity, verdict
(forwarded/dropped), drop reason, protocol and ports. When Hubble Relay is not
configured it returns NOT_INSTALLED — never fabricated flows. The flow crosses
the hexagonal layers: MCP Tool → GetCiliumFlowsUseCase → CiliumHubblePort
(driven port) → CiliumHubbleAdapter (secondary) → Hubble Relay HTTP client.

### Flow 1 — Happy Path: Query Hubble Flows

```mermaid
sequenceDiagram
    participant User as User
    participant Tool as get_cilium_flows (MCP Tool)
    participant UseCase as GetCiliumFlowsUseCase
    participant Port as CiliumHubblePort (ABC)
    participant Adapter as CiliumHubbleAdapter (secondary)
    participant Hubble as Hubble Relay
    participant Client as Hubble HTTP client

    User->>Tool: "Show recent flows for payments"
    Tool->>UseCase: execute(GetCiliumFlowsCommand(namespace, window, limit))
    UseCase->>Port: get_flows(CiliumFlowQuery)
    Port->>Adapter: query flow logs

    Adapter->>Client: fetch_hubble_flows(namespace, window, limit)
    Client->>Hubble: GET /flows (HUBBLE_URL)
    Hubble-->>Client: flow JSON

    Note over Adapter: map to FlowEntry (verdict, identities, protocol, ports)
    Adapter-->>Port: CiliumFlowsResult(flows)
    Port-->>UseCase: CiliumFlowsResult
    UseCase-->>Tool: GetCiliumFlowsResponse(flows)
    Tool-->>User: { installed, total_flows, flows, note, ... }
```

### Flow 2 — Errors: Not Installed, Unreachable, Timeout

```mermaid
sequenceDiagram
    participant Tool as get_cilium_flows (MCP Tool)
    participant Adapter as CiliumHubbleAdapter (secondary)
    participant Client as Hubble HTTP client

    alt No Hubble Relay configured
        Adapter->>Client: hubble_available()
        Client-->>Adapter: False
        Adapter-->>Tool: CiliumFlowsResult(installed=False)
        Tool-->>Tool: { installed=False, status="not_installed", note=... }
    else Timeout
        Adapter->>Client: fetch_hubble_flows()
        Client-->>Adapter: timeout
        Adapter-->>Tool: AdapterTimeoutError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    else Unreachable
        Adapter->>Client: fetch_hubble_flows()
        Client-->>Adapter: connection refused
        Adapter-->>Tool: ClusterUnreachableError
        Tool-->>Tool: { installed=False, status="unknown", error=... }
    end
```

### Flow 3 — Checker Node: Honest Flows

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Result as CiliumFlowsResult
    participant Store as Memory / Response

    Checker->>Result: cross-check against raw Hubble objects

    alt Flow invented
        Checker-->>Checker: FAIL (flow must come from Hubble)
        Checker-->>Store: flows from observed flow log
    else Identity fabricated
        Checker-->>Checker: FLAG (identities observed only)
        Checker-->>Store: source_identity / destination_identity from flow
    else Verdict omitted
        Checker-->>Checker: FAIL (verdict required)
        Checker-->>Store: verdict = FORWARDED/DROPPED/UNKNOWN
    else Observed and valid
        Checker-->>Store: PASS (store flows)
    end
```

### Flow 4 — DuckDB Memory: Query-Before, Store-After, Offline Fallback

```mermaid
sequenceDiagram
    participant Tool as get_cilium_flows (MCP Tool)
    participant Cache as Cache / DuckDB
    participant Adapter as CiliumHubbleAdapter (secondary)

    Note over Tool: VSS search before (semantic cache hit)
    Tool->>Cache: search_similar("recent flows for payments")
    Cache-->>Tool: similar prior flows (optional shortcut)

    Tool->>Adapter: get_flows(query)
    Adapter-->>Tool: CiliumFlowsResult

    Note over Tool: store after (observed, not invented)
    Tool->>Cache: store flows + note

    Note over Tool: offline fallback (no Hubble)
    Cache-->>Tool: NOT_INSTALLED answer with explicit note
```

## Key Points

- `GetCiliumFlowsUseCase` depends only on `CiliumHubblePort`.
- Flows are read from a Hubble Relay HTTP endpoint (`HUBBLE_URL`), filtered by
  namespace/pod/direction/verdict and bounded by window and limit.
- Each flow carries timestamp, source/destination (and namespace), identities,
  verdict (forwarded/dropped, `UNKNOWN` when absent), drop reason, protocol,
  destination port and optional L7 protocol.
- NOT_INSTALLED is returned when Hubble Relay is not configured — never a
  fabricated flow; transport errors are translated to `HexawynError`.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_returns_flows` | `tests/unit/adapters/secondary/cilium/test_cilium_hubble_adapter.py` | ✅ |
| `test_not_installed_when_no_hubble_url` | `tests/unit/adapters/secondary/cilium/test_cilium_hubble_adapter.py` | ✅ |
| `test_fetch_returns_flows` | `tests/unit/adapters/secondary/cilium/test_hubble_client.py` | ✅ |
| `test_maps_flow_fields` | `tests/unit/domain/services/test_flow_builder.py` | ✅ |
| `test_missing_verdict_reported_unknown` | `tests/unit/domain/services/test_flow_builder.py` | ✅ |
| `test_filters_by_namespace` | `tests/unit/domain/services/test_flow_builder.py` | ✅ |
| `test_limit_clamps_volume` | `tests/unit/domain/services/test_flow_builder.py` | ✅ |
| `test_execute_returns_flows` | `tests/unit/application/use_case/cilium/test_uc_get_cilium_flows_use_case.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/cilium.py` — `CiliumFlowQuery`, `CiliumFlowEntry`, `CiliumFlowsResult`
- `src/hexawyn/domain/services/cilium/flow_builder.py` — pure flow mapping/filtering
- `src/hexawyn/adapters/secondary/cilium/hubble_client.py` — Hubble HTTP client (`HUBBLE_URL`)
- `src/hexawyn/adapters/secondary/cilium/cilium_hubble_adapter.py` — `CiliumHubbleAdapter`
- `src/hexawyn/application/ports/driven/cilium_hubble_port.py` — `CiliumHubblePort`
- `src/hexawyn/application/use_case/cilium/get_cilium_flows/` — Command, Response, UseCase
- `src/hexawyn/mcp/tools/get_cilium_flows.py` — MCP tool
- `src/hexawyn/mcp/adapters/cilium_adapters.py` — `build_cilium_hubble_adapter()`
