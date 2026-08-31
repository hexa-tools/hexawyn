# Use Case 44 — KEDA Event-Driven Autoscaling (ScaledObjects, Triggers, HPA)

## Sample Questions

- "Why isn't my ScaledObject payments-consumer scaling even though the Kafka queue is full?"
- "What KEDA ScaledObjects are configured across my cluster?"
- "Are there any KEDA triggers with broken authentication?"
- "Which workloads are configured to scale to zero overnight?"
- "Is KEDA installed in my cluster and what version?"
- "What's the status of the HPA managed by KEDA for auth-service?"
- "Is there a ScaledObject whose cooldown is currently blocking scaling?"
- "How many KEDA ScaledObjects manage our production vs staging clusters?"
- "Did my ScaledJob batch-processing run successfully last night?"

---

Nine MCP tools for KEDA diagnostics: `keda_detect` (auto-detect KEDA installation + version + managed namespaces), `keda_scaledobjects_list` (all ScaledObjects with HPA status, triggers, multi-cluster), `keda_scaledobject_get` (full detail: triggers, HPA, cooldown, fallback), `keda_scaledobject_status` (real-time current vs HPA target replicas, last scale time), `keda_scaledobject_triggers` (all triggers with auth status), `keda_trigger_auth_list` (TriggerAuthentication + ClusterTriggerAuthentication), `keda_trigger_auth_get` (auth detail without exposing secret values), `keda_scaledjobs_list` (ScaledJobs status), `keda_scaledjob_get` (ScaledJob detail with job execution counters). All read-only — no scaling, no patching, no HPA recreation. Multi-cluster aware via optional `cluster_name` parameter.

### Flow 1 — Happy Path: KEDA Detection + List ScaledObjects

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as keda_detect / keda_scaledobjects_list
    participant UseCase as KedaDetectUseCase
    participant Service as KedaDetectService
    participant Port as KedaPort (ABC)
    participant Adapter as KedaAdapter
    participant K8s as Kubernetes API

    AI->>MCP: Call "keda_detect"
    MCP->>Tool: @mcp.tool() dispatch

    Tool->>UseCase: execute(KedaDetectCommand())
    UseCase->>Service: detect(command)
    Service->>Port: detect_engine()

    Port->>Adapter: KedaAdapter
    Adapter->>K8s: Check KEDA CRDs (keda.sh)
    K8s-->>Adapter: ✅ CRD found

    Note over Adapter: KEDA v2.14.0 detected<br/>12 ScaledObjects: 10 ready, 1 error, 1 scaled-to-zero<br/>3 ScaledJobs · 8 managed namespaces

    Adapter-->>Port: KedaDetectionResult(installed=True, version="2.14.0")
    Port-->>Service: result
    Service-->>UseCase: KedaDetectResponse(installed=True, total_scaledobjects=12)
    UseCase-->>Tool: response
    Tool-->>MCP: {installed: true, version: "2.14.0", total_scaledobjects: 12, error: 1}
    MCP-->>AI: "KEDA v2.14.0 detected — 12 ScaledObjects across 8 namespaces. 10 ready, 1 in error, 1 scaled to zero."
```

### Flow 2 — Trigger Auth Error Diagnosis

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as keda_scaledobject_get
    participant Service as KedaScaledObjectGetService
    participant Port as KedaPort
    participant Adapter as KedaAdapter
    participant K8s as Kubernetes API

    AI->>Tool: Call "keda_scaledobject_get"<br/>name="payments-consumer"<br/>namespace="production"

    Tool->>Service: get(command)
    Service->>Port: get_scaledobject("payments-consumer", "production")
    Port->>Adapter: read ScaledObject + associated TriggerAuth

    Adapter->>K8s: GET /apis/keda.sh/v1alpha1/scaledobjects/payments-consumer
    K8s-->>Adapter: ScaledObject with trigger Kafka

    Adapter->>K8s: GET TriggerAuthentication "kafka-auth"
    K8s-->>Adapter: TriggerAuth — references Secret "kafka-credentials"

    Adapter->>K8s: Verify Secret "kafka-credentials" exists
    K8s-->>Adapter: ❌ Secret not found

    Note over Adapter: KedaTrigger(authentication_status=False)<br/>error_message="Secret kafka-credentials not found in namespace production"

    Adapter-->>Port: KedaScaledObject(phase=ERROR, triggers=[{auth: false}])
    Port-->>Service: scaled_object
    Service-->>Tool: response with diagnostic
    Tool-->>MCP: {phase: "error", triggers: [{authentication_status: false, error: "secret not found"}]}
    MCP-->>AI: "Payments-consumer is in ERROR state. The Kafka trigger 'kafka-auth' references Secret 'kafka-credentials' which no longer exists in the production namespace. Fix: recreate the secret or update the TriggerAuthentication."
```

### Flow 3 — Cooldown Blocking Legitimate Scaling

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as keda_scaledobject_status
    participant Adapter as KedaAdapter
    participant K8s as Kubernetes API

    AI->>Tool: Call "keda_scaledobject_status"<br/>name="order-processor"<br/>namespace="production"

    Tool->>Adapter: get_status("order-processor", "production")
    Adapter->>K8s: GET ScaledObject + associated HPA
    K8s-->>Adapter: ScaledObject cooldownPeriod=300s<br/>HPA target=8 replicas · current=3

    Adapter->>K8s: GET events for ScaledObject
    K8s-->>Adapter: Last scale event: +2 replicas, 120s ago

    Note over Adapter: cooldownPeriod=300s active<br/>120s remaining before next scale<br/>HPA wants 8, currently at 3

    Adapter-->>Tool: KedaScaledObject(phase=COOLDOWN, hpa_target=8, current=3, cooldown=300, last_scale=120s ago)
    Tool-->>AI: "Order-processor is in COOLDOWN — last scaled 120s ago, cooldown period is 300s. HPA wants 8 replicas but currently at 3. Next scale possible in ~180 seconds. This is normal KEDA behavior, not an error."
