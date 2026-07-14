-- Incidents table: stores all investigations with embeddings
CREATE TABLE IF NOT EXISTS incidents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    retained_until TIMESTAMPTZ NOT NULL DEFAULT now() + INTERVAL '90 days',
    age_days INTEGER GENERATED ALWAYS AS (
        DATEDIFF('day', timestamp, now())
    ) VIRTUAL,
    cluster_name VARCHAR NOT NULL,
    namespace VARCHAR,
    resource_name VARCHAR,
    resource_kind VARCHAR,
    tool_name VARCHAR NOT NULL,
    cause TEXT,
    symptoms TEXT[],
    solution TEXT,
    severity VARCHAR DEFAULT 'low',
    feedback INTEGER DEFAULT 0,
    weight FLOAT DEFAULT 1.0,
    embedding FLOAT[768],
    sanitized BOOLEAN DEFAULT false
);

-- Topology snapshots
CREATE TABLE IF NOT EXISTS topology_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    cluster_name VARCHAR NOT NULL,
    snapshot JSON NOT NULL
);

-- Security audits
CREATE TABLE IF NOT EXISTS security_audits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    cluster_name VARCHAR NOT NULL,
    findings JSON NOT NULL,
    severity VARCHAR NOT NULL
);

-- Schema version tracking
CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER PRIMARY KEY,
    applied_at TIMESTAMPTZ DEFAULT now(),
    description VARCHAR
);

-- Cost audits: namespace-level cost snapshots (DuckDB local)
CREATE TABLE IF NOT EXISTS cost_audits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    namespace TEXT NOT NULL,
    pod_count INTEGER DEFAULT 0,
    total_cost DECIMAL(12,2),
    total_waste DECIMAL(12,2),
    waste_percent DECIMAL(5,2),
    savings_right_sizing DECIMAL(12,2),
    savings_spot DECIMAL(12,2),
    savings_total DECIMAL(12,2),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details JSON DEFAULT '{}'::json
);

CREATE INDEX IF NOT EXISTS idx_cost_audits_namespace ON cost_audits(namespace);
CREATE INDEX IF NOT EXISTS idx_cost_audits_timestamp ON cost_audits(timestamp);

-- Usage quota: tracks monthly investigation and Slack usage
CREATE TABLE IF NOT EXISTS usage_quota (
    id                   UUID    PRIMARY KEY DEFAULT gen_random_uuid(),
    month                VARCHAR NOT NULL UNIQUE,  -- "2026-06"
    tier                 VARCHAR NOT NULL DEFAULT 'free',
    investigation_count  INTEGER NOT NULL DEFAULT 0,
    investigation_limit  INTEGER NOT NULL DEFAULT 50,
    slack_count          INTEGER NOT NULL DEFAULT 0,
    slack_limit          INTEGER NOT NULL DEFAULT 5,
    created_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at           TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Alerts history: stores every notification sent by the platform
CREATE TABLE IF NOT EXISTS alerts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    cluster_name VARCHAR NOT NULL DEFAULT 'default',
    check_name VARCHAR,
    severity VARCHAR NOT NULL DEFAULT 'info',
    title VARCHAR,
    text TEXT NOT NULL,
    source VARCHAR NOT NULL DEFAULT 'scheduler',
    notified BOOLEAN DEFAULT FALSE,
    delivery_status VARCHAR DEFAULT 'sent'
);

CREATE INDEX IF NOT EXISTS idx_alerts_timestamp ON alerts(timestamp);
CREATE INDEX IF NOT EXISTS idx_alerts_check_name ON alerts(check_name);
