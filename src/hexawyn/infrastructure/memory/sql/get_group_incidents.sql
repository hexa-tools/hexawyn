SELECT id
FROM incidents
WHERE namespace = ?
  AND resource_name = ?
  AND tool_name = ?
  AND cluster_name = ?
  AND timestamp > now() - (INTERVAL '1' DAY * ?)
  AND consolidated_knowledge_id IS NULL
ORDER BY timestamp ASC;
