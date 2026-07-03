from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.ports.driven.tekton_port import NamespacedPipelineRunInfo, TektonPort
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_response import (
    GenerateIncidentTriageReportResponse,
    ImpactAssessmentDict,
    RootCauseCandidateDict,
    TimelineEntryDict,
)
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_service_port import (
    GenerateIncidentTriageReportServicePort,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest, PodLogLine
from hexawyn.domain.models.constants import IncidentTriageConstants
from hexawyn.domain.models.incident_triage import IncidentTriageReport, IncidentTriageRequest
from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest, NamespaceEvent
from hexawyn.domain.models.pipeline_failure_analysis import (
    AnalyzeFailedPipelineRequest,
    FailureAnalysis,
)
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest
from hexawyn.domain.services.failure_analysis.rca import analyze_pipeline_failure
from hexawyn.domain.services.incident_triage.markdown_formatter import format_report_as_markdown
from hexawyn.domain.services.incident_triage.report_builder import generate_incident_triage_report

_cfg = IncidentTriageConstants()
_FAILED_RUN_STATUS = "Failed"


class GenerateIncidentTriageReportService(GenerateIncidentTriageReportServicePort):
    def __init__(
        self,
        events_port: NamespaceEventsPort,
        k8s_port: K8sPort,
        pod_logs_port: PodLogsPort,
        tekton_port: TektonPort,
        pipeline_run_logs_port: PipelineRunLogsPort,
    ) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
        self._pod_logs_port = pod_logs_port
        self._tekton_port = tekton_port
        self._pipeline_run_logs_port = pipeline_run_logs_port

    def generate(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace, time_window_minutes=command.time_window_minutes
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = self._fetch_related_namespace_events(command)

        request = IncidentTriageRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            related_namespaces=command.related_namespaces,
        )
        report = generate_incident_triage_report(
            request=request,
            events=events,
            pods=pods,
            pod_logs=pod_logs,
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def _fetch_unhealthy_pod_logs(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["name"]] = self._pod_logs_port.fetch_logs(
                    AnalyzePodLogsRequest(
                        pod_name=pod["name"],
                        namespace=command.namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def _fetch_pipeline_failures(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["status"] == _FAILED_RUN_STATUS
            and _within_window(run["start_time"], command.time_window_minutes)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def _analyze_pipeline_run(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=namespace
            )
            step_logs = self._pipeline_run_logs_port.fetch_step_logs(
                PipelineRunLogsRequest(pipeline_run_name=run["name"], namespace=namespace)
            )
        except Exception:
            return []

        result = analyze_pipeline_failure(
            AnalyzeFailedPipelineRequest(pipeline_name=run["name"], namespace=namespace),
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def _fetch_related_namespace_events(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    GetNamespaceEventsRequest(
                        namespace=namespace, time_window_minutes=command.time_window_minutes
                    )
                )
            except Exception:
                continue
        return related


def _within_window(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def _to_response(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(
                timestamp=entry.timestamp,
                source=entry.source,
                object=entry.object,
                reason=entry.reason,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(
                description=candidate.description,
                category=candidate.category.value,
                confidence=candidate.confidence,
                evidence=candidate.evidence,
                involved_objects=candidate.involved_objects,
            )
            for candidate in report.root_causes
        ],
        impact=ImpactAssessmentDict(
            affected_services=report.impact.affected_services,
            estimated_user_impact=report.impact.estimated_user_impact,
            duration_minutes=report.impact.duration_minutes,
            ongoing=report.impact.ongoing,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,
        mttr_minutes=report.mttr_minutes,
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,
        formatted_report=format_report_as_markdown(report),
    )
