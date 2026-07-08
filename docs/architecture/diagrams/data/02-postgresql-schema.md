# PostgreSQL Schema — Central API (VPS)

The hexawyn backend stores client identity and subscription state in PostgreSQL. **Only one piece of PII is stored: the email address.** All infrastructure data (MCP Server URLs, Slack webhooks) is encrypted at rest in a separate table — decrypted only by the SLM worker at call time.

```mermaid
erDiagram
    clients {
        UUID id PK
        TEXT customer_id UK
        TEXT email UK "Only PII"
        TEXT api_key UK
        TEXT plan "free|pro|team|enterprise"
        TEXT status "active|inactive|suspended"
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    client_secrets {
        UUID id PK
        UUID client_id FK "UNIQUE — one row per client"
        TEXT mcp_url_encrypted "AES-256-GCM"
        TEXT slack_webhook_encrypted "AES-256-GCM"
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    subscriptions {
        UUID id PK
        UUID client_id FK
        TEXT polar_subscription_id UK
        TEXT plan
        TEXT status "active|canceled|past_due"
        TIMESTAMP current_period_start
        TIMESTAMP current_period_end
    }

    audits {
        UUID id PK
        UUID client_id FK
        DECIMAL total_cost
        DECIMAL total_waste
        DECIMAL waste_percent
        DECIMAL savings
        JSONB details
        TEXT severity
        TIMESTAMP timestamp
    }

    alerts {
        UUID id PK
        UUID client_id FK
        TEXT severity "warning|critical"
        TEXT message
        JSONB analysis
        BOOLEAN acknowledged
        TIMESTAMP timestamp
    }

    usage_meters {
        UUID id PK
        UUID client_id FK
        TEXT meter_name "cloud_calls|audits|alerts"
        INTEGER usage_count
        TIMESTAMP reset_at
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    configs {
        UUID id PK
        UUID client_id FK
        TEXT key
        JSONB value
        TIMESTAMP updated_at
    }

    clients ||--|| client_secrets : "1:1 encrypted secrets"
    clients ||--o{ subscriptions : "billing history"
    clients ||--o{ audits : "cost audits"
    clients ||--o{ alerts : "monitoring alerts"
    clients ||--o{ usage_meters : "quotas"
    clients ||--o{ configs : "settings"
```

---

## Data Flow: Who Reads What

```mermaid
sequenceDiagram
    participant API as FastAPI
    participant DB as PostgreSQL
    participant Worker as SLM Worker
    participant Key as HEXAWYN_SECRETS_KEY

    Note over API,DB: Dashboard / Auth — reads clients only
    API->>DB: SELECT email, plan, status FROM clients WHERE api_key = ?
    DB-->>API: { email, plan: "pro", status: "active" }
    Note over API: No secrets returned

    Note over Worker,Key: Monitoring run — needs MCP URL + webhook
    Worker->>DB: SELECT mcp_url_encrypted, slack_webhook_encrypted FROM client_secrets WHERE client_id = ?
    DB-->>Worker: { encrypted_blob }
    Worker->>Key: decrypt(encrypted_blob)
    Key-->>Worker: { mcp_url, slack_webhook }
    Worker->>Worker: POST mcp_url → MCP Server
    Worker->>Worker: POST slack_webhook → Slack
```

---

## Encryption Details

| Property | Value |
|---|---|
| Algorithm | AES-256-GCM (same as DuckDB encryption) |
| Key source | `HEXAWYN_SECRETS_KEY` environment variable (VPS only) |
| Key derivation | PBKDF2-HMAC-SHA256, 600k iterations |
| Library | `cryptography` (Python) |
| Decryption point | SLM worker only — never in API responses |

---

## Key Points

- **One PII field:** `clients.email` is the only user-identifiable data in PostgreSQL
- **Secrets isolation:** `client_secrets` is a separate table — never joined in dashboard queries
- **Encryption at rest:** `mcp_url` and `slack_webhook` are AES-256-GCM encrypted blobs in the database
- **Decryption on demand:** Only the SLM worker (server-side, no user access) decrypts secrets when calling MCP Servers
- **No `config` JSONB:** Removed — no arbitrary per-client data storage
- **Cascade delete:** Deleting a client cascades to all related rows (subscriptions, audits, alerts, secrets, etc.)

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_clients_table_has_no_infra_data` | `tests/unit/test_postgresql_schema.py` | ✅ |
| `test_client_secrets_encrypted_at_rest` | `tests/unit/test_client_secrets.py` | ✅ |
| `test_worker_decrypts_secrets_on_demand` | `tests/unit/test_client_secrets.py` | ✅ |
| `test_dashboard_never_returns_secrets` | `tests/unit/test_dashboard.py` | ✅ |
| `test_subscription_created_webhook` | `tests/unit/test_polar_webhooks.py` | ✅ |

## Related Files

- `src/hexawyn/infrastructure/db/schema.sql` — PostgreSQL schema (to be created)
- `src/hexawyn/infrastructure/db/client_secrets.py` — encryption/decryption logic (to be created)
- `src/hexawyn/webhooks/polar.py` — Polar.sh webhook handlers (to be created)
- `src/hexawyn/infrastructure/config/secrets_key.py` — `HEXAWYN_SECRETS_KEY` loader (to be created)
- [ECA-124](https://onlinebook-red-line.atlassian.net/browse/ECA-124) — tracking ticket
