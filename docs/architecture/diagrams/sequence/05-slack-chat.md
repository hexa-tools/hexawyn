# Slack Chat — Same LangGraph, Different Adapter

User asks a question via Slack using an `@hexawyn` mention. The Slack chat adapter is just a different primary adapter — it runs the exact same LangGraph pipeline as the CLI. Quota is shared: a Slack question counts toward the same 50/month Free tier limit.

```mermaid
sequenceDiagram
    participant User
    participant Slack
    participant SCA as SlackChatAdapter
    participant parse_intent
    participant QM as QuotaManager
    participant DuckDB
    participant LangGraph
    participant LLM
    participant store_memory
    participant format_response

    User->>Slack: "@hexawyn why is payments-api crashing?"
    Slack->>SCA: webhook event

    Note over SCA: Primary adapter — same LangGraph as CLI

    SCA->>parse_intent: query

    Note over parse_intent,QM: [FREE] shared pool: 50/month
    parse_intent->>QM: check_quota()
    QM->>DuckDB: investigation_count?
    DuckDB-->>QM: count=23, limit=50
    QM-->>parse_intent: OK

    parse_intent-->>SCA: intent + tool_name

    SCA->>LangGraph: execute full 9-node pipeline
    LangGraph->>LLM: generate response
    LLM-->>LangGraph: investigation result

    LangGraph->>QM: increment_quota()
    QM->>DuckDB: UPDATE count=24

    LangGraph->>store_memory: save result
    store_memory->>DuckDB: INSERT INTO incidents

    LangGraph->>format_response: result + Slack markdown
    format_response-->>SCA: formatted for Slack

    SCA->>Slack: post thread reply

    Slack-->>User: "@user Cause: OOM kill in payments-api.<br/>Recommendation: Increase memory limit to 512Mi.<br/><br/>[24/50 free investigations · 26 remaining]"
```

## Key Points

- Slack Chat and CLI share the SAME investigation quota pool — 50/month total across both channels
- The Slack adapter is a primary adapter (inbound) — it feeds into the same LangGraph pipeline as the CLI
- Responses are formatted in Slack markdown (not Textual widgets)
- Quota display is appended to every response: `[24/50 free investigations · 26 remaining]`
- Demo mode also applies to Slack — no quota consumed when `HEXAWYN_DEMO_MODE=true`
