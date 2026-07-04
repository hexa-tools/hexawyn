"""Centralized constants for hexawyn — single source of truth.

All magic numbers, thresholds, and cross-file duplicated values
consolidated into typed module-level constants and dataclasses.
"""

from dataclasses import dataclass

# ── Version & URLs ──────────────────────────────────────────────
VERSION: str = "0.1.0b0"
PRICING_URL: str = "https://hexawyn.com/pricing"
TELEMETRY_URL: str = "https://api.hexawyn.com/v1/telemetry"

# ── Kubernetes ──────────────────────────────────────────────────
K8S_API_TIMEOUT_SECONDS: int = 5
HEALTHY_POD_STATUSES: frozenset[str] = frozenset({"Running", "Succeeded"})
POD_CACHE_TTL_SECONDS: float = 5.0

# ── Cache ───────────────────────────────────────────────────────
CACHE_TTL_SECONDS: int = 300

# ── Health Scoring ──────────────────────────────────────────────
MAX_HEALTH_SCORE: int = 100
CRITICAL_FINDING_PENALTY: int = 30
WARNING_FINDING_PENALTY: int = 10
HEALTH_SCORE_GREEN_THRESHOLD: int = 80
HEALTH_SCORE_YELLOW_THRESHOLD: int = 50

# ── UI ──────────────────────────────────────────────────────────
MAX_SUGGESTION_CHIPS: int = 4
MAX_TOP_ISSUES: int = 2

# ── Quota ───────────────────────────────────────────────────────
QUOTA_LOW_WARNING_THRESHOLD: int = 5

# ── VSS / DuckDB ────────────────────────────────────────────────
DEFAULT_VSS_LIMIT: int = 5
DEFAULT_VSS_MIN_SCORE: float = 0.80

# ── Cryptography ────────────────────────────────────────────────
AES_256_KEY_LENGTH: int = 32
SALT_SIZE: int = 32
PBKDF2_ITERATIONS: int = 600_000
AES_GCM_NONCE_SIZE: int = 12
AES_GCM_MIN_ENCRYPTED_LENGTH: int = 13

# ── MCP Server ──────────────────────────────────────────────────
DEFAULT_MCP_PORT: int = 8000
DEFAULT_MCP_HOST: str = "0.0.0.0"

# ── Log Search ──────────────────────────────────────────────────
DEFAULT_LOG_SEARCH_WINDOW_MINUTES: int = 15


@dataclass(frozen=True)
class QuotaConstants:
    """Per-tier quota limits."""

    free_monthly_investigations: int = 50
    free_monthly_slack_alerts: int = 5
    free_history_days: int = 7
    dev_monthly_investigations: int = 200
    dev_monthly_slack_alerts: int = 50
    dev_history_days: int = 30
    startup_monthly_investigations: int = 500
    startup_history_days: int = 90
    unlimited_sentinel: int = -1


@dataclass(frozen=True)
class LogAnalysisConstants:
    """Thresholds and limits for log analysis strategies."""

    streaming_chunk_size: int = 5000
    streaming_min_lines: int = 10000
    smart_summary_min_lines: int = 50000
    hybrid_min_lines: int = 20000
    max_summary_items: int = 10
    default_log_lines: int = 10000
    token_budget: int = 150000
    token_safety_buffer: float = 0.8
    max_extrapolation_factor: float = 3.0
    token_sample_max_lines: int = 100
    chars_per_token_divisor: float = 4.0


@dataclass(frozen=True)
class EventAnalysisConstants:
    """Thresholds for Kubernetes event analysis and correlation."""

    correlation_time_window_minutes: int = 5
    failure_cascade_window_minutes: int = 30
    failure_cascade_min_events: int = 3
    max_correlated_events: int = 10
    temporal_anomaly_zscore_threshold: float = 2.5
    min_data_points_for_anomaly: int = 5


@dataclass(frozen=True)
class LogAnomalyDetectionConstants:
    """Thresholds for statistical + ML log anomaly detection (ECA-14)."""

    zscore_threshold: float = 3.0
    min_lines_for_analysis: int = 100
    low_confidence_line_window: int = 10
    isolation_forest_contamination: float = 0.05
    isolation_forest_random_state: int = 42
    isolation_forest_min_samples: int = 10
    isolation_forest_min_score_deviation: float = 1.5


@dataclass(frozen=True)
class NamespaceEventsConstants:
    """Thresholds for the namespace Warning/Error events triage use case (ECA-5)."""

    recurring_count_threshold: int = 5
    top_n_default: int = 20
    urgency_recent_window_seconds: int = 60


