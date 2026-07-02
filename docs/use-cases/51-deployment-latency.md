# Use Case 51 — Deployment Latency Comparison

## Sample Questions

- "Is the latency of payment-service increasing since the last deployment?"
- "Did the latest deployment introduce a performance regression?"
- "Compare service latency before and after the deployment 3 hours ago"
- "Is there a p99 regression after the rollout?"
- "Should we rollback based on the latency delta?"

---

One MCP tool: `deployment_latency`. Compares pre-deploy vs post-deploy OTel/p99 latencies, computes percentage deltas, returns regression verdict with rollback suggestion if p99 exceeds threshold.

### Flow 1 — Happy Path: Regression Detected

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as deployment_latency
    participant Service as DeploymentLatencyService
    participant Port as DeploymentLatencyComparisonPort
    participant Adapter as OTelDeploymentComparisonAdapter
    participant OTel as OTel/Prometheus
    participant K8s as Kubernetes API

    AI->>MCP: "Is payment-service latency regressing since deploy?"
    MCP->>Tool: deployment_latency("payment-service", 20.0)

    Tool->>Service: compare(command)
    Service->>Port: fetch_pre_deploy_latency(req)
    Port->>Adapter: OTelDeploymentComparisonAdapter
    Adapter->>OTel: p99 latency before deployment time
    OTel-->>Adapter: p50=85, p95=180, p99=210, count=5000

    Service->>Port: fetch_post_deploy_latency(req)
    Port->>Adapter: OTelDeploymentComparisonAdapter
    Adapter->>OTel: p99 latency after deployment time
    OTel-->>Adapter: p50=92, p95=310, p99=450, count=4000

    Note over Service: p99 delta = (450-210)/210*100 = +114.3%<br/>exceeds 20% threshold → REGRESSION

    Service-->>Tool: DeploymentLatencyResponse(verdict=REGRESSION, suggestion="rollback")
    Tool-->>MCP: {verdict: "regression", p99_delta_pct: 114.3, suggestion: "consider rollback"}
    MCP-->>AI: "REGRESSION detected. p99: 210ms → 450ms (+114.3%). Exceeds 20% threshold. Consider rollback to previous version."
```

### Flow 2 — No Regression

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as deployment_latency
    participant Service as DeploymentLatencyService

    AI->>Tool: deployment_latency("stable-svc")
    Tool->>Service: compare()
    Note over Service: p99 before=210ms, after=225ms (+7.1%)<br/>within 20% threshold → NO_REGRESSION

    Service-->>Tool: verdict=NO_REGRESSION
    Tool-->>AI: "No significant regression. p99: 210ms → 225ms (+7.1%) — within 20% threshold."
```

### Flow 3 — Insufficient Data

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as deployment_latency
    participant Service as DeploymentLatencyService

    AI->>Tool: deployment_latency("just-deployed-svc")
    Tool->>Service: compare()
    Note over Service: post_deploy samples=3 < min(10)<br/>INCONCLUSIVE

    Service-->>Tool: verdict=INCONCLUSIVE, suggestion="Insufficient post-deployment samples"
    Tool-->>AI: "INCONCLUSIVE: only 3 samples after deployment (min: 10). Wait for more traffic data."
```

### Flow 4 — Checker Node: Deployment Timestamp Validation

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate deployment comparison
    alt LLM says "rollback" for -150% improvement (misread sign)
        Checker-->>LLM: ❌ FAIL — sign of delta must be correct
    alt LLM claims regression but delta is within threshold
        Checker-->>LLM: ❌ FAIL — verdict must match threshold
    alt LLM omits before/after absolute values
        Checker-->>LLM: ⚠️ FLAG — p99 absolute values must be cited with deltas
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **Delta formula** — `(after - before) / before * 100` per percentile
- **Regression threshold** — p99 delta ≥ 20% → REGRESSION, suggest rollback
- **Improvement** — p99 delta ≤ -20% → IMPROVED
- **Min samples** — post-deployment must have ≥ 10 samples, otherwise INCONCLUSIVE

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_regression` | `tests/unit/test_deployment_latency.py` | ✅ |
| `test_no_regression` | `tests/unit/test_deployment_latency.py` | ✅ |
| `test_insufficient_data` | `tests/unit/test_deployment_latency.py` | ✅ |
| `test_returns_regression` | `tests/unit/test_deployment_latency_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/deployment_latency.py` — WindowLatency, DeploymentComparisonResult
- `src/hexawyn/application/ports/driven/deployment_latency_comparison_port.py` — DeploymentLatencyComparisonPort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_deployment_comparison_adapter.py` — adapter
- `src/hexawyn/mcp/tools/deployment_latency.py` — MCP tool
