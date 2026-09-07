SELECT
    id, pattern, resource_name, resource_kind, namespace, tool_name,
    occurrence_count, first_seen, last_seen, weight, confidence,
    array_cosine_similarity(embedding, ?::FLOAT[768]) * weight AS score
FROM consolidated_knowledge
WHERE cluster_name = ?
  AND embedding IS NOT NULL
ORDER BY score DESC
LIMIT ?;
