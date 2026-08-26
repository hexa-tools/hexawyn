# Use Case 105 — Executive SLA Report (ECA-87)

Answers: *"Generate an executive SLA report for all customer-facing services this
quarter."* — a Director-level reliability report for stakeholders.

Produces quarterly uptime per service, SLA target vs actual, all breaches (date,
duration, impacted users, root-cause reference), and the quarter-over-quarter
reliability trend. Planned-maintenance windows are excluded from the SLA
calculation and services onboarded mid-quarter are prorated. Output is
chart-ready — no raw logs.

## Sample Questions

- "Generate an executive SLA report for all customer-facing services this quarter."
- "What was our uptime per service versus SLA target this quarter?"
- "Which services breached their SLA, and for how long?"
- "Is our reliability improving or degrading compared to last quarter?"
- "Give me a stakeholder-ready SLA summary with breaches and impacted users."

---

## 1. Happy Path — Full Hexagonal Chain

```mermaid
sequenceDiagram
    participant Director
    participant MCP as MCP Tool<br/>(generate_sla_report)
    participant UC as UseCase<br/>(GenerateSlaReportUseCase)
    participant Svc as Service<br/>(GenerateSlaReportService)
    participant Domain as Domain<br/>(SlaReportService + uptime_calculator + sla_trend)
    participant Port as Driven Port<br/>(SlaReportPort)
    participant Facade as Facade Adapter<br/>(SlaReportAdapter)
    participant Sources as weekly reliability / SLO sources

    Director->>MCP: generate_sla_report(quarter="2026-Q1")
    MCP->>Svc: build service(port=facade)
    MCP->>UC: execute(command)
    UC->>Svc: generate(command)
    Svc->>Port: get_quarter_sla_data("2026-Q1")
    Port->>Facade: get_quarter_sla_data(...)
    Facade->>Sources: roll up weekly reliability + incidents → quarter
    Sources-->>Facade: QuarterSlaData
    Facade-->>Svc: QuarterSlaData (has_data=true)
    Svc->>Port: get_previous_quarter_avg_uptime("2026-Q1")
    Port-->>Svc: 99.5
    Svc->>Domain: generate(data, quarter, previous_avg=99.5)
    Domain->>Domain: evaluate_service (exclude maintenance, prorate onboarding)
    Domain->>Domain: attach breaches per service (skip planned maintenance)
    Domain->>Domain: classify_trend (99.5 → 99.8 = improving)
    Domain-->>Svc: SlaReport
    Svc-->>MCP: Response(report)
    MCP-->>Director: 2 met · 1 breached · trend improving · chart-ready
```

---

## 2. Status & Coverage Flows

```mermaid
sequenceDiagram
    participant Domain as SlaReportService
    participant Calc as uptime_calculator

    Domain->>Calc: evaluate_service(raw)
    alt all above target (TC1)
        Calc-->>Domain: met=true (green)
    else 100% uptime
        Calc-->>Domain: met=true, exceeded=true
    else below target (TC2)
        Calc-->>Domain: met=false → breach highlighted with duration + RCA link
    else onboarded mid-quarter (TC3)
        Calc->>Calc: coverage_days < quarter_days
        Calc-->>Domain: prorated=true (measured over covered days only)
    end
    Note over Domain: planned-maintenance minutes excluded from downtime
```

---

## 3. Checker Node

```mermaid
sequenceDiagram
    participant Gen as generate_response
    participant Checker as checker_node / semantic_layer
    participant Store as store_memory
    participant Format as format_response

    Gen->>Checker: narrative + SlaReport
    alt No data reported as 100% uptime (TC4)
        Checker->>Checker: has_data=false ⇒ must warn, not claim uptime
        Checker->>Gen: FAIL — surface missing-data warning
    else Maintenance counted against SLA
        Checker->>Checker: planned windows must be excluded
        Checker->>Gen: FAIL
    else Prorated service penalized for pre-onboarding weeks (TC3)
        Checker->>Gen: FAIL — measure only covered days
    else Raw logs leaked into executive report
        Checker->>Gen: FAIL — chart-ready data only
    else PASS
        Checker->>Store: persist report
        Store->>Format: rendered executive report
    end
```

---

## Key Points

