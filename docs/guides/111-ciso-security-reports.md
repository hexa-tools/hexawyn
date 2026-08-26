# Use Case 111 — CISO Security Reports (critical CVEs + stale credentials + unauthorized access)

Three CISO-facing reports in pure business language, zero Kubernetes jargon.

## Slice 1 — Critical CVE Report
- Tool: `report_critical_vulnerabilities`
- "3 critical vulnerabilities across 2 services, oldest: 12 days."

## Slice 2 — Stale Credentials
- Tool: `report_stale_credentials`
- "8 credentials not rotated in 90 days, 3 of them critical."

## Slice 3 — Unauthorized Access
- Tool: `report_unauthorized_access`
- "52 attempts, external source, alert level HIGH."
- Alert level depends on source (internal=medium, external count>20=high).

## Related Files
24 source files · 6171 tests · `docs/use-cases/111-ciso-security-reports.md`
