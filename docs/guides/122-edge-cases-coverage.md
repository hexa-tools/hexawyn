# Use Case — Edge Cases Coverage Strategy

Systematic approach to adding boundary-condition tests across ALL layers of the hexawyn codebase. Target: 130+ use cases, every source layer with real business logic must have edge case coverage.

## Sample Questions

N/A — this is a quality engineering process, not a user-facing tool.

## Key Metrics — Full Scope

| Layer | Source files | Test files | Tests | Edge cases | Status |
|---|---|---|---|---|---|
| **Domain models** | 5 | 5 | 153 | 79 | ✅ DONE |
| **Domain services** | 2 | 2 | 67 | 26 | ✅ DONE |
| **Infrastructure** | 3 | 3 | 48 | 15 | ✅ DONE |
| **Application service** | 141 | 32 | ~303 | — | 🔴 SEVERE |
| **Application use_case** | 136 | 3 | ~26 | — | 🔴 VERY SEVERE |
| **MCP server.py** | 1 | 0 | 0 | — | 🔴 MANDATORY |
| **MCP tools** | 147 | 18 | ~72 | — | 🔴 SEVERE |
| **Adapters secondary** | 151 | 76 | ~500 | — | 🟡 MODERATE |
| **CLI** | 23 | 13 | ~80 | — | 🟡 MODERATE |
| **Domain services (rest)** | 43 subdirs | varied | varies | — | 🟡 MODERATE |

## Progression globale

```
[██████████████████████████████████████████████████████] 95%
 Phase 1-4 done · 7562 tests passants · make check ✅
```

## Key Metrics — Full Scope (Final)

| Layer | Status | Delta |
|---|---|---|
| Domain models + services + infra | ✅ DONE | +120 |
| Application service | ✅ DONE | +53 |
| Application use_case | ✅ DONE | +272 |
| MCP server.py | ✅ DONE | +102 |
| MCP tools | ✅ DONE | +330 |
| CLI | ✅ DONE | +6 |
| **Total** | **6679 → 7562** | **+883** |

## Plan d'attaque

### Phase 1 — Domain + Infrastructure ✅ DONE
- Domain models (5 fichiers, +79 edge cases)
- Domain services (2 fichiers, +26 edge cases)
- Infrastructure (3 fichiers, +15 edge cases)

### Phase 2 — Application Services + Use Cases 🔴 IN PROGRESS
Target: edge cases on every application service and use case with real business logic.

Already done (6 services with edge cases):
- `test_container_image_vulnerability_service.py` (5)
- `test_pod_security_standards_audit_service.py` (5)
- `test_east_west_network_segmentation_service.py` (5)
- `test_unintended_external_exposure_service.py` (5)
- `test_audit_rbac_permissions_service.py` (5)
- `test_secret_rotation_audit_service.py` (5)

Remaining services (~26 test files need edge cases):
- `test_adaptive_namespace_investigation_service.py`
- `test_admin_endpoint_audit_service.py`
- `test_analyze_failed_pipeline_service.py`
- `test_analyze_incident_cost_service.py`
- `test_analyze_pod_logs_service.py`
- `test_canary_comparison_service.py`
- `test_check_cluster_operator_health_service.py`
- `test_compute_budget_intelligence_service.py`
- `test_detect_log_anomalies_service.py`
- `test_detect_over_provisioned_namespaces_service.py`
- `test_detect_pod_anomalies_service.py`
- `test_diff_helm_values_service.py`
- `test_estimate_rightsizing_savings_service.py`
- `test_generate_incident_triage_report_service.py`
- `test_generate_sla_report_service.py`
- `test_get_namespace_events_service.py`
- `test_hot_node_analysis_service.py`
- `test_live_topology_mapper_service.py`
- `test_plan_spike_provisioning_service.py`
- `test_report_platform_reliability_service.py`
- `test_run_what_if_simulation_service.py`
- `test_search_resources_by_labels_service.py`
- `test_semantic_log_search_service.py`
- `test_summarize_namespace_events_service.py`
- `test_watch_pod_logs_service.py`
- `test_project_budget_service.py`

Use cases (~133 need tests from scratch):
- Port-level tests exist for driving ports (command/response/port ABCs)
- Use case orchestrator tests needed: inject mock service, verify delegation

### Phase 3 — MCP Server + Tools 🔴 NEXT
- `mcp/server.py`: wiring hub, every `build_*_adapter()` must have test
- `mcp/tools/`: 129 tools without tests, user-facing entry points

### Phase 4 — Adapters Secondary + CLI + Domain Services 🟡 AFTER
- Secondary adapters (~75 missing)
- CLI entry points (main.py, app.py, tui.py, command_router.py)
- Remaining domain service engines

## Key Points

- Only files with real business logic need edge cases (not ABCs, stubs, frozen dataclasses)
- Each edge case must match the existing test pattern exactly
- Exception propagation, empty result handling, boundary values — top 3 categories
- 6799 tests passants, zéro régression
- MCP server.py is MANDATORY per AGENTS.md — every build_*_adapter() needs test

## Test Coverage

| What | File | Status |
|---|---|---|
| Domain model boundaries | `tests/unit/domain/models/test_*` | ✅ 79 edge cases |
| Domain services edge cases | `tests/unit/domain/services/test_*` | ✅ 26 edge cases |
| Infrastructure edge cases | `tests/unit/infrastructure/*/test_*` | ✅ 15 edge cases |
| Application service edge cases | `tests/unit/application/service/test_*` | 🔴 6/32 files |
| Application use case tests | `tests/unit/application/use_case/test_*` | 🔴 3/136 |
| MCP server wiring | `tests/unit/mcp/test_server.py` | 🔴 0 tests |
| MCP tool coverage | `tests/unit/mcp/tools/test_*` | 🔴 18/147 |
| ABC port validation | `tests/unit/application/ports/*/test_*` | ✅ sufficient |

## Related Files

- `docs/use-cases/117-quota-progress-bar.md`
- `docs/use-cases/118-memory-consolidation.md`
- `docs/use-cases/119-eval-duale-release-gate.md`
- `docs/use-cases/120-retrieval-gate.md`
- `docs/use-cases/121-startup-scan-slm.md`
