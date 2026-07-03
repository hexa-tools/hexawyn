"""Unit tests for generate_incident_triage_report — automated incident triage/RCA report.

Test data mirrors the ticket's own fixture: payment namespace, 2h window,
DB connection pool exhausted at 14:15, cascaded to 3 services, resolved at
15:42 (MTTR 87 minutes).
"""

from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.domain.models.analyze_pod_logs import PodLogLine
from hexawyn.domain.models.incident_triage import IncidentCauseCategory, IncidentTriageRequest
from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.models.pipeline_failure_analysis import FailureAnalysis, FailureType
from hexawyn.domain.services.incident_triage.report_builder import generate_incident_triage_report


def _event(
    event_type: str,
    reason: str,
    message: str,
    obj: str,
    last_seen: str,
    count: int = 1,
) -> NamespaceEvent:
    return NamespaceEvent(
        event_type=event_type,
        reason=reason,
        message=message,
        object=obj,
        count=count,
        last_seen=last_seen,
    )


def _pod(name: str, status: str = "Running", restarts: int = 0) -> dict:
    return {
        "name": name,
        "namespace": "payment",
        "status": status,
        "restarts": restarts,
        "age": "2h",
        "node": "node-1",
    }


def _log_line(timestamp: str, level: str, message: str) -> PodLogLine:
    return PodLogLine(timestamp=timestamp, level=level, message=message, run_index=0, is_json=False)


def _request(
    namespace: str = "payment", related_namespaces: list[str] | None = None
) -> IncidentTriageRequest:
    return IncidentTriageRequest(
        namespace=namespace,
        time_window_minutes=120,
        related_namespaces=related_namespaces or [],
    )


_DB_CASCADE_EVENTS = [
    _event(
        "Warning",
        "FailedConnect",
        "connection pool exhausted for postgres",
        "payment-db",
        "2024-06-01T14:15:00Z",
    ),
    _event(
        "Warning",
        "BackOff",
        "Back-off restarting failed container: connection pool exhausted",
        "checkout-service-abc",
        "2024-06-01T14:16:30Z",
    ),
    _event(
        "Warning",
        "BackOff",
        "connection pool exhausted downstream",
        "orders-service-xyz",
        "2024-06-01T14:18:00Z",
    ),
    _event(
        "Warning",
        "BackOff",
        "connection pool exhausted downstream",
        "inventory-service-def",
        "2024-06-01T14:20:00Z",
    ),
]

_OBSERVED_AT = datetime(2024, 6, 1, 16, 0, 0, tzinfo=UTC)


