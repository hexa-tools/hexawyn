# Slack Alert — Automatic Push Notification

hexawyn detects a critical finding (e.g., CrashLoop, OOM kill, SLO breach) during a scheduled health check and automatically sends a Slack alert. Slack alerts use a SEPARATE quota — 5 alerts/month on Free tier, unlimited on Pro.

```mermaid
sequenceDiagram
    participant HC as Health Check (scheduled)
    participant SAA as SlackAlertAdapter
    participant QM as QuotaManager
    participant DuckDB
    participant Slack

    HC->>HC: global health check triggered

    Note over HC: Finding: CrashLoop in payments-api<br/>severity = critical

    HC->>SAA: send_alert(finding)

    Note over SAA,QM: [FREE] separate pool: 5 alerts/month

    SAA->>QM: check_slack_quota()
    QM->>DuckDB: SELECT slack_count FROM usage_quota<br/>WHERE month = '2026-06'
    DuckDB-->>QM: slack_count = 3, slack_limit = 5

    alt slack quota OK
        QM-->>SAA: OK (remaining: 2)

        SAA->>Slack: POST webhook (alert message)
        Slack-->>SAA: 200 OK

        SAA->>QM: increment_slack_quota()
        QM->>DuckDB: UPDATE slack_count = 4
        DuckDB-->>QM: OK

        Slack-->>User: "⚠️ Alert: payments-api in CrashLoopBackOff<br/>Restarts: 8 | Namespace: payments<br/>Cluster: prod-eks-us-east-1"
    else slack quota exceeded
        QM-->>SAA: raise SlackQuotaExceededError(3, 5)

        Note over SAA: Alert suppressed — quota exhausted<br/>Logged but not sent to Slack
    end
```

## Key Points

- Slack alerts are PUSH notifications — hexawyn sends them automatically when critical findings are detected (no user trigger)
- Slack alerts use a SEPARATE quota pool from investigations — 5/month Free, unlimited Pro
- SlackQuotaExceededError is raised when the 5-alert limit is reached — the alert is suppressed but logged
- Alerts only fire for `severity=critical` findings — degraded and warning levels do not trigger Slack
- Pro tier users have unlimited Slack alerts and Slack chat — both pools use limit=-1
