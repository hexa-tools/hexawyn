# 86 — Detect Missing Probes

Scan all deployments/pods across namespaces for probe configuration.
Detect missing liveness probes, readiness probes, or both.
Prioritize production workloads serving external traffic with no probes (critical).
Suggest appropriate probe types based on the container's exposed ports.

## Sample Questions

- "Which services have no liveness or readiness probes configured — which workloads are flying blind with no health check?"
- "Are there any production deployments missing health probes?"
- "List all deployments without readiness probes in the production namespace."
- "How many critical workloads have no probes at all?"
- "Show me pods with misconfigured probe ports that don't match their exposed ports."

---

## 1. Happy Path — Full Hexagonal Chain

```mermaid
sequenceDiagram
    participant User
    participant MCP as MCP Tool
    participant UC as DetectMissingProbesUseCase
    participant Svc as DetectMissingProbesService
    participant Engine as ProbeAuditEngine
    participant Port as ProbeAuditPort
    participant Adapter as VanillaAdapter
    participant K8s as Kubernetes API

    User->>MCP: detect_missing_probes(namespace="production")
    MCP->>MCP: build_probe_audit_adapter()
    MCP->>Svc: DetectMissingProbesService(port=adapter)
    MCP->>UC: DetectMissingProbesUseCase(service=svc)
    MCP->>UC: execute(DetectMissingProbesCommand(namespace="production"))
    UC->>Svc: detect_missing_probes(command)
    Svc->>Port: get_probe_audit_data(namespace="production")
    Port->>Adapter: get_probe_audit_data(namespace="production")

    Note over Adapter,K8s: list_pod_for_all_namespaces

    Adapter-->>Port: list[ProbeDeploymentRawData]

    Note over Adapter: extract containers, probes, ports per pod

    Port-->>Svc: raw deployment data

    Svc->>Engine: detect(deployments)
    Engine->>Engine: _find_missing_probes()
    Engine->>Engine: _classify_severity()
    Engine->>Engine: _suggest_readiness_probe()
    Engine->>Engine: _suggest_liveness_probe()
    Engine-->>Svc: ProbeAuditResult

    Svc-->>UC: DetectMissingProbesResponse
    UC-->>MCP: response

    Note over MCP: serialize to dict

    MCP-->>User: total_without_probes=3, critical=1, warning=2
```

## 2. Error Flows

```mermaid
sequenceDiagram
    participant MCP as MCP Tool
    participant Svc as Service
    participant Adapter as VanillaAdapter
    participant K8s as Kubernetes API

    alt Cluster Unreachable
        Adapter->>K8s: list_pod_for_all_namespaces(timeout=15s)
        K8s-->>Adapter: ApiException
        Adapter->>Adapter: catch ApiException
        Adapter-->>Svc: raise ClusterUnreachableError("Cannot list pods for probe audit")
        Svc->>Svc: NO try/catch — propagate
        MCP->>MCP: catch Exception
        MCP-->>User: {"error": "Cannot list pods...", "total_without_probes": 0}
    else RBAC Denied
        Adapter->>K8s: list_pod_for_all_namespaces()
        K8s-->>Adapter: Forbidden (403)
        Adapter->>Adapter: catch ApiException
        Adapter-->>Svc: raise InsufficientPermissionsError
        MCP->>MCP: catch Exception
        MCP-->>User: {"error": "Forbidden...", "total_without_probes": 0}
    end
```

## 3. Checker Node Flow

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Engine as ProbeAuditEngine
    participant Result as ProbeAuditResult

    Checker->>Engine: detect(deployments)

    alt PASS — no missing probes
        Engine-->>Checker: total_without_probes=0
        Checker-->>User: "All workloads have health probes configured ✓"
    else FLAG — misconfigured probes (port mismatch)
        Engine-->>Checker: misconfigured_probes=[{deployment: "broken-probe", missing: ["readiness_port_mismatch"]}]
        Checker-->>User: "Warning: 1 deployment has misconfigured probes"
    else FAIL — critical workloads missing probes
        Engine-->>Checker: total_without_probes=8, critical=3
        Checker-->>User: "8 workloads have no probes. 3 critical: payment-service, auth-service, ..."
    else DEGRADED — DuckDB unavailable
        Engine-->>Checker: result (no memory stored)
        Checker-->>User: "Probe audit completed (memory unavailable for caching)"
    end
```

## 4. Severity Classification Logic

```mermaid
sequenceDiagram
    participant Engine as ProbeAuditEngine
    participant Classifier as _classify_severity

    Engine->>Classifier: classify(namespace="production", has_service=True, is_exposed=True, type="Deployment")

    alt Production + Exposed Externally
        Classifier-->>Engine: "critical"
    else Production + Has Service (internal)
        Classifier-->>Engine: "warning"
    else StatefulSet + Has Service
        Classifier-->>Engine: "critical"
    else Job / CronJob / DaemonSet
        Classifier-->>Engine: "informational"
    else No Service + No Exposure
        Classifier-->>Engine: "informational"
    else Staging/Dev with Service
        Classifier-->>Engine: "warning"
    end
```

---

## Key Points

- Scans all deployments/pods across namespaces for liveness and readiness probe configuration
- Excludes init containers from probe checks (probes not applicable to init containers)
- DaemonSet workloads without probes receive `informational` severity (node-level infrastructure)
- StatefulSet workloads without probes receive `critical` severity when they have a service (stateful = harder to restart)
- Detects misconfigured probes (port mismatch between exposed ports and probe ports)
- Generates probe suggestions based on container ports: HTTP ports (80, 443, 8080...) get `httpGet`, others get `tcpSocket`, no-port containers get `exec` suggestion

---

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_both_probes_missing_critical` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_has_readiness_but_no_liveness_warning` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_batch_job_no_probes_informational` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_all_probes_present_no_issues` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_eight_deployments_missing_probes_all_listed` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_daemonset_no_probes_informational` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_statefulset_no_probes_critical` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_init_containers_excluded_from_check` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_no_exposed_ports_exec_probe_suggestion` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_only_init_containers_no_main_container` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_probe_misconfigured_wrong_path_detected` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_http_probe_suggestion_for_port_8080` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_tcp_probe_suggestion_for_non_http_port` | `tests/unit/test_probe_audit_engine.py` | ✅ |
| `test_delegates_to_use_case_and_returns_dict` | `tests/unit/test_detect_missing_probes_mcp.py` | ✅ |
| `test_is_abstract` | `tests/unit/test_probe_audit_port_and_service.py` | ✅ |
| `test_calls_port_with_namespace_filter` | `tests/unit/test_probe_audit_port_and_service.py` | ✅ |
| `test_build_probe_audit_adapter_returns_probe_audit_port` | `tests/unit/test_server.py` | ✅ |

---

## Related Files

- `src/hexawyn/domain/models/probe_audit.py` — MissingProbe, ProbeAuditResult models
- `src/hexawyn/domain/services/probe_audit/probe_audit_engine.py` — pure domain logic
- `src/hexawyn/application/ports/driven/probe_audit_port.py` — driven port ABC + TypedDict
- `src/hexawyn/application/ports/driving/detect_missing_probes/` — command, response, service port
- `src/hexawyn/application/service/detect_missing_probes_service.py` — application service
- `src/hexawyn/application/use_case/detect_missing_probes/` — use case orchestrator
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py` — VanillaAdapter (get_probe_audit_data)
- `src/hexawyn/mcp/server.py` — build_probe_audit_adapter()
- `src/hexawyn/mcp/tools/detect_missing_probes.py` — MCP tool
