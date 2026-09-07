from __future__ import annotations

from collections.abc import Iterable, Sequence
from datetime import timedelta
from typing import Protocol, cast

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_MAX_LINES_PER_CONTAINER = 5000
_UNKNOWN_CONTAINER = "unknown"
_FORBIDDEN_STATUS = 403
_CREDENTIALS_HINT = "Run 'az login' or attach a managed identity, then retry."
_CONTAINER_LOG_TABLE = "ContainerLogV2"


class _LogsTable(Protocol):
    columns: Sequence[str]
    rows: Iterable[Sequence[object]]


class _LogsResult(Protocol):
    status: object
    tables: Sequence[_LogsTable]


class LogsClient(Protocol):
    """Minimal contract for the azure-monitor-query LogsQueryClient used here."""

    def query_workspace(
        self, workspace_id: str, query: str, *, timespan: timedelta
    ) -> _LogsResult: ...


class AzureLogAnalyticsAdapter(LogSearchPort):
    """LogSearchPort backed by Azure Log Analytics (ContainerLogV2) via KQL.

    Reads pod/container logs from the Log Analytics workspace — no
    `kubectl logs` needed on AKS.
    """

    def __init__(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = workspace_id
        self._logs_client = logs_client

    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        table = self._query(self._logs_kql(pod_name, namespace), time_window_minutes)
        if table is None:
            return []
        return self._group_by_container(table)

    def _logs_kql(self, pod_name: str, namespace: str) -> str:
        return (
            f"{_CONTAINER_LOG_TABLE} "
            f'| where PodName == "{pod_name}" and PodNamespace == "{namespace}" '
            f"| project ContainerName, LogMessage "
            f"| take {_MAX_LINES_PER_CONTAINER * 4}"
        )

    def _query(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise ClusterUnreachableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            if getattr(exc, "status_code", None) == _FORBIDDEN_STATUS:
                raise InsufficientPermissionsError(
                    "Access denied reading Azure Log Analytics.",
                    context={"workspace": self._workspace_id},
                ) from exc
            raise ClusterUnreachableError(
                "Unable to query Azure Log Analytics.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise ClusterUnreachableError(
                "Azure Log Analytics query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def _group_by_container(self, table: _LogsTable) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        columns = list(table.columns)
        for row in table.rows:
            mapping = dict(zip(columns, [row[i] for i in range(len(columns))], strict=False))
            container = str(mapping.get("ContainerName", _UNKNOWN_CONTAINER))
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            for line in str(mapping.get("LogMessage", "")).splitlines():
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

    def _client_or_create(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client
