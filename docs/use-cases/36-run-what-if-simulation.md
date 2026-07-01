# Use Case 36 — Run What-If Simulation

## Sample Questions

- "What would happen to the cluster if I scale down the auth-service to 1 replica? Simulate the impact on latency, error rate, and dependent services."
- "If I double the replicas of payment-service, which downstream services will be affected?"
- "Simulate scaling the checkout-service from 3 to 1 — is it safe during peak traffic?"
- "Show me the blast radius if I remove the caching layer — which services depend on redis?"
- "What's the risk level of reducing api-gateway to 2 replicas given current CPU usage?"

---

Accepts a target service and a proposed change (e.g. scale replicas), identifies dependent services via topology analysis, evaluates current traffic load vs capacity after the change, estimates risk level (Low/Medium/High/Critical) based on replica headroom, checks PodDisruptionBudget and HPA constraints, detects circular dependencies, and returns a structured impact report with latency delta and error risk estimation.

---

## Flow 1 — Happy Path (auth-service 3→1, 62% CPU, High risk)

```mermaid
sequenceDiagram
    actor SRE
    participant MCP as MCP Tool<br/>(run_what_if_simulation)
    participant UC as RunWhatIfSimulationUseCase
    participant Svc as RunWhatIfSimulationService
    participant Port as WhatIfSimulationPort (ABC)
    participant Adapter as VanillaAdapter
    participant K8s as Kubernetes API
    participant Engine as WhatIfScenarioSimulatorService

    SRE->>MCP: run_what_if_simulation("auth-service",<br/>"production", proposed_replicas=1)
    MCP->>UC: execute(RunWhatIfSimulationCommand)
    UC->>Svc: simulate(command)

    Svc->>Port: get_current_replicas("production", "auth-service")
    Port->>Adapter: get_current_replicas()
    Adapter->>K8s: AppsV1Api.list_deployment_for_all_namespaces()
    K8s-->>Adapter: auth-service deployment (replicas=3)
    Adapter-->>Svc: 3

    Svc->>Port: get_current_cpu_utilization("production", "auth-service")
    Port->>Adapter: get_current_cpu_utilization()
    Adapter->>K8s: Prometheus query (cpu_usage / cpu_requests * 100)
    K8s-->>Adapter: 62.0
    Adapter-->>Svc: 62.0

    Svc->>Port: get_service_topology("production", "auth-service")
    Port->>Adapter: get_service_topology()
    Adapter-->>Svc: {auth-service: [checkout-service, payment-service]}

    Svc->>Port: get_pdb_info("production", "auth-service")
    Port->>Adapter: get_pdb_info()
    Adapter->>K8s: list_namespaced_pod_disruption_budget("production")
    K8s-->>Adapter: PDB(min_available=2)
    Adapter-->>Svc: {min_available: 2}

    Svc->>Port: get_hpa_info("production", "auth-service")
    Port->>Adapter: get_hpa_info()
    Adapter->>K8s: list_namespaced_horizontal_pod_autoscaler("production")
    K8s-->>Adapter: no HPA found
    Adapter-->>Svc: None

    Svc->>Port: get_dependency_graph("production")
    Adapter-->>Svc: {}

    Svc->>Engine: compute_scenario(scenario, topology, pdb, hpa, deps)
    Note over Engine: compute_capacity_headroom(62, 3, 1) → 186%<br/>assess_risk_level(186%) → HIGH<br/>check_pdb_violation(min_available=2, proposed=1) → True<br/>estimate_latency_delta(186%) → 46.5%

    Engine-->>Svc: ImpactReport(risk=HIGH, pdb_violation=True,<br/>affected=[checkout, payment])

    Svc-->>UC: RunWhatIfSimulationResponse
    UC-->>MCP: response
    MCP-->>SRE: {target:"auth-service", risk:"HIGH",<br/>pdb_violation:true, recommendation:"Do not scale below 2..."}
```

---

## Flow 2 — Error Flows (service not found, RBAC denied, Prometheus unavailable, cluster unreachable)

