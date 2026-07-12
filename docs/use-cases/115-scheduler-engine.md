# Use Case 115 — Generic Scheduling Engine (ECA-157)

Periodically executes existing use cases (cert audits, GitOps drift, SLO
breach…) on a configurable cron schedule, detects state changes via
`payload_digest`, and notifies Slack when a result differs from the previous
run.

The scheduler is **agnostic**: it knows no specific use case — it runs a
use case by name, computes a digest, compares it with the last run, and
decides whether to notify. This is what allows the control-plane (ECA-125)
to reuse it unchanged.

## CLI Commands (v1 — no natural language interface)

```bash
# Create a scheduled check
hexawyn schedule create --name certs --use-case certs_list --every 6h --notify on-change

# List all checks
hexawyn schedule list

# Detail of a check
hexawyn schedule get certs

# Execution history
hexawyn schedule history certs --limit 10

# Overview
hexawyn schedule status

# Enable / disable
hexawyn schedule enable certs
hexawyn schedule disable certs

# Delete
hexawyn schedule delete certs

# Manual run (outside cron)
hexawyn schedule run certs

# Start the scheduler (long-running)
hexawyn schedule start
hexawyn schedule start --dry-run
```

---

## 1. Happy Path — Full Hexagonal Chain

```mermaid
sequenceDiagram
    participant SRE
    participant CLI as CLI<br/>(hexawyn schedule start)
    participant Scheduler as SchedulerAdapter<br/>(native Python loop)
    participant Runner as CheckRunnerUseCase<br/>(agnostic engine)
    participant Store as DuckDBScheduleStore<br/>(persistence)
    participant UseCase as Existing Use Case<br/>(certs_list, gitops_apps…)
    participant Digest as payload_digest<br/>(SHA-256)
    participant DuckDB
    participant Alert as AlertHistoryDecorator<br/>(Slack + alerts table)
    participant Slack

    SRE->>CLI: hexawyn schedule create --name certs --use-case certs_list --every 6h
    CLI->>CLI: shortcut_to_cron("6h") → "0 */6 * * *"
    CLI->>Store: save_check(CronCheck)
    Store->>DuckDB: INSERT INTO schedule_checks

    SRE->>CLI: hexawyn schedule start
    CLI->>Scheduler: start(enabled_checks)
    Note over Scheduler: while True: sleep(60s)<br/>_interval_minutes per check

    Scheduler->>Runner: execute(check) [every 6h]
    Runner->>UseCase: certs_list()
    UseCase-->>Runner: {"status": "ok", "certs": 3}

    Runner->>Digest: SHA-256(payload_json)
    Digest-->>Runner: "a1b2c3..."

    Runner->>Store: last_result("certs")
    Store->>DuckDB: SELECT … ORDER BY id DESC LIMIT 1
    DuckDB-->>Store: previous CheckResult (digest="old_hash")

    alt digest changed (or first run)
        Runner->>Runner: changed=True, phase=ALERTING
        Runner->>Alert: send_alert(AlertMessage)
        Alert->>Slack: warning: [certs] change detected
        Slack-->>Alert: OK
        Alert->>DuckDB: INSERT INTO alerts (source, severity, notified…)
    else digest identical
        Runner->>Runner: changed=False, phase=SUCCESS
    end

    Runner->>Store: save_result(CheckResult)
    Store->>DuckDB: INSERT INTO schedule_results
```

---

## 2. Change Detection & Notification Flows

```mermaid
sequenceDiagram
    participant Runner as CheckRunnerUseCase
    participant Store as DuckDBScheduleStore
    participant Decorator as AlertHistoryDecorator
    participant Slack as SlackAlertAdapter
    participant DuckDB

    Runner->>Runner: use case output → json.dumps → SHA-256 → digest
    Runner->>Store: last_result(check_name)

    alt first run (previous is None)
        Runner->>Runner: changed = True
    else digest matches previous payload_digest
        Runner->>Runner: changed = False
    else digest differs
        Runner->>Runner: changed = True
    end

    alt notify_policy == "always"
        Runner->>Decorator: send_alert(AlertMessage)
    else notify_policy == "on_change" AND changed
        Runner->>Decorator: send_alert(AlertMessage)
    else notify_policy == "on_failure" AND phase == "failed"
        Runner->>Decorator: send_alert(AlertMessage)
    else no notification
        Note over Runner: skip
    end

    Decorator->>Slack: send_alert(message)
    Slack-->>Decorator: success / failure
    Decorator->>DuckDB: INSERT INTO alerts<br/>(check_name, severity, text, source, notified, delivery_status)
    Note over Decorator: alert is recorded even when Slack delivery fails
    Decorator-->>Runner: notified = success
```

