# Use Case 114 — Cross-Cluster Incident Correlation

Detects whether the same failure pattern is happening simultaneously across
multiple clusters: same ImagePullBackOff on payment-service in prod-eu and
prod-us, cascading onset (US → EU 10 min later), or NodePressure on all clusters.

## Sample Questions

- "Is the same issue affecting multiple clusters simultaneously?"
- "Is this a global infrastructure problem or isolated to one cluster?"
- "Are all our clusters having the same ImagePullBackOff error?"
- "Did the incident cascade from US to EU?"

## Key Points

- **Failure pattern matching** across clusters within a configurable time window (default ±30 min)
- **Scope classification**: isolated (1) / regional (2+) / global (all)
- **Cascading detection**: onsets staggered within the window
- **Shared dependency** surfaced as likely root cause (e.g. container registry)
- **Suggestion** = actionnable root-cause hypothesis

## Related Files (10)

`src/hexawyn/domain/models/cross_cluster_correlation.py` · `src/hexawyn/domain/services/cross_cluster_correlation/cross_cluster_correlation_service.py` · `src/hexawyn/application/ports/driven/cross_cluster_incident_port.py` · `src/hexawyn/application/ports/driving/detect_cross_cluster_incident/` · `src/hexawyn/application/service/detect_cross_cluster_incident_service.py` · `src/hexawyn/application/use_case/detect_cross_cluster_incident/detect_cross_cluster_incident_use_case.py` · `src/hexawyn/adapters/secondary/gitops/cross_cluster_incident_adapter.py` · `src/hexawyn/adapters/secondary/gitops/cross_cluster_incident_source.py` · `src/hexawyn/mcp/tools/detect_cross_cluster_incident.py` · `src/hexawyn/mcp/server.py`
