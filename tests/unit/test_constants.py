"""Unit tests for hexawyn centralized constants."""

import dataclasses

import pytest

from hexawyn.domain.models.constants import (
    AES_256_KEY_LENGTH,
    AES_GCM_NONCE_SIZE,
    CACHE_TTL_SECONDS,
    CRITICAL_FINDING_PENALTY,
    DEFAULT_LOG_SEARCH_WINDOW_MINUTES,
    DEFAULT_MCP_PORT,
    DEFAULT_VSS_LIMIT,
    DEFAULT_VSS_MIN_SCORE,
    HEALTH_SCORE_GREEN_THRESHOLD,
    HEALTH_SCORE_YELLOW_THRESHOLD,
    HEALTHY_POD_STATUSES,
    K8S_API_TIMEOUT_SECONDS,
    MAX_HEALTH_SCORE,
    MAX_SUGGESTION_CHIPS,
    MAX_TOP_ISSUES,
    PBKDF2_ITERATIONS,
    PRICING_URL,
    QUOTA_LOW_WARNING_THRESHOLD,
    SALT_SIZE,
    VERSION,
    WARNING_FINDING_PENALTY,
    EventAnalysisConstants,
    LogAnalysisConstants,
    PodPrioritizationConstants,
    QuotaConstants,
    ScoringConstants,
)


class TestVersionAndUrls:
    def test_version_is_string(self) -> None:
        assert isinstance(VERSION, str)
        assert len(VERSION) > 0

    def test_pricing_url_is_https(self) -> None:
        assert PRICING_URL.startswith("https://")


class TestKubernetesConstants:
    def test_k8s_api_timeout_positive(self) -> None:
        assert K8S_API_TIMEOUT_SECONDS > 0

    def test_healthy_pod_statuses_is_frozenset(self) -> None:
        assert isinstance(HEALTHY_POD_STATUSES, frozenset)
        assert "Running" in HEALTHY_POD_STATUSES
        assert "Succeeded" in HEALTHY_POD_STATUSES


class TestCacheConstants:
    def test_cache_ttl_positive(self) -> None:
        assert CACHE_TTL_SECONDS > 0
        assert CACHE_TTL_SECONDS == 300


class TestHealthScoringConstants:
    def test_max_health_score_is_100(self) -> None:
        assert MAX_HEALTH_SCORE == 100

    def test_critical_penalty_greater_than_warning(self) -> None:
        assert CRITICAL_FINDING_PENALTY > WARNING_FINDING_PENALTY

    def test_green_above_yellow(self) -> None:
        assert HEALTH_SCORE_GREEN_THRESHOLD > HEALTH_SCORE_YELLOW_THRESHOLD

    def test_scores_within_range(self) -> None:
        assert 0 <= MAX_HEALTH_SCORE <= 100
        assert 0 <= HEALTH_SCORE_GREEN_THRESHOLD <= 100
        assert 0 <= HEALTH_SCORE_YELLOW_THRESHOLD <= 100

    def test_penalties_do_not_exceed_max_score(self) -> None:
        assert CRITICAL_FINDING_PENALTY <= MAX_HEALTH_SCORE
        assert WARNING_FINDING_PENALTY <= CRITICAL_FINDING_PENALTY


class TestUiConstants:
    def test_max_suggestion_chips_positive(self) -> None:
        assert MAX_SUGGESTION_CHIPS > 0
        assert MAX_SUGGESTION_CHIPS == 4

    def test_max_top_issues_positive(self) -> None:
        assert MAX_TOP_ISSUES > 0
        assert MAX_TOP_ISSUES == 2


class TestQuotaConstants:
    def test_quota_low_warning_positive(self) -> None:
        assert QUOTA_LOW_WARNING_THRESHOLD > 0
        assert QUOTA_LOW_WARNING_THRESHOLD == 5

    def test_quota_dataclass_defaults(self) -> None:
        q = QuotaConstants()
        assert q.free_monthly_investigations == 50
        assert q.free_monthly_slack_alerts == 5
        assert q.free_history_days == 7
        assert q.dev_monthly_investigations == 200
        assert q.dev_history_days == 30
        assert q.startup_monthly_investigations == 500
        assert q.startup_history_days == 90
        assert q.unlimited_sentinel == -1


