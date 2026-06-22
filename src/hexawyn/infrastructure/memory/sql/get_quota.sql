SELECT
    id,
    month,
    investigation_count,
    investigation_limit,
    slack_count,
    slack_limit,
    created_at,
    updated_at
FROM usage_quota
WHERE month = ?
LIMIT 1;
