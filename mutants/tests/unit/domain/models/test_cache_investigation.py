from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.cache import CachedInvestigation, CacheValidationResult


class TestCachedInvestigation:
    def test_default_expires_at_is_6_hours_from_created(self):
        now = datetime.now(UTC)
        entry = CachedInvestigation(
            id="a",
            cache_key="key-1",
            finding_type="CrashLoopBackOff",
            root_cause="OOM",
            recommendation="increase memory",
            severity="high",
            cluster_name="prod",
            namespace="payments",
            resource_name="api-7d9f",
            resource_kind="Pod",
            pod_status_at_cache_time="CrashLoopBackOff",
            pod_restart_count_at_cache=3,
            tool_name="investigate_pod",
            created_at=now,
        )
        assert entry.expires_at is not None
        assert entry.expires_at == now + timedelta(hours=6)

    def test_is_expired_false_when_fresh(self):
        entry = CachedInvestigation(
            id="a",
            cache_key="key-1",
            finding_type="CrashLoopBackOff",
            root_cause="OOM",
            recommendation="increase memory",
            severity="high",
            cluster_name="prod",
            namespace="payments",
            resource_name="api-7d9f",
            resource_kind="Pod",
            pod_status_at_cache_time="CrashLoopBackOff",
            pod_restart_count_at_cache=3,
            tool_name="investigate_pod",
            created_at=datetime.now(UTC),
        )
        assert entry.is_expired is False

    def test_is_expired_true_when_past_expiry(self):
        entry = CachedInvestigation(
            id="a",
            cache_key="key-1",
            finding_type="CrashLoopBackOff",
            root_cause="OOM",
            recommendation="increase memory",
            severity="high",
            cluster_name="prod",
            namespace="payments",
            resource_name="api-7d9f",
            resource_kind="Pod",
            pod_status_at_cache_time="CrashLoopBackOff",
            pod_restart_count_at_cache=3,
            tool_name="investigate_pod",
            created_at=datetime.now(UTC) - timedelta(hours=7),
        )
        assert entry.is_expired is True

    def test_sanitized_is_true_by_default(self):
        entry = CachedInvestigation(
            id="a",
            cache_key="key-1",
            finding_type="CrashLoopBackOff",
            root_cause="OOM",
            recommendation="increase memory",
            severity="high",
            cluster_name="prod",
            namespace="payments",
            resource_name="api-7d9f",
            resource_kind="Pod",
            pod_status_at_cache_time="CrashLoopBackOff",
            pod_restart_count_at_cache=3,
            tool_name="investigate_pod",
        )
        assert entry.sanitized is True


class TestCacheValidationResult:
    def test_valid_result(self):
        result = CacheValidationResult(is_valid=True, reason="VALID")
        assert result.is_valid is True
        assert result.reason == "VALID"

    def test_invalid_result_with_reason(self):
        result = CacheValidationResult(
            is_valid=False, reason="POD_STATUS_CHANGED: CrashLoopBackOff → Running"
        )
        assert result.is_valid is False
        assert "POD_STATUS_CHANGED" in result.reason
