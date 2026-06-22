SELECT
    id,
    timestamp,
    age_days,
    cluster_name,
    namespace,
    tool_name,
    resource_name,
    resource_kind,
    cause,
    solution,
    severity,
    weight,
    array_cosine_similarity(embedding, ?::DOUBLE[?]) * weight
        / ln(age_days + 2) AS score
FROM incidents
WHERE cluster_name = ?
  AND retained_until > now()
  AND sanitized = false
ORDER BY score DESC
LIMIT ?
