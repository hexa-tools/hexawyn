# Use Case — Get Quota Usage

## Sample Questions

- "What is our current quota usage?"
- "How many investigations have we used this month?"
- "Am I close to my quota limit?"

---

Reports plan quota usage through: MCP Tool → GetQuotaUsageUseCase → PlanPort +
UsageMeterPort → pricing/usage adapters.

### Flow 1 — Happy Path

```mermaid
sequenceDiagram
    participant AI as AI Agent
    participant Tool as get_quota_usage()
    participant UseCase as GetQuotaUsageUseCase
    participant Plan as PlanPort (ABC)
    participant Meter as UsageMeterPort (ABC)

    AI->>Tool: Call "get_quota_usage"
    Tool->>UseCase: use_case(plan_port, usage_meter).execute(command)
    UseCase->>Plan: get plan
    UseCase->>Meter: current usage
    Plan-->>UseCase: plan limits
    Meter-->>UseCase: usage count
    UseCase-->>Tool: quota usage
    Tool-->>AI: { used, limit, remaining }
```

### Flow 2 — Errors

```mermaid
sequenceDiagram
    participant Tool as get_quota_usage()
    participant Meter as UsageMeterPort

    Tool->>Meter: read usage
    alt backend unavailable
        Meter-->>Tool: error
    end
    Tool-->>Tool: { error: "..." }
```

## Key Points

- Combines plan limits (PlanPort) with metered usage (UsageMeterPort).
- No cluster dependency — purely quota/billing data.

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_returns_response` | `tests/unit/application/use_case/cluster/test_uc_get_quota_usage_use_case.py` | ✅ |
| `test_tool_returns_dict` | `tests/unit/tools/test_get_quota_usage.py` | ✅ |

## Related Files

- `src/hexawyn/mcp/tools/get_quota_usage.py`
- `src/hexawyn/application/use_case/cluster/get_quota_usage/`
- `src/hexawyn/application/ports/driven/plan_port.py`
- `src/hexawyn/application/ports/driven/usage_meter_port.py`
