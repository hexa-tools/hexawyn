# Use Case 113 — Multi-Cluster Health Comparison (prod-eu vs prod-us)

Compares the health of two clusters side-by-side: failing pods, CPU/memory
utilisation, active incidents, health delta, and identifies which cluster is
in worse shape. Support for maintenance mode and unreachable clusters.

## Sample Questions

- "Compare the health of cluster prod-eu vs prod-us."
- "Which cluster has more failing pods — EU or US?"
- "Is prod-eu in worse shape than prod-us during this incident?"
- "What are the health deltas between our two production regions?"

## Key Points

- **Normalization per-100 pods** when cluster sizes differ significantly
- **Maintenance detection** — cordoned nodes shown as maintenance, not degraded
- **Unreachable handling** — partial comparison with error note
- **Health delta** = failing pods gap + CPU gap + incident gap
- Reuses existing `FleetHealthPort` — no new adapter needed

## Related Files (7)

`src/hexawyn/domain/models/cluster_health_comparison.py` · `src/hexawyn/domain/services/cluster_health_comparison/cluster_health_comparison_service.py` · `src/hexawyn/application/ports/driving/compare_cluster_health/` · `src/hexawyn/application/service/compare_cluster_health_service.py` · `src/hexawyn/application/use_case/compare_cluster_health/compare_cluster_health_use_case.py` · `src/hexawyn/mcp/tools/compare_cluster_health.py`
