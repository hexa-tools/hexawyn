CREATE TABLE IF NOT EXISTS cache_investigations (
    id VARCHAR PRIMARY KEY,
    cache_key VARCHAR NOT NULL,
    finding_type VARCHAR NOT NULL,
    root_cause TEXT NOT NULL,
    recommendation TEXT NOT NULL,
    severity VARCHAR NOT NULL,
    cluster_name VARCHAR NOT NULL,
    namespace VARCHAR NOT NULL,
    resource_name VARCHAR NOT NULL,
    resource_kind VARCHAR NOT NULL,
    pod_status_at_cache_time VARCHAR NOT NULL,
    pod_restart_count_at_cache INTEGER NOT NULL,
    tool_name VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    sanitized BOOLEAN NOT NULL DEFAULT TRUE
)