- **Aggregator via Facade**: the domain never touches the reliability/SLO
  sources; a Facade adapter rolls weekly data up into `QuarterSlaData`.
- **Planned maintenance excluded**: scheduled windows are removed from downtime
  so they never count against the SLA (edge case).
- **Mid-quarter proration** (TC3): a service onboarded late is measured only
  over its covered days and flagged `prorated`.
- **`exceeded` distinct from `met`**: 100% uptime is shown as exceeding target,
  not merely "OK" (edge case).
- **Each incident counted separately**: multiple breaches on the same day are
  distinct entries.
- **Breaches carry impacted users + root-cause reference** — executive-friendly,
  no raw logs.
- **No-data honesty** (TC4): missing incident data yields a warning, never a
  fabricated 100% uptime.

---

## Tests

All test files created for this use case:

```
tests/unit/test_sla_report.py                             # domain model
tests/unit/test_sla_report_port.py                        # driven port + TypedDicts
tests/unit/test_uptime_calculator.py                      # status, proration, maintenance exclusion
tests/unit/test_sla_trend.py                              # improving/degrading/stable
tests/unit/test_sla_report_service.py                     # assembly, breaches, no-data, trend
tests/unit/test_sla_report_adapter.py                     # Facade delegation
tests/unit/test_sla_report_source.py                      # default no-data source
tests/unit/test_generate_sla_report_command.py            # driving command
tests/unit/test_generate_sla_report_response.py           # driving response
tests/unit/test_generate_sla_report_service_port.py       # driving service port (ABC)
tests/unit/test_generate_sla_report_service.py            # application service
tests/unit/test_generate_sla_report_use_case.py           # use case
tests/unit/test_generate_sla_report_mcp.py                # MCP tool
tests/unit/test_server.py                                 # build_sla_report_adapter factory
```

Domain-logic stubs (uptime, proration, trend):

```python
def test_met_when_uptime_equals_target():
    # uptime == target => met, not exceeded
    ...

def test_hundred_percent_exceeds():
    # 100% uptime => exceeded True
    ...

def test_prorated_when_coverage_less_than_quarter():
    # onboarded mid-quarter => prorated True (TC3)
    ...

def test_maintenance_minutes_improve_effective_uptime():
    # planned maintenance excluded from downtime
    ...

def test_planned_maintenance_breach_excluded():
    # maintenance breach not counted against SLA
    ...

def test_missing_data_warns():
    # has_data=false => warning, no fabricated uptime (TC4)
    ...
```

| Test Scenario (ticket) | Test | Status |
|---|---|---|
| TC1: all above target → green | `test_all_services_above_target_green` | ✅ |
| TC2: one breached → highlighted w/ duration + RCA | `test_ticket_scenario` / `test_breaches_attached_to_their_service` | ✅ |
| TC3: mid-quarter onboarding → prorated | `test_mid_quarter_onboarding_prorated` | ✅ |
| TC4: no data → warning | `test_missing_data_warns` | ✅ |
| Edge: planned maintenance excluded | `test_planned_maintenance_breach_excluded` | ✅ |
| Edge: multiple incidents same day counted separately | `test_breaches_attached_to_their_service` | ✅ |
| Edge: 100% uptime exceeds target | `test_hundred_percent_exceeds` | ✅ |

---

## Related Files

- `src/hexawyn/domain/models/sla_report.py`
- `src/hexawyn/domain/services/sla_report/uptime_calculator.py`
- `src/hexawyn/domain/services/sla_report/sla_trend.py`
- `src/hexawyn/domain/services/sla_report/sla_report_service.py`
- `src/hexawyn/application/ports/driven/sla_report_port.py`
- `src/hexawyn/application/ports/driving/generate_sla_report/`
- `src/hexawyn/application/service/generate_sla_report_service.py`
- `src/hexawyn/application/use_case/generate_sla_report/generate_sla_report_use_case.py`
- `src/hexawyn/adapters/secondary/gitops/sla_report_adapter.py`
- `src/hexawyn/adapters/secondary/gitops/sla_report_source.py`
- `src/hexawyn/mcp/tools/generate_sla_report.py`
- `src/hexawyn/mcp/server.py` (`build_sla_report_adapter`)
