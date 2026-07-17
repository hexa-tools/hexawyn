# Use Case — Startup Scan via SLM

At CLI launch, the TUI sends local pod data to the control-plane's startup scan endpoint. The control-plane's LangGraph startup graph analyzes the pods and returns health scores, suggestions, and narrative summaries via the SLM. Results are displayed in the TUI sidebar.

Replaced direct DeepSeek calls with control-plane SLM integration for better maintainability and offline resilience (pod-based fallback when control-plane unreachable).

## Sample Questions

N/A — this runs automatically at CLI startup.

---

### Flow 1 — Startup Scan with Pods from CLI

```mermaid
sequenceDiagram
    participant TUI as HexawynTUI
    participant Adapter as K8s Adapter (local)
    participant Runtime as HttpRuntimeAdapter
    participant CP as Control-Plane API
    participant Graph as LangGraph startup graph
    participant SLM as SLM (qwen/llama)

    TUI->>TUI: on_mount() → _generate_ai_suggestion()

    TUI->>Adapter: safe_pods(adapter)
    Adapter-->>TUI: 37 pods (Running, Pending, Failed)

    TUI->>Runtime: run_startup_scan(cluster, pods=[...])
    Runtime->>CP: POST /api/v1/startup-scan
    Note over Runtime,CP: Headers: X-API-Key, X-Machine-ID

    CP->>Graph: build_startup_graph().stream(state)
    Graph->>Graph: load_pods (skip K8s — pods from CLI)
    Graph->>Graph: detect_provider → detect_crashloop → ... → aggregate
    Graph->>SLM: generate_suggestions(prompt)
    SLM-->>Graph: health_score=95, suggestions=[...], narrative="Cluster stable"

    Graph-->>CP: StartupScanResult
    CP-->>Runtime: {health_score, narrative, suggestions, ...}
    Runtime-->>TUI: StartupScanResult

    TUI->>TUI: self.ai_suggestion = suggestions[0]
    TUI-->>TUI: refresh sidebar with suggestion

    alt Control-plane unreachable
        TUI->>Adapter: safe_pods(adapter)
        TUI->>TUI: _fallback_suggestion(pods)
        Note over TUI: "All 37 pods healthy — no issues detected"
    end
```

### Flow 2 — Machine Fingerprint Binding

```mermaid
sequenceDiagram
    participant CLI as Hexawyn CLI
    participant MID as MachineID (hardware fingerprint)
    participant Client as RuntimeClient
    participant CP as Control-Plane
    participant VK as Valkey (Redis)

    CLI->>MID: get_machine_id()
    MID->>MID: /etc/machine-id + hostname + MAC → SHA-256
    MID-->>CLI: a1b2c3d4e5f6...

    CLI->>Client: startup_scan(cluster, pods)
    Client->>CP: POST /api/v1/startup-scan
    Note over Client,CP: X-API-Key + X-Machine-ID

    CP->>VK: GET machine:sk-xxx
    alt First bind
        VK-->>CP: null
        CP->>VK: SET machine:sk-xxx = a1b2c3d4e5f6
        Note over CP: Machine bound to API key
    else Same machine
        VK-->>CP: a1b2c3d4e5f6
        Note over CP: Machine matches — OK
    else Different machine
        VK-->>CP: x9y0z1... (different)
        Note over CP: WARNING — machine_mismatch
        CP-->>Client: 200 OK (graceful — logs only)
    end
```

## Key Points

- CLI sends pods to control-plane → control-plane doesn't need its own K8s connection
- Hardware fingerprint prevents API key sharing across machines
- Fallback to pod-based suggestions when control-plane is unreachable
- Error narratives (e.g., "cluster is down", "0 pods") are filtered out
- Cross-platform: Linux (/etc/machine-id), macOS (IOPlatformUUID), Windows (MachineGuid)

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_startup_scan_endpoint_returns_200` | `tests/integration/test_startup_scan_integration.py` | ✅ |
| `test_startup_scan_via_runtime_client` | `tests/integration/test_startup_scan_integration.py` | ✅ |
| `test_linux_machine_id` | `tests/unit/infrastructure/config/test_machine_id.py` | ✅ |
| `test_hardware_fingerprint_returns_24_char_hex` | `tests/unit/infrastructure/config/test_machine_id.py` | ✅ |
| `test_uses_pre_loaded_pods_when_present` | `hexa-control-plane/tests/unit/test_load_pods.py` | ✅ |

## Related Files

- `src/hexawyn/cli/tui.py` — _generate_ai_suggestion, _fallback_suggestion
- `src/hexawyn/adapters/secondary/runtime_client.py` — startup_scan(pods)
- `src/hexawyn/application/service/http_runtime_adapter.py` — run_startup_scan
- `src/hexawyn/infrastructure/config/machine_id.py` — Hardware fingerprint
- hexa-control-plane: `api/routers/startup.py`, `load_pods.py`, `runtime_adapter.py`
