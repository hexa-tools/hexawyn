UPDATE incidents
SET consolidated_knowledge_id = ?, consolidated_at = now()
WHERE id IN (SELECT unnest(?::UUID[]));
