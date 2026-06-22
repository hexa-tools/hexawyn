# DuckDB Schema — Tables and VSS Search

hexawyn uses DuckDB for persistent memory: storing past investigations, vector similarity search (VSS), and quota tracking.

## Incidents Table

Stores all investigation results with embeddings for similarity search.

```sql
CREATE TABLE IF NOT EXISTS incidents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT now(),
    retained_until TIMESTAMPTZ NOT NULL DEFAULT now() + INTERVAL '90 days',
    age_days INTEGER GENERATED ALWAYS AS (DATEDIFF('day', timestamp, now())) VIRTUAL,
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
    embedding DOUBLE[1536],
    sanitized BOOLEAN DEFAULT false
);
```

## VSS Search Query (Recency-Weighted)

```sql
SELECT id, timestamp, age_days, cluster_name, namespace,
       resource_name, resource_kind, tool_name, cause,
       solution, severity, weight,
       array_cosine_similarity(embedding, ?::DOUBLE[1536]) * weight
           / ln(age_days + 2) AS score
FROM incidents
WHERE cluster_name = ?
  AND timestamp > now() - INTERVAL '7' DAY
  AND retained_until > now()
  AND sanitized = false
ORDER BY score DESC
LIMIT 5;
```

## Usage Quota Table

```sql
CREATE TABLE IF NOT EXISTS usage_quota (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    month VARCHAR NOT NULL UNIQUE,
    investigation_count INTEGER NOT NULL DEFAULT 0,
    investigation_limit INTEGER NOT NULL DEFAULT 50,
    slack_count INTEGER NOT NULL DEFAULT 0,
    slack_limit INTEGER NOT NULL DEFAULT 5,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## HNSW Index

```sql
CREATE INDEX IF NOT EXISTS idx_incidents_embedding
ON incidents USING HNSW (embedding)
WITH (metric = 'cosine');
```

## Key Points

- **text-embedding-3-small**: 1536-dimensional embeddings for VSS via HNSW index with cosine similarity
- **Recency weighting**: `score / ln(age_days + 2)` — today's incidents score higher than old ones
- **History limits**: Free tier = 7 days (`INTERVAL '7' DAY`), Pro tier = 90 days
- **TTL**: `retained_until` defaults to 90 days — older incidents are filtered by `retained_until > now()`
- **Quota**: usage_quota uses ON CONFLICT upsert — a single row per month, incremented atomically
