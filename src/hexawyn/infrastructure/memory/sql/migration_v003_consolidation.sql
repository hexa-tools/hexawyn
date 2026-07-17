ALTER TABLE incidents ADD COLUMN IF NOT EXISTS consolidated_knowledge_id UUID;
ALTER TABLE incidents ADD COLUMN IF NOT EXISTS consolidated_at TIMESTAMPTZ;
