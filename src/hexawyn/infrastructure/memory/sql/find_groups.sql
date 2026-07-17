SELECT namespace, resource_name, tool_name, COUNT(*) AS cnt
FROM incidents
WHERE cause IS NOT NULL
  AND cause != ''
  AND cluster_name = ?
  AND timestamp > now() - (INTERVAL '1' DAY * ?)
  AND consolidated_knowledge_id IS NULL
GROUP BY namespace, resource_name, tool_name
HAVING COUNT(*) >= ?
ORDER BY cnt DESC;
