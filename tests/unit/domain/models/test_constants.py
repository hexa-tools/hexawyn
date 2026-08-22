"""Tests for domain/models/constants.py — all constants, their types and values."""

from __future__ import annotations

import hexawyn.domain.models.constants as c
import pytest


class TestVersionAndUrls:
    def test_version_is_string(self) -> None:
        assert c.VERSION == "0.1.0b6"

    def test_pricing_url(self) -> None:
        assert c.PRICING_URL.startswith("https://")

    def test_telemetry_url(self) -> None:
        assert c.TELEMETRY_URL.startswith("https://")


class TestKubernetesConstants:
    def test_k8s_api_timeout(self) -> None:
        assert c.K8S_API_TIMEOUT_SECONDS == 5  # noqa: PLR2004

    def test_stuck_pipeline_threshold(self) -> None:
        assert c.STUCK_PIPELINE_RUN_THRESHOLD_SECONDS == 3600  # noqa: PLR2004

    def test_pipeline_outlier_threshold(self) -> None:
        assert c.PIPELINE_OUTLIER_THRESHOLD == 2.0  # noqa: PLR2004

    def test_pipeline_run_status_priority(self) -> None:
        assert c.PIPELINE_RUN_STATUS_PRIORITY == {"Failed": 0, "Running": 1, "Succeeded": 2}

    def test_hours_per_month(self) -> None:
        assert c.HOURS_PER_MONTH == 730  # noqa: PLR2004

    def test_healthy_pod_statuses(self) -> None:
        assert "Running" in c.HEALTHY_POD_STATUSES
        assert "Failed" not in c.HEALTHY_POD_STATUSES

    def test_pod_unhealthy_order(self) -> None:
        assert c.POD_UNHEALTHY_ORDER["CrashLoopBackOff"] == 0
        assert c.POD_UNHEALTHY_ORDER["Error"] == 1
        assert c.POD_UNHEALTHY_ORDER["Terminating"] == 4  # noqa: PLR2004

    def test_pod_cache_ttl(self) -> None:
        assert c.POD_CACHE_TTL_SECONDS == 5.0  # noqa: PLR2004


class TestCache:
    def test_cache_ttl(self) -> None:
        assert c.CACHE_TTL_SECONDS == 300  # noqa: PLR2004


class TestHealthScoring:
    def test_all_thresholds(self) -> None:
        assert c.MAX_HEALTH_SCORE == 100  # noqa: PLR2004
        assert c.CRITICAL_FINDING_PENALTY == 30  # noqa: PLR2004
        assert c.WARNING_FINDING_PENALTY == 10  # noqa: PLR2004
        assert c.HEALTH_SCORE_GREEN_THRESHOLD == 80  # noqa: PLR2004
        assert c.HEALTH_SCORE_YELLOW_THRESHOLD == 50  # noqa: PLR2004


class TestUI:
    def test(self) -> None:
        assert c.MAX_SUGGESTION_CHIPS == 4  # noqa: PLR2004
        assert c.MAX_TOP_ISSUES == 2  # noqa: PLR2004


class TestQuota:
    def test_quota_warning(self) -> None:
        assert c.QUOTA_LOW_WARNING_THRESHOLD == 5  # noqa: PLR2004


class TestVSS:
    def test(self) -> None:
        assert c.DEFAULT_VSS_LIMIT == 5  # noqa: PLR2004
        assert c.DEFAULT_VSS_MIN_SCORE == 0.80  # noqa: PLR2004


class TestCrypto:
    def test(self) -> None:
        assert c.AES_256_KEY_LENGTH == 32  # noqa: PLR2004
        assert c.SALT_SIZE == 32  # noqa: PLR2004
        assert c.PBKDF2_ITERATIONS == 600_000  # noqa: PLR2004
        assert c.AES_GCM_NONCE_SIZE == 12  # noqa: PLR2004
        assert c.AES_GCM_MIN_ENCRYPTED_LENGTH == 13  # noqa: PLR2004


class TestMCP:
    def test(self) -> None:
        assert c.DEFAULT_MCP_PORT == 8000  # noqa: PLR2004
        assert c.DEFAULT_MCP_HOST == "0.0.0.0"


