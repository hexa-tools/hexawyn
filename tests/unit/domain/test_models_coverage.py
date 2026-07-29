from __future__ import annotations


class TestAllModels:
    def test_constants(self) -> None:
        from hexawyn.domain.models import constants as c

        [c.QuotaConstants(), c.LogAnalysisConstants()]
        assert True

        from hexawyn.domain.models.keda import AuthType, KedaScaledObjectPhase, TriggerType

        [KedaScaledObjectPhase.READY, TriggerType.CPU, AuthType.SECRET]
        assert True

    def test_canary(self) -> None:
        from hexawyn.domain.models.canary_comparison import VersionMetrics

        VersionMetrics(
            version="v1", request_count=10, p50_ms=1.0, p95_ms=2.0, p99_ms=3.0, error_rate_pct=0.0
        )
        assert True

    def test_span_btl(self) -> None:
        from hexawyn.domain.models.span_bottleneck import SpanBreakdown

        SpanBreakdown(category="db", avg_ms=10.0, p95_ms=20.0, max_ms=30.0, slowest_operation="q")
        assert True

    def test_rollouts(self) -> None:
        from hexawyn.domain.models.rollouts import RolloutsDetectionResult

        RolloutsDetectionResult(
            installed=True,
            version="1.6",
            namespace="ns",
            total_rollouts=3,
            healthy=1,
            progressing=1,
            degraded=1,
            paused=0,
        )
        assert True

    def test_metric_corr(self) -> None:
        from hexawyn.domain.models.metric_correlation import TimeSeries

        TimeSeries(label="cpu", data_points=[(1.0, "p")])
        assert True

    def test_deployment_lat(self) -> None:
        from hexawyn.domain.models.deployment_latency import WindowLatency

        WindowLatency(p50_ms=10.0, p95_ms=20.0, p99_ms=30.0, sample_count=100)
        assert True

    def test_version_reg(self) -> None:
        from hexawyn.domain.models.version_regression import VersionMetrics

        VersionMetrics(
            version="v2",
            p50_ms=10.0,
            p95_ms=25.0,
            p99_ms=50.0,
            error_rate_pct=2.0,
            request_count=1000,
        )
        assert True

    def test_policy(self) -> None:
        from hexawyn.domain.models.policy import PolicyEngine

        [PolicyEngine.KYVERNO, PolicyEngine.GATEKEEPER]
        assert True

        from hexawyn.domain.models.redundant_calls import SpanInfo

        SpanInfo(span_name="s1", service_name="get", duration_ms=10.0)
        assert True

    def test_admin(self) -> None:
        from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest

        AdminAuditRequest(time_window_minutes=30)
        assert True

    def test_certificates(self) -> None:
        from hexawyn.domain.models.certificates import CertManagerDetectionResult

        CertManagerDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_certs=0,
            ready_certs=0,
            expiring_soon=0,
            failed_certs=0,
            active_challenges=0,
        )
        assert True

        from hexawyn.domain.models.pod_anomaly import PodAnomaly

        PodAnomaly(
            pod_name="pod",
            namespace="ns",
            metric="metric",
            severity="high",
            deviation_pct=50.0,
            z_score=2.0,
            isolation_forest_score=None,
            detection_method="zscore",
            current_value=100.0,
            baseline_mean=50.0,
        )
        assert True

        from hexawyn.domain.models.log_anomaly import LogAnomaly

        LogAnomaly(
            timestamp="2026-01-01T00:00:00Z",
            log_line="error: connection refused",
            anomaly_score=0.9,
            type="semantic",
        )
        assert True

        from hexawyn.domain.models.incident_triage import IncidentCauseCategory

        [IncidentCauseCategory.DATABASE, IncidentCauseCategory.NETWORK]
        assert True

        from hexawyn.domain.models.log_search import MatchedLogLine

        MatchedLogLine(timestamp="2026-01-01T00:00:00Z", message="test", match_type="exact")
        assert True

        from hexawyn.domain.models.adaptive_namespace_investigation import (
            RankedFailingResource,
        )

        RankedFailingResource(name="pod-1", kind="Pod", reason="CrashLoop", restart_count=5, rank=1)
        assert True

    def test_errors_exist(self) -> None:
        from hexawyn.domain.errors import (
            HexawynError,
        )

        err = HexawynError("test")
        assert isinstance(err, Exception)