class TestVssConstants:
    def test_default_limit_positive(self) -> None:
        assert DEFAULT_VSS_LIMIT > 0
        assert DEFAULT_VSS_LIMIT == 5

    def test_default_min_score_between_zero_and_one(self) -> None:
        assert 0.0 <= DEFAULT_VSS_MIN_SCORE <= 1.0
        assert DEFAULT_VSS_MIN_SCORE == 0.80


class TestCryptoConstants:
    def test_aes_key_length_is_32(self) -> None:
        assert AES_256_KEY_LENGTH == 32

    def test_salt_size_matches_key_length(self) -> None:
        assert SALT_SIZE == AES_256_KEY_LENGTH

    def test_pbkdf2_iterations_minimum(self) -> None:
        assert PBKDF2_ITERATIONS >= 100_000

    def test_nonce_size_is_12(self) -> None:
        assert AES_GCM_NONCE_SIZE == 12


class TestMcpConstants:
    def test_default_port_in_range(self) -> None:
        assert 1 <= DEFAULT_MCP_PORT <= 65535
        assert DEFAULT_MCP_PORT == 8000


class TestLogSearchConstants:
    def test_default_window_minutes_positive(self) -> None:
        assert DEFAULT_LOG_SEARCH_WINDOW_MINUTES > 0
        assert DEFAULT_LOG_SEARCH_WINDOW_MINUTES == 15


class TestLogAnalysisConstants:
    def test_defaults(self) -> None:
        lac = LogAnalysisConstants()
        assert lac.streaming_chunk_size == 5000
        assert lac.streaming_min_lines == 10000
        assert lac.smart_summary_min_lines == 50000
        assert lac.hybrid_min_lines == 20000
        assert lac.max_summary_items == 10
        assert lac.default_log_lines == 10000
        assert lac.token_budget == 150000
        assert lac.token_safety_buffer == 0.8
        assert lac.token_sample_max_lines == 100
        assert lac.chars_per_token_divisor == 4.0

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(LogAnalysisConstants)


class TestEventAnalysisConstants:
    def test_defaults(self) -> None:
        eac = EventAnalysisConstants()
        assert eac.correlation_time_window_minutes == 5
        assert eac.failure_cascade_window_minutes == 30
        assert eac.failure_cascade_min_events == 3
        assert eac.max_correlated_events == 10
        assert eac.temporal_anomaly_zscore_threshold == 2.5

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(EventAnalysisConstants)


class TestScoringConstants:
    def test_defaults(self) -> None:
        sc = ScoringConstants()
        assert sc.base_confidence == 0.5
        assert sc.max_confidence == 1.0
        assert sc.confidence_high_threshold == 0.8
        assert sc.confidence_medium_threshold == 0.5
        assert sc.base_impact == 5.0
        assert sc.max_impact == 10.0
        assert sc.min_impact == 1.0
        assert sc.impact_critical_threshold == 8.0
        assert sc.impact_medium_threshold == 4.0
        assert sc.combined_confidence_weight == 0.4
        assert sc.combined_impact_weight == 0.6
        assert sc.severity_critical_threshold == 0.85
        assert sc.cascade_high_threshold == 10
        assert sc.cascade_medium_threshold == 5

    def test_weights_sum_is_one(self) -> None:
        sc = ScoringConstants()
        total = (
            sc.base_confidence
            + sc.logs_analyzed_weight
            + sc.root_cause_found_weight
            + sc.timeline_available_weight
        )
        assert total == pytest.approx(1.0)

    def test_combined_weights_sum_is_one(self) -> None:
        sc = ScoringConstants()
        assert sc.combined_confidence_weight + sc.combined_impact_weight == 1.0

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(ScoringConstants)


class TestPodPrioritizationConstants:
    def test_defaults(self) -> None:
        ppc = PodPrioritizationConstants()
        assert ppc.failed_status_score == 100
        assert ppc.pending_status_score == 50
        assert ppc.other_status_score == 25
        assert ppc.restart_weight == 10
        assert ppc.max_restart_bonus == 30

    def test_failed_higher_than_pending(self) -> None:
        ppc = PodPrioritizationConstants()
        assert ppc.failed_status_score > ppc.pending_status_score
        assert ppc.pending_status_score > ppc.other_status_score

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(PodPrioritizationConstants)
