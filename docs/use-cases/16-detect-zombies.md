# Use Case 16 — Detect Zombie Deployments (Idle Pod Detection)

## Sample Questions

- "Which pods have been running with 0 traffic for the last 24 hours — are there zombie deployments we can safely remove?"
- "Can you list all pods that received no network traffic in the last day?"
- "Are there any zombie workloads wasting compute resources in my cluster?"
- "How much money would I save by removing idle pods from production?"
- "Show me pods with zero RPS — flag the ones safe to decommission."

---

## Happy Path

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant UC as DetectZombiesUseCase
    participant Svc as DetectZombiesService
    participant Engine as ZombieDetectionEngine
    participant Adapter as VanillaAdapter
    participant K8s as K8s API
    participant Prom as Prometheus

    User->>MCP: detect_zombies(analysis_window_hours=24)
    MCP->>UC: execute(command)
    UC->>Svc: detect_zombies(command)
    Svc->>Adapter: get_zombie_workloads(window_hours=24)
    Adapter->>K8s: list_pod_for_all_namespaces()
    K8s-->>Adapter: [Pod list]
    Adapter->>Prom: rate(container_network_receive_bytes_total[24h])
    Prom-->>Adapter: [traffic bytes per pod]
    Note over Adapter: Exclude Terminating pods<br/>Exclude kubelet health-check traffic<br/>Flag CronJob workers separately
    Adapter-->>Svc: [ZombiePodData]
    Svc->>Engine: detect(data, analysis_window_hours)
    Note over Engine: zero_traffic_detection() → candidates<br/>risk_classification() → safe/needs_review<br/>compute_waste() → CPU + memory savings
    Engine-->>Svc: ZombieDetectionResult
    Svc-->>UC: DetectZombiesResponse
    UC-->>MCP: response
    MCP-->>User: zombie_candidates, total_wasted_cores, total_wasted_gb
```

---

## Error Flows

```mermaid
sequenceDiagram
    actor User
    participant MCP as MCP Tool
    participant Adapter as VanillaAdapter
    participant K8s as K8s API
    participant Prom as Prometheus

    User->>MCP: detect_zombies()
    MCP->>Adapter: get_zombie_workloads(24)

    alt Cluster Unreachable
        Adapter->>K8s: list_pod_for_all_namespaces()
        K8s--xAdapter: ConnectionError / Forbidden
        Adapter-->>MCP: ClusterUnreachableError
        MCP-->>User: error: "ClusterUnreachableError: ..."
    else Prometheus Unavailable
        K8s-->>Adapter: [Pod list OK]
        Adapter->>Prom: rate(bytes_total[24h])
        Prom--xAdapter: Connection refused
        Note over Adapter: Fallback to OTel trace count<br/>if available
        alt OTel Available
            Adapter-->>MCP: degraded result with fallback note
        else No OTel
            Adapter-->>MCP: PrometheusUnavailableError
            MCP-->>User: error: "PrometheusUnavailableError: ..."
        end
    else No Zombies Found
        Adapter-->>MCP: empty candidates list
        MCP-->>User: "No zombie deployments detected — all pods receiving traffic"
    end
```

---

## Health-Check Filtering & Edge Cases

```mermaid
sequenceDiagram
    participant Engine as ZombieDetectionEngine
    participant Data as Pod List

    Note over Engine: Edge case: health-check only traffic
    Data-->>Engine: pod with 0.001 RPS (kubelet probes only)
    Note over Engine: traffic_rps < PROBE_NOISE_THRESHOLD → treated as zero
    Note over Engine: risk = review_needed (service pointing to it)

    Note over Engine: Edge case: CronJob worker
    Data-->>Engine: pod with 0 RPS over 24h but CronJob owner
    Note over Engine: Check traffic over last 7 days
    Note over Engine: If 7d traffic = 0 → zombie candidate<br/>If 7d traffic > 0 → not a zombie (periodic burst)

    Note over Engine: Edge case: Terminating pod
    Data-->>Engine: pod with phase=Terminating
    Note over Engine: Excluded from candidates entirely

    Note over Engine: Edge case: sidecar container
    Data-->>Engine: pod with multiple containers (sidecar)
    Note over Engine: Traffic counted from all containers in pod<br/>Not from parent alone
