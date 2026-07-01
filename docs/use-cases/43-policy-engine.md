# Use Case 43 — Policy Engine Detection (Kyverno / OPA Gatekeeper)

## Sample Questions

- "Why was my deployment denied by Kyverno?"
- "What policy violations exist in the production namespace?"
- "Does my cluster use Kyverno or OPA Gatekeeper?"
- "Which policies are in enforce vs audit mode?"
- "Explain why this pod violates the security policy"
- "Are there any non-compliant resources in my cluster?"
- "What policies are blocking root containers?"

---

Six MCP tools for policy engines: `policy_detect` (auto-detects Kyverno vs Gatekeeper), `policy_list` (all policies with action and violations), `policy_get` (policy detail), `policy_violations_list` (current violations with severity), `policy_explain_denial` (natural-language explanation + fix suggestion), `policy_audit` (global compliance report per namespace). All read-only.

### Flow 1 — Happy Path: Detect + List Policies

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as policy_detect / policy_list
    participant UseCase as PolicyDetectUseCase
    participant Service as PolicyDetectService
    participant Port as PolicyPort (ABC)
    participant Adapter as PolicyDetector
    participant K8s as Kubernetes API

    AI->>MCP: Call "policy_detect"
    MCP->>Tool: @mcp.tool() dispatch

    Tool->>UseCase: execute(PolicyDetectCommand())
    UseCase->>Service: detect(command)
    Service->>Port: detect_engine()

    Port->>Adapter: PolicyDetector
    Adapter->>K8s: Check Kyverno CRDs (kyverno.io)
    K8s-->>Adapter: ✅ CRD found

    Note over Adapter: Kyverno v1.13.0 detected<br/>8 policies: 5 enforce, 3 audit

    Adapter-->>Port: PolicyDetectionResult(engine=KYVERNO, total_policies=8)
    Port-->>Service: result
    Service-->>UseCase: PolicyDetectResponse(engine="kyverno", total_policies=8)
    UseCase-->>Tool: response
    Tool-->>MCP: {engine: "kyverno", total_policies: 8, total_violations: 12}
    MCP-->>AI: "Kyverno v1.13.0 detected — 8 policies, 12 violations (4 high severity)."
```

### Flow 2 — Enforcement Denial Explained

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as policy_explain_denial
    participant Service as PolicyExplainDenialService
    participant Port as PolicyPort
    participant Adapter as KyvernoAdapter
    participant K8s as Kubernetes API

    AI->>Tool: Call "policy_explain_denial"<br/>resource_kind="Deployment"<br/>resource_name="nginx"<br/>namespace="default"

    Tool->>Service: explain(command)
    Service->>Port: explain_denial(...)
    Port->>Adapter: explain_denial("Deployment", "nginx", "default")

    Adapter->>K8s: GET .../policyreports?resource=nginx
    K8s-->>Adapter: PolicyReport with violation

    Note over Adapter: Map to PolicyDenialExplanation<br/>policy=require-run-as-non-root<br/>rule=check-containers<br/>human_explanation: "Your deployment runs as root..."<br/>fix_suggestion: "Set securityContext.runAsNonRoot to true"

    Adapter-->>Port: PolicyDenialExplanation(human_explanation, fix_suggestion)
    Port-->>Service: explanation
    Service-->>Tool: response
    Tool-->>MCP: {policy_name: "require-run-as-non-root", human_explanation: "...", fix_suggestion: "..."}
    MCP-->>AI: "nginx deployment denied by 'require-run-as-non-root'.<br/>The 'check-containers' rule blocks root containers.<br/>Fix: set securityContext.runAsNonRoot to true."
```

### Flow 3 — Audit Violation (Non-Blocking)

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as policy_violations_list
    participant Adapter as KyvernoAdapter
    participant K8s as Kubernetes API

    AI->>Tool: Call "policy_violations_list" namespace="staging"
    Tool->>Adapter: list_violations(namespace="staging")
    Adapter->>K8s: GET .../policyreports?namespace=staging
    K8s-->>Adapter: PolicyReport — AUDIT violation

    Note over Adapter: action=AUDIT → non-blocking<br/>severity=MEDIUM<br/>resource=nginx-deployment

    Adapter-->>Tool: PolicyViolation(action=AUDIT, severity=MEDIUM)
    Tool-->>AI: "1 violation in staging (AUDIT only, non-blocking).<br/>nginx-deployment violates require-run-as-non-root (MEDIUM)."
```

### Flow 4 — No Policy Engine Found

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as policy_detect
    participant Adapter as PolicyDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "policy_detect"
    Tool->>Adapter: detect_engine()
    Adapter->>K8s: Check Kyverno CRDs
    K8s-->>Adapter: ❌ Not found
    Adapter->>K8s: Check Gatekeeper CRDs
    K8s-->>Adapter: ❌ Not found

    Note over Adapter: PolicyEngineNotFoundError<br/>"No policy engine detected"

    Adapter-->>Tool: PolicyDetectionResult(engine=NONE)
    Tool-->>AI: "No policy engine detected.<br/>Install Kyverno or OPA Gatekeeper: https://kyverno.io"
```

## Key Points

- **Enforce vs audit** — `ENFORCE` blocks resources, `AUDIT` only logs; distinction critical for devs
- **Denial explanation** — `policy_explain_denial` always returns `human_explanation` + `fix_suggestion`
- **Violation severity** — HIGH/MEDIUM/LOW/INFO for prioritization
- **Multi-engine** — detects Kyverno (ClusterPolicy, Policy) vs Gatekeeper (ConstraintTemplate, Constraint)
- **Compliance audit** — `policy_audit` aggregates violations per namespace

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_tool_returns_detection` | `tests/unit/test_policy_tools.py` | ✅ |
| `test_tool_returns_policies` | `tests/unit/test_policy_tools.py` | ✅ |
| `test_tool_returns_violations` | `tests/unit/test_policy_tools.py` | ✅ |
| `test_tool_returns_explanation` | `tests/unit/test_policy_tools.py` | ✅ |
| `test_tool_returns_audit` | `tests/unit/test_policy_tools.py` | ✅ |
| `test_all_policy_tools_have_register` | `tests/unit/test_policy_tools.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/policy.py` — Policy, PolicyViolation, PolicyDenialExplanation, PolicyDetectionResult
- `src/hexawyn/domain/errors.py` — PolicyEngineNotFoundError
- `src/hexawyn/application/ports/driven/policy_port.py` — PolicyPort ABC
- `src/hexawyn/adapters/secondary/gitops/policy_detector.py` — PolicyDetector
- `src/hexawyn/mcp/tools/policy_detect.py` — detect tool
- `src/hexawyn/mcp/tools/policy_list.py` — list tool
- `src/hexawyn/mcp/tools/policy_get.py` — get tool
- `src/hexawyn/mcp/tools/policy_violations_list.py` — violations tool
- `src/hexawyn/mcp/tools/policy_explain_denial.py` — explain denial tool
- `src/hexawyn/mcp/tools/policy_audit.py` — audit tool