class TestLogSearch:
    def test(self) -> None:
        assert c.DEFAULT_LOG_SEARCH_WINDOW_MINUTES == 15  # noqa: PLR2004


class TestDataClasses:
    def test_quota_constants(self) -> None:
        qc = c.QuotaConstants()
        assert qc.free_monthly_investigations == 50  # noqa: PLR2004
        assert qc.free_history_days == 7  # noqa: PLR2004
        assert qc.unlimited_sentinel == -1

    def test_log_analysis_constants(self) -> None:
        lac = c.LogAnalysisConstants()
        assert lac.streaming_chunk_size == 5000  # noqa: PLR2004
        assert lac.token_budget == 150000  # noqa: PLR2004

    def test_log_anomaly_detection_constants(self) -> None:
        ldc = c.LogAnomalyDetectionConstants()
        assert ldc.zscore_threshold == 3.0  # noqa: PLR2004

    def test_scoring_constants(self) -> None:
        sc = c.ScoringConstants()
        assert sc.base_confidence > 0
        assert sc.max_confidence > sc.base_confidence

    def test_pod_prioritization_constants(self) -> None:
        pp = c.PodPrioritizationConstants()
        assert isinstance(pp.failed_status_score, int)
        assert isinstance(pp.other_status_score, int)

    def test_adaptive_investigation_constants(self) -> None:
        ai = c.AdaptiveInvestigationConstants()
        assert isinstance(ai.default_depth, int)

    def test_image_vulnerability_constants(self) -> None:
        iv = c.ImageVulnerabilityConstants()
        assert isinstance(iv.production_namespace, str)

    def test_pod_security_constants(self) -> None:
        ps = c.PodSecurityConstants()
        assert isinstance(ps.high_severity_capabilities, tuple)

    def test_network_policy_constants(self) -> None:
        np = c.NetworkPolicyConstants()
        assert isinstance(np.system_namespaces, tuple)

    def test_all_dataclasses_instantiable(self) -> None:
        classes = [
            c.QuotaConstants,
            c.LogAnalysisConstants,
            c.EventAnalysisConstants,
            c.LogAnomalyDetectionConstants,
            c.NamespaceEventsConstants,
            c.AdvancedEventAnalyticsConstants,
            c.PipelineFailureAnalysisConstants,
            c.IncidentTriageConstants,
            c.MetricsQueryConstants,
            c.LabelSearchConstants,
            c.LogSearchConstants,
            c.NamespaceOverviewConstants,
            c.PodAnomalyDetectionConstants,
            c.SemanticSearchConstants,
            c.LicenseConstants,
            c.ScoringConstants,
            c.PodPrioritizationConstants,
            c.AdaptiveInvestigationConstants,
            c.ClusterCapacityForecastConstants,
            c.HeadroomSimulationConstants,
            c.HotNodeAnalysisConstants,
            c.ConfigurationDriftConstants,
            c.ManualChangeDetectionConstants,
            c.RBACAuditConstants,
            c.PodSecurityConstants,
            c.ImageVulnerabilityConstants,
            c.SecretRotationConstants,
            c.NetworkPolicyConstants,
            c.ExternalExposureConstants,
        ]
        for cls in classes:
            instance = cls()
            assert isinstance(instance, cls)


def test_constants_module_is_importable() -> None:
    assert c.__doc__ is not None


@pytest.mark.parametrize(
    "const_name",
    [
        "VERSION",
        "CACHE_TTL_SECONDS",
        "MAX_HEALTH_SCORE",
        "K8S_API_TIMEOUT_SECONDS",
        "HOURS_PER_MONTH",
        "STUCK_PIPELINE_RUN_THRESHOLD_SECONDS",
        "POD_CACHE_TTL_SECONDS",
        "PIPELINE_OUTLIER_THRESHOLD",
        "PIPELINE_CANCELLED_STATUS",
        "PIPELINE_RUN_STATUS_PRIORITY",
        "HEALTHY_POD_STATUSES",
        "POD_UNHEALTHY_ORDER",
    ],
)
def test_all_constants_exist(const_name: str) -> None:
    assert hasattr(c, const_name)
