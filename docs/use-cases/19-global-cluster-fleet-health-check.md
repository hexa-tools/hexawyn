# Use Case 19 — Global Cluster Fleet Health Check

## Sample Questions

- "Give me a global health check of the cluster fleet — what is the overall status right now?"
- "Which cluster is the least healthy in my fleet?"
- "Are all my Kubernetes clusters reachable?"
- "What are the critical issues across all clusters?"
- "Is the fleet health improving or degrading compared to last week?"
- "Show me a breakdown by category — nodes, pods, CPU, certificates — for every cluster."

---

## Happy Path

```mermaid
sequenceDiagram
    autonumber
    actor SRE as SRE / Director
    participant MCP as MCP Tool (global_health_check)
    participant UC as GlobalHealthCheckUseCase
    participant SVC as GlobalHealthCheckService
    participant DOM as FleetHealthScoreService (domain)
    participant PORT as FleetHealthPort
    participant ADAPT as FleetHealthAdapter
    participant KB1 as K8s Cluster 1 (prod-eu)
    participant KB2 as K8s Cluster 2 (prod-us)
    participant KB3 as K8s Cluster 3 (staging-eu — unreachable)
    participant PROM as Prometheus

    SRE->>MCP: global_health_check(max_clusters=10, timeout_seconds=8)
    MCP->>UC: execute(GlobalHealthCheckCommand)
    UC->>SVC: global_health_check(command)
    SVC->>PORT: list_contexts()
    PORT->>ADAPT: list_contexts()
    ADAPT-->>PORT: ["prod-eu", "prod-us", "staging-eu"]
    PORT-->>SVC: ["prod-eu", "prod-us", "staging-eu"]

    note over SVC: ThreadPoolExecutor — all contexts in parallel

    par prod-eu
        SVC->>PORT: get_cluster_raw_metrics("prod-eu")
        PORT->>ADAPT: get_cluster_raw_metrics("prod-eu")
        ADAPT->>KB1: list_node (timeout 5s)
        KB1-->>ADAPT: 5 nodes (5 ready)
        ADAPT->>KB1: list_pod_for_all_namespaces (timeout 5s)
        KB1-->>ADAPT: 120 pods (117 running, 3 CrashLoop)
        ADAPT->>PROM: node CPU / memory utilization query
        PROM-->>ADAPT: cpu=0.72, mem=0.65
        ADAPT->>KB1: list_secret_for_all_namespaces (TLS)
        KB1-->>ADAPT: 1 cert expiring in 5 days
        ADAPT-->>PORT: ClusterRawMetrics(crashloop=3, certs_critical=1)
        PORT-->>SVC: ClusterRawMetrics
        SVC->>DOM: compute_health_score(metrics)
        DOM-->>SVC: score=89, categories={nodes:OK, pods:WARNING, cpu:OK, certs:CRITICAL}
    and prod-us
        SVC->>PORT: get_cluster_raw_metrics("prod-us")
        PORT->>ADAPT: get_cluster_raw_metrics("prod-us")
        ADAPT->>KB2: list_node / list_pod_for_all_namespaces
        KB2-->>ADAPT: 4 nodes ready, 80 pods running
        ADAPT->>PROM: CPU / memory query
        PROM-->>ADAPT: cpu=0.45, mem=0.50
        ADAPT-->>PORT: ClusterRawMetrics(crashloop=0, certs_critical=0)
        PORT-->>SVC: ClusterRawMetrics
        SVC->>DOM: compute_health_score(metrics)
        DOM-->>SVC: score=100, all categories OK
    and staging-eu
        SVC->>PORT: get_cluster_raw_metrics("staging-eu")
        PORT->>ADAPT: get_cluster_raw_metrics("staging-eu")
        ADAPT->>KB3: load_kubeconfig / validate_connection
        KB3-->>ADAPT: connection_timeout (error)
        ADAPT-->>PORT: ClusterUnreachableError("connection_timeout")
        PORT-->>SVC: exception caught
        SVC->>DOM: make_unreachable_report("staging-eu", "connection_timeout")
        DOM-->>SVC: ClusterHealthReport(reachable=False, score=None)
    end

    SVC->>DOM: aggregate_fleet([prod-eu, prod-us, staging-eu])
    DOM-->>SVC: FleetHealthReport(fleet_score=95, reachable=2, unreachable=1)
    SVC-->>UC: GlobalHealthCheckResponse(report, trend="stable")
    UC-->>MCP: GlobalHealthCheckResponse
    MCP-->>SRE: {clusters:[...], fleet_score:95, fleet_status:"healthy", unreachable_count:1}
```