```

---

## Prometheus Fallback — OTel Trace Count

```mermaid
sequenceDiagram
    participant Adapter as VanillaAdapter
    participant Prom as Prometheus
    participant OTel as OTel Collector

    Adapter->>Prom: rate(container_network_receive_bytes_total[24h])
    Prom--xAdapter: metric not found

    Note over Adapter: Fallback: OTel span count
    Adapter->>OTel: count of spans tagged by pod_name over 24h
    OTel-->>Adapter: [span_counts]
    Note over Adapter: span_count == 0 → treated as zero traffic
    Adapter-->>Adapter: Build ZombiePodData from OTel fallback
    Note over Adapter: data_source = "otel_fallback"<br/>confidence = "medium"
```

---

## Key Points

- **Zero traffic detection** : `rate(container_network_receive_bytes_total[24h]) == 0` on Prometheus. Fallback to OTel span count if Prometheus metric missing.
- **Health-check filtering** : kubelet probe traffic (very low bytes, no user-facing RPS) is excluded via `_is_probe_traffic()` heuristic.
- **Risk classification** : `safe_to_remove` = no traffic + no Service pointing to it + no CronJob owner. `review_needed` = zero traffic but service/cronjob relationship exists.
- **CronJob detection** : pods owned by CronJob get a 7-day traffic window instead of 24h. Periodic burst workers are never zombies.
- **Waste computation** : total CPU cores and memory GB wasted across all zombie candidates, using resource requests (not limits).
- **Free tier** : Prometheus is optional — adapter returns `prometheus_available=False` and estimates traffic from OTel or deployment context.

## Test Coverage

| Layer | File |
|-------|------|
| Domain models | `tests/unit/test_zombie_detection_models.py` |
| Domain engine | `tests/unit/test_zombie_detection_engine.py` |
| Port + app service + use case | `tests/unit/test_detect_zombies_port_and_service.py` |
| MCP tool + VanillaAdapter | `tests/unit/test_detect_zombies_mcp_and_adapter.py` |

## Tests

| Test | Scenario |
|------|----------|
| `test_legacy_api_zero_traffic_safe_to_remove` | 0 RPS for 24h, no deps → safe_to_remove |
| `test_batch_processor_cronjob_not_zombie` | 0 RPS 24h but CronJob with 7d traffic → not zombie |
| `test_test_deploy_no_deps_wasted_memory` | 0 RPS, no deps, 2GB memory → zombie with saving |
| `test_all_pods_have_traffic_no_zombies` | Every pod has traffic → empty result |
| `test_multiple_zombies_total_waste_computed` | 5 zombie pods → total cores/GB computed |
| `test_terminating_pod_excluded` | Pod in Terminating → not in candidates |
| `test_health_check_only_treated_as_zero` | Probe-only traffic → treated as zero |
| `test_sidecar_traffic_from_all_containers` | Multi-container pod → aggregate traffic |
| `test_prometheus_unavailable_otel_fallback` | Prom down → OTel fallback used |

## Related Files

- `src/hexawyn/domain/models/zombie_detection.py`
- `src/hexawyn/domain/services/zombie_detection/zombie_detection_engine.py`
- `src/hexawyn/application/ports/driven/zombie_detection_port.py`
- `src/hexawyn/application/ports/driving/detect_zombies/`
- `src/hexawyn/application/service/detect_zombies_service.py`
- `src/hexawyn/application/use_case/detect_zombies/detect_zombies_use_case.py`
- `src/hexawyn/mcp/tools/detect_zombies.py`
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py`
