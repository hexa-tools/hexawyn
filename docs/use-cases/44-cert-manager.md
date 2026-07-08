# Use Case 44 — Cert-Manager Certificate Monitoring

## Sample Questions

- "Are there any TLS certificates expiring in the next 30 days?"
- "Why was the payments-api certificate not renewed?"
- "What is the status of all my Cert-Manager certificates?"
- "Are all my Let's Encrypt certificates valid?"
- "Are there any failed ACME challenges in my cluster?"
- "Which certificate expires the soonest?"
- "Is automatic renewal working correctly?"

---

Eight MCP tools for Cert-Manager: `certs_detect`, `certs_list`, `certs_get`, `certs_status_explain`, `certs_issuers_list`, `certs_issuer_get`, `certs_challenges_list`, `certs_requests_list`. All read-only — renewal is never triggered.

### Flow 1 — Happy Path: Detect + List + Alert Expiring

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP Server
    participant Tool as certs_detect / certs_list
    participant Port as CertManagerPort (ABC)
    participant Adapter as CertManagerDetector
    participant K8s as Kubernetes API

    AI->>MCP: Call "certs_detect"
    MCP->>Tool: dispatch
    Tool->>Port: detect()
    Port->>Adapter: CertManagerDetector
    Adapter->>K8s: Check cert-manager CRDs
    K8s-->>Adapter: v1.16.2 found, 15 certs

    Adapter-->>Port: CertManagerDetectionResult(total_certs=15, expiring_soon=3)
    Port-->>Tool: result
    Tool-->>MCP: {installed: true, expiring_soon: 3, failed_certs: 1}
    MCP-->>AI: "Cert-Manager v1.16.2 installed. 15 certs: 12 ready, 3 expiring within 30 days, 1 failed."
```

### Flow 2 — Certificate Expired / Renewal Failed

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as certs_get + certs_status_explain
    participant Adapter as CertManagerDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "certs_get" name="payments-tls" namespace="production"
    Tool->>Adapter: get_certificate("payments-tls", "production")
    Adapter->>K8s: GET .../certificates/payments-tls
    K8s-->>Adapter: Certificate NOT_READY

    Note over Adapter: status=NOT_READY<br/>message="ACME challenge failed: DNS propagation timeout"<br/>auto_renew=False

    Adapter-->>Tool: Certificate(NOT_READY, message=...)
    Tool-->>AI: "payments-tls is NOT_READY.<br/>Cause: ACME challenge failed — DNS propagation timeout.<br/>Auto-renew is disabled. Manual renewal needed."
```

### Flow 3 — ACME Challenge in Error

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as certs_challenges_list
    participant Adapter as CertManagerDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "certs_challenges_list" namespace="production"
    Tool->>Adapter: list_challenges(namespace="production")
    Adapter->>K8s: GET .../challenges?namespace=production
    K8s-->>Adapter: Challenge errored

    Note over Adapter: type=dns-01, domain=payments.example.com<br/>state=errored, reason="DNS record not propagated"

    Adapter-->>Tool: AcmeChallenge(state="errored", reason=...)
    Tool-->>AI: "1 ACME challenge in error: payments.example.com<br/>dns-01 failed — DNS record not propagated."
```

### Flow 4 — Cert-Manager Not Installed

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as certs_detect
    participant Adapter as CertManagerDetector
    participant K8s as Kubernetes API

    AI->>Tool: Call "certs_detect"
    Tool->>Adapter: detect()
    Adapter->>K8s: Check cert-manager.io CRDs
    K8s-->>Adapter: ❌ CRD not found

    Note over Adapter: CertManagerNotFoundError

    Adapter-->>Tool: CertManagerDetectionResult(installed=False)
    Tool-->>AI: "Cert-Manager not detected. Install: https://cert-manager.io/docs/installation/"
```

## Key Points

- **Expiration alerts** — `days_until_expiry` and `expiring_soon` count (threshold: 30 days)
- **ACME challenge tracking** — `certs_challenges_list` shows pending/errored challenges with reasons
- **Issuer types** — Let's Encrypt, Vault, self-signed, CA, Venafi auto-detected
- **Read-only** — renewal is never triggered; operators retain control via `kubectl cert-manager renew`
- **Auto-renew status** — `auto_renew` field flags disabled automatic renewal

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_tool_returns_detection` | `tests/unit/test_certs_tools.py` | ✅ |
| `test_tool_returns_certs` | `tests/unit/test_certs_tools.py` | ✅ |
| `test_tool_returns_detail` | `tests/unit/test_certs_tools.py` | ✅ |
| `test_all_certs_tools_have_register` | `tests/unit/test_certs_tools.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/certificates.py` — Certificate, CertificateIssuer, AcmeChallenge, CertManagerDetectionResult
- `src/hexawyn/domain/errors.py` — CertManagerNotFoundError
- `src/hexawyn/application/ports/driven/cert_manager_port.py` — CertManagerPort ABC
- `src/hexawyn/adapters/secondary/gitops/cert_manager_detector.py` — CertManagerDetector
- `src/hexawyn/mcp/tools/certs_*.py` — 8 tools
