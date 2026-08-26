# Use Case 39 — Live Dependency Map

## Sample Questions

- "Generate a live dependency map of all services currently running in the cluster — show me which services call which, and highlight single points of failure."
- "Which services would take down the most other services if they went down right now?"
- "Can you draw me a call graph of the production namespace and flag anything risky?"
- "How much would it cost us in downtime if auth-service failed — how many services depend on it?"
- "List all single points of failure in the checkout namespace based on current service topology."
- "Are there any circular dependencies between our microservices?"

---

Discovers every Service in the cluster (or a single namespace), infers caller→callee edges from Istio `VirtualService` CRDs with a graceful fallback to `NetworkPolicy` ingress rules when the mesh is not installed, and builds a directed dependency graph. Flags services with `replicas == 1` that other services depend on as single points of failure, detects cycles via DFS, marks orphan and `ExternalName` nodes, and exports both a structured graph and a ready-to-render Mermaid diagram.

---

## Flow 1 — Happy Path (api-gateway, auth-service SPOF, payment-service)

```mermaid
sequenceDiagram
    actor Engineer
    participant MCP as MCP Tool<br/>(live_topology_mapper)
    participant UC as LiveTopologyMapperUseCase
    participant Svc as LiveTopologyMapperService
    participant K8sPort as KubernetesTopologyPort (ABC)
    participant IstioPort as IstioTopologyPort (ABC)
    participant K8sAdapter as KubernetesTopologyAdapter
    participant IstioAdapter as IstioTopologyAdapter
    participant K8s as Kubernetes API
    participant Istio as Istio VirtualService CRDs
    participant Engine as TopologyGraphBuilderService
    participant Exporter as topology exporter
    participant DuckDB as DuckDB (topology_snapshots)

    Engineer->>MCP: live_topology_mapper(namespace=None)
    MCP->>UC: execute(LiveTopologyMapperCommand)
    UC->>Svc: map_topology(command)

    Svc->>K8sPort: list_services(None)
    K8sPort->>K8sAdapter: list_services()
    K8sAdapter->>K8s: CoreV1Api.list_service_for_all_namespaces()<br/>+ AppsV1Api.list_deployment_for_all_namespaces()
    K8s-->>K8sAdapter: api-gateway(3), auth-service(1), payment-service(2)
    K8sAdapter-->>Svc: [ServiceRecordData, ...]

    Svc->>IstioPort: get_virtual_service_edges(None)
    IstioPort->>IstioAdapter: get_virtual_service_edges()
    IstioAdapter->>Istio: CustomObjectsApi.list_cluster_custom_object<br/>(networking.istio.io/v1beta1/virtualservices)
    Istio-->>IstioAdapter: no VirtualServices found
    IstioAdapter-->>Svc: None (mesh not installed)

    Svc->>K8sPort: get_network_policy_edges(None)
    K8sPort->>K8sAdapter: get_network_policy_edges()
    K8sAdapter->>K8s: NetworkingV1Api.list_network_policy_for_all_namespaces()
    K8s-->>K8sAdapter: NetworkPolicies (pod_selector labels)
    K8sAdapter-->>Svc: [api-gateway→auth-service,<br/>api-gateway→payment-service,<br/>payment-service→auth-service]

    Svc->>Engine: build_graph(services, edges,<br/>inference_source=NETWORK_POLICY)
    Note over Engine: in_degree(auth-service)=2, replicas=1 → is_spof=True<br/>DFS cycle scan → no cycles found

    Engine-->>Svc: DependencyGraph(nodes=3, spof=[auth-service])

    Svc->>Exporter: to_mermaid(graph) / to_structured_dict(graph)
    Exporter-->>Svc: mermaid_diagram, structured export

    Svc->>DuckDB: save_snapshot("prod-cluster", export)
    Note over DuckDB: best-effort — a storage failure never blocks the response

    Svc-->>UC: LiveTopologyMapperResponse
    UC-->>MCP: response
    MCP-->>Engineer: {nodes: 3, single_points_of_failure: ["auth-service"],<br/>inference_source: "NETWORK_POLICY", mermaid_diagram: "graph TD..."}
```

