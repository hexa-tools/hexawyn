CREATE INDEX IF NOT EXISTS idx_incidents_embedding
ON incidents
USING HNSW (embedding)
WITH (metric = 'cosine');
