SELECT
    id,
    timestamp,
    age_days,
    cluster_name,
    namespace,
    resource_name,
    resource_kind,
    tool_name,
    cause,
    solution,
    severity,
    weight,
    array_cosine_similarity(embedding, ?::FLOAT[?]) * weight
        / ln(age_days + 2) AS score
FROM incidents
WHERE cluster_name = ?
  AND timestamp > now() - (INTERVAL '1' DAY * ?)
  AND retained_until > now()
  AND sanitized = false
ORDER BY score DESC
LIMIT ?;
