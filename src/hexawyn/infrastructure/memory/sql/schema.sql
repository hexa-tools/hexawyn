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
    embedding FLOAT[1536],
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

-- Usage quota: tracks monthly investigation and Slack usage
CREATE TABLE IF NOT EXISTS usage_quota (
    id                UUID    PRIMARY KEY DEFAULT gen_random_uuid(),
    month             VARCHAR NOT NULL UNIQUE,
    investigation_count  INTEGER NOT NULL DEFAULT 0,
    investigation_limit  INTEGER NOT NULL DEFAULT 50,
    slack_count       INTEGER NOT NULL DEFAULT 0,
    slack_limit       INTEGER NOT NULL DEFAULT 5,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);
