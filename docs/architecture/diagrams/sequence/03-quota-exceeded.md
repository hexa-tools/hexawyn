# Quota Exceeded — Free Tier Blocked

Free tier user has used all 50 investigations this month. The investigation is blocked immediately at parse_intent — no LangGraph nodes beyond the first are executed. The user sees a clear upgrade message.

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant parse_intent
    participant QM as QuotaManager
    participant DuckDB
    participant format_response

    User->>CLI: "check the health of prod-eu"
    CLI->>parse_intent: query

    Note over parse_intent,QM: [FREE] quota check
    parse_intent->>QM: check_quota()
    QM->>DuckDB: SELECT investigation_count FROM usage_quota<br/>WHERE month = '2026-06'
    DuckDB-->>QM: count = 50, limit = 50

    Note over QM: is_exceeded = True

    alt quota exceeded
        QM-->>parse_intent: raise QuotaExceededError(used=50, limit=50)

        Note over parse_intent,LangGraph: LangGraph catches error → status = ERROR

        parse_intent-->>CLI: error state

        CLI->>format_response: error + upgrade message
        format_response-->>CLI: formatted error

        CLI-->>User: "❌ You've used 50/50 free investigations this month.<br/>Quota resets on the 1st of next month.<br/>Upgrade to Pro for unlimited access:<br/>https://hexawyn.com/pro<br/>Activate your license: hexa license activate <YOUR-KEY>"
    else quota OK
        Note over parse_intent,format_response: continue normal pipeline
    end
```

## Key Points

- Quota is checked at parse_intent — the FIRST LangGraph node. No expensive operations (LLM, K8s API) are triggered before this check
- QuotaExceededError is raised as a HexawynError subclass — caught by the LangGraph error handler
- The error message includes: current usage (50/50), reset date, upgrade URL, and license activation command
- Pro tier (limit=-1) never raises QuotaExceededError — `is_exceeded` always returns False
- Slack alerts have a separate quota (5/month Free) via SlackQuotaExceededError
