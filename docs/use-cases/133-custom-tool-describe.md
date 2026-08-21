# Use Case — Describe Custom Tool

## Sample Questions

- "What does the pci-compliance custom tool do?"
- "Show the parameters and schema of a registered custom tool."

---

Returns a custom tool's contract (parameters, output schema, transport,
endpoint) from the control-plane: MCP Tool → RuntimeClient → Runtime API.

### Flow 1 — Happy Path

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as custom_tool_describe()
    participant Client as RuntimeClient
    participant CP as Control-Plane API

    AI->>Tool: Call "custom_tool_describe" (name="pci-compliance")
    Tool->>Client: RuntimeClient(endpoint=get_runtime_endpoint())
    Client->>CP: GET /custom-tools/{name}
    CP-->>Client: { parameters, output_schema, transport, endpoint }
    Client-->>Tool: contract
    Tool->>Client: close()
    Tool-->>AI: contract
```

### Flow 2 — Errors

```mermaid
sequenceDiagram
    participant Tool as custom_tool_describe()
    participant Client as RuntimeClient

    Tool->>Client: RuntimeClient(endpoint="")
    alt endpoint not configured
        Tool-->>Tool: { error: "Runtime endpoint not configured" }
    else API error
        Client-->>Tool: ApiException
        Tool-->>Tool: { error: "..." }
    end
```

## Key Points

- No local use case/port — the tool proxies to the control-plane runtime.
- Requires `HEXAWYN_RUNTIME_ENDPOINT` (or config) to be set.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_returns_dict` | `tests/unit/mcp/tools/test_tool_custom_tool_describe.py` | ✅ |

## Related Files

- `src/hexawyn/mcp/tools/custom_tool_describe.py`
- `src/hexawyn/adapters/secondary/runtime_client.py`
- `src/hexawyn/infrastructure/config/config_manager.py` — get_runtime_endpoint()
