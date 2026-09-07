from __future__ import annotations

from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.ports.driven.tekton_port import NamespacedPipelineRunInfo, TektonPort
from hexawyn.application.use_case.troubleshooting.generate_incident_triage_report.command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.use_case.troubleshooting.generate_incident_triage_report.response import (
    GenerateIncidentTriageReportResponse,
    ImpactAssessmentDict,
    RootCauseCandidateDict,
    TimelineEntryDict,
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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut: MutantDict = {}  # type: ignore


class GenerateIncidentTriageReportUseCase:
    @_mutmut_mutated(mutants_xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut)
    def __init__(  # noqa: PLR0913
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
    def xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_orig(  # noqa: PLR0913
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
    def xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_1(  # noqa: PLR0913
        self,
        events_port: NamespaceEventsPort,
        k8s_port: K8sPort,
        pod_logs_port: PodLogsPort,
        tekton_port: TektonPort,
        pipeline_run_logs_port: PipelineRunLogsPort,
    ) -> None:
        self._events_port = None
        self._k8s_port = k8s_port
        self._pod_logs_port = pod_logs_port
        self._tekton_port = tekton_port
        self._pipeline_run_logs_port = pipeline_run_logs_port
    def xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_2(  # noqa: PLR0913
        self,
        events_port: NamespaceEventsPort,
        k8s_port: K8sPort,
        pod_logs_port: PodLogsPort,
        tekton_port: TektonPort,
        pipeline_run_logs_port: PipelineRunLogsPort,
    ) -> None:
        self._events_port = events_port
        self._k8s_port = None
        self._pod_logs_port = pod_logs_port
        self._tekton_port = tekton_port
        self._pipeline_run_logs_port = pipeline_run_logs_port
    def xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_3(  # noqa: PLR0913
        self,
        events_port: NamespaceEventsPort,
        k8s_port: K8sPort,
        pod_logs_port: PodLogsPort,
        tekton_port: TektonPort,
        pipeline_run_logs_port: PipelineRunLogsPort,
    ) -> None:
        self._events_port = events_port
        self._k8s_port = k8s_port
        self._pod_logs_port = None
        self._tekton_port = tekton_port
        self._pipeline_run_logs_port = pipeline_run_logs_port
    def xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_4(  # noqa: PLR0913
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
        self._tekton_port = None
        self._pipeline_run_logs_port = pipeline_run_logs_port
    def xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_5(  # noqa: PLR0913
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
        self._pipeline_run_logs_port = None

    @_mutmut_mutated(mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut)
    def execute(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_orig(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_1(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(None)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_2(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = None
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_3(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            None
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_4(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=None,
                time_window_minutes=command.time_window_minutes,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_5(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=None,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_6(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                time_window_minutes=command.time_window_minutes,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_7(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_8(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = None
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_9(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=None)
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_10(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = None
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_11(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(None, command)
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_12(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, None)
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_13(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(command)
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_14(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, )
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_15(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = None
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_16(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(None)
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_17(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = None

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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_18(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = self._fetch_related_namespace_events(None)

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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_19(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = self._fetch_related_namespace_events(command)

        request = None
        report = generate_incident_triage_report(
            request=request,
            events=events,
            pods=pods,
            pod_logs=pod_logs,
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_20(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = self._fetch_related_namespace_events(command)

        request = IncidentTriageRequest(
            namespace=None,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_21(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = self._fetch_related_namespace_events(command)

        request = IncidentTriageRequest(
            namespace=command.namespace,
            time_window_minutes=None,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_22(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = self._fetch_related_namespace_events(command)

        request = IncidentTriageRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
            related_namespaces=None,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_23(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = self._fetch_related_namespace_events(command)

        request = IncidentTriageRequest(
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_24(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = self._fetch_related_namespace_events(command)

        request = IncidentTriageRequest(
            namespace=command.namespace,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_25(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
            )
        )
        pods = self._k8s_port.list_pods(namespace=command.namespace)
        pod_logs = self._fetch_unhealthy_pod_logs(pods, command)
        pipeline_failures = self._fetch_pipeline_failures(command)
        related_namespace_events = self._fetch_related_namespace_events(command)

        request = IncidentTriageRequest(
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
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

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_26(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
        report = None
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_27(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            request=None,
            events=events,
            pods=pods,
            pod_logs=pod_logs,
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_28(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            events=None,
            pods=pods,
            pod_logs=pod_logs,
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_29(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            pods=None,
            pod_logs=pod_logs,
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_30(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            pod_logs=None,
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_31(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            pipeline_failures=None,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_32(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            related_namespace_events=None,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_33(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            events=events,
            pods=pods,
            pod_logs=pod_logs,
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_34(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            pods=pods,
            pod_logs=pod_logs,
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_35(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            pod_logs=pod_logs,
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_36(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            pipeline_failures=pipeline_failures,
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_37(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            related_namespace_events=related_namespace_events,
        )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_38(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
            )
        return _to_response(report)

    def xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_39(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        self._validate_namespace_exists(command.namespace)

        events = self._events_port.list_events(
            GetNamespaceEventsRequest(
                namespace=command.namespace,
                time_window_minutes=command.time_window_minutes,
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
        return _to_response(None)

    @_mutmut_mutated(mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut)
    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_orig(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_1(self, namespace: str) -> None:
        namespaces = None
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_2(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_3(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(None):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_4(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["XXnameXX"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_5(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["NAME"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_6(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] != namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_7(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                None, context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_8(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context=None
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_9(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                context={"namespace": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_10(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_11(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"XXnamespaceXX": namespace}
            )

    def xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_12(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"NAMESPACE": namespace}
            )

    @_mutmut_mutated(mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut)
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_orig(
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_1(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = None
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_2(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["XXstatusXX"] != "Running"]
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_3(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["STATUS"] != "Running"]
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_4(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] == "Running"]
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_5(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "XXRunningXX"]
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_6(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "running"]
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_7(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "RUNNING"]
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_8(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = None
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_9(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["name"]] = None
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_10(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["XXnameXX"]] = self._pod_logs_port.fetch_logs(
                    AnalyzePodLogsRequest(
                        pod_name=pod["name"],
                        namespace=command.namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_11(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["NAME"]] = self._pod_logs_port.fetch_logs(
                    AnalyzePodLogsRequest(
                        pod_name=pod["name"],
                        namespace=command.namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_12(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["name"]] = self._pod_logs_port.fetch_logs(
                    None
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_13(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["name"]] = self._pod_logs_port.fetch_logs(
                    AnalyzePodLogsRequest(
                        pod_name=None,
                        namespace=command.namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_14(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["name"]] = self._pod_logs_port.fetch_logs(
                    AnalyzePodLogsRequest(
                        pod_name=pod["name"],
                        namespace=None,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_15(
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
                        time_window_minutes=None,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_16(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["name"]] = self._pod_logs_port.fetch_logs(
                    AnalyzePodLogsRequest(
                        namespace=command.namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_17(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["name"]] = self._pod_logs_port.fetch_logs(
                    AnalyzePodLogsRequest(
                        pod_name=pod["name"],
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_18(
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
                        )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_19(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["name"]] = self._pod_logs_port.fetch_logs(
                    AnalyzePodLogsRequest(
                        pod_name=pod["XXnameXX"],
                        namespace=command.namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_20(
        self, pods: list[PodInfo], command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[PodLogLine]]:
        unhealthy = [pod for pod in pods if pod["status"] != "Running"]
        pod_logs: dict[str, list[PodLogLine]] = {}
        for pod in unhealthy[: _cfg.max_pods_logs_fetched]:
            try:
                pod_logs[pod["name"]] = self._pod_logs_port.fetch_logs(
                    AnalyzePodLogsRequest(
                        pod_name=pod["NAME"],
                        namespace=command.namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return pod_logs

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_21(
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
                break
        return pod_logs

    @_mutmut_mutated(mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut)
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_orig(
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_1(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = None
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_2(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=None, limit=100
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_3(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=None
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_4(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            limit=100
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_5(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, )
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_6(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=101
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_7(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = None

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_8(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["status"] == _FAILED_RUN_STATUS or _within_window(run["start_time"], command.time_window_minutes)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_9(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["XXstatusXX"] == _FAILED_RUN_STATUS
            and _within_window(run["start_time"], command.time_window_minutes)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_10(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["STATUS"] == _FAILED_RUN_STATUS
            and _within_window(run["start_time"], command.time_window_minutes)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_11(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["status"] != _FAILED_RUN_STATUS
            and _within_window(run["start_time"], command.time_window_minutes)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_12(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["status"] == _FAILED_RUN_STATUS
            and _within_window(None, command.time_window_minutes)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_13(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["status"] == _FAILED_RUN_STATUS
            and _within_window(run["start_time"], None)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_14(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["status"] == _FAILED_RUN_STATUS
            and _within_window(command.time_window_minutes)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_15(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["status"] == _FAILED_RUN_STATUS
            and _within_window(run["start_time"], )
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_16(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["status"] == _FAILED_RUN_STATUS
            and _within_window(run["XXstart_timeXX"], command.time_window_minutes)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_17(
        self, command: GenerateIncidentTriageReportCommand
    ) -> list[tuple[str, FailureAnalysis]]:
        runs = self._tekton_port.list_pipeline_runs_in_namespace(
            namespace=command.namespace, limit=100
        )
        failed_in_window = [
            run
            for run in runs
            if run["status"] == _FAILED_RUN_STATUS
            and _within_window(run["START_TIME"], command.time_window_minutes)
        ]

        failures: list[tuple[str, FailureAnalysis]] = []
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_18(
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

        failures: list[tuple[str, FailureAnalysis]] = None
        for run in failed_in_window:
            failures.extend(self._analyze_pipeline_run(run, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_19(
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
            failures.extend(None)
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_20(
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
            failures.extend(self._analyze_pipeline_run(None, command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_21(
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
            failures.extend(self._analyze_pipeline_run(run, None))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_22(
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
            failures.extend(self._analyze_pipeline_run(command.namespace))
        return failures

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_23(
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
            failures.extend(self._analyze_pipeline_run(run, ))
        return failures

    @_mutmut_mutated(mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut)
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_orig(
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_1(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = None
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_2(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=None, namespace=namespace
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_3(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=None
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_4(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                namespace=namespace
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_5(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], )
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_6(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["XXnameXX"], namespace=namespace
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_7(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["NAME"], namespace=namespace
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_8(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=namespace
            )
            step_logs = None
        except Exception:
            return []

        result = analyze_pipeline_failure(
            AnalyzeFailedPipelineRequest(pipeline_name=run["name"], namespace=namespace),
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_9(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=namespace
            )
            step_logs = self._pipeline_run_logs_port.fetch_step_logs(
                None
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_10(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=namespace
            )
            step_logs = self._pipeline_run_logs_port.fetch_step_logs(
                PipelineRunLogsRequest(pipeline_run_name=None, namespace=namespace)
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_11(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=namespace
            )
            step_logs = self._pipeline_run_logs_port.fetch_step_logs(
                PipelineRunLogsRequest(pipeline_run_name=run["name"], namespace=None)
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_12(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=namespace
            )
            step_logs = self._pipeline_run_logs_port.fetch_step_logs(
                PipelineRunLogsRequest(namespace=namespace)
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_13(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=namespace
            )
            step_logs = self._pipeline_run_logs_port.fetch_step_logs(
                PipelineRunLogsRequest(pipeline_run_name=run["name"], )
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_14(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=namespace
            )
            step_logs = self._pipeline_run_logs_port.fetch_step_logs(
                PipelineRunLogsRequest(pipeline_run_name=run["XXnameXX"], namespace=namespace)
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_15(
        self, run: NamespacedPipelineRunInfo, namespace: str
    ) -> list[tuple[str, FailureAnalysis]]:
        try:
            task_runs = self._tekton_port.list_task_runs(
                pipeline_name=run["name"], namespace=namespace
            )
            step_logs = self._pipeline_run_logs_port.fetch_step_logs(
                PipelineRunLogsRequest(pipeline_run_name=run["NAME"], namespace=namespace)
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

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_16(
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

        result = None
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_17(
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
            None,
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_18(
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
            None,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_19(
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
            None,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_20(
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
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_21(
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
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_22(
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
            )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_23(
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
            AnalyzeFailedPipelineRequest(pipeline_name=None, namespace=namespace),
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_24(
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
            AnalyzeFailedPipelineRequest(pipeline_name=run["name"], namespace=None),
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_25(
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
            AnalyzeFailedPipelineRequest(namespace=namespace),
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_26(
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
            AnalyzeFailedPipelineRequest(pipeline_name=run["name"], ),
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_27(
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
            AnalyzeFailedPipelineRequest(pipeline_name=run["XXnameXX"], namespace=namespace),
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_28(
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
            AnalyzeFailedPipelineRequest(pipeline_name=run["NAME"], namespace=namespace),
            task_runs,
            step_logs,
        )
        start_time = run["start_time"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_29(
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
        start_time = None
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_30(
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
        start_time = run["start_time"] and ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_31(
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
        start_time = run["XXstart_timeXX"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_32(
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
        start_time = run["START_TIME"] or ""
        return [(start_time, failure) for failure in result.failures]

    def xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_33(
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
        start_time = run["start_time"] or "XXXX"
        return [(start_time, failure) for failure in result.failures]

    @_mutmut_mutated(mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut)
    def _fetch_related_namespace_events(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    GetNamespaceEventsRequest(
                        namespace=namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return related

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_orig(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    GetNamespaceEventsRequest(
                        namespace=namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return related

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_1(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = None
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    GetNamespaceEventsRequest(
                        namespace=namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return related

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_2(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = None
            except Exception:
                continue
        return related

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_3(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    None
                )
            except Exception:
                continue
        return related

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_4(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    GetNamespaceEventsRequest(
                        namespace=None,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return related

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_5(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    GetNamespaceEventsRequest(
                        namespace=namespace,
                        time_window_minutes=None,
                    )
                )
            except Exception:
                continue
        return related

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_6(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    GetNamespaceEventsRequest(
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                continue
        return related

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_7(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    GetNamespaceEventsRequest(
                        namespace=namespace,
                        )
                )
            except Exception:
                continue
        return related

    def xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_8(
        self, command: GenerateIncidentTriageReportCommand
    ) -> dict[str, list[NamespaceEvent]]:
        related: dict[str, list[NamespaceEvent]] = {}
        for namespace in command.related_namespaces:
            try:
                related[namespace] = self._events_port.list_events(
                    GetNamespaceEventsRequest(
                        namespace=namespace,
                        time_window_minutes=command.time_window_minutes,
                    )
                )
            except Exception:
                break
        return related

mutants_xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut['_mutmut_orig'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut['xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_1'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut['xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_2'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut['xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_3'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut['xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_4'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut['xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_5'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ__init____mutmut_5 # type: ignore # mutmut generated

mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['_mutmut_orig'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_1'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_2'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_3'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_4'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_5'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_6'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_7'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_8'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_9'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_10'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_11'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_12'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_13'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_14'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_15'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_16'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_17'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_18'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_19'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_20'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_21'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_22'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_23'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_24'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_25'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_26'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_27'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_28'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_29'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_30'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_31'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_32'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_33'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_34'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_35'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_36'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_37'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_38'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut['xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_39'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated

mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['_mutmut_orig'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_1'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_2'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_3'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_4'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_5'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_6'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_7'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_8'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_9'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_10'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_11'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_12'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_validate_namespace_exists__mutmut_12 # type: ignore # mutmut generated

mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['_mutmut_orig'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_1'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_2'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_3'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_4'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_5'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_6'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_7'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_8'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_9'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_10'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_11'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_12'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_13'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_14'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_15'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_16'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_17'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_18'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_19'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_20'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_21'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_unhealthy_pod_logs__mutmut_21 # type: ignore # mutmut generated

mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['_mutmut_orig'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_1'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_2'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_3'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_4'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_5'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_6'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_7'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_8'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_9'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_10'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_11'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_12'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_13'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_14'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_15'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_16'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_17'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_18'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_19'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_20'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_21'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_22'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_23'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_pipeline_failures__mutmut_23 # type: ignore # mutmut generated

mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['_mutmut_orig'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_1'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_2'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_3'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_4'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_5'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_6'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_7'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_8'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_9'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_10'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_11'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_12'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_13'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_14'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_15'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_16'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_17'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_18'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_19'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_20'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_21'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_22'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_23'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_24'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_25'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_26'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_27'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_28'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_29'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_30'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_31'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_32'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_33'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_analyze_pipeline_run__mutmut_33 # type: ignore # mutmut generated

mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut['_mutmut_orig'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_1'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_2'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_3'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_4'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_5'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_6'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_7'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut['xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_8'] = GenerateIncidentTriageReportUseCase.xǁGenerateIncidentTriageReportUseCaseǁ_fetch_related_namespace_events__mutmut_8 # type: ignore # mutmut generated
mutants_x__within_window__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__within_window__mutmut)
def _within_window(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_orig(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_1(start_time: str | None, window_minutes: int) -> bool:
    if start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_2(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return True
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_3(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = None
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_4(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(None)
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_5(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace(None, "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_6(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", None))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_7(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_8(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", ))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_9(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("XXZXX", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_10(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_11(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "XX+00:00XX"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_12(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return True
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_13(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed > datetime.now(UTC) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_14(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) + timedelta(minutes=window_minutes)


def x__within_window__mutmut_15(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(None) - timedelta(minutes=window_minutes)


def x__within_window__mutmut_16(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=None)

mutants_x__within_window__mutmut['_mutmut_orig'] = x__within_window__mutmut_orig # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_1'] = x__within_window__mutmut_1 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_2'] = x__within_window__mutmut_2 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_3'] = x__within_window__mutmut_3 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_4'] = x__within_window__mutmut_4 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_5'] = x__within_window__mutmut_5 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_6'] = x__within_window__mutmut_6 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_7'] = x__within_window__mutmut_7 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_8'] = x__within_window__mutmut_8 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_9'] = x__within_window__mutmut_9 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_10'] = x__within_window__mutmut_10 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_11'] = x__within_window__mutmut_11 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_12'] = x__within_window__mutmut_12 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_13'] = x__within_window__mutmut_13 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_14'] = x__within_window__mutmut_14 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_15'] = x__within_window__mutmut_15 # type: ignore # mutmut generated
mutants_x__within_window__mutmut['x__within_window__mutmut_16'] = x__within_window__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_orig(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_1(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=None,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_2(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=None,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_3(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=None,
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_4(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                object=entry.object,
                reason=entry.reason,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=None,
        impact=ImpactAssessmentDict(
            affected_services=report.impact.affected_services,
            estimated_user_impact=report.impact.estimated_user_impact,
            duration_minutes=report.impact.duration_minutes,
            ongoing=report.impact.ongoing,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_5(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
                confidence=candidate.confidence,
                evidence=candidate.evidence,
                involved_objects=candidate.involved_objects,
            )
            for candidate in report.root_causes
        ],
        impact=None,
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_6(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        remediation_steps=None,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_7(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolved=None,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_8(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=None,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_9(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=None,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_10(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=None,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_11(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=None,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_12(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=None,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_13(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=None,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_14(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=None,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_15(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=None,
    )


def x__to_response__mutmut_16(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_17(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_18(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_19(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                object=entry.object,
                reason=entry.reason,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        impact=ImpactAssessmentDict(
            affected_services=report.impact.affected_services,
            estimated_user_impact=report.impact.estimated_user_impact,
            duration_minutes=report.impact.duration_minutes,
            ongoing=report.impact.ongoing,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_20(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
                confidence=candidate.confidence,
                evidence=candidate.evidence,
                involved_objects=candidate.involved_objects,
            )
            for candidate in report.root_causes
        ],
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_21(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_22(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_23(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_24(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_25(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_26(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_27(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_28(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_29(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_30(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        )


def x__to_response__mutmut_31(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=None,
                source=entry.source,
                object=entry.object,
                reason=entry.reason,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_32(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=None,
                object=entry.object,
                reason=entry.reason,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_33(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                object=None,
                reason=entry.reason,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_34(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                object=entry.object,
                reason=None,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_35(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                object=entry.object,
                reason=entry.reason,
                message=None,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_36(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                object=entry.object,
                reason=entry.reason,
                message=entry.message,
                severity=None,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_37(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                source=entry.source,
                object=entry.object,
                reason=entry.reason,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_38(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                object=entry.object,
                reason=entry.reason,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_39(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                reason=entry.reason,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_40(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                object=entry.object,
                message=entry.message,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_41(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                object=entry.object,
                reason=entry.reason,
                severity=entry.severity,
            )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_42(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
                timestamp=entry.timestamp,
                source=entry.source,
                object=entry.object,
                reason=entry.reason,
                message=entry.message,
                )
            for entry in report.timeline
        ],
        root_causes=[
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_43(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=None,
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_44(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=None,
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_45(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
                confidence=None,
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_46(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
                confidence=candidate.confidence,
                evidence=None,
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_47(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
                confidence=candidate.confidence,
                evidence=candidate.evidence,
                involved_objects=None,
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_48(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_49(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_50(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_51(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
                confidence=candidate.confidence,
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_52(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
                confidence=candidate.confidence,
                evidence=candidate.evidence,
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_53(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
                confidence=candidate.confidence,
                evidence=candidate.evidence,
                involved_objects=candidate.involved_objects,
            )
            for candidate in report.root_causes
        ],
        impact=ImpactAssessmentDict(
            affected_services=None,
            estimated_user_impact=report.impact.estimated_user_impact,
            duration_minutes=report.impact.duration_minutes,
            ongoing=report.impact.ongoing,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_54(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
            estimated_user_impact=None,
            duration_minutes=report.impact.duration_minutes,
            ongoing=report.impact.ongoing,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_55(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
            duration_minutes=None,
            ongoing=report.impact.ongoing,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_56(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
            ongoing=None,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_57(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
                description=candidate.description,
                category=candidate.category.value,
                confidence=candidate.confidence,
                evidence=candidate.evidence,
                involved_objects=candidate.involved_objects,
            )
            for candidate in report.root_causes
        ],
        impact=ImpactAssessmentDict(
            estimated_user_impact=report.impact.estimated_user_impact,
            duration_minutes=report.impact.duration_minutes,
            ongoing=report.impact.ongoing,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_58(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
            duration_minutes=report.impact.duration_minutes,
            ongoing=report.impact.ongoing,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_59(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
            ongoing=report.impact.ongoing,
        ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_60(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
            ),
        remediation_steps=report.remediation_steps,
        resolved=report.resolved,
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(report),
    )


def x__to_response__mutmut_61(report: IncidentTriageReport) -> GenerateIncidentTriageReportResponse:
    return GenerateIncidentTriageReportResponse(
        namespace=report.namespace,
        time_window_minutes=report.time_window_minutes,
        timeline=[
            TimelineEntryDict(  # type: ignore
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
            RootCauseCandidateDict(  # type: ignore
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
        resolution_time=report.resolution_time,  # type: ignore
        mttr_minutes=report.mttr_minutes,  # type: ignore
        ntp_drift_detected=report.ntp_drift_detected,
        ntp_drift_note=report.ntp_drift_note,
        cross_namespace_correlation=report.cross_namespace_correlation,  # type: ignore
        insufficient_data=report.insufficient_data,
        data_checked=report.data_checked,  # type: ignore
        formatted_report=format_report_as_markdown(None),
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_15'] = x__to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_16'] = x__to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_17'] = x__to_response__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_18'] = x__to_response__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_19'] = x__to_response__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_20'] = x__to_response__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_21'] = x__to_response__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_22'] = x__to_response__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_23'] = x__to_response__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_24'] = x__to_response__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_25'] = x__to_response__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_26'] = x__to_response__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_27'] = x__to_response__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_28'] = x__to_response__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_29'] = x__to_response__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_30'] = x__to_response__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_31'] = x__to_response__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_32'] = x__to_response__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_33'] = x__to_response__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_34'] = x__to_response__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_35'] = x__to_response__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_36'] = x__to_response__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_37'] = x__to_response__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_38'] = x__to_response__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_39'] = x__to_response__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_40'] = x__to_response__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_41'] = x__to_response__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_42'] = x__to_response__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_43'] = x__to_response__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_44'] = x__to_response__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_45'] = x__to_response__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_46'] = x__to_response__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_47'] = x__to_response__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_48'] = x__to_response__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_49'] = x__to_response__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_50'] = x__to_response__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_51'] = x__to_response__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_52'] = x__to_response__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_53'] = x__to_response__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_54'] = x__to_response__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_55'] = x__to_response__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_56'] = x__to_response__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_57'] = x__to_response__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_58'] = x__to_response__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_59'] = x__to_response__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_60'] = x__to_response__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_61'] = x__to_response__mutmut_61 # type: ignore # mutmut generated
