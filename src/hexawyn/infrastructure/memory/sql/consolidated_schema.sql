CREATE TABLE IF NOT EXISTS consolidated_knowledge (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pattern TEXT NOT NULL,
    resource_name VARCHAR,
    resource_kind VARCHAR,
    namespace VARCHAR,
    tool_name VARCHAR NOT NULL,
    cluster_name VARCHAR NOT NULL DEFAULT 'unknown',
    occurrence_count INTEGER NOT NULL DEFAULT 1,
    first_seen TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_seen TIMESTAMPTZ NOT NULL DEFAULT now(),
    source_incident_ids UUID[] NOT NULL,
    embedding FLOAT[768],
    weight FLOAT DEFAULT 1.0,
    confidence FLOAT DEFAULT 0.5,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now()
);
