# Use Case — List Custom Tools

## Sample Questions

- "What custom tools are registered and available?"
- "List all registered custom tools with their transport and endpoint."

---

Lists all registered custom tools from the control-plane: MCP Tool →
RuntimeClient → Runtime API.

### Flow 1 — Happy Path

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as custom_tools_list()
    participant Client as RuntimeClient
    participant CP as Control-Plane API

    AI->>Tool: Call "custom_tools_list"
    Tool->>Client: RuntimeClient(endpoint=get_runtime_endpoint())
    Client->>CP: GET /custom-tools
    CP-->>Client: list of tools
    Client-->>Tool: tools
    Tool->>Client: close()
    Tool-->>AI: [{ name, transport, endpoint, description }]
```

### Flow 2 — Errors

```mermaid
sequenceDiagram
    participant Tool as custom_tools_list()
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

- Reads the registry from the runtime, not from a local store.
- Requires the runtime endpoint to be configured.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_returns_dict` | `tests/unit/mcp/tools/test_tool_custom_tools_list.py` | ✅ |

## Related Files

- `src/hexawyn/mcp/tools/custom_tools_list.py`
- `src/hexawyn/adapters/secondary/runtime_client.py`
- `src/hexawyn/infrastructure/config/config_manager.py` — get_runtime_endpoint()
