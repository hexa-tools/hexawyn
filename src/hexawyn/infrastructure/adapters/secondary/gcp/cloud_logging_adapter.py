from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Protocol

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_MAX_LINES_PER_CONTAINER = 5000
_UNKNOWN_CONTAINER = "unknown"
_CREDENTIALS_HINT = "Run 'gcloud auth application-default login', then retry."


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


class GCPCloudLoggingAdapter(LogSearchPort):
    """LogSearchPort backed by Google Cloud Logging on GKE.

    Reads pod/container logs from Cloud Logging via `list_entries` filtered
    by resource type + pod name — no `kubectl logs` needed.
    """

    def __init__(self, project_id: str, logging_client: LoggingClient | None = None) -> None:
        self._project_id = project_id
        self._logging_client = logging_client
        self._resource_names = [f"projects/{project_id}"]

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

    def _container_name(self, entry: _LogEntry) -> str:
        labels = getattr(entry.resource, "labels", {})
        if isinstance(labels, dict):
            return str(labels.get("container_name", _UNKNOWN_CONTAINER))
        return _UNKNOWN_CONTAINER

    def _client_or_create(self) -> LoggingClient:
        client = self._logging_client
        if client is None:
            from google.cloud import logging_v2

            client = _as_logging_client(logging_v2.Client(project=self._project_id))
            self._logging_client = client
        return client


def _as_logging_client(client: object) -> LoggingClient:
    return client  # type: ignore[return-value]