---

## Flow 2 — Error Flows (RBAC denied, cluster unreachable, Istio CRD missing, DuckDB unavailable)

```mermaid
sequenceDiagram
    actor Engineer
    participant MCP as MCP Tool
    participant K8sAdapter as KubernetesTopologyAdapter
    participant IstioAdapter as IstioTopologyAdapter
    participant K8s as Kubernetes API

    Engineer->>MCP: live_topology_mapper(namespace="production")

    alt RBAC denied listing Services
        MCP->>K8sAdapter: list_services("production")
        K8sAdapter->>K8s: CoreV1Api.list_namespaced_service()
        K8s-->>K8sAdapter: ApiException(403 Forbidden)
        K8sAdapter->>K8sAdapter: catch → return []
        K8sAdapter-->>MCP: [] (graceful degradation)
    else Cluster unreachable
        MCP->>K8sAdapter: list_services("production")
        K8sAdapter->>K8s: connection timeout
        K8sAdapter->>K8sAdapter: catch → return []
        MCP-->>Engineer: {nodes: [], error: null, note: "no services discovered"}
    else Istio CRD not installed
        MCP->>IstioAdapter: get_virtual_service_edges("production")
        IstioAdapter->>K8s: CustomObjectsApi.list_namespaced_custom_object<br/>(networking.istio.io/v1beta1)
        K8s-->>IstioAdapter: ApiException(404 — CRD not found)
        IstioAdapter->>IstioAdapter: catch → return None
        MCP-->>Engineer: falls back to NetworkPolicy inference<br/>inference_source="NETWORK_POLICY"
    else Snapshot storage unavailable
        MCP->>MCP: build_topology_snapshot_adapter() raises DuckDBUnavailableError
        MCP->>MCP: catch → snapshot_port=None, continue without history
        MCP-->>Engineer: response returned normally (persistence skipped)
    end
```

---

## Flow 3 — Edge Cases (SPOF, orphan, cycle, truncation, ExternalName)

```mermaid
sequenceDiagram
    actor Engineer
    participant Svc as LiveTopologyMapperService
    participant Engine as TopologyGraphBuilderService

    alt 5-service chain a→b→c→d→e
        Svc->>Engine: build_graph(5 services, 4 chained edges)
        Engine-->>Svc: DependencyGraph(nodes=5, edges=4, cycles=[])
    else auth-service SPOF (replicas=1, 3 dependents)
        Svc->>Engine: build_graph(services, edges)
        Engine->>Engine: in_degree(auth-service)=3 AND replicas=1 → is_spof=True
        Engine-->>Svc: single_points_of_failure=["auth-service"]
    else Isolated service, no callers or callees
        Svc->>Engine: build_graph(services incl. reporting-service)
        Engine->>Engine: in_degree=0 AND out_degree=0 → NodeType.ORPHAN
        Engine-->>Svc: orphan_nodes=["reporting-service"]
    else Circular dependency a→b→a
        Svc->>Engine: build_graph(services, [a→b, b→a])
        Engine->>Engine: DFS visiting-set revisits a → cycle recorded
        Engine-->>Svc: cycles=[["a","b","a"]]
    else Cluster with >200 services, no namespace scope
        Svc->>Engine: build_graph(250 services, namespace_scope=None)
        Engine->>Engine: truncate to 200, sorted by name
        Engine-->>Svc: truncated=True, len(nodes)=200
    else ExternalName service (stripe-external)
        Svc->>Engine: build_graph(services incl. stripe-external)
        Engine->>Engine: service.is_external=True → NodeType.EXTERNAL
        Engine-->>Svc: node stripe-external marked EXTERNAL
    end
```

---

## Flow 4 — Checker Node (semantic validation, hexa-control-plane)

