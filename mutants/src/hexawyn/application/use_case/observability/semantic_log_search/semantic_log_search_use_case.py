# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawPodLogData
from hexawyn.application.use_case.observability.semantic_log_search.command import (
    SemanticLogSearchCommand,
)
from hexawyn.application.use_case.observability.semantic_log_search.response import (
    MatchedLogLineDict,
    PodLogMatchDict,
    SemanticLogSearchResponse,
    ServiceGroupDict,
    SkippedNamespaceDict,
    SkippedPodDict,
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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSemanticLogSearchUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut: MutantDict = {}  # type: ignore


class SemanticLogSearchUseCase:
    @_mutmut_mutated(mutants_xǁSemanticLogSearchUseCaseǁ__init____mutmut)
    def __init__(self, port: LogSearchPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port
    def xǁSemanticLogSearchUseCaseǁ__init____mutmut_orig(self, port: LogSearchPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port
    def xǁSemanticLogSearchUseCaseǁ__init____mutmut_1(self, port: LogSearchPort, k8s_port: K8sPort) -> None:
        self._port = None
        self._k8s_port = k8s_port
    def xǁSemanticLogSearchUseCaseǁ__init____mutmut_2(self, port: LogSearchPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut)
    def execute(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_orig(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_1(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = None
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_2(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = self._resolve_namespaces(None)
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_3(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = self._resolve_namespaces(command.namespace)
        namespaces_total = None
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_4(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = self._resolve_namespaces(command.namespace)
        namespaces_total = len(namespaces)
        scanned_namespaces: list[str] = None
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_5(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = self._resolve_namespaces(command.namespace)
        namespaces_total = len(namespaces)
        scanned_namespaces: list[str] = []
        skipped_namespaces: list[SkippedNamespace] = None
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_6(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = self._resolve_namespaces(command.namespace)
        namespaces_total = len(namespaces)
        scanned_namespaces: list[str] = []
        skipped_namespaces: list[SkippedNamespace] = []
        skipped_pods: list[SkippedPod] = None
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_7(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = self._resolve_namespaces(command.namespace)
        namespaces_total = len(namespaces)
        scanned_namespaces: list[str] = []
        skipped_namespaces: list[SkippedNamespace] = []
        skipped_pods: list[SkippedPod] = []
        raw_pod_logs: list[RawPodLogData] = None
        for namespace in namespaces:
            try:
                pods = self._k8s_port.list_pods(namespace=namespace)
            except InsufficientPermissionsError as exc:
                skipped_namespaces.append(SkippedNamespace(namespace=namespace, reason=str(exc)))
                continue
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_8(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = self._resolve_namespaces(command.namespace)
        namespaces_total = len(namespaces)
        scanned_namespaces: list[str] = []
        skipped_namespaces: list[SkippedNamespace] = []
        skipped_pods: list[SkippedPod] = []
        raw_pod_logs: list[RawPodLogData] = []
        for namespace in namespaces:
            try:
                pods = None
            except InsufficientPermissionsError as exc:
                skipped_namespaces.append(SkippedNamespace(namespace=namespace, reason=str(exc)))
                continue
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_9(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
        namespaces = self._resolve_namespaces(command.namespace)
        namespaces_total = len(namespaces)
        scanned_namespaces: list[str] = []
        skipped_namespaces: list[SkippedNamespace] = []
        skipped_pods: list[SkippedPod] = []
        raw_pod_logs: list[RawPodLogData] = []
        for namespace in namespaces:
            try:
                pods = self._k8s_port.list_pods(namespace=None)
            except InsufficientPermissionsError as exc:
                skipped_namespaces.append(SkippedNamespace(namespace=namespace, reason=str(exc)))
                continue
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_10(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                skipped_namespaces.append(None)
                continue
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_11(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                skipped_namespaces.append(SkippedNamespace(namespace=None, reason=str(exc)))
                continue
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_12(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                skipped_namespaces.append(SkippedNamespace(namespace=namespace, reason=None))
                continue
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_13(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                skipped_namespaces.append(SkippedNamespace(reason=str(exc)))
                continue
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_14(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                skipped_namespaces.append(SkippedNamespace(namespace=namespace, ))
                continue
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_15(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                skipped_namespaces.append(SkippedNamespace(namespace=namespace, reason=str(None)))
                continue
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_16(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                break
            scanned_namespaces.append(namespace)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_17(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
            scanned_namespaces.append(None)
            for pod in pods:
                self._collect_pod_logs(
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_18(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    None,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_19(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    None,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_20(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    None,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_21(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    None,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_22(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    None,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_23(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_24(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_25(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_26(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_27(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_28(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = None
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_pods,
            skipped_namespaces,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_29(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=None,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_30(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=None,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_31(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=None,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_32(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=None,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_33(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_34(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_35(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            time_window_minutes=command.time_window_minutes,  # type: ignore
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_36(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
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

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_37(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = None
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_38(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            None,
            raw_pod_logs,
            skipped_pods,
            skipped_namespaces,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_39(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            None,
            skipped_pods,
            skipped_namespaces,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_40(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            None,
            skipped_namespaces,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_41(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_pods,
            None,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_42(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_pods,
            skipped_namespaces,
            None,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_43(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_pods,
            skipped_namespaces,
            scanned_namespaces,
            None,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_44(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            raw_pod_logs,
            skipped_pods,
            skipped_namespaces,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_45(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            skipped_pods,
            skipped_namespaces,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_46(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_namespaces,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_47(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_pods,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_48(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_pods,
            skipped_namespaces,
            namespaces_total,
        )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_49(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_pods,
            skipped_namespaces,
            scanned_namespaces,
            )
        return _to_response(result)

    def xǁSemanticLogSearchUseCaseǁexecute__mutmut_50(self, command: SemanticLogSearchCommand) -> SemanticLogSearchResponse:
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
                    pod,
                    namespace,
                    command.time_window_minutes,
                    raw_pod_logs,
                    skipped_pods,
                )
        request = LogSearchRequest(
            pattern=command.pattern,
            is_regex=command.is_regex,  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,  # type: ignore
        )
        result = search_pod_logs(
            request,
            raw_pod_logs,
            skipped_pods,
            skipped_namespaces,
            scanned_namespaces,
            namespaces_total,
        )
        return _to_response(None)

    @_mutmut_mutated(mutants_xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut)
    def _resolve_namespaces(self, namespace: str | None) -> list[str]:
        if namespace is not None:
            self._validate_namespace_exists(namespace)
            return [namespace]
        return [ns["name"] for ns in self._k8s_port.list_namespaces()]

    def xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_orig(self, namespace: str | None) -> list[str]:
        if namespace is not None:
            self._validate_namespace_exists(namespace)
            return [namespace]
        return [ns["name"] for ns in self._k8s_port.list_namespaces()]

    def xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_1(self, namespace: str | None) -> list[str]:
        if namespace is None:
            self._validate_namespace_exists(namespace)
            return [namespace]
        return [ns["name"] for ns in self._k8s_port.list_namespaces()]

    def xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_2(self, namespace: str | None) -> list[str]:
        if namespace is not None:
            self._validate_namespace_exists(None)
            return [namespace]
        return [ns["name"] for ns in self._k8s_port.list_namespaces()]

    def xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_3(self, namespace: str | None) -> list[str]:
        if namespace is not None:
            self._validate_namespace_exists(namespace)
            return [namespace]
        return [ns["XXnameXX"] for ns in self._k8s_port.list_namespaces()]

    def xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_4(self, namespace: str | None) -> list[str]:
        if namespace is not None:
            self._validate_namespace_exists(namespace)
            return [namespace]
        return [ns["NAME"] for ns in self._k8s_port.list_namespaces()]

    @_mutmut_mutated(mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut)
    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_orig(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_1(self, namespace: str) -> None:
        namespaces = None
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_2(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_3(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(None):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_4(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["XXnameXX"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_5(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["NAME"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_6(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] != namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_7(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                None, context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_8(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context=None
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_9(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                context={"namespace": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_10(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_11(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"XXnamespaceXX": namespace}
            )

    def xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_12(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"NAMESPACE": namespace}
            )

    @_mutmut_mutated(mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut)
    def _collect_pod_logs(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_orig(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_1(  # noqa: PLR0913
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = None
        status = str(pod["status"])
        if status in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_2(  # noqa: PLR0913
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = str(None)
        status = str(pod["status"])
        if status in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_3(  # noqa: PLR0913
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = str(pod["XXnameXX"])
        status = str(pod["status"])
        if status in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_4(  # noqa: PLR0913
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = str(pod["NAME"])
        status = str(pod["status"])
        if status in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_5(  # noqa: PLR0913
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = str(pod["name"])
        status = None
        if status in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_6(  # noqa: PLR0913
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = str(pod["name"])
        status = str(None)
        if status in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_7(  # noqa: PLR0913
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = str(pod["name"])
        status = str(pod["XXstatusXX"])
        if status in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_8(  # noqa: PLR0913
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = str(pod["name"])
        status = str(pod["STATUS"])
        if status in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_9(  # noqa: PLR0913
        self,
        pod: PodInfo,
        namespace: str,
        time_window_minutes: int,
        raw_pod_logs: list[RawPodLogData],
        skipped_pods: list[SkippedPod],
    ) -> None:
        pod_name = str(pod["name"])
        status = str(pod["status"])
        if status not in _NO_LOG_STATUSES:
            skipped_pods.append(
                SkippedPod(
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_10(  # noqa: PLR0913
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
                None
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_11(  # noqa: PLR0913
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
                    pod_name=None,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_12(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=None,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_13(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=None,
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_14(  # noqa: PLR0913
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
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_15(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    reason=f"{status}: no logs available",
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_16(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_17(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = None
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_18(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                None, namespace, time_window_minutes
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_19(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, None, time_window_minutes
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_20(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, None
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_21(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                namespace, time_window_minutes
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_22(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, time_window_minutes
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_23(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, )
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

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_24(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, time_window_minutes
            )
        except _PER_POD_ERRORS as exc:
            skipped_pods.append(None)
            return
        if not container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_25(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, time_window_minutes
            )
        except _PER_POD_ERRORS as exc:
            skipped_pods.append(SkippedPod(pod_name=None, namespace=namespace, reason=str(exc)))
            return
        if not container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_26(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, time_window_minutes
            )
        except _PER_POD_ERRORS as exc:
            skipped_pods.append(SkippedPod(pod_name=pod_name, namespace=None, reason=str(exc)))
            return
        if not container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_27(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, time_window_minutes
            )
        except _PER_POD_ERRORS as exc:
            skipped_pods.append(SkippedPod(pod_name=pod_name, namespace=namespace, reason=None))
            return
        if not container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_28(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, time_window_minutes
            )
        except _PER_POD_ERRORS as exc:
            skipped_pods.append(SkippedPod(namespace=namespace, reason=str(exc)))
            return
        if not container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_29(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, time_window_minutes
            )
        except _PER_POD_ERRORS as exc:
            skipped_pods.append(SkippedPod(pod_name=pod_name, reason=str(exc)))
            return
        if not container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_30(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, time_window_minutes
            )
        except _PER_POD_ERRORS as exc:
            skipped_pods.append(SkippedPod(pod_name=pod_name, namespace=namespace, ))
            return
        if not container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_31(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
                )
            )
            return
        try:
            container_logs = self._port.fetch_pod_container_logs(
                pod_name, namespace, time_window_minutes
            )
        except _PER_POD_ERRORS as exc:
            skipped_pods.append(SkippedPod(pod_name=pod_name, namespace=namespace, reason=str(None)))
            return
        if not container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_32(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
        if container_logs:
            skipped_pods.append(
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_33(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
                None
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_34(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
                SkippedPod(pod_name=None, namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_35(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
                SkippedPod(pod_name=pod_name, namespace=None, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_36(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
                SkippedPod(pod_name=pod_name, namespace=namespace, reason=None)
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_37(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
                SkippedPod(namespace=namespace, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_38(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
                SkippedPod(pod_name=pod_name, reason="no logs available")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_39(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
                SkippedPod(pod_name=pod_name, namespace=namespace, )
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_40(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="XXno logs availableXX")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_41(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
                SkippedPod(pod_name=pod_name, namespace=namespace, reason="NO LOGS AVAILABLE")
            )
            return
        raw_pod_logs.append(
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_42(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
            None
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_43(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
            RawPodLogData(pod_name=None, namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_44(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
            RawPodLogData(pod_name=pod_name, namespace=None, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_45(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
            RawPodLogData(pod_name=pod_name, namespace=namespace, containers=None)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_46(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
            RawPodLogData(namespace=namespace, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_47(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
            RawPodLogData(pod_name=pod_name, containers=container_logs)
        )

    def xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_48(  # noqa: PLR0913
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
                    pod_name=pod_name,
                    namespace=namespace,
                    reason=f"{status}: no logs available",
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
            RawPodLogData(pod_name=pod_name, namespace=namespace, )
        )

mutants_xǁSemanticLogSearchUseCaseǁ__init____mutmut['_mutmut_orig'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ__init____mutmut['xǁSemanticLogSearchUseCaseǁ__init____mutmut_1'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ__init____mutmut['xǁSemanticLogSearchUseCaseǁ__init____mutmut_2'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['_mutmut_orig'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_1'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_2'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_3'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_4'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_5'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_6'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_7'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_8'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_9'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_10'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_11'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_12'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_13'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_14'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_15'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_16'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_17'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_18'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_19'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_20'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_21'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_22'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_23'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_24'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_25'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_26'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_27'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_28'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_29'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_30'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_31'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_32'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_33'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_34'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_35'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_36'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_37'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_38'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_39'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_40'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_41'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_42'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_43'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_44'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_45'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_46'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_47'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_48'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_49'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁexecute__mutmut['xǁSemanticLogSearchUseCaseǁexecute__mutmut_50'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated

mutants_xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut['_mutmut_orig'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut['xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_1'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut['xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_2'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut['xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_3'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut['xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_4'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_resolve_namespaces__mutmut_4 # type: ignore # mutmut generated

mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['_mutmut_orig'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_1'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_2'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_3'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_4'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_5'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_6'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_7'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_8'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_9'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_10'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_11'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut['xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_12'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_validate_namespace_exists__mutmut_12 # type: ignore # mutmut generated

mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['_mutmut_orig'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_1'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_2'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_3'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_4'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_5'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_6'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_7'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_8'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_9'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_10'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_11'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_12'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_13'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_14'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_15'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_16'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_17'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_18'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_19'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_20'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_21'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_22'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_23'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_24'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_25'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_26'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_27'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_28'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_29'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_30'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_31'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_32'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_33'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_33 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_34'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_34 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_35'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_35 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_36'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_36 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_37'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_37 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_38'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_38 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_39'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_39 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_40'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_40 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_41'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_41 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_42'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_42 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_43'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_43 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_44'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_44 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_45'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_45 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_46'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_46 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_47'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_47 # type: ignore # mutmut generated
mutants_xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut['xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_48'] = SemanticLogSearchUseCase.xǁSemanticLogSearchUseCaseǁ_collect_pod_logs__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_orig(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_1(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=None,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_2(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=None,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_3(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=None,  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_4(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=None,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_5(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=None,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_6(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=None,  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_7(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=None,  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_8(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=None,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_9(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=None,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_10(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=None,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_11(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=None,
    )


def x__to_response__mutmut_12(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_13(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_14(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_15(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_16(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_17(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_18(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_19(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_20(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_21(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_22(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        )


def x__to_response__mutmut_23(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(None) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_24(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(None) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(ns) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
    )


def x__to_response__mutmut_25(result: LogSearchResult) -> SemanticLogSearchResponse:
    return SemanticLogSearchResponse(
        pattern=result.pattern,
        time_window_minutes=result.time_window_minutes,  # type: ignore
        groups=[_to_group_dict(group) for group in result.groups],  # type: ignore
        pods_affected=result.pods_affected,  # type: ignore
        services_affected=result.services_affected,  # type: ignore
        skipped_pods=[_to_skipped_pod_dict(pod) for pod in result.skipped_pods],  # type: ignore
        skipped_namespaces=[_to_skipped_namespace_dict(None) for ns in result.skipped_namespaces],  # type: ignore
        scanned_namespaces=result.scanned_namespaces,  # type: ignore
        namespaces_total=result.namespaces_total,  # type: ignore
        no_matches=result.no_matches,  # type: ignore
        summary=result.summary,
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
mutants_x__to_group_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_group_dict__mutmut)
def _to_group_dict(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(  # type: ignore
        service_name=group.service_name,
        namespace=group.namespace,
        pods=[_to_pod_match_dict(pod) for pod in group.pods],
    )


def x__to_group_dict__mutmut_orig(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(  # type: ignore
        service_name=group.service_name,
        namespace=group.namespace,
        pods=[_to_pod_match_dict(pod) for pod in group.pods],
    )


def x__to_group_dict__mutmut_1(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(  # type: ignore
        service_name=None,
        namespace=group.namespace,
        pods=[_to_pod_match_dict(pod) for pod in group.pods],
    )


def x__to_group_dict__mutmut_2(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(  # type: ignore
        service_name=group.service_name,
        namespace=None,
        pods=[_to_pod_match_dict(pod) for pod in group.pods],
    )


def x__to_group_dict__mutmut_3(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(  # type: ignore
        service_name=group.service_name,
        namespace=group.namespace,
        pods=None,
    )


def x__to_group_dict__mutmut_4(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(  # type: ignore
        namespace=group.namespace,
        pods=[_to_pod_match_dict(pod) for pod in group.pods],
    )


def x__to_group_dict__mutmut_5(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(  # type: ignore
        service_name=group.service_name,
        pods=[_to_pod_match_dict(pod) for pod in group.pods],
    )


def x__to_group_dict__mutmut_6(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(  # type: ignore
        service_name=group.service_name,
        namespace=group.namespace,
        )


def x__to_group_dict__mutmut_7(group: ServiceGroup) -> ServiceGroupDict:
    return ServiceGroupDict(  # type: ignore
        service_name=group.service_name,
        namespace=group.namespace,
        pods=[_to_pod_match_dict(None) for pod in group.pods],
    )

mutants_x__to_group_dict__mutmut['_mutmut_orig'] = x__to_group_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_1'] = x__to_group_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_2'] = x__to_group_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_3'] = x__to_group_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_4'] = x__to_group_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_5'] = x__to_group_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_6'] = x__to_group_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_7'] = x__to_group_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_pod_match_dict__mutmut)
def _to_pod_match_dict(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=match.pod_name,
        namespace=match.namespace,
        container=match.container,
        matching_lines=[_to_line_dict(line) for line in match.matching_lines],
    )


def x__to_pod_match_dict__mutmut_orig(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=match.pod_name,
        namespace=match.namespace,
        container=match.container,
        matching_lines=[_to_line_dict(line) for line in match.matching_lines],
    )


def x__to_pod_match_dict__mutmut_1(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=None,
        namespace=match.namespace,
        container=match.container,
        matching_lines=[_to_line_dict(line) for line in match.matching_lines],
    )


def x__to_pod_match_dict__mutmut_2(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=match.pod_name,
        namespace=None,
        container=match.container,
        matching_lines=[_to_line_dict(line) for line in match.matching_lines],
    )


def x__to_pod_match_dict__mutmut_3(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=match.pod_name,
        namespace=match.namespace,
        container=None,
        matching_lines=[_to_line_dict(line) for line in match.matching_lines],
    )


def x__to_pod_match_dict__mutmut_4(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=match.pod_name,
        namespace=match.namespace,
        container=match.container,
        matching_lines=None,
    )


def x__to_pod_match_dict__mutmut_5(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        namespace=match.namespace,
        container=match.container,
        matching_lines=[_to_line_dict(line) for line in match.matching_lines],
    )


def x__to_pod_match_dict__mutmut_6(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=match.pod_name,
        container=match.container,
        matching_lines=[_to_line_dict(line) for line in match.matching_lines],
    )


def x__to_pod_match_dict__mutmut_7(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=match.pod_name,
        namespace=match.namespace,
        matching_lines=[_to_line_dict(line) for line in match.matching_lines],
    )


def x__to_pod_match_dict__mutmut_8(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=match.pod_name,
        namespace=match.namespace,
        container=match.container,
        )


def x__to_pod_match_dict__mutmut_9(match: PodLogMatch) -> PodLogMatchDict:
    return PodLogMatchDict(  # type: ignore
        pod_name=match.pod_name,
        namespace=match.namespace,
        container=match.container,
        matching_lines=[_to_line_dict(None) for line in match.matching_lines],
    )

mutants_x__to_pod_match_dict__mutmut['_mutmut_orig'] = x__to_pod_match_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut['x__to_pod_match_dict__mutmut_1'] = x__to_pod_match_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut['x__to_pod_match_dict__mutmut_2'] = x__to_pod_match_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut['x__to_pod_match_dict__mutmut_3'] = x__to_pod_match_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut['x__to_pod_match_dict__mutmut_4'] = x__to_pod_match_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut['x__to_pod_match_dict__mutmut_5'] = x__to_pod_match_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut['x__to_pod_match_dict__mutmut_6'] = x__to_pod_match_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut['x__to_pod_match_dict__mutmut_7'] = x__to_pod_match_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut['x__to_pod_match_dict__mutmut_8'] = x__to_pod_match_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_pod_match_dict__mutmut['x__to_pod_match_dict__mutmut_9'] = x__to_pod_match_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_line_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_line_dict__mutmut)
def _to_line_dict(line: MatchedLogLine) -> MatchedLogLineDict:
    return MatchedLogLineDict(  # type: ignore
        timestamp=line.timestamp, message=line.message, match_type=line.match_type
    )


def x__to_line_dict__mutmut_orig(line: MatchedLogLine) -> MatchedLogLineDict:
    return MatchedLogLineDict(  # type: ignore
        timestamp=line.timestamp, message=line.message, match_type=line.match_type
    )


def x__to_line_dict__mutmut_1(line: MatchedLogLine) -> MatchedLogLineDict:
    return MatchedLogLineDict(  # type: ignore
        timestamp=None, message=line.message, match_type=line.match_type
    )


def x__to_line_dict__mutmut_2(line: MatchedLogLine) -> MatchedLogLineDict:
    return MatchedLogLineDict(  # type: ignore
        timestamp=line.timestamp, message=None, match_type=line.match_type
    )


def x__to_line_dict__mutmut_3(line: MatchedLogLine) -> MatchedLogLineDict:
    return MatchedLogLineDict(  # type: ignore
        timestamp=line.timestamp, message=line.message, match_type=None
    )


def x__to_line_dict__mutmut_4(line: MatchedLogLine) -> MatchedLogLineDict:
    return MatchedLogLineDict(  # type: ignore
        message=line.message, match_type=line.match_type
    )


def x__to_line_dict__mutmut_5(line: MatchedLogLine) -> MatchedLogLineDict:
    return MatchedLogLineDict(  # type: ignore
        timestamp=line.timestamp, match_type=line.match_type
    )


def x__to_line_dict__mutmut_6(line: MatchedLogLine) -> MatchedLogLineDict:
    return MatchedLogLineDict(  # type: ignore
        timestamp=line.timestamp, message=line.message, )

mutants_x__to_line_dict__mutmut['_mutmut_orig'] = x__to_line_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_line_dict__mutmut['x__to_line_dict__mutmut_1'] = x__to_line_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_line_dict__mutmut['x__to_line_dict__mutmut_2'] = x__to_line_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_line_dict__mutmut['x__to_line_dict__mutmut_3'] = x__to_line_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_line_dict__mutmut['x__to_line_dict__mutmut_4'] = x__to_line_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_line_dict__mutmut['x__to_line_dict__mutmut_5'] = x__to_line_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_line_dict__mutmut['x__to_line_dict__mutmut_6'] = x__to_line_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_skipped_pod_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_skipped_pod_dict__mutmut)
def _to_skipped_pod_dict(pod: SkippedPod) -> SkippedPodDict:
    return SkippedPodDict(pod_name=pod.pod_name, namespace=pod.namespace, reason=pod.reason)


def x__to_skipped_pod_dict__mutmut_orig(pod: SkippedPod) -> SkippedPodDict:
    return SkippedPodDict(pod_name=pod.pod_name, namespace=pod.namespace, reason=pod.reason)


def x__to_skipped_pod_dict__mutmut_1(pod: SkippedPod) -> SkippedPodDict:
    return SkippedPodDict(pod_name=None, namespace=pod.namespace, reason=pod.reason)


def x__to_skipped_pod_dict__mutmut_2(pod: SkippedPod) -> SkippedPodDict:
    return SkippedPodDict(pod_name=pod.pod_name, namespace=None, reason=pod.reason)


def x__to_skipped_pod_dict__mutmut_3(pod: SkippedPod) -> SkippedPodDict:
    return SkippedPodDict(pod_name=pod.pod_name, namespace=pod.namespace, reason=None)


def x__to_skipped_pod_dict__mutmut_4(pod: SkippedPod) -> SkippedPodDict:
    return SkippedPodDict(namespace=pod.namespace, reason=pod.reason)


def x__to_skipped_pod_dict__mutmut_5(pod: SkippedPod) -> SkippedPodDict:
    return SkippedPodDict(pod_name=pod.pod_name, reason=pod.reason)


def x__to_skipped_pod_dict__mutmut_6(pod: SkippedPod) -> SkippedPodDict:
    return SkippedPodDict(pod_name=pod.pod_name, namespace=pod.namespace, )

mutants_x__to_skipped_pod_dict__mutmut['_mutmut_orig'] = x__to_skipped_pod_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_skipped_pod_dict__mutmut['x__to_skipped_pod_dict__mutmut_1'] = x__to_skipped_pod_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_skipped_pod_dict__mutmut['x__to_skipped_pod_dict__mutmut_2'] = x__to_skipped_pod_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_skipped_pod_dict__mutmut['x__to_skipped_pod_dict__mutmut_3'] = x__to_skipped_pod_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_skipped_pod_dict__mutmut['x__to_skipped_pod_dict__mutmut_4'] = x__to_skipped_pod_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_skipped_pod_dict__mutmut['x__to_skipped_pod_dict__mutmut_5'] = x__to_skipped_pod_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_skipped_pod_dict__mutmut['x__to_skipped_pod_dict__mutmut_6'] = x__to_skipped_pod_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_skipped_namespace_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_skipped_namespace_dict__mutmut)
def _to_skipped_namespace_dict(ns: SkippedNamespace) -> SkippedNamespaceDict:
    return SkippedNamespaceDict(namespace=ns.namespace, reason=ns.reason)


def x__to_skipped_namespace_dict__mutmut_orig(ns: SkippedNamespace) -> SkippedNamespaceDict:
    return SkippedNamespaceDict(namespace=ns.namespace, reason=ns.reason)


def x__to_skipped_namespace_dict__mutmut_1(ns: SkippedNamespace) -> SkippedNamespaceDict:
    return SkippedNamespaceDict(namespace=None, reason=ns.reason)


def x__to_skipped_namespace_dict__mutmut_2(ns: SkippedNamespace) -> SkippedNamespaceDict:
    return SkippedNamespaceDict(namespace=ns.namespace, reason=None)


def x__to_skipped_namespace_dict__mutmut_3(ns: SkippedNamespace) -> SkippedNamespaceDict:
    return SkippedNamespaceDict(reason=ns.reason)


def x__to_skipped_namespace_dict__mutmut_4(ns: SkippedNamespace) -> SkippedNamespaceDict:
    return SkippedNamespaceDict(namespace=ns.namespace, )

mutants_x__to_skipped_namespace_dict__mutmut['_mutmut_orig'] = x__to_skipped_namespace_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_skipped_namespace_dict__mutmut['x__to_skipped_namespace_dict__mutmut_1'] = x__to_skipped_namespace_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_skipped_namespace_dict__mutmut['x__to_skipped_namespace_dict__mutmut_2'] = x__to_skipped_namespace_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_skipped_namespace_dict__mutmut['x__to_skipped_namespace_dict__mutmut_3'] = x__to_skipped_namespace_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_skipped_namespace_dict__mutmut['x__to_skipped_namespace_dict__mutmut_4'] = x__to_skipped_namespace_dict__mutmut_4 # type: ignore # mutmut generated