class TestClearRootCause:
    """TC1: Clear root cause (DB down) → timeline shows cascade, remediation mentions restoring the DB."""

    def test_cascade_unified_under_single_database_root_cause(self) -> None:
        report = generate_incident_triage_report(
            request=_request(),
            events=_DB_CASCADE_EVENTS,
            pods=[_pod("payment-db"), _pod("checkout-service-abc")],
            pod_logs={},
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert len(report.root_causes) == 1
        top = report.root_causes[0]
        assert top.category == IncidentCauseCategory.DATABASE
        assert set(top.involved_objects) == {
            "payment-db",
            "checkout-service-abc",
            "orders-service-xyz",
            "inventory-service-def",
        }

    def test_timeline_shows_full_cascade_in_order(self) -> None:
        report = generate_incident_triage_report(
            request=_request(),
            events=_DB_CASCADE_EVENTS,
            pods=[],
            pod_logs={},
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        objects_in_order = [entry.object for entry in report.timeline]
        assert objects_in_order == [
            "payment-db",
            "checkout-service-abc",
            "orders-service-xyz",
            "inventory-service-def",
        ]

    def test_remediation_mentions_restoring_the_database(self) -> None:
        report = generate_incident_triage_report(
            request=_request(),
            events=_DB_CASCADE_EVENTS,
            pods=[],
            pod_logs={},
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert len(report.remediation_steps) == 1
        lowered = report.remediation_steps[0].lower()
        assert "restore" in lowered
        assert "database" in lowered

    def test_impact_assessment_lists_all_affected_services(self) -> None:
        report = generate_incident_triage_report(
            request=_request(),
            events=_DB_CASCADE_EVENTS,
            pods=[],
            pod_logs={},
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert set(report.impact.affected_services) == {
            "payment-db",
            "checkout-service-abc",
            "orders-service-xyz",
            "inventory-service-def",
        }
        assert report.impact.estimated_user_impact


class TestAmbiguousRootCause:
    """TC2: Ambiguous root cause (multiple concurrent failures) → candidates ranked by confidence."""

    def test_two_unrelated_concurrent_failures_both_ranked(self) -> None:
        events = [
            _event(
                "Warning",
                "FailedConnect",
                "database connection timeout to postgres:5432",
                "payment-db",
                "2024-06-01T14:15:00Z",
            ),
            _event(
                "Warning",
                "NetworkNotReady",
                "dial tcp: connection refused to auth-service",
                "auth-service-xyz",
                "2024-06-01T14:15:30Z",
            ),
        ]

        report = generate_incident_triage_report(
            request=_request(),
            events=events,
            pods=[],
            pod_logs={},
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert len(report.root_causes) == 2
        categories = {candidate.category for candidate in report.root_causes}
        assert categories == {IncidentCauseCategory.DATABASE, IncidentCauseCategory.NETWORK}
        confidences = [candidate.confidence for candidate in report.root_causes]
        assert confidences == sorted(confidences, reverse=True)
        assert len(report.remediation_steps) == 2


class TestResolvedIncident:
    """TC3: Incident already resolved before report generation → resolution time + MTTR."""

    def test_resolution_time_and_mttr_computed(self) -> None:
        events = [
            *_DB_CASCADE_EVENTS,
            _event(
                "Normal",
                "Started",
                "Started container payment-db",
                "payment-db",
                "2024-06-01T15:42:00Z",
            ),
        ]

        report = generate_incident_triage_report(
            request=_request(),
            events=events,
            pods=[],
            pod_logs={},
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert report.resolved is True
        assert report.resolution_time == "2024-06-01T15:42:00Z"
        assert report.mttr_minutes == 87
        assert report.impact.ongoing is False

    def test_unresolved_incident_reports_ongoing(self) -> None:
        report = generate_incident_triage_report(
            request=_request(),
            events=_DB_CASCADE_EVENTS,
            pods=[],
            pod_logs={},
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert report.resolved is False
        assert report.mttr_minutes is None
        assert report.impact.ongoing is True


class TestInsufficientData:
    """TC4: No events or logs found for the time window → 'insufficient data' + what was checked."""

    def test_empty_sources_return_insufficient_data(self) -> None:
        report = generate_incident_triage_report(
            request=_request(),
            events=[],
            pods=[],
            pod_logs={},
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert report.insufficient_data is True
        assert report.data_checked
        assert report.root_causes == []
        assert report.timeline == []


class TestPipelineFailureIntegration:
    def test_pipeline_failure_folded_in_as_root_cause_candidate(self) -> None:
        failure = FailureAnalysis(
            task_name="deploy-payment-v3",
            root_cause="AssertionError: expected 200 got 500",
            failure_type=FailureType.REGRESSION,
            confidence=0.85,
            impact_score=5.5,
            remediation="Review the recent code changes to this task.",
        )

        report = generate_incident_triage_report(
            request=_request(),
            events=[],
            pods=[],
            pod_logs={},
            pipeline_failures=[("2024-06-01T14:10:00Z", failure)],
            observed_at=_OBSERVED_AT,
        )

        assert len(report.root_causes) == 1
        assert report.root_causes[0].category == IncidentCauseCategory.DEPLOYMENT
        assert report.root_causes[0].confidence == 0.85
        assert report.timeline[0].source == "pipeline"


class TestCrossNamespaceCorrelation:
    """Edge case: incident spans multiple namespaces → cross-namespace correlation included."""

    def test_related_namespace_events_matching_top_category_are_correlated(self) -> None:
        related_events = {
            "billing": [
                _event(
                    "Warning",
                    "FailedConnect",
                    "database connection pool exhausted for shared postgres",
                    "billing-db",
                    "2024-06-01T14:17:00Z",
                )
            ]
        }

        report = generate_incident_triage_report(
            request=_request(related_namespaces=["billing"]),
            events=_DB_CASCADE_EVENTS,
            pods=[],
            pod_logs={},
            pipeline_failures=[],
            related_namespace_events=related_events,
            observed_at=_OBSERVED_AT,
        )

        assert report.cross_namespace_correlation
        assert any("billing" in entry for entry in report.cross_namespace_correlation)


class TestNtpDrift:
    """Edge case: logs and events have conflicting timestamps → NTP drift noted."""

    def test_log_timestamp_far_before_event_flags_drift(self) -> None:
        pod_logs = {
            "checkout-service-abc": [
                _log_line(
                    "2024-06-01T14:10:00Z",
                    "ERROR",
                    "connection pool exhausted talking to payment-db",
                )
            ]
        }

        report = generate_incident_triage_report(
            request=_request(),
            events=_DB_CASCADE_EVENTS,
            pods=[],
            pod_logs=pod_logs,
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert report.ntp_drift_detected is True
        assert "checkout-service-abc" in report.ntp_drift_note

    def test_consistent_timestamps_do_not_flag_drift(self) -> None:
        pod_logs = {
            "checkout-service-abc": [
                _log_line(
                    "2024-06-01T14:16:35Z",
                    "ERROR",
                    "connection pool exhausted talking to payment-db",
                )
            ]
        }

        report = generate_incident_triage_report(
            request=_request(),
            events=_DB_CASCADE_EVENTS,
            pods=[],
            pod_logs=pod_logs,
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert report.ntp_drift_detected is False


class TestLogLineFiltering:
    def test_info_level_log_lines_are_excluded_from_timeline(self) -> None:
        pod_logs = {
            "checkout-service-abc": [
                _log_line("2024-06-01T14:16:35Z", "INFO", "handling request"),
            ]
        }

        report = generate_incident_triage_report(
            request=_request(),
            events=_DB_CASCADE_EVENTS,
            pods=[],
            pod_logs=pod_logs,
            pipeline_failures=[],
            observed_at=_OBSERVED_AT,
        )

        assert all(entry.source != "log" for entry in report.timeline)


class TestCrossNamespaceNormalEventsIgnored:
    def test_normal_type_related_events_do_not_correlate(self) -> None:
        related_events = {
            "billing": [
                _event(
                    "Normal",
                    "Started",
                    "database connection pool healthy",
                    "billing-db",
                    "2024-06-01T14:17:00Z",
                )
            ]
        }

        report = generate_incident_triage_report(
            request=_request(related_namespaces=["billing"]),
            events=_DB_CASCADE_EVENTS,
            pods=[],
            pod_logs={},
            pipeline_failures=[],
            related_namespace_events=related_events,
            observed_at=_OBSERVED_AT,
        )

        assert report.cross_namespace_correlation == []
