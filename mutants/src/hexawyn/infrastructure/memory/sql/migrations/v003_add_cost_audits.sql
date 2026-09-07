-- Migration v003: cost_audits table for namespace-level cost snapshots
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

INSERT OR REPLACE INTO schema_version (version, description)
VALUES (3, 'Add cost_audits table for namespace cost snapshots');