---

## 3. Checker Node

```mermaid
sequenceDiagram
    participant Gen as generate_response
    participant Checker as checker_node / semantic_layer
    participant Store as DuckDB
    participant Format as format_response

    Gen->>Checker: narrative + scheduler alert
    alt CronCheck misreads "scale to zero" / "suspended" as a failure
        Checker-->>Gen: FAIL — rely on underlying use-case checker nodes
    else notify_policy=ON_CHANGE but notification fires every tick without real change
        Checker->>Store: compare current digest vs previous
        Checker-->>Gen: FAIL — payload_digest unchanged, suppress notification
    else Invalid cron expression accepted silently
        Checker-->>Gen: FAIL — cron must raise ValueError, phase=FAILED
    else Scheduler attempts to mutate cluster (read-only contract)
        Checker-->>Gen: FAIL — Mutation Guard, read-only strict
    else Multi-cluster result lacks cluster_name context
        Checker-->>Format: FLAG — cluster_name required
    else Downtime misfire not coalesced (N executions replayed)
        Checker-->>Format: FLAG — coalesce to single execution
    else PASS
        Checker->>Store: persist alert in alerts table
        Store->>Format: rendered answer
    end
```

---

## 4. DuckDB — Schedule Schema

```mermaid
erDiagram
    schedule_checks {
        VARCHAR name PK
        VARCHAR schedule
        VARCHAR use_case
        JSON params
        BOOLEAN enabled
        VARCHAR notify_policy
        JSON destinations
        INTEGER timeout_seconds
    }

    schedule_results {
        INTEGER id PK
        VARCHAR check_name FK
        VARCHAR phase
        TIMESTAMPTZ started_at
        TIMESTAMPTZ finished_at
        INTEGER duration_ms
        VARCHAR summary
        VARCHAR payload_digest
        BOOLEAN changed
        VARCHAR error_message
        BOOLEAN notified
    }

    alerts {
        UUID id PK
        TIMESTAMPTZ timestamp
        VARCHAR cluster_name
        VARCHAR check_name
        VARCHAR severity
        VARCHAR title
        TEXT text
        VARCHAR source
        BOOLEAN notified
        VARCHAR delivery_status
    }

    schedule_checks ||--o{ schedule_results : "1 check → N runs"
    schedule_checks ||--o{ alerts : "1 check → N alerts"
```

---

## Key Points

- **Use-case agnostic**: the scheduler knows no specific use case; it runs a
  string name via an injected `UseCaseRegistry` and compares results.
- **Change detection via `payload_digest`** (SHA-256): compares the hash of the
  current output with the last run. No heuristics, no thresholds.
- **Notify policy**: `always` (every tick), `on_change` (only when digest
  differs), `on_failure` (only on error).
- **Alerts persisted**: every alert sent (or attempted) is recorded in the
  `alerts` table via `AlertHistoryDecorator`, with delivery status.
- **Native Python scheduler**: `while True` + `time.sleep(60)`, zero external
  dependencies. Supports `--every` shortcuts (15m, 30m, 1h, 6h, 12h, 24h).
- **Disabled by default**: `HEXAWYN_SCHEDULER_ENABLED=false` — existing MCP
  behaviour is completely unchanged for users who do not activate it.

---

## Related Files

- `src/hexawyn/domain/models/schedule.py`
- `src/hexawyn/domain/services/schedule/check_runner.py`
- `src/hexawyn/domain/services/schedule/cron_shortcut.py`
- `src/hexawyn/domain/services/schedule/duckdb_schedule_store.py`
- `src/hexawyn/domain/services/schedule/alert_history.py`
- `src/hexawyn/application/ports/driven/schedule_store_port.py`
- `src/hexawyn/infrastructure/config/schedule_source.py`
- `src/hexawyn/cli/commands/schedule_command.py`
- `src/hexawyn/infrastructure/memory/sql/schema.sql`
- `src/hexawyn/infrastructure/memory/sql/migrations/v004_add_alerts.sql`