@dataclass(frozen=True)
class AdvancedEventAnalyticsConstants:
    """Thresholds for the 6h advanced namespace event analytics report (ECA-19/ECA-20)."""

    storm_min_events: int = 50
    storm_window_seconds: int = 120
    top_reasons_limit: int = 5
    sampling_threshold: int = 5000
    sample_events_per_incident: int = 50


@dataclass(frozen=True)
class PipelineFailureAnalysisConstants:
    """Thresholds for automated pipeline failure RCA (ECA-8/ECA-11)."""

    flaky_test_min_failures: int = 3
    flaky_test_window_runs: int = 5


@dataclass(frozen=True)
class IncidentTriageConstants:
    """Thresholds for the incident triage/RCA report (composes ECA-19 events,
    ECA-14 log analysis, pipeline-failure RCA, and pod status)."""

    default_time_window_minutes: int = 120
    ntp_drift_threshold_seconds: int = 30
    max_pods_logs_fetched: int = 5


@dataclass(frozen=True)
class MetricsQueryConstants:
    """Thresholds for PromQL instant/range query execution."""

    max_results: int = 10000
    default_step: str = "15s"
    default_timeout_seconds: float = 15.0


@dataclass(frozen=True)
class LabelSearchConstants:
    """Thresholds for label-selector-based resource search across resource kinds."""

    max_results: int = 500


@dataclass(frozen=True)
class LogSearchConstants:
    """Thresholds for pattern-based pod log search across all namespaces."""

    max_lines_per_pod: int = 5
    max_tail_lines: int = 5000
    semantic_similarity_threshold: float = 0.5
    default_time_window_minutes: int = 60


@dataclass(frozen=True)
class NamespaceOverviewConstants:
    """Thresholds for the conservative (token-budgeted) namespace overview."""

    default_max_tokens: int = 2000
    chars_per_token_divisor: float = 4.0


@dataclass(frozen=True)
class PodAnomalyDetectionConstants:
    """Thresholds for pod metrics anomaly detection vs 7-day baseline
    (Z-score + Isolation Forest dual detection)."""

    zscore_threshold: float = 3.0
    zscore_high_threshold: float = 4.0
    zscore_critical_threshold: float = 5.0
    isolation_forest_contamination: float = 0.05
    isolation_forest_random_state: int = 42
    isolation_forest_min_samples: int = 10
    isolation_forest_min_score_deviation: float = 1.5
    min_pod_age_hours_for_baseline: float = 24.0
    default_baseline_window_days: int = 7
    recent_window_hours: float = 6.0


@dataclass(frozen=True)
class SemanticSearchConstants:
    """Thresholds for semantic search and intent classification."""

    default_vss_limit: int = 5
    default_vss_min_score: float = 0.80
    max_retries: int = 3
    max_suggestions: int = 4


@dataclass(frozen=True)
class LicenseConstants:
    """Default license claim values and durations."""

    default_clusters_max: int = 1
    default_users_max: int = 1
    default_investigations_monthly: int = 50
    default_history_days: int = 7
    default_providers: frozenset[str] = frozenset({"vanilla"})
    jwt_leeway_seconds: int = 300


@dataclass(frozen=True)
class ScoringConstants:
    """Thresholds for RCA confidence scoring and impact assessment."""

    base_confidence: float = 0.5
    logs_analyzed_weight: float = 0.2
    root_cause_found_weight: float = 0.2
    timeline_available_weight: float = 0.1
    max_confidence: float = 1.0

    confidence_high_threshold: float = 0.8
    confidence_medium_threshold: float = 0.5

    base_impact: float = 5.0
    affected_task_weight: float = 0.5
    related_incident_weight: float = 1.0
    timeline_event_weight: float = 0.2
    max_impact: float = 10.0
    min_impact: float = 1.0

    impact_critical_threshold: float = 8.0
    impact_high_threshold: float = 6.0
    impact_medium_threshold: float = 4.0

    combined_confidence_weight: float = 0.4
    combined_impact_weight: float = 0.6

    severity_critical_threshold: float = 0.85
    severity_high_threshold: float = 0.7
    severity_medium_threshold: float = 0.5

    cascade_high_threshold: int = 10
    cascade_medium_threshold: int = 5


@dataclass(frozen=True)
class PodPrioritizationConstants:
    """Score weights for pod prioritization in log processing."""

    failed_status_score: int = 100
    pending_status_score: int = 50
    other_status_score: int = 25
    restart_weight: int = 10
    max_restart_bonus: int = 30


@dataclass(frozen=True)
class AdaptiveInvestigationConstants:
    """Thresholds for adaptive namespace investigation drill-down."""

    default_depth: int = 3
    max_events_per_resource: int = 5
    max_log_lines_per_resource: int = 20
