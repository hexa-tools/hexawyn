-- v001: Initial schema — incidents, topology_snapshots, security_audits
-- Applied: initial release
CREATE TABLE IF NOT EXISTS incidents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    age_days INTEGER GENERATED ALWAYS AS (
        DATEDIFF('day', timestamp, now())
    ) VIRTUAL,
    cluster_name VARCHAR NOT NULL,
    tool_name VARCHAR NOT NULL,
    cause TEXT,
    symptoms TEXT[],
    solution TEXT,
    severity VARCHAR DEFAULT 'low',
    feedback INTEGER DEFAULT 0,
    weight FLOAT DEFAULT 1.0,
    embedding FLOAT[768],
    retained_until TIMESTAMPTZ DEFAULT now() + INTERVAL '90 days',
    sanitized BOOLEAN DEFAULT false
);

CREATE TABLE IF NOT EXISTS topology_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    cluster_name VARCHAR NOT NULL,
    snapshot JSON NOT NULL
);

CREATE TABLE IF NOT EXISTS security_audits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    cluster_name VARCHAR NOT NULL,
    findings JSON NOT NULL,
    severity VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER PRIMARY KEY,
    applied_at TIMESTAMPTZ DEFAULT now(),
    description VARCHAR
);

INSERT INTO schema_version (version, description) VALUES (1, 'Initial schema');
