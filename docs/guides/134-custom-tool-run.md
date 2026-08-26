# Use Case — Run Custom Tool

## Sample Questions

- "Run my finops-zombie-check custom tool on the data namespace."
- "Execute the pci-compliance analyzer with these parameters."

---

Executes a registered custom tool through the control-plane: MCP Tool →
RuntimeClient → Runtime API.

### Flow 1 — Happy Path

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as custom_tool_run()
    participant Client as RuntimeClient
    participant CP as Control-Plane API

    AI->>Tool: Call "custom_tool_run" (name, params="{}")
    Tool->>Client: RuntimeClient(endpoint=get_runtime_endpoint())
    Client->>CP: POST /custom-tools/{name}/run {params}
    CP-->>Client: result
    Client-->>Tool: execution result
    Tool->>Client: close()
    Tool-->>AI: result
```

### Flow 2 — Errors

```mermaid
sequenceDiagram
    participant Tool as custom_tool_run()
    participant Client as RuntimeClient

    Tool->>Client: RuntimeClient(endpoint="")
    alt endpoint not configured
        Tool-->>Tool: { error: "Runtime endpoint not configured" }
    else tool execution failed
        Client-->>Tool: error
        Tool-->>Tool: { error: "..." }
    end
```

## Key Points

- Thin proxy to the runtime — no local execution logic.
- `params` is a JSON string passed through to the runtime.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_returns_dict` | `tests/unit/mcp/tools/test_tool_custom_tool_run.py` | ✅ |

## Related Files

- `src/hexawyn/mcp/tools/custom_tool_run.py`
- `src/hexawyn/adapters/secondary/runtime_client.py`
- `src/hexawyn/infrastructure/config/config_manager.py` — get_runtime_endpoint()