```mermaid
sequenceDiagram
    participant Checker as Checker Node<br/>(hexa-control-plane)
    participant Svc as LiveTopologyMapperService
    participant DuckDB as DuckDB (topology_snapshots)

    Checker->>Svc: validate_topology_response(result)

    alt PASS — all validations green
        Svc->>Svc: SPOF flagged ✓ · cycles noted ✓<br/>all discovered nodes present ✓ · inference source explicit ✓
        Checker-->>MCP: PASS — format_response with graph + mermaid diagram
    else FAIL — SPOF not flagged
        Svc->>Svc: auth-service replicas=1, in_degree=3, LLM omits SPOF
        Checker->>Checker: (replicas==1 AND in_degree>0) must be in single_points_of_failure
        Checker-->>MCP: FAIL — "Missing SPOF: auth-service"
    else FLAG — cycle not mentioned
        Svc->>Svc: cycles=[["a","b","a"]] returned, LLM presents graph without noting it
        Checker->>Checker: DFS over returned edges confirms cycle exists
        Checker-->>MCP: FLAG — "Circular dependency a→b→a not mentioned"
    else FAIL — orphan node omitted
        Svc->>Svc: reporting-service discovered but LLM excludes it from graph
        Checker->>Checker: cross-check discovered services vs response.nodes
        Checker-->>MCP: FAIL — "Missing node: reporting-service"
    else FLAG — inference source not explicit
        Svc->>Svc: mesh absent, LLM presents "live topology" without naming NetworkPolicy inference
        Checker->>Checker: response.inference_source must be surfaced to the user
        Checker-->>MCP: FLAG — "Inference source (NetworkPolicy) not disclosed"
    else FAIL — edge direction reversed
        Svc->>Svc: NetworkPolicy ingress says api-gateway→auth-service,<br/>LLM presents auth-service→api-gateway
        Checker->>Checker: verify edge.caller/callee against ingress/egress direction
        Checker-->>MCP: FAIL — "Edge direction reversed: api-gateway→auth-service"
    else FLAG — topology changed since last snapshot
        Svc->>DuckDB: save_snapshot("prod-cluster", export)
        Checker->>DuckDB: compare against last stored snapshot
        DuckDB-->>Checker: last week auth-service had replicas=2 (not SPOF)
        Checker-->>MCP: FLAG — "New SPOF introduced: auth-service (2→1 replicas)"
    end
```

---

## Key Points

- **SPOF rule** — `replicas == 1 AND in_degree > 0`, computed entirely in the domain engine (`TopologyGraphBuilderService`) with zero Kubernetes dependency.
- **Two independent driven ports** (`KubernetesTopologyPort`, `IstioTopologyPort`, Interface Segregation) — Istio is tried first; any failure (CRD missing, RBAC denied, unreachable) returns `None` and the service transparently falls back to NetworkPolicy inference. The active source is always recorded in `inference_source`, never left implicit.
- **Istio edge inference is a documented best-effort heuristic** — only `VirtualService` HTTP match rules with an explicit `sourceLabels.app` produce an edge; ambiguous rules are skipped rather than guessing direction. Prometheus-based mesh telemetry (`istio_requests_total`) is a future extension point, not implemented here.
- **Truncation** — graphs over 200 services are truncated (stable, sorted by name) unless a `namespace_scope` is given, matching the ">200 services" edge case.
- **DuckDB snapshot persistence is save-only and best-effort** — a storage failure never blocks the topology response. Historical SPOF-change comparison ("new SPOF introduced") is a semantic-checker concern in `hexa-control-plane`, not this repository.

## Test Coverage

