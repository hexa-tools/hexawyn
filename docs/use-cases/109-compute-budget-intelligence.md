# Use Case 109 — Budget Intelligence (Business Impact Slice 3)

Monitors projected cloud spend against a configured monthly budget
(`business.cloud_budget_monthly`), alerts on overruns, and suggests
optimization actions.

## Key Points

- **Alert triggered when projected_spend > budget_monthly**.
- **Without `cloud_budget_monthly`** no alert is generated.
- **Recommendations** are deterministic (verify workloads, optimize CPU, reschedule non-critical).
- Output in executive language: nothing technical, nothing Kubernetes.

## Related Files (9)

`src/hexawyn/domain/models/budget_intelligence.py` · `src/hexawyn/domain/services/budget_intelligence/budget_intelligence_service.py` · `src/hexawyn/application/ports/driven/budget_intelligence_port.py` · `src/hexawyn/application/ports/driving/compute_budget_intelligence/` · `src/hexawyn/application/service/compute_budget_intelligence_service.py` · `src/hexawyn/application/use_case/compute_budget_intelligence/compute_budget_intelligence_use_case.py` · `src/hexawyn/adapters/secondary/gitops/budget_intelligence_adapter.py` · `src/hexawyn/adapters/secondary/gitops/budget_intelligence_source.py` · `src/hexawyn/mcp/tools/compute_budget_intelligence.py` · `src/hexawyn/mcp/server.py`