---

## Error Flows

```mermaid
sequenceDiagram
    actor SRE
    participant MCP as MCP Tool
    participant SVC as GlobalHealthCheckService
    participant ADAPT as FleetHealthAdapter

    SRE->>MCP: global_health_check()

    alt No kubeconfig / no contexts found
        ADAPT-->>SVC: [] (empty context list)
        Note over SVC: list_contexts() returns [] → no clusters to scan
        SVC-->>MCP: FleetHealthReport(fleet_score=None, reachable=0, clusters=[])
        MCP-->>SRE: {fleet_status: "no_cluster_reachable", error: "No kubeconfig contexts found"}

    else All clusters unreachable
        Note over SVC: Every per-cluster call raises ClusterUnreachableError
        SVC->>SVC: all reports → reachable=False, score=None
        SVC-->>MCP: FleetHealthReport(fleet_score=None, unreachable=N)
        MCP-->>SRE: {fleet_status: "no_cluster_reachable", unreachable_count: N}

    else Prometheus unavailable on a cluster
        ADAPT-->>SVC: ClusterRawMetrics(cpu_utilization=None, memory_utilization=None)
        Note over SVC: compute_health_score() → category cpu=UNKNOWN, mem=UNKNOWN
        Note over SVC: Score computed without CPU/memory deduction
        MCP-->>SRE: score with caveat "prometheus_unavailable=True"

    else Timeout on large fleet (max_clusters exceeded)
        Note over SVC: ThreadPoolExecutor timeout → partial results
        Note over SVC: Clusters not yet scanned → ClusterUnreachableError per context
        MCP-->>SRE: partial report with unreachable_count for timed-out clusters
    end
```

---

## Checker Node — Response Quality Validation

```mermaid
sequenceDiagram
    participant Tool as MCP Tool
    participant Gen as generate_response (LLM)
    participant CK as checker_node
    participant Mem as store_memory
    participant Fmt as format_response

    Tool-->>Gen: FleetHealthReport (scores, categories, unreachable list)
    Gen-->>CK: LLM-generated fleet health summary

    alt PASS — fleet_score correct, critical clusters highlighted
        CK->>Mem: store_memory(query, result, cluster)
        Mem-->>Fmt: stored
        CK-->>Fmt: status=PASS
        Fmt-->>SRE: fleet health summary

    else FAIL — unreachable clusters excluded from average (wrong denominator)
        Note over CK: fleet_score must average reachable clusters only
        Note over CK: If LLM divides by total instead of reachable → FAIL
        CK-->>Gen: retry with corrected prompt
        Note over CK,Gen: retry_count += 1

    else FAIL — score formula error (wrong deduction)
        Note over CK: 3 crashloop / 10 pods → int(3/10 * 40) = 12 pts deducted<br/>LLM says "20 pts" → FAIL
        CK-->>Gen: retry with checker hint

    else FAIL (attempt ≥ 3) — DEGRADED
        CK-->>Fmt: status=DEGRADED
        Fmt-->>SRE: raw report + "summary generation failed"

    else FLAG — Prometheus down on ≥1 cluster (UNKNOWN categories)
        Note over CK: cpu/memory = UNKNOWN when Prometheus unavailable<br/>LLM must not report these as OK
        CK->>Mem: store_memory(with flag metadata)
        CK-->>Fmt: status=FLAG, caveats=["prometheus_unavailable on prod-eu"]
        Fmt-->>SRE: summary + caveat banner
    end
```

---

## DuckDB — Fleet Health Trend