```

### Flow 4 — KEDA Not Installed

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as keda_detect
    participant Adapter as KedaAdapter
    participant K8s as Kubernetes API

    AI->>Tool: Call "keda_detect"
    Tool->>Adapter: detect_engine()
    Adapter->>K8s: Check KEDA CRDs (keda.sh)
    K8s-->>Adapter: ❌ CRD not found

    Note over Adapter: ComponentNotInstalledError<br/>"KEDA CRDs not found — no keda.sh API group"

    Adapter-->>Tool: KedaDetectionResult(installed=False)
    Tool-->>AI: "KEDA is not installed in this cluster. Install via: https://keda.sh/docs/deploy/"
```

### Flow 5 — Multi-Cluster Awareness

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as keda_scaledobjects_list
    participant Adapter as KedaAdapter
    participant K8sProdEU as K8s prod-eu
    participant K8sProdUS as K8s prod-us
    participant K8sStaging as K8s staging

    AI->>Tool: Call "keda_scaledobjects_list" cluster_name="prod-eu"
    Tool->>Adapter: list_scaledobjects(cluster="prod-eu")

    Adapter->>K8sProdEU: GET ScaledObjects
    K8sProdEU-->>Adapter: 5 ScaledObjects (prod-eu)

    Note over Adapter: Cluster context isolated<br/>Only prod-eu ScaledObjects returned<br/>prod-us and staging excluded

    Adapter-->>Tool: [5 ScaledObjects prod-eu]
    Tool-->>AI: "5 KEDA ScaledObjects in prod-eu: 4 ready, 1 in error (payments-consumer — Kafka auth missing)."

    Note over AI,K8sStaging: User asks: "Compare all clusters"

    AI->>Tool: Call "keda_scaledobjects_list" cluster_name="*"
    Tool->>Adapter: list_scaledobjects(cluster="*")
    Adapter->>K8sProdEU: GET ScaledObjects
    Adapter->>K8sProdUS: GET ScaledObjects
    Adapter->>K8sStaging: GET ScaledObjects
    K8sProdEU-->>Adapter: 5 ScaledObjects
    K8sProdUS-->>Adapter: 3 ScaledObjects
    K8sStaging-->>Adapter: 1 ScaledObject

    Adapter-->>Tool: 9 ScaledObjects across 3 clusters
    Tool-->>AI: "9 KEDA ScaledObjects across 3 clusters: prod-eu(5), prod-us(3), staging(1)."
```

## Key Points

- **Trigger auth validation** — KEDA adapter verifies that referenced Secrets/ConfigMaps exist; `authentication_status=False` if missing
- **Cooldown awareness** — cooldown blocking scale is normal behavior, not an error; explained with remaining time
- **Scale to zero** — `idle_replicas=0` is intentional, not a bug; distinguished from ERROR state
- **Multi-cluster** — each tool accepts optional `cluster_name`; `*` aggregates all clusters for fleet-wide view
- **Read-only** — no scale up/down, no pause, no HPA recreation; Mutation Guard enforced on all tools

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_tool_returns_detection` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_tool_returns_scaledobjects` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_tool_returns_scaledobject_detail` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_tool_returns_scaledobject_status` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_tool_returns_triggers` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_tool_returns_trigger_auth` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_tool_returns_scaledjobs` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_tool_returns_scaledjob_detail` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_all_keda_tools_have_register` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_trigger_auth_failure_detected` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_cooldown_phase_detected` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_scaled_to_zero_not_error` | `tests/unit/test_keda_tools.py` | ⬜ |
| `test_multi_cluster_isolation` | `tests/unit/test_keda_tools.py` | ⬜ |

## Related Files

- `src/hexawyn/domain/models/keda.py` — KedaScaledObject, KedaTrigger, KedaTriggerAuth, KedaScaledJob, KedaDetectionResult
- `src/hexawyn/domain/errors.py` — ComponentNotInstalledError
- `src/hexawyn/application/ports/driven/keda_port.py` — KedaPort ABC
- `src/hexawyn/adapters/secondary/keda/keda_adapter.py` — KedaAdapter (reads KEDA CRDs)
- `src/hexawyn/adapters/secondary/keda/keda_detector.py` — KedaDetector (auto-detect CRDs)
- `src/hexawyn/mcp/tools/keda_detect.py` — detect tool
- `src/hexawyn/mcp/tools/keda_scaledobjects_list.py` — list tool
- `src/hexawyn/mcp/tools/keda_scaledobject_get.py` — get tool
- `src/hexawyn/mcp/tools/keda_scaledobject_status.py` — status tool
- `src/hexawyn/mcp/tools/keda_scaledobject_triggers.py` — triggers tool
- `src/hexawyn/mcp/tools/keda_trigger_auth_list.py` — auth list tool
- `src/hexawyn/mcp/tools/keda_trigger_auth_get.py` — auth get tool
- `src/hexawyn/mcp/tools/keda_scaledjobs_list.py` — scaledjobs list tool
- `src/hexawyn/mcp/tools/keda_scaledjob_get.py` — scaledjob get tool
