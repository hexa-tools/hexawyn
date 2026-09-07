INSERT INTO usage_quota (month, tier, investigation_count, investigation_limit)
VALUES (?, ?, 1, ?)
ON CONFLICT (month)
DO UPDATE SET
    investigation_count = usage_quota.investigation_count + 1,
    updated_at          = now();
