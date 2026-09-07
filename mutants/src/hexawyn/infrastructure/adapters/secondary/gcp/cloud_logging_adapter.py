from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Protocol

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_MAX_LINES_PER_CONTAINER = 5000
_UNKNOWN_CONTAINER = "unknown"
_CREDENTIALS_HINT = "Run 'gcloud auth application-default login', then retry."


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _LogEntry(Protocol):
    payload: str
    timestamp: datetime | None
    resource: object  # labels: dict[str, str]


class LoggingClient(Protocol):
    """Minimal contract for the google-cloud-logging Client used here."""

    def list_entries(
        self,
        *,
        resource_names: list[str] | None,
        filter_: str | None,
        max_results: int | None,
    ) -> list[_LogEntry]:
        """Return log entries matching the filter."""
mutants_xǁGCPCloudLoggingAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class GCPCloudLoggingAdapter(LogSearchPort):
    """LogSearchPort backed by Google Cloud Logging on GKE.

    Reads pod/container logs from Cloud Logging via `list_entries` filtered
    by resource type + pod name — no `kubectl logs` needed.
    """

    @_mutmut_mutated(mutants_xǁGCPCloudLoggingAdapterǁ__init____mutmut)
    def __init__(self, project_id: str, logging_client: LoggingClient | None = None) -> None:
        self._project_id = project_id
        self._logging_client = logging_client
        self._resource_names = [f"projects/{project_id}"]

    def xǁGCPCloudLoggingAdapterǁ__init____mutmut_orig(self, project_id: str, logging_client: LoggingClient | None = None) -> None:
        self._project_id = project_id
        self._logging_client = logging_client
        self._resource_names = [f"projects/{project_id}"]

    def xǁGCPCloudLoggingAdapterǁ__init____mutmut_1(self, project_id: str, logging_client: LoggingClient | None = None) -> None:
        self._project_id = None
        self._logging_client = logging_client
        self._resource_names = [f"projects/{project_id}"]

    def xǁGCPCloudLoggingAdapterǁ__init____mutmut_2(self, project_id: str, logging_client: LoggingClient | None = None) -> None:
        self._project_id = project_id
        self._logging_client = None
        self._resource_names = [f"projects/{project_id}"]

    def xǁGCPCloudLoggingAdapterǁ__init____mutmut_3(self, project_id: str, logging_client: LoggingClient | None = None) -> None:
        self._project_id = project_id
        self._logging_client = logging_client
        self._resource_names = None

    @_mutmut_mutated(mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut)
    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_orig(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_1(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = None
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_2(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(None)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_3(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = None
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_4(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end + timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_5(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=None)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_6(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = None
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_7(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = None
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_8(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=None, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_9(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=None, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_10(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_11(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_12(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_13(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                None,
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_14(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context=None,
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_15(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_16(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_17(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"XXprojectXX": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_18(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"PROJECT": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_19(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "XXpodXX": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_20(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "POD": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_21(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                None,
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_22(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context=None,
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_23(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_24(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_25(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "XXAccess denied reading Cloud Logging.XX",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_26(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "access denied reading cloud logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_27(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "ACCESS DENIED READING CLOUD LOGGING.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_28(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"XXprojectXX": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_29(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"PROJECT": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_30(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                None,
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_31(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context=None,
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_32(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_33(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_34(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "XXCloud Logging query failed.XX",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_35(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "cloud logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_36(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "CLOUD LOGGING QUERY FAILED.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_37(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"XXprojectXX": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_38(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"PROJECT": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_39(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "XXpodXX": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_40(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "POD": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_41(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "XXerrorXX": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_42(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "ERROR": str(exc)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_43(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(None)},
            ) from exc
        return self._group_by_container(entries)

    def xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_44(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        from google.api_core.exceptions import GoogleAPICallError, PermissionDenied
        from google.auth.exceptions import DefaultCredentialsError

        end = datetime.now(UTC)
        start = end - timedelta(minutes=time_window_minutes)
        filter_ = (
            f'resource.type="k8s_container" '
            f'resource.labels.pod_name="{pod_name}" '
            f'resource.labels.namespace_name="{namespace}" '
            f'timestamp>="{start.isoformat()}"'
        )
        try:
            entries = self._client_or_create().list_entries(
                resource_names=self._resource_names, filter_=filter_, max_results=None
            )
        except DefaultCredentialsError as exc:
            raise ClusterUnreachableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id, "pod": pod_name},
            ) from exc
        except PermissionDenied as exc:
            raise InsufficientPermissionsError(
                "Access denied reading Cloud Logging.",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise ClusterUnreachableError(
                "Cloud Logging query failed.",
                context={"project": self._project_id, "pod": pod_name, "error": str(exc)},
            ) from exc
        return self._group_by_container(None)

    @_mutmut_mutated(mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut)
    def _group_by_container(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_orig(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_1(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = None
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_2(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = None
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_3(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = None
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_4(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(None)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_5(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = None
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_6(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(None, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_7(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, None)
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_8(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault([])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_9(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, )
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_10(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) > _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_11(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(None)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_12(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                break
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_13(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(None).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_14(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = None
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_15(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(None)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_16(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=None,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_17(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=None,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_18(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=None,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_19(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_20(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_21(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                )
            for container, lines in lines_by_container.items()
        ]

    def xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_22(self, entries: list[_LogEntry]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for entry in entries:
            container = self._container_name(entry)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(entry.payload).splitlines():
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container not in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    @_mutmut_mutated(mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut)
    def _container_name(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_orig(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_1(self, entry: _LogEntry) -> str:
        labels = None
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_2(self, entry: _LogEntry) -> str:
        labels = getattr(None, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_3(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, None, {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_4(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", None)
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_5(self, entry: _LogEntry) -> str:
        labels = getattr("labels", {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_6(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_7(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", )
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_8(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "XXlabelsXX", {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_9(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "LABELS", {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_10(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(None)
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_11(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get(None, _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_12(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", None))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_13(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get(_UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_14(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", ))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_15(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get("XXcontainer_nameXX", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_16(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get("CONTAINER_NAME", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    @_mutmut_mutated(mutants_xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> LoggingClient:
        client = self._logging_client
        if client is None:
            from google.cloud import logging_v2

            client = _as_logging_client(logging_v2.Client(project=self._project_id))
            self._logging_client = client
        return client

    def xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_orig(self) -> LoggingClient:
        client = self._logging_client
        if client is None:
            from google.cloud import logging_v2

            client = _as_logging_client(logging_v2.Client(project=self._project_id))
            self._logging_client = client
        return client

    def xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_1(self) -> LoggingClient:
        client = None
        if client is None:
            from google.cloud import logging_v2

            client = _as_logging_client(logging_v2.Client(project=self._project_id))
            self._logging_client = client
        return client

    def xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_2(self) -> LoggingClient:
        client = self._logging_client
        if client is not None:
            from google.cloud import logging_v2

            client = _as_logging_client(logging_v2.Client(project=self._project_id))
            self._logging_client = client
        return client

    def xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_3(self) -> LoggingClient:
        client = self._logging_client
        if client is None:
            from google.cloud import logging_v2

            client = None
            self._logging_client = client
        return client

    def xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_4(self) -> LoggingClient:
        client = self._logging_client
        if client is None:
            from google.cloud import logging_v2

            client = _as_logging_client(None)
            self._logging_client = client
        return client

    def xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_5(self) -> LoggingClient:
        client = self._logging_client
        if client is None:
            from google.cloud import logging_v2

            client = _as_logging_client(logging_v2.Client(project=None))
            self._logging_client = client
        return client

    def xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_6(self) -> LoggingClient:
        client = self._logging_client
        if client is None:
            from google.cloud import logging_v2

            client = _as_logging_client(logging_v2.Client(project=self._project_id))
            self._logging_client = None
        return client

mutants_xǁGCPCloudLoggingAdapterǁ__init____mutmut['_mutmut_orig'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ__init____mutmut['xǁGCPCloudLoggingAdapterǁ__init____mutmut_1'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ__init____mutmut['xǁGCPCloudLoggingAdapterǁ__init____mutmut_2'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ__init____mutmut['xǁGCPCloudLoggingAdapterǁ__init____mutmut_3'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['_mutmut_orig'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_1'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_2'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_3'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_4'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_5'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_6'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_7'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_8'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_9'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_10'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_11'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_12'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_13'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_14'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_15'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_16'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_17'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_18'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_19'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_20'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_21'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_22'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_23'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_24'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_25'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_26'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_27'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_28'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_29'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_30'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_31'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_32'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_33'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_34'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_35'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_36'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_37'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_38'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_39'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_40'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_41'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_42'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_43'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut['xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_44'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁfetch_pod_container_logs__mutmut_44 # type: ignore # mutmut generated

mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['_mutmut_orig'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_1'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_2'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_3'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_4'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_5'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_6'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_7'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_8'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_9'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_10'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_11'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_12'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_13'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_14'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_15'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_16'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_17'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_18'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_19'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_20'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_21'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut['xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_22'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_group_by_container__mutmut_22 # type: ignore # mutmut generated

mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['_mutmut_orig'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_1'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_2'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_3'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_4'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_5'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_6'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_7'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_8'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_9'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_10'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_11'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_12'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_13'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_14'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_15'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_container_name__mutmut['xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_16'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_container_name__mutmut_16 # type: ignore # mutmut generated

mutants_xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut['xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_1'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut['xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_2'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut['xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_3'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut['xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_4'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut['xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_5'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut['xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_6'] = GCPCloudLoggingAdapter.xǁGCPCloudLoggingAdapterǁ_client_or_create__mutmut_6 # type: ignore # mutmut generated


def _as_logging_client(client: object) -> LoggingClient:
    return client  # type: ignore[return-value]
