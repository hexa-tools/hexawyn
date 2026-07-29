from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.cache import (
    CACHE_TTL_SECONDS,
    CachedInvestigation,
    CacheEntry,
    CacheValidationResult,
)


class TestCacheEntry:
    def test_ttl_is_300_seconds(self) -> None:
        assert CACHE_TTL_SECONDS == 300  # noqa: PLR2004

    def test_is_valid_when_fresh(self) -> None:
        entry = CacheEntry(
            query_hash="abc123",
            result="CrashLoopBackOff detected",
            created_at=datetime.now(),
        )
        assert entry.is_valid is True

    def test_is_expired_when_old(self) -> None:
        entry = CacheEntry(
            query_hash="abc123",
            result="CrashLoopBackOff detected",
            created_at=datetime.now() - timedelta(seconds=301),
        )
        assert entry.is_valid is False

    def test_is_expired_exactly_at_ttl(self) -> None:
        entry = CacheEntry(
            query_hash="abc123",
            result="CrashLoopBackOff detected",
            created_at=datetime.now() - timedelta(seconds=300),
        )
        assert entry.is_valid is False

    def test_stores_result(self) -> None:
        entry = CacheEntry(query_hash="abc123", result="OOM detected", created_at=datetime.now())
        assert entry.result == "OOM detected"

    def test_stores_query_hash(self) -> None:
        entry = CacheEntry(query_hash="abc123", result="OOM detected", created_at=datetime.now())
        assert entry.query_hash == "abc123"

    def test_age_seconds_returns_positive_value(self) -> None:
        entry = CacheEntry(
            query_hash="abc123",
            result="test",
            created_at=datetime.now() - timedelta(seconds=10),
        )
        assert entry.age_seconds >= 10  # noqa: PLR2004

    def test_age_seconds_for_old_entry(self) -> None:
        entry = CacheEntry(
            query_hash="abc123",
            result="test",
            created_at=datetime.now() - timedelta(seconds=3600),
        )
        assert entry.age_seconds >= 3600  # noqa: PLR2004

    def test_is_valid_one_second_before_ttl(self) -> None:
        entry = CacheEntry(
            query_hash="abc123",
            result="test",
            created_at=datetime.now() - timedelta(seconds=299),
        )
        assert entry.is_valid is True

    def test_created_at_default_factory_is_recent(self) -> None:
        entry = CacheEntry(query_hash="abc123", result="test")
        assert entry.created_at is not None
        assert entry.age_seconds < 5  # noqa: PLR2004

    def test_age_seconds_with_future_created_at_is_negative(self) -> None:
        entry = CacheEntry(
            query_hash="abc",
            result="test",
            created_at=datetime.now() + timedelta(hours=1),
        )
        assert entry.age_seconds < 0

    def test_is_valid_true_with_future_created_at(self) -> None:
        entry = CacheEntry(
            query_hash="abc",
            result="test",
            created_at=datetime.now() + timedelta(days=30),
        )
        assert entry.is_valid is True

    def test_is_valid_false_for_extremely_old_entry(self) -> None:
        entry = CacheEntry(
            query_hash="abc",
            result="test",
            created_at=datetime.now() - timedelta(days=365),
        )
        assert entry.is_valid is False

    def test_empty_query_hash_accepted(self) -> None:
        entry = CacheEntry(query_hash="", result="test")
        assert entry.query_hash == ""
        assert entry.result == "test"

    def test_empty_result_accepted(self) -> None:
        entry = CacheEntry(query_hash="abc", result="")
        assert entry.result == ""
        assert entry.query_hash == "abc"


