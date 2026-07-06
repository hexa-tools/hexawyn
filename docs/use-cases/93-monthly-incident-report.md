# 93 — Monthly Incident Report

Compute a monthly operational incident summary: total incident count,
downtime minutes per severity (P1/P2/P3), most impacted services ranked
by downtime, and month-over-month trend.

## Sample Questions

- "How many incidents occurred this month and what was the total downtime in minutes?"
- "Show me the P1, P2, and P3 breakdown for this month vs last month."
- "Which services were most impacted by incidents this month?"
- "Are incidents increasing or decreasing compared to the previous month?"

---

## 1. Happy Path

```mermaid
sequenceDiagram
    participant User
    participant MCP as MCP Tool
    participant UC as UseCase
    participant Svc as Service
    participant Engine as MonthlyIncidentReportEngine
    participant Port as MonthlyIncidentPort
    participant Adapter as MonthlyIncidentAdapter
    participant DB as Incident DB

    User->>MCP: compute_monthly_incident_report("2026-07")
    MCP->>Svc: ComputeMonthlyIncidentReportService(port)
    MCP->>UC: execute(command)
    UC->>Svc: compute(command)
    Svc->>Port: fetch_incidents("2026-07")
    Svc->>Port: fetch_incidents("2026-06")
    Port->>Adapter: fetch_incidents()
    Adapter->>DB: query incidents WHERE month=
    DB-->>Adapter: list of incidents
    Adapter-->>Port: list[IncidentSnapshotData]
    Svc->>Engine: compute(current_incidents, prev_incidents)
    Engine->>Engine: count per severity (P1/P2/P3)
    Engine->>Engine: sum downtime per severity
    Engine->>Engine: rank services by downtime
    Engine->>Engine: compare vs previous month
    Engine-->>Svc: MonthlyIncidentReport
    MCP-->>User: P1=3 (180min), P2=5 (40min), decreasing ✓
```

---

## Key Points

- Severity levels: P1, P2, P3 — counts and downtime aggregated per level
- Planned maintenance incidents excluded from count and downtime
- Services ranked by total downtime (descending) — identifies most impacted
- Month-over-month: compares total count, computes incidents_decreasing flag
- Empty month returns clean "0 incidents" report with all zeros

---

## Related Files

- `src/hexawyn/domain/models/monthly_incident_report.py`
- `src/hexawyn/domain/services/monthly_incident/monthly_incident_report_engine.py`
- `src/hexawyn/application/ports/driven/monthly_incident_port.py`
- `src/hexawyn/application/ports/driving/compute_monthly_incident_report/`
- `src/hexawyn/mcp/tools/compute_monthly_incident_report.py`
