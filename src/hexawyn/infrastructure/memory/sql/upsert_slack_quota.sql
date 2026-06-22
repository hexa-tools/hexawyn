INSERT INTO usage_quota (month, slack_count, slack_limit)
VALUES (?, 1, ?)
ON CONFLICT (month)
DO UPDATE SET
    slack_count = usage_quota.slack_count + 1,
    updated_at  = now();