class TestCachedInvestigation:
    @staticmethod
    def _make_ci(**kwargs: object) -> object:
        from hexawyn.domain.models.cache import CachedInvestigation

        defaults: dict[str, object] = {
            "id": "a",
            "cache_key": "k",
            "finding_type": "t",
            "root_cause": "r",
            "recommendation": "fix",
            "severity": "low",
            "cluster_name": "prod",
            "namespace": "ns",
            "resource_name": "res",
            "resource_kind": "Deployment",
            "pod_status_at_cache_time": "Running",
            "pod_restart_count_at_cache": 0,
            "tool_name": "t",
            "created_at": datetime.now(UTC),
        }
        defaults.update(kwargs)
        return CachedInvestigation(**defaults)

    def test_constructs_with_required_fields(self) -> None:
        ci = self._make_ci()
        assert ci.id == "a"
        assert ci.finding_type == "t"
        assert ci.root_cause == "r"

    def test_default_sanitized_is_true(self) -> None:
        ci = self._make_ci()
        assert ci.sanitized is True

    def test_post_init_sets_expires_at_when_none(self) -> None:
        ci = self._make_ci()
        assert ci.expires_at is not None
        assert ci.expires_at > ci.created_at

    def test_post_init_preserves_explicit_expires_at(self) -> None:
        explicit = datetime.now() + timedelta(days=7)
        ci = self._make_ci(expires_at=explicit)
        assert ci.expires_at == explicit

    def test_is_expired_when_in_past(self) -> None:
        ci = self._make_ci(expires_at=datetime.now(UTC) - timedelta(hours=1))
        assert ci.is_expired is True

    def test_is_not_expired_when_in_future(self) -> None:
        ci = self._make_ci(expires_at=datetime.now(UTC) + timedelta(hours=6))
        assert ci.is_expired is False

    def test_is_not_expired_when_expires_at_is_none(self) -> None:
        ci = self._make_ci(expires_at=None)
        assert ci.is_expired is False

    def test_is_expired_one_second_after_expires_at(self) -> None:
        just_expired = datetime.now(UTC) - timedelta(seconds=1)
        ci = self._make_ci(expires_at=just_expired)
        assert ci.is_expired is True

    def test_is_not_expired_one_second_before_expires_at(self) -> None:
        still_valid = datetime.now(UTC) + timedelta(seconds=1)
        ci = self._make_ci(expires_at=still_valid)
        assert ci.is_expired is False

    def test_negative_restart_count_accepted(self) -> None:
        ci = self._make_ci(pod_restart_count_at_cache=-1)
        assert ci.pod_restart_count_at_cache == -1

    def test_zero_restart_count_is_valid(self) -> None:
        ci = self._make_ci(pod_restart_count_at_cache=0)
        assert ci.pod_restart_count_at_cache == 0

    def test_large_restart_count_boundary(self) -> None:
        ci = self._make_ci(pod_restart_count_at_cache=999_999)
        assert ci.pod_restart_count_at_cache == 999_999  # noqa: PLR2004

    def test_empty_fields_accepted(self) -> None:
        ci = self._make_ci(
            cache_key="",
            finding_type="",
            root_cause="",
            recommendation="",
            cluster_name="",
            namespace="",
            resource_name="",
            resource_kind="",
            tool_name="",
        )
        assert ci.cache_key == ""
        assert ci.cluster_name == ""

    def test_post_init_sets_starter_ttl_by_default(self) -> None:
        from hexawyn.domain.models.cache import _CACHE_TTL_BY_LICENSE

        starter_ttl = _CACHE_TTL_BY_LICENSE["starter"]
        ci = CachedInvestigation(
            id="abc",
            cache_key="k",
            finding_type="t",
            root_cause="r",
            recommendation="fix",
            severity="low",
            cluster_name="prod",
            namespace="ns",
            resource_name="res",
            resource_kind="Deployment",
            pod_status_at_cache_time="Running",
            pod_restart_count_at_cache=0,
            tool_name="t",
            created_at=datetime.now(UTC),
        )
        expected_expiry = ci.created_at + timedelta(seconds=starter_ttl)
        assert ci.expires_at is not None
        difference = abs((ci.expires_at - expected_expiry).total_seconds())
        assert difference < 1

    def test_post_init_uses_correct_license_ttl(self) -> None:
        from hexawyn.domain.models.cache import _CACHE_TTL_BY_LICENSE

        team_ttl = _CACHE_TTL_BY_LICENSE["team"]
        assert team_ttl == 24 * 3600
        scale_up_ttl = _CACHE_TTL_BY_LICENSE["scale_up"]
        assert scale_up_ttl == 48 * 3600

    def test_equality_same_values(self) -> None:
        now = datetime.now(UTC)
        a = self._make_ci(created_at=now)
        b = self._make_ci(created_at=now)
        assert a == b

    def test_equality_different_id(self) -> None:
        a = self._make_ci(id="id-a")
        b = self._make_ci(id="id-b")
        assert a != b


class TestCacheValidationResult:
    def test_validation_result_valid(self) -> None:
        from hexawyn.domain.models.cache import CacheValidationResult

        r = CacheValidationResult(is_valid=True, reason="VALID")
        assert r.is_valid is True
        assert r.reason == "VALID"

    def test_validation_result_invalid_ttl_expired(self) -> None:
        from hexawyn.domain.models.cache import CacheValidationResult

        r = CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")
        assert r.is_valid is False
        assert r.reason == "TTL_EXPIRED"

    def test_validation_result_invalid_pod_status_changed(self) -> None:
        from hexawyn.domain.models.cache import CacheValidationResult

        r = CacheValidationResult(is_valid=False, reason="POD_STATUS_CHANGED")
        assert r.is_valid is False

    def test_validation_result_equality(self) -> None:
        from hexawyn.domain.models.cache import CacheValidationResult

        a = CacheValidationResult(is_valid=True, reason="VALID")
        b = CacheValidationResult(is_valid=True, reason="VALID")
        c = CacheValidationResult(is_valid=False, reason="TTL_EXPIRED")
        assert a == b
        assert a != c

    def test_empty_reason_accepted(self) -> None:
        r = CacheValidationResult(is_valid=True, reason="")
        assert r.reason == ""
        assert r.is_valid is True

    def test_false_reason_is_not_none(self) -> None:
        r = CacheValidationResult(is_valid=False, reason="FORCE_REFRESH")
        assert r.is_valid is False
        assert r.reason == "FORCE_REFRESH"