```mermaid
sequenceDiagram
    participant MCP as MCP Tool
    participant Duck as DuckDB (local)
    participant SVC as GlobalHealthCheckService
    participant ADAPT as FleetHealthAdapter

    MCP->>Duck: SELECT fleet_score, scanned_at FROM fleet_health_history WHERE scanned_at > NOW()-INTERVAL 7 DAY ORDER BY scanned_at DESC LIMIT 1

    alt Previous score found (trend computation)
        Duck-->>MCP: {fleet_score: 85, scanned_at: "2026-06-24"}
        Note over SVC: previous=85, current=95 → trend="improving"
        MCP->>Duck: INSERT INTO fleet_health_history (fleet_score, clusters_json, scanned_at)
        Duck-->>MCP: OK
        MCP-->>SRE: report + fleet_score_trend="improving"

    else No previous score (first run)
        Duck-->>MCP: (empty result)
        Note over SVC: trend="unknown" (no baseline)
        MCP->>Duck: INSERT INTO fleet_health_history ...
        MCP-->>SRE: report + fleet_score_trend="unknown"

    else DuckDB unavailable (offline mode)
        Duck--xMCP: IOError / file locked
        Note over MCP: Bypass history — run scan without trend
        MCP->>SVC: global_health_check(command)
        ADAPT-->>SVC: ClusterRawMetrics
        SVC-->>MCP: FleetHealthReport(trend=None)
        MCP-->>SRE: report (no trend available)
    end
```

---

## Key Points

- **Parallel execution** — `ThreadPoolExecutor` scans all contexts simultaneously; each cluster failure is caught individually so one unreachable cluster never blocks the others.
- **Score formula** — `score = 100 - 20×nodes_not_ready - int(crashloop/total×40) - cpu/mem pressure deductions - cert deductions - security deductions`, floored at 0.
- **Fleet aggregate** — `fleet_score` averages only reachable clusters; unreachable clusters are excluded from the denominator and counted in `unreachable_count`.
- **Prometheus optional** — when Prometheus is unavailable, CPU/memory categories become `UNKNOWN` (not `OK`); score is computed without those deductions.
- **Trend** — `fleet_score_trend` is derived from DuckDB history; `"improving"` when score rises >10%, `"degrading"` when it drops >10%, `"stable"` otherwise.

## Test Coverage

| Layer | File |
|-------|------|
| Domain score formula | `tests/unit/test_fleet_health_score_service.py` |
| Domain aggregation | `tests/unit/test_fleet_health_score_service.py` |
| Application service + parallelism | `tests/unit/test_global_health_check_use_case.py` |
| FleetHealthPort + use case | `tests/unit/test_global_health_check_use_case.py` |
| FleetHealthAdapter | `tests/unit/test_fleet_health_adapter.py` |

## Tests

| Test | Scenario |
|------|----------|
| `test_healthy_cluster_score_100` | Zero crashloop, zero pressure → score=100 |
| `test_3_crashloop_10_pods_deducts_12pts` | `int(3/10 * 40) = 12` pts deducted |
| `test_node_not_ready_deducts_20_each` | 1 node not ready → -20 pts |
| `test_cpu_over_90_deducts_15` | cpu_utilization=0.91 → -15 pts |
| `test_cert_critical_deducts_10` | 1 cert CRITICAL → -10 pts |
| `test_security_violations_capped_at_15` | 10 violations → max -15 pts |
| `test_score_floored_at_zero` | Many issues → score=0, never negative |
| `test_unreachable_excluded_from_aggregate` | 3 clusters, 1 unreachable → avg of 2 |
| `test_all_unreachable_fleet_score_none` | All unreachable → fleet_score=None |
| `test_trend_improving_when_score_rises` | previous=72, current=89 → "improving" |
| `test_trend_degrading_when_score_falls` | previous=89, current=72 → "degrading" |
| `test_prometheus_unavailable_cpu_unknown` | cpu_utilization=None → category=UNKNOWN |

## Related Files

- `src/hexawyn/domain/models/fleet_health.py`
- `src/hexawyn/domain/services/fleet_health/fleet_health_score_service.py`
- `src/hexawyn/application/ports/driven/fleet_health_port.py`
- `src/hexawyn/application/ports/driving/global_health_check/`
- `src/hexawyn/application/service/global_health_check_service.py`
- `src/hexawyn/application/use_case/global_health_check/global_health_check_use_case.py`
- `src/hexawyn/adapters/secondary/fleet_health_adapter.py`
- `src/hexawyn/mcp/tools/global_health_check.py`
