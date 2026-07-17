"""Unit tests for incident triage/RCA report domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.incident_triage import (
    ImpactAssessment,
    IncidentCauseCategory,
    IncidentTriageReport,
    IncidentTriageRequest,
    RootCauseCandidate,
    TimelineEntry,
)


class TestIncidentCauseCategory:
    def test_expected_members(self) -> None:
        assert IncidentCauseCategory.DATABASE.value == "database"
        assert IncidentCauseCategory.RESOURCE_EXHAUSTION.value == "resource_exhaustion"
        assert IncidentCauseCategory.NETWORK.value == "network"
        assert IncidentCauseCategory.IMAGE_OR_CONFIG.value == "image_or_config"
        assert IncidentCauseCategory.DEPLOYMENT.value == "deployment"
        assert IncidentCauseCategory.UNKNOWN.value == "unknown"


class TestTimelineEntry:
    def test_fields(self) -> None:
        entry = TimelineEntry(
            timestamp="2024-06-01T14:15:00Z",
            source="event",
            namespace="payment",
            object="payment-db",
            reason="FailedConnect",
            message="connection pool exhausted",
            severity="Warning",
        )
        assert entry.timestamp == "2024-06-01T14:15:00Z"
        assert entry.source == "event"
        assert entry.object == "payment-db"


class TestRootCauseCandidate:
    def test_defaults(self) -> None:
        candidate = RootCauseCandidate(
            description="database issue on payment-db",
            category=IncidentCauseCategory.DATABASE,
            confidence=0.85,
        )
        assert candidate.evidence == []
        assert candidate.involved_objects == []


class TestImpactAssessment:
    def test_defaults(self) -> None:
        impact = ImpactAssessment()
        assert impact.affected_services == []
        assert impact.estimated_user_impact == ""
        assert impact.duration_minutes == 0
        assert impact.ongoing is False


class TestIncidentTriageRequest:
    def test_defaults(self) -> None:
        request = IncidentTriageRequest(namespace="payment")
        assert request.time_window_minutes == 120
        assert request.related_namespaces == []

    def test_custom_values(self) -> None:
        request = IncidentTriageRequest(
            namespace="payment", time_window_minutes=60, related_namespaces=["billing"]
        )
        assert request.time_window_minutes == 60
        assert request.related_namespaces == ["billing"]


class TestIncidentTriageReport:
    def test_defaults(self) -> None:
        report = IncidentTriageReport(namespace="payment", time_window_minutes=120)
        assert report.timeline == []
        assert report.root_causes == []
        assert report.remediation_steps == []
        assert report.resolved is False
        assert report.resolution_time is None
        assert report.mttr_minutes is None
        assert report.ntp_drift_detected is False
        assert report.cross_namespace_correlation == []
        assert report.insufficient_data is False
        assert report.data_checked == []

    def test_with_root_causes(self) -> None:
        candidate = RootCauseCandidate(
            description="database issue on payment-db",
            category=IncidentCauseCategory.DATABASE,
            confidence=0.85,
        )
        report = IncidentTriageReport(
            namespace="payment", time_window_minutes=120, root_causes=[candidate]
        )
        assert len(report.root_causes) == 1
        assert report.root_causes[0].category == IncidentCauseCategory.DATABASE