```mermaid
sequenceDiagram
    actor SRE
    participant MCP as MCP Tool
    participant Adapter as VanillaAdapter
    participant K8s as Kubernetes API

    SRE->>MCP: run_what_if_simulation("unknown-svc", "production", 1)

    alt Service not found (0 replicas from K8s)
        MCP->>Adapter: get_current_replicas("production", "unknown-svc")
        Adapter->>K8s: list_deployment_for_all_namespaces()
        K8s-->>Adapter: deployment list (no match)
        Adapter-->>MCP: 0
        MCP-->>SRE: {error: null, risk:"LOW",<br/>current_replicas:0, note:"Service not found or has 0 replicas"}
    else RBAC denied (403)
        MCP->>Adapter: get_current_replicas("production", "auth-service")
        Adapter->>K8s: list_deployment_for_all_namespaces()
        K8s-->>Adapter: ApiException(status=403)
        Adapter->>Adapter: return 0 (graceful degradation)
        Adapter-->>MCP: 0
    else Prometheus unavailable (metrics fallback)
        MCP->>Adapter: get_current_cpu_utilization("production", "auth-service")
        Adapter->>K8s: Prometheus HTTP GET
        K8s-->>Adapter: ConnectionError / timeout
        Adapter->>Adapter: catch → return 0.0
        Adapter-->>MCP: 0.0
        MCP-->>SRE: {risk:"MEDIUM",<br/>note:"CPU metrics unavailable — risk estimated from replica count only"}
    else Cluster unreachable
        MCP->>Adapter: get_current_replicas("production", "auth-service")
        Adapter->>K8s: list_deployment_for_all_namespaces()
        K8s-->>Adapter: RuntimeError("connection refused")
        Adapter->>Adapter: return 0
        MCP-->>SRE: {risk:"UNKNOWN", error:"Cannot reach cluster"}
    end
```

---

## Flow 3 — Edge Cases (HPA detected, PDB violation, circular dependency, scale-up)

```mermaid
sequenceDiagram
    actor SRE
    participant MCP as MCP Tool
    participant Svc as RunWhatIfSimulationService
    participant Engine as WhatIfScenarioSimulatorService

    alt HPA compensates scale-down
        SRE->>MCP: scale auth-service 3→1 (HPA min=1, max=5)
        MCP->>Svc: simulate(command)
        Svc->>Engine: compute_scenario(hpa_detected=True)
        Engine->>Engine: check_hpa_presence → can_compensate=True
        Engine-->>Svc: ImpactReport(hpa_detected=True)
        Svc-->>MCP: {hpa_detected:true,<br/>note:"HPA may compensate for scale-down"}
    else PDB blocks change
        SRE->>MCP: scale auth-service 3→1 (PDB minAvailable=2)
        MCP->>Svc: simulate(command)
        Svc->>Engine: compute_scenario(pdb_min_available=2)
        Engine->>Engine: check_pdb_violation(proposed=1, min=2) → True
        Engine-->>Svc: ImpactReport(pdb_violation=True, risk=CRITICAL)
        Svc-->>MCP: {pdb_violation:true,<br/>recommendation:"Scaling violates PodDisruptionBudget"}
    else Circular dependency detected
        SRE->>MCP: scale auth-service (A→B→A cycle)
        MCP->>Svc: simulate(command)
        Svc->>Engine: compute_scenario(dependency_graph={A:[B], B:[A]})
        Engine->>Engine: detect_circular_dependency → True
        Engine-->>Svc: ImpactReport(circular_dependency=True)
        Svc-->>MCP: {circular_dependency:true,<br/>note:"Circular dependency A→B→A detected"}
    else Scale-up (positive impact)
        SRE->>MCP: scale auth-service 1→5
        MCP->>Svc: simulate(command)
        Svc->>Engine: compute_scenario(proposed=5, current=1)
        Engine->>Engine: proposed > current → risk=LOW<br/>_build_recommendation → "Headroom increase detected..."
        Engine-->>Svc: ImpactReport(risk=LOW)
        Svc-->>MCP: {risk:"LOW",<br/>recommendation:"Headroom increase — scaling from 1 to 5 adds capacity."}
    end
```

---

## Flow 4 — Checker Node (semantic validation + DuckDB store)

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant Svc as RunWhatIfSimulationService
    participant DuckDB as DuckDB (memory)

    Checker->>Svc: validate_simulation_response(result)

    alt PASS — all validations green
        Svc->>Svc: risk level correct ✓<br/>all dependents listed ✓<br/>HPA mentioned ✓<br/>PDB flagged ✓
        Note over Checker,DuckDB: Store simulation in DuckDB for historical comparison
        Checker->>DuckDB: INSERT INTO what_if_simulations<br/>(target, risk, proposed, computed_at)

        Checker-->>MCP: PASS — format_response with simulation result
    else FAIL — mutation language detected
        Svc->>Svc: LLM suggests "je vais appliquer le changement"
        Checker->>Checker: BLOCKED — read-only tool must never suggest mutations

        Checker-->>MCP: FAIL — "Mutation attempt blocked: this is a read-only simulation tool"
    else FAIL — incorrect risk level
        Svc->>Svc: headroom=186%, LLM says "Medium risk"
        Checker->>Checker: Verify: 186% > 150% threshold → Should be HIGH
        Checker-->>MCP: FAIL — "Risk level corrected: HIGH (headroom 186%)"
    else FAIL — missing dependent service
        Svc->>Svc: Topology returns [checkout, payment], LLM cites only [checkout]
        Checker->>Checker: Cross-check: payment-service is missing from impact
        Checker-->>MCP: FAIL — "Missing dependent service: payment-service"
    else FLAG — HPA not mentioned in response
        Svc->>Svc: HPA detected but LLM output omits it
        Checker->>Checker: HPA detected → response must mention auto-scaling
        Checker-->>MCP: FLAG — "HPA detected on auth-service: auto-scaling may compensate"
    end
