# 88 — Generate Weekly Reliability Report

Generate a weekly reliability report for all production services including uptime,
error rate, p99 latency, SLO compliance, top 3 incidents, and overall health score.

## Sample Questions

- "Generate a weekly reliability report for all production services — include uptime, error rate, p99 latency, SLO compliance, and top 3 incidents."
- "How did our services perform this week against their SLOs?"
- "Show me a health report with SLO pass/fail for all production services."
- "What were the top 3 incidents last week ranked by impact?"
- "Give me the weekly reliability summary for stakeholder review."

---

## 1. Happy Path

```mermaid
sequenceDiagram
    participant User
    participant MCP as MCP Tool
    participant UC as UseCase
    participant Svc as Service
    participant Engine as WeeklyReliabilityReportEngine
    participant Port as WeeklyReliabilityReportPort
    participant Adapter as PrometheusReliabilityAdapter
    participant Prom as Prometheus

    User->>MCP: generate_weekly_reliability_report(window=7)
    MCP->>Svc: GenerateWeeklyReliabilityReportService(port)
    MCP->>UC: execute(command)
    UC->>Svc: generate_report(command)
    Svc->>Port: fetch_service_reliability(7)
    Port->>Adapter: fetch_service_reliability(7)
    Adapter->>Prom: instant_query(uptime query)
    Prom-->>Adapter: [{service: "payment", value: 0.9992}, ...]
    Adapter-->>Port: list[ServiceReliabilityRawData]
    Port-->>Svc: raw data

    Svc->>Port: fetch_incidents(7)
    Port->>Adapter: fetch_incidents(7)
    Adapter-->>Port: list[IncidentRawData]
    Port-->>Svc: incidents

    Svc->>Engine: compute(services, incidents)
    Engine->>Engine: evaluate_slo, rank_incidents, health_score
    Engine-->>Svc: WeeklyReliabilityReport
    Svc-->>UC: response
    UC-->>MCP: response
    MCP-->>User: health=50%, 2 SLO pass, 1 SLO fail
```

## 2. Error Flows

```mermaid
sequenceDiagram
    participant Svc as Service
    participant Adapter as PrometheusReliabilityAdapter
    participant Prom as Prometheus

    alt Prometheus Unreachable
        Adapter->>Prom: instant_query()
        Prom-->>Adapter: Timeout / HTTPError
        Adapter->>Adapter: catch Exception → return []
        Adapter-->>Svc: [] (empty)
        Svc->>Svc: engine.compute([], []) → 0 services
    end
```

## 3. Checker Node

```mermaid
sequenceDiagram
    participant Checker as Checker
    participant Engine as Engine

    Checker->>Engine: compute(services, incidents)

    alt PASS — all SLO green
        Engine-->>Checker: health=100%, slo_fail=0
    else FLAG — >3 incidents, only 3 shown
        Engine-->>Checker: total_incident_count=7, top_incidents=3
    else FAIL — SLO verdict inverted
        Engine-->>Checker: uptime=99.72 < slo=99.9 → fail (not pass)
    end
```

---

## Key Points

- Computes uptime from Prometheus success rate (rate of non-5xx / rate of all requests)
- SLO evaluation: `uptime_pct >= slo_target → pass, else fail`
- Incidents ranked by impact: `duration_minutes * error_rate` descending, top 3 only
- Health score: `(slo_pass_count / total_services) * 100`
- Prometheus errors return empty lists → engine handles gracefully (0 services, 0 incidents)
- Each service evaluated against its own SLO target

---

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_slo_pass_when_uptime_above_target` | `test_weekly_reliability_report_engine.py` | ✅ |
| `test_slo_fail_when_uptime_below_target` | `test_weekly_reliability_report_engine.py` | ✅ |
| `test_top_three_incidents_by_impact` | `test_weekly_reliability_report_engine.py` | ✅ |
| `test_more_than_three_incidents_keeps_total_count` | `test_weekly_reliability_report_engine.py` | ✅ |
| `test_all_slo_pass_health_100` | `test_weekly_reliability_report_engine.py` | ✅ |
| `test_mixed_slo_targets_evaluated_individually` | `test_weekly_reliability_report_engine.py` | ✅ |
| `test_delegates_to_service` | `test_weekly_reliability_report_port_and_service.py` | ✅ |
| `test_calls_port_with_window` | `test_weekly_reliability_report_port_and_service.py` | ✅ |
| `test_fetch_service_reliability_returns_data` | `test_reliability_report_adapter.py` | ✅ |
| `test_delegates_and_returns_dict` | `test_generate_weekly_report_mcp.py` | ✅ |

---

## Related Files

- `src/hexawyn/domain/models/weekly_reliability_report.py`
- `src/hexawyn/domain/services/reliability_report/weekly_reliability_report_engine.py`
- `src/hexawyn/application/ports/driven/weekly_reliability_report_port.py`
- `src/hexawyn/application/ports/driving/generate_weekly_reliability_report/`
- `src/hexawyn/application/service/generate_weekly_reliability_report_service.py`
- `src/hexawyn/application/use_case/generate_weekly_reliability_report/`
- `src/hexawyn/adapters/secondary/gitops/prometheus_reliability_adapter.py`
- `src/hexawyn/mcp/tools/generate_weekly_reliability_report.py`
- `src/hexawyn/mcp/server.py`
