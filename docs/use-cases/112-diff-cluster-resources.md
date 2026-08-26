# Use Case 112 — Multi-Cluster Resource Diff (staging vs production)

Compares resource inventories between two clusters: finds resources present
in staging but not yet promoted to production, detects version mismatches,
flags secrets requiring manual promotion, and generates a promotion checklist.

## Sample Questions

- "Show me all resources that exist in staging but not in production."
- "What is missing or not yet promoted before the release?"
- "Are there any version mismatches between staging and production?"
- "What is my promotion checklist for the next deployment?"
- "Do I have any secrets I need to promote manually?"

## Key Points

- **Missing resources** = staging has it, prod doesn't → `never_promoted`
- **Version mismatches** = image tag or replica count differs
- **Secrets** → flagged `secret_manual` (must be promoted manually)
- **Promotion checklist** = `ready_to_promote` + `requires_review` (version conflicts)
- **Prod-only resources** → listed separately as `informational`

## Related Files (10)

`src/hexawyn/domain/models/cluster_diff.py` · `src/hexawyn/domain/services/cluster_diff/cluster_diff_service.py` · `src/hexawyn/application/ports/driven/cluster_diff_port.py` · `src/hexawyn/application/ports/driving/diff_cluster_resources/` · `src/hexawyn/application/service/diff_cluster_resources_service.py` · `src/hexawyn/application/use_case/diff_cluster_resources/diff_cluster_resources_use_case.py` · `src/hexawyn/adapters/secondary/gitops/cluster_diff_adapter.py` · `src/hexawyn/adapters/secondary/gitops/cluster_diff_source.py` · `src/hexawyn/mcp/tools/diff_cluster_resources.py` · `src/hexawyn/mcp/server.py`