| Test | File | Scenario |
|---|---|---|
| `test_single_points_of_failure_lists_spof_names` | `tests/unit/test_dependency_graph.py` | SPOF derived from node flags |
| `test_orphan_nodes_lists_orphan_names` | `tests/unit/test_dependency_graph.py` | Orphan derived from node type |
| `test_five_service_chain_returns_correct_graph` | `tests/unit/topology/test_mapper.py` | 5-service chain a→b→c→d→e |
| `test_replica_one_with_three_dependents_is_flagged_spof` | `tests/unit/topology/test_mapper.py` | auth-service SPOF (ticket test data) |
| `test_isolated_service_with_no_callers_or_callees_is_orphan` | `tests/unit/topology/test_mapper.py` | Orphan node |
| `test_circular_dependency_is_detected` | `tests/unit/topology/test_mapper.py` | a→b→a cycle detected |
| `test_external_name_service_is_marked_external` | `tests/unit/topology/test_mapper.py` | ExternalName → EXTERNAL |
| `test_truncates_when_over_200_services_and_no_namespace_scope` | `tests/unit/topology/test_mapper.py` | >200 services truncation |
| `test_namespace_scope_prevents_truncation_even_over_200` | `tests/unit/topology/test_mapper.py` | Namespace scope bypasses truncation |
| `test_edge_referencing_deleted_service_is_dropped` | `tests/unit/topology/test_mapper.py` | Deleted-service dangling edge dropped |
| `test_spof_node_gets_styled_class` | `tests/unit/topology/test_exporter.py` | Mermaid SPOF styling |
| `test_shape_matches_graph` | `tests/unit/topology/test_exporter.py` | Structured export shape |
| `test_builds_edge_from_pod_selector_labels` | `tests/unit/test_kubernetes_topology_adapter.py` | NetworkPolicy → edge inference |
| `test_returns_empty_list_when_service_listing_fails` | `tests/unit/test_kubernetes_topology_adapter.py` | RBAC denied → graceful `[]` |
| `test_builds_edge_from_source_labels` | `tests/unit/test_istio_topology_adapter.py` | VirtualService sourceLabels → edge |
| `test_returns_none_when_crd_not_installed` | `tests/unit/test_istio_topology_adapter.py` | Mesh absent → `None` fallback signal |
| `test_uses_istio_edges_when_available` | `tests/unit/test_live_topology_mapper_service.py` | Istio preferred over NetworkPolicy |
| `test_falls_back_to_network_policy_when_istio_unavailable` | `tests/unit/test_live_topology_mapper_service.py` | Fallback + inference_source |
| `test_saves_snapshot_when_snapshot_port_provided` | `tests/unit/test_live_topology_mapper_service.py` | DuckDB snapshot save wiring |
| `test_save_snapshot_failure_is_swallowed` | `tests/unit/test_topology_snapshot_repository.py` | Best-effort, non-blocking persistence |
| `test_tool_returns_structured_result` | `tests/unit/test_live_topology_mapper_mcp_tool.py` | Full MCP tool orchestration |
| `test_snapshot_adapter_failure_does_not_break_tool` | `tests/unit/test_live_topology_mapper_mcp_tool.py` | DuckDB unavailable → tool still succeeds |

## Related Files

- `src/hexawyn/domain/models/dependency_graph.py` — `NodeType`, `InferenceSource`, `ServiceNode`, `DependencyEdge`, `DependencyGraph`
- `src/hexawyn/domain/services/topology/mapper.py` — `TopologyGraphBuilderService` (SPOF, orphan, cycle, truncation)
- `src/hexawyn/domain/services/topology/exporter.py` — `to_mermaid`, `to_structured_dict`
- `src/hexawyn/application/ports/driven/kubernetes_topology_port.py` — `KubernetesTopologyPort`
- `src/hexawyn/application/ports/driven/istio_topology_port.py` — `IstioTopologyPort`
- `src/hexawyn/application/ports/driven/topology_snapshot_port.py` — `TopologySnapshotPort`
- `src/hexawyn/application/ports/driving/live_topology_mapper/` — Command, Response, ServicePort
- `src/hexawyn/application/service/live_topology_mapper_service.py` — Application service (orchestrates both ports + engine)
- `src/hexawyn/application/use_case/live_topology_mapper/live_topology_mapper_use_case.py` — UseCase (thin delegation)
- `src/hexawyn/adapters/secondary/kubernetes_topology_adapter.py` — `KubernetesTopologyAdapter`
- `src/hexawyn/adapters/secondary/istio_topology_adapter.py` — `IstioTopologyAdapter`
- `src/hexawyn/infrastructure/memory/topology_snapshot_repository.py` — `TopologySnapshotRepository`
- `src/hexawyn/mcp/tools/live_topology_mapper.py` — MCP entry point
