"""Unit tests for GenerateIncidentTriageReportService (mocks all 5 driven ports)."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.service.generate_incident_triage_report_service import (
    GenerateIncidentTriageReportService,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_event import NamespaceEvent


def _event(
    reason: str = "FailedConnect", obj: str = "payment-db", last_seen: str = "2024-06-01T14:15:00Z"
) -> NamespaceEvent:
    return NamespaceEvent(
        event_type="Warning",
        reason=reason,
        message="connection pool exhausted for postgres",
        object=obj,
        count=1,
        last_seen=last_seen,
    )


def _pod(name: str, status: str = "Running") -> dict:
    return {
        "name": name,
        "namespace": "payment",
        "status": status,
        "restarts": 2,
        "age": "2h",
        "node": "n1",
    }


def _make_service(
    events_port: MagicMock | None = None,
    k8s_port: MagicMock | None = None,
    pod_logs_port: MagicMock | None = None,
    tekton_port: MagicMock | None = None,
    pipeline_run_logs_port: MagicMock | None = None,
) -> GenerateIncidentTriageReportService:
    if k8s_port is None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "payment", "status": "Active", "age": "10d"}
        ]
        k8s_port.list_pods.return_value = []

    if events_port is None:
        events_port = MagicMock()
        events_port.list_events.return_value = []

    if pod_logs_port is None:
        pod_logs_port = MagicMock()
        pod_logs_port.fetch_logs.return_value = []

    if tekton_port is None:
        tekton_port = MagicMock()
        tekton_port.list_pipeline_runs_in_namespace.return_value = []

    pipeline_run_logs_port = pipeline_run_logs_port or MagicMock()

    return GenerateIncidentTriageReportService(
        events_port=events_port,
        k8s_port=k8s_port,
        pod_logs_port=pod_logs_port,
        tekton_port=tekton_port,
        pipeline_run_logs_port=pipeline_run_logs_port,
    )


class TestNamespaceValidation:
    def test_raises_when_namespace_missing(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [{"name": "other", "status": "Active", "age": "1d"}]
        service = _make_service(k8s_port=k8s_port)

        with pytest.raises(ResourceNotFoundError):
            service.generate(GenerateIncidentTriageReportCommand(namespace="ghost"))


class TestHappyPath:
    def test_generate_returns_report_with_formatted_markdown(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = [_event()]
        service = _make_service(events_port=events_port)

        response = service.generate(
            GenerateIncidentTriageReportCommand(namespace="payment", time_window_minutes=120)
        )

        assert response.namespace == "payment"
        assert response.error is None
        assert len(response.root_causes) == 1
        assert "# Incident Report" in response.formatted_report


class TestUnhealthyPodLogFetching:
    def test_only_unhealthy_pods_get_logs_fetched_and_capped(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "payment", "status": "Active", "age": "10d"}
        ]
        k8s_port.list_pods.return_value = [
            _pod("healthy-1", status="Running"),
            *[_pod(f"unhealthy-{i}", status="CrashLoopBackOff") for i in range(8)],
        ]
        pod_logs_port = MagicMock()
        pod_logs_port.fetch_logs.return_value = []

        service = _make_service(k8s_port=k8s_port, pod_logs_port=pod_logs_port)
        service.generate(GenerateIncidentTriageReportCommand(namespace="payment"))

        assert pod_logs_port.fetch_logs.call_count == 5

    def test_pod_log_fetch_failure_does_not_abort_report(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [
            {"name": "payment", "status": "Active", "age": "10d"}
        ]
        k8s_port.list_pods.return_value = [_pod("broken-pod", status="CrashLoopBackOff")]
        pod_logs_port = MagicMock()
        pod_logs_port.fetch_logs.side_effect = Exception("adapter timeout")

        events_port = MagicMock()
        events_port.list_events.return_value = [_event()]

        service = _make_service(
            k8s_port=k8s_port, pod_logs_port=pod_logs_port, events_port=events_port
        )
        response = service.generate(GenerateIncidentTriageReportCommand(namespace="payment"))

        assert response.error is None
        assert len(response.root_causes) == 1


class TestPipelineRunWindowFiltering:
    def test_only_failed_runs_within_window_are_analyzed(self) -> None:
        tekton_port = MagicMock()
        now = datetime.now(UTC)
        in_window_start = (now - timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        out_of_window_start = (now - timedelta(minutes=300)).strftime("%Y-%m-%dT%H:%M:%SZ")
        tekton_port.list_pipeline_runs_in_namespace.return_value = [
            {
                "name": "deploy-payment-v3",
                "status": "Failed",
                "start_time": in_window_start,
                "duration": "1m",
                "duration_seconds": 60,
                "pipeline_ref": "deploy-payment-v3",
            },
            {
                "name": "deploy-payment-old",
                "status": "Failed",
                "start_time": out_of_window_start,
                "duration": "1m",
                "duration_seconds": 60,
                "pipeline_ref": "deploy-payment-old",
            },
            {
                "name": "deploy-payment-ok",
                "status": "Succeeded",
                "start_time": in_window_start,
                "duration": "1m",
                "duration_seconds": 60,
                "pipeline_ref": "deploy-payment-ok",
            },
        ]
        tekton_port.list_task_runs.return_value = []

        service = _make_service(tekton_port=tekton_port)
        service.generate(
            GenerateIncidentTriageReportCommand(namespace="payment", time_window_minutes=120)
        )

        tekton_port.list_task_runs.assert_called_once_with(
            pipeline_name="deploy-payment-v3", namespace="payment"
        )

    def test_pipeline_analysis_failure_does_not_abort_report(self) -> None:
        tekton_port = MagicMock()
        in_window_start = (datetime.now(UTC) - timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        tekton_port.list_pipeline_runs_in_namespace.return_value = [
            {
                "name": "deploy-payment-v3",
                "status": "Failed",
                "start_time": in_window_start,
                "duration": "1m",
                "duration_seconds": 60,
                "pipeline_ref": "deploy-payment-v3",
            }
        ]
        tekton_port.list_task_runs.side_effect = Exception("tekton unavailable")

        events_port = MagicMock()
        events_port.list_events.return_value = [_event()]

        service = _make_service(tekton_port=tekton_port, events_port=events_port)
        response = service.generate(GenerateIncidentTriageReportCommand(namespace="payment"))

        assert response.error is None
        assert len(response.root_causes) == 1

    def test_run_with_missing_start_time_is_not_analyzed(self) -> None:
        tekton_port = MagicMock()
        tekton_port.list_pipeline_runs_in_namespace.return_value = [
            {
                "name": "deploy-payment-v3",
                "status": "Failed",
                "start_time": None,
                "duration": "1m",
                "duration_seconds": 60,
                "pipeline_ref": "deploy-payment-v3",
            }
        ]

        service = _make_service(tekton_port=tekton_port)
        service.generate(GenerateIncidentTriageReportCommand(namespace="payment"))

        tekton_port.list_task_runs.assert_not_called()

    def test_run_with_malformed_start_time_is_not_analyzed(self) -> None:
        tekton_port = MagicMock()
        tekton_port.list_pipeline_runs_in_namespace.return_value = [
            {
                "name": "deploy-payment-v3",
                "status": "Failed",
                "start_time": "not-a-timestamp",
                "duration": "1m",
                "duration_seconds": 60,
                "pipeline_ref": "deploy-payment-v3",
            }
        ]

        service = _make_service(tekton_port=tekton_port)
        service.generate(GenerateIncidentTriageReportCommand(namespace="payment"))

        tekton_port.list_task_runs.assert_not_called()


class TestRelatedNamespaces:
    def test_related_namespaces_trigger_additional_event_fetches(self) -> None:
        events_port = MagicMock()
        events_port.list_events.return_value = []

        service = _make_service(events_port=events_port)
        service.generate(
            GenerateIncidentTriageReportCommand(namespace="payment", related_namespaces=["billing"])
        )

        assert events_port.list_events.call_count == 2
        called_namespaces = {
            call.args[0].namespace for call in events_port.list_events.call_args_list
        }
        assert called_namespaces == {"payment", "billing"}

    def test_related_namespace_fetch_failure_is_skipped(self) -> None:
        events_port = MagicMock()

        def _list_events(request: object) -> list:
            if request.namespace == "billing":  # type: ignore[attr-defined]
                raise Exception("billing namespace unreachable")
            return [_event()]

        events_port.list_events.side_effect = _list_events

        service = _make_service(events_port=events_port)
        response = service.generate(
            GenerateIncidentTriageReportCommand(namespace="payment", related_namespaces=["billing"])
        )

        assert response.error is None
        assert response.cross_namespace_correlation == []
