# Use Case 45 — KEDA Autoscaling

## Sample Questions

- "Why is my payments-consumer ScaledObject not scaling even though the Kafka queue is full?"
- "What ScaledObjects are configured in my cluster?"
- "Are there any KEDA triggers with authentication errors?"
- "Which workloads are configured to scale to zero at night?"
- "Is KEDA installed in my cluster and what version?"
- "What is the HPA status managed by KEDA for the auth-service?"
- "Is there a ScaledObject with an active cooldown blocking scaling right now?"
- "How many KEDA ScaledObjects are in production vs staging?"
- "Did my batch-processing ScaledJob run successfully last night?"

---

Nine MCP tools for KEDA: `keda_detect`, `keda_scaledobjects_list`, `keda_scaledobject_get`, `keda_scaledobject_status`, `keda_scaledobject_triggers`, `keda_triggerauth_list`, `keda_triggerauth_get`, `keda_scaledjobs_list`, `keda_scaledjob_get`. All read-only — never triggers scale.

### Flow 1 — Happy Path: Detect + Diagnose ScaledObject

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as keda_detect / keda_scaledobject_get
    participant Port as KedaPort (ABC)
    participant Adapter as KedaDetector
    participant K8s as Kubernetes API

    AI->>MCP: Call "keda_scaledobject_get" name="payments-consumer"
    MCP->>Tool: dispatch
    Tool->>Port: get_scaledobject("payments-consumer", "production")
    Port->>Adapter: KedaDetector
    Adapter->>K8s: GET /apis/keda.sh/v1alpha1/scaledobjects/payments-consumer
    K8s-->>Adapter: ScaledObject + HPA + events

    Note over Adapter: phase=COOLDOWN, current=3, hpa_target=5<br/>cooldown=300s, last_scale=120s ago<br/>Kafka trigger: auth OK ✓

    Adapter-->>Port: KedaScaledObject(COOLDOWN, triggers=[...])
    Port-->>Tool: result
    Tool-->>MCP: {phase: "cooldown", current_replicas: 3, hpa_target_replicas: 5}
    MCP-->>AI: "payments-consumer: cooldown active (120s of 300s). HPA wants 5 replicas, currently at 3. Kafka trigger auth OK. Will resume scaling in 180s."
```

### Flow 2 — Trigger Auth Failure

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as keda_scaledobject_get
    participant Adapter as KedaDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "keda_scaledobject_get" name="auth-service"
    Tool->>Adapter: get_scaledobject("auth-service", "production")
    Adapter->>K8s: GET .../scaledobjects/auth-service
    K8s-->>Adapter: ScaledObject ERROR

    Note over Adapter: phase=ERROR<br/>Kafka trigger: auth_status=False<br/>error_message="Secret kafka-auth not found"<br/>FALLBACK replicas=3 active

    Adapter-->>Tool: KedaScaledObject(ERROR, fallback_replicas=3)
    Tool-->>AI: "auth-service ERROR: Kafka trigger authentication failed — Secret 'kafka-auth' not found. Running in FALLBACK mode at 3 replicas."
```

### Flow 3 — Scale to Zero (Normal Behavior)

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as keda_scaledobject_status
    participant Adapter as KedaDetector

    AI->>Tool: Call "keda_scaledobject_status" name="batch-worker"
    Tool->>Adapter: get_scaledobject("batch-worker", "data")
    K8s-->>Adapter: ScaledObject SCALED_TO_ZERO

    Note over Adapter: phase=SCALED_TO_ZERO<br/>idle_replicas=0, min_replicas=0<br/>This is INTENTIONAL — Cron trigger at 6am daily

    Adapter-->>Tool: KedaScaledObject(SCALED_TO_ZERO)
    Tool-->>AI: "batch-worker is SCALED TO ZERO (normal). Idle replicas set to 0. Cron trigger will scale up at 06:00."
```

### Flow 4 — KEDA Not Installed

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as keda_detect
    participant Adapter as KedaDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "keda_detect"
    Tool->>Adapter: detect()
    Adapter->>K8s: Check keda.sh CRDs
    K8s-->>Adapter: ❌ CRD not found

    Note over Adapter: ComponentNotInstalledError

    Adapter-->>Tool: KedaDetectionResult(installed=False)
    Tool-->>AI: "KEDA not detected. Install: https://keda.sh/docs/deploy/"
```

## Key Points

- **Cooldown awareness** — `cooldown_period_seconds` and `last_scale_time` explain WHY scaling is waiting
- **Fallback mode** — when a trigger errors, KEDA falls back to `fallback_replicas` (safe default)
- **Scale to zero** — `idle_replicas=0` is NOT an error; it's intentional with cron triggers
- **Trigger auth** — `authentication_status` per-trigger with `error_message` for diagnosis
- **HPA correlation** — `hpa_target_replicas` vs `current_replicas` gives real scaling status
- **Read-only** — never triggers scale; operators retain control via KEDA or kubectl

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_installed` | `tests/unit/test_keda_tools.py` | ✅ |
| `test_list` | `tests/unit/test_keda_tools.py` | ✅ |
| `test_get` | `tests/unit/test_keda_tools.py` | ✅ |
| `test_all_keda_tools` | `tests/unit/test_keda_tools.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/keda.py` — KedaScaledObject, KedaTrigger, KedaTriggerAuth, KedaScaledJob, KedaDetectionResult
- `src/hexawyn/domain/errors.py` — ComponentNotInstalledError
- `src/hexawyn/application/ports/driven/keda_port.py` — KedaPort ABC
- `src/hexawyn/adapters/secondary/gitops/keda_detector.py` — KedaDetector
- `src/hexawyn/mcp/tools/keda_*.py` — 9 tools
