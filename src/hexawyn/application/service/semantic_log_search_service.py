from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawPodLogData
from hexawyn.application.use_case.semantic_log_search.command import (
    SemanticLogSearchCommand,
)
from hexawyn.application.use_case.semantic_log_search.response import (
    MatchedLogLineDict,
    PodLogMatchDict,
    SemanticLogSearchResponse,
    ServiceGroupDict,
    SkippedNamespaceDict,
    SkippedPodDict,
)
from hexawyn.application.ports.driving.semantic_log_search.semantic_log_search_service_port import (
    SemanticLogSearchServicePort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.log_search import (
    LogSearchRequest,
    LogSearchResult,
    MatchedLogLine,
    PodLogMatch,
    ServiceGroup,
    SkippedNamespace,
    SkippedPod,
)
from hexawyn.domain.services.log_search.pod_log_search import search_pod_logs

_NO_LOG_STATUSES = frozenset({"Pending", "Unknown"})
_PER_POD_ERRORS = (ResourceNotFoundError, InsufficientPermissionsError, ClusterUnreachableError)


class SemanticLogSearchService(SemanticLogSearchServicePort):
    def __init__(self, port: LogSearchPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port

    def search(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = self._resolve_namespaces(command.namespace)
        namespaces_total = len(namespaces)

        scanned_namespaces: list[str] = []
        skipped_namespaces: list[SkippedNamespace] = []
        skipped_pods: list[SkippedPod] = []
        raw_pod_logs: list[RawPodLogData] = []

        for namespace in namespaces:
            try:
                pods = self._k8s_port.list_pods(namespace=namespace)
            except InsufficientPermissionsError as exc:
                skipped_namespaces.append(SkippedNamespace(namespace=namespace, reason=str(exc)))
                continue
            scanned_namespaces.append(namespace)

            for pod in pods:
                self._collect_pod_logs(
                    pod, namespace, command.time_window_minutes, raw_pod_logs, skipped_pods
                )

        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_pods,
            skipped_namespaces,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def _resolve_namespaces(self, namespace: str | None) -> list[str]:
        if namespace is not None:
            self._validate_namespace_exists(namespace)
            return [namespace]
        return [ns["name"] for ns in self._k8s_port.list_namespaces()]

    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def _collect_pod_logs(
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = str(pod["name"])
        status = str(pod["status"])
        if status in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name, namespace=namespace, reason=f"{status}: no logs available"
                )
            )
            return

        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, time_window_minutes
            )
        except _PER_POD_ERRORS as exc:
            skipped_pods.append(SkippedPod(pod_name=pod_name, namespace=namespace, reason=str(exc)))
            return

        if not container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return

        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )


def _to_response(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,
        groups=[_to_group_dict(group) for group in result.groups],
        pods_affected=result.pods_affected,
        services_affected=result.services_affected,
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],
        scanned_namespaces=result.scanned_namespaces,
        namespaces_total=result.namespaces_total,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def _to_group_dict(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(
        service_name=group.service_name,
        namespace=group.namespace,
        pods=[_to_pod_match_dict(pod) for pod in group.pods],
    )


def _to_pod_match_dict(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(
        pod_name=match.pod_name,
        namespace=match.namespace,
        container=match.container,
        matching_lines=[_to_line_dict(line) for line in match.matching_lines],
    )


def _to_line_dict(line: MatchedLogLine) -> MatchedLogLineDict:
    return MatchedLogLineDict(
        timestamp=line.timestamp, message=line.message, match_type=line.match_type
    )


def _to_skipped_pod_dict(pod: SkippedPod) -> SkippedPodDict:
    return SkippedPodDict(pod_name=pod.pod_name, namespace=pod.namespace, reason=pod.reason)


def _to_skipped_namespace_dict(ns: SkippedNamespace) -> SkippedNamespaceDict:
    return SkippedNamespaceDict(namespace=ns.namespace, reason=ns.reason)
