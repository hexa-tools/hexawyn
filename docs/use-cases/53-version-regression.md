# Use Case 53 — Version Regression Detection

## Sample Questions

- "Have new versions of the recommendation service introduced a regression?"
- "Did v1.3 of the checkout service cause a latency regression?"
- "Compare p99 and error rate between the latest two deployments of auth-service"
- "Is the new release of the payment API slower than the previous version?"
- "Detect if the latest canary version has deteriorated from the stable baseline"

---

One MCP tool: `version_regression`. Groups OTel traces by deployment.version, compares latest version against previous baseline, flags regressions exceeding thresholds (p99 +20%, error rate +0.5%).

### Flow 1 — Happy Path: Regression Detected

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as version_regression
    participant Service as VersionRegressionService
    participant Port as VersionRegressionPort
    participant Adapter as OTelVersionRegressionAdapter
    participant OTel as OTel Trace API

    AI->>MCP: "Has recommendation-service regressed with new version?"
    MCP->>Tool: version_regression("recommendation-service", 120)

    Tool->>Service: detect(command)
    Service->>Port: fetch_baseline_metrics(req)
    Port->>Adapter: OTelVersionRegressionAdapter
    Adapter->>OTel: query deployment.version=v1.2 traces
    OTel-->>Adapter: p50=45, p95=120, p99=150, error=0.1%

    Service->>Port: fetch_current_metrics(req)
    Port->>Adapter: OTelVersionRegressionAdapter
    Adapter->>OTel: query deployment.version=v1.3 traces
    OTel-->>Adapter: p50=52, p95=250, p99=380, error=0.8%

    Note over Service: p99 delta = +153.3% > 20% → CRITICAL<br/>error delta = +0.7% > 0.5% → WARNING

    Service-->>Tool: VersionComparisonResult(verdict=regression_detected, flags=[...])
    Tool-->>MCP: {verdict: "regression_detected", p99_delta_pct: 153.3, error_delta_pct: 0.7, flags: [...]}
    MCP-->>AI: "REGRESSION in v1.3 vs v1.2:<br/>p99: 150ms → 380ms (+153.3%) CRITICAL<br/>error_rate: 0.1% → 0.8% (+0.7%) WARNING"
```

### Flow 2 — No Regression

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as version_regression
    participant Service as VersionRegressionService

    AI->>Tool: version_regression("stable-svc")
    Tool->>Service: detect()
    Note over Service: p99 delta = +7% (< 20%), error delta = +0.05% (< 0.5%)<br/>no_regression

    Service-->>Tool: verdict=no_regression, flags=[]
    Tool-->>AI: "No regression detected. v1.3 p99: 160ms vs v1.2 150ms (+7%) — within threshold."
```

### Flow 3 — Only One Version

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as version_regression
    participant Adapter as OTelVersionRegressionAdapter
    participant OTel as OTel Trace API

    AI->>Tool: version_regression("new-service")
    Tool->>Adapter: fetch metrics
    OTel-->>Adapter: only version=v1.0 found

    Adapter-->>Tool: baseline=v1.0, current=unknown
    Tool-->>AI: "Only one version (v1.0) found in traces. No comparison possible."
```

### Flow 4 — Checker Node: Validation

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response
    participant DuckDB as DuckDB

    Checker->>LLM: Validate version comparison
    alt Delta % incorrect (math error)
        Checker-->>LLM: ❌ FAIL — (current-baseline)/baseline*100
    alt LLM flags regression below threshold
        Checker-->>LLM: ❌ FAIL — threshold must be respected
    alt Rollback misinterpreted as regression
        Checker-->>LLM: ❌ FAIL — chronological order matters
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
    Checker->>DuckDB: Store version comparison for recurrence detection
```

## Key Points

- **Version grouping** — `deployment.version` OTel attribute + k8s image tag fallback
- **p99 threshold** — ≥ +20% → CRITICAL flag
- **Error threshold** — ≥ +0.5pp → WARNING flag
- **DuckDB** — stores comparisons for detecting recurrence patterns across releases

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_regression` | `tests/unit/test_version_regression.py` | ✅ |
| `test_no_regression` | `tests/unit/test_version_regression.py` | ✅ |
| `test_error_rate_regression` | `tests/unit/test_version_regression.py` | ✅ |
| `test_returns_regression` | `tests/unit/test_version_regression_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/version_regression.py` — VersionMetrics, RegressionFlag, VersionComparisonResult
- `src/hexawyn/application/ports/driven/version_regression_port.py` — VersionRegressionPort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_version_regression_adapter.py` — adapter
- `src/hexawyn/mcp/tools/version_regression.py` — MCP tool