```

---

## Key Points

- Computes **capacity headroom** post-scale: `current_cpu_utilization × current_replicas / proposed_replicas`
- **Risk levels**: headroom < 80% = Low, 80-150% = Medium, 150-200% = High, >200% = Critical
- **Scale-up always Low risk** — proposed_replicas > current_replicas bypasses headroom checks
- **PodDisruptionBudget** checked via K8s Policy API — scales violating `minAvailable` are flagged
- **HPA detection** via K8s Autoscaling API — if HPA `min_replicas > proposed`, auto-scaling can compensate
- **Circular dependency** detected via DFS traversal of the service dependency graph (A→B→A cycle)
- **Read-only tool** — checker node BLOCKS any response suggesting direct mutation (apply/scale/delete)
- Prometheus unavailable → risk estimated from replica count alone with caveat noted in response

## Test Coverage

| Test | File | Scenario |
|---|---|---|
| `test_3_to_1_at_62_pct_is_high` | `test_what_if_scenario_simulator_service.py` | 3→1 at 62% CPU → HIGH risk |
| `test_5_to_3_at_20_pct_is_low` | `test_what_if_scenario_simulator_service.py` | 5→3 at 20% CPU → LOW risk |
| `test_headroom_over_200_is_critical` | `test_what_if_scenario_simulator_service.py` | Headroom >200% → CRITICAL |
| `test_scale_up_always_low` | `test_what_if_scenario_simulator_service.py` | 1→5 scale-up → LOW risk |
| `test_violates_pdb_min_available_2` | `test_what_if_scenario_simulator_service.py` | PDB minAvailable=2, proposed=1 → violation |
| `test_hpa_can_compensate_scale_down` | `test_what_if_scenario_simulator_service.py` | HPA min=1, max=5, proposed=1 → compensates |
| `test_circular_dependency_detected` | `test_what_if_scenario_simulator_service.py` | A→B→A cycle → detected |
| `test_no_dependents_isolated_change` | `test_what_if_scenario_simulator_service.py` | No dependents → isolated change |
| `test_simulate_high_risk_scenario` | `test_run_what_if_simulation_service.py` | Full orchestration → HIGH, PDB violation |
| `test_vanilla_adapter_implements_port` | `test_run_what_if_simulation_mcp_and_adapter.py` | VanillaAdapter implements WhatIfSimulationPort |
| `test_get_pdb_info_returns_none_when_no_pdb` | `test_run_what_if_simulation_mcp_and_adapter.py` | No PDB → None returned |
| `test_get_hpa_info_returns_none_when_no_hpa` | `test_run_what_if_simulation_mcp_and_adapter.py` | No HPA → None returned |
| `test_get_current_replicas_returns_zero_for_unknown` | `test_run_what_if_simulation_mcp_and_adapter.py` | Unknown service → 0 replicas |
| `test_tool_returns_error_on_exception` | `test_run_what_if_simulation_mcp_and_adapter.py` | Adapter fails → error in response |
| `test_tool_returns_structured_result` | `test_run_what_if_simulation_mcp_and_adapter.py` | MCP tool returns correct JSON structure |

## Related Files

- `src/hexawyn/domain/models/simulation.py` — `ScenarioInput`, `ImpactReport`, `ServiceImpact`, `RiskLevel`
- `src/hexawyn/domain/services/simulation/what_if_scenario_simulator_service.py` — Headroom, risk, PDB, HPA, circular dependency detection
- `src/hexawyn/application/ports/driven/what_if_simulation_port.py` — `WhatIfSimulationPort` ABC + `DependentServiceData`, `PDBData`, `HPAData`
- `src/hexawyn/application/ports/driving/run_what_if_simulation/` — Command, Response, ServicePort
- `src/hexawyn/application/service/run_what_if_simulation_service.py` — Application service (orchestrates port + engine)
- `src/hexawyn/application/use_case/run_what_if_simulation/` — UseCase (thin delegation)
- `src/hexawyn/adapters/secondary/vanilla/vanilla_adapter.py` — VanillaAdapter implements WhatIfSimulationPort
- `src/hexawyn/mcp/tools/run_what_if_simulation.py` — MCP entry point
