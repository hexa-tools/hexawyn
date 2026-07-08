# Use Case 54 — Sensitive Data Access Audit

## Sample Questions

- "Has any request accessed sensitive data like /user/*/ssn in the last 10 minutes?"
- "Who accessed the PII endpoints in the last hour?"
- "Flag any external IPs accessing /admin/pii"
- "Show me all requests to /user/*/ssn from non-internal services"
- "Audit sensitive endpoint access with allowlist filtering"

---

One MCP tool: `sensitive_data_audit`. Queries OTel traces matching sensitive URL patterns, flags requests from non-allowlisted callers as suspicious, returns alert level.

### Flow 1 — Happy Path: External Access Flagged

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant MCP as FastMCP
    participant Tool as sensitive_data_audit
    participant Service as SensitiveDataAuditService
    participant Port as ComplianceAuditPort
    participant Adapter as OTelComplianceAuditAdapter
    participant OTel as OTel Trace API

    AI->>MCP: "Who accessed /user/*/ssn?"
    MCP->>Tool: sensitive_data_audit("/user/*/ssn", 10, "user-service")

    Tool->>Service: audit(command)
    Service->>Port: fetch_access_matches(req)
    Port->>Adapter: OTelComplianceAuditAdapter
    Adapter->>OTel: query http.url ~ /user/*/ssn, last 10min
    OTel-->>Adapter: 2 matches (192.168.1.45 + 203.0.113.5)

    Note over Service: user-service in allowlist → unflagged<br/>unknown not in allowlist → flagged<br/>1 flagged → alert_level=MEDIUM

    Service-->>Tool: SensitiveAuditResult(flagged=[unknown], unflagged=[user-service])
    Tool-->>MCP: {total_matches: 2, flagged: [{ip: "203.0.113.5", url: "/user/456/ssn"}], alert_level: "medium"}
    MCP-->>AI: "2 accesses to /user/*/ssn. 1 FLAGGED: 203.0.113.5 (unknown) accessed /user/456/ssn at 10:28Z. 1 internal (user-service) — allowed."
```

### Flow 2 — All Allowlisted

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as sensitive_data_audit
    participant Service as SensitiveDataAuditService

    AI->>Tool: sensitive_data_audit("/user/*/ssn", 10, "user-service,audit-svc")
    Tool->>Service: audit()
    Note over Service: All matches from allowlisted services<br/>flagged=0 → alert_level=NONE

    Service-->>Tool: flagged=[], alert_level=NONE
    Tool-->>AI: "3 accesses — all from allowlisted services. No suspicious activity."
```

### Flow 3 — No Matches

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as sensitive_data_audit
    participant Service as SensitiveDataAuditService

    AI->>Tool: sensitive_data_audit("/ghost/*", 10)
    Tool->>Service: audit()
    Note over Service: matches=[], total=0

    Service-->>Tool: alert_level=NONE
    Tool-->>AI: "No requests matched /ghost/* in the last 10 minutes."
```

### Flow 4 — Checker Node: Alert Level Validation

```mermaid
sequenceDiagram
    participant Checker as Checker Node
    participant LLM as LLM Response

    Checker->>LLM: Validate audit claims
    alt LLM says "HIGH alert" for 2 flagged (threshold >5)
        Checker-->>LLM: ❌ FAIL — alert_level must match count (HIGH >5, MEDIUM >0)
    alt LLM reports caller as "external" when IP is internal
        Checker-->>LLM: ⚠️ FLAG — verify caller_ip is truly external vs allowlist
    alt LLM omits user_id from span attribute
        Checker-->>LLM: ⚠️ FLAG — user_id should be surfaced if available in span
    else All checks pass
        Checker-->>LLM: ✅ PASS
    end
```

## Key Points

- **Allowlist** — expected callers excluded from flagged results
- **Alert level** — HIGH (>5 flagged), MEDIUM (>0), NONE (0)
- **Pattern matching** — wildcard pattern support (e.g. /user/*/ssn)
- **Caller attribution** — caller_ip, caller_service, user_id from OTel attributes

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_flags_external` | `tests/unit/test_sensitive_data_audit.py` | ✅ |
| `test_allowlisted_excluded` | `tests/unit/test_sensitive_data_audit.py` | ✅ |
| `test_no_matches` | `tests/unit/test_sensitive_data_audit.py` | ✅ |
| `test_returns_flagged` | `tests/unit/test_sensitive_data_audit_tool.py` | ✅ |

## Related Files

- `src/hexawyn/domain/models/sensitive_data_audit.py` — AccessMatch, SensitiveAuditResult
- `src/hexawyn/application/ports/driven/compliance_audit_port.py` — ComplianceAuditPort ABC
- `src/hexawyn/adapters/secondary/gitops/otel_compliance_audit_adapter.py` — adapter
- `src/hexawyn/mcp/tools/sensitive_data_audit.py` — MCP tool
