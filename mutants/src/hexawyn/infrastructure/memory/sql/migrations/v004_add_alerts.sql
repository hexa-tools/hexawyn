-- v004: Alerts history — stores every notification sent by the platform
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
