UPDATE usage_quota
SET investigation_count = 0,
    slack_count         = 0,
    updated_at          = now()
WHERE month = ?;
