# Use Case 111 — CISO Security Reports (critical CVEs + stale credentials + unauthorized access)

Three CISO-facing reports in pure business language, zero Kubernetes jargon.

## Slice 1 — Critical CVE Report
- Tool: `report_critical_vulnerabilities`
- "3 vulnérabilités critiques sur 2 services, plus ancienne : 12 jours."

## Slice 2 — Stale Credentials
- Tool: `report_stale_credentials`
- "8 identifiants non renouvelés depuis 90 jours dont 3 critiques."

## Slice 3 — Unauthorized Access
- Tool: `report_unauthorized_access`
- "52 tentatives, source externe, niveau d'alerte ÉLEVÉ."
- Alert level depends on source (internal=medium, external count>20=high).

## Related Files
24 fichiers source · 6171 tests · `docs/use-cases/111-ciso-security-reports.md`
