from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Protocol, cast

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    ClusterUnreachableError,
    InsufficientPermissionsError,
)

_MAX_LINES_PER_CONTAINER = 5000
_UNKNOWN_CONTAINER = "unknown"
_RATE_LIMIT_STATUS = 429
_UNAUTHORIZED_STATUSES = (401, 403)


class _LogAttribute(Protocol):
    message: str
    timestamp: str
    service: str


class _Log(Protocol):
    attributes: _LogAttribute


class _LogsResponse(Protocol):
    data: list[_Log] | None


class LogsApi(Protocol):
    """Minimal contract for the Datadog v2 LogsApi used here."""

    def list_logs(self, *, body: object) -> _LogsResponse: ...


class DatadogLogsAdapter(LogSearchPort):
    """LogSearchPort backed by Datadog Logs API.

    Reads pod/container logs natively — no `kubectl logs` on Datadog-
    instrumented clusters.
    """

    def __init__(
        self,
        logs_api: LogsApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._logs_api = logs_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        data = self._list_logs(pod_name, namespace, time_window_minutes)
        return self._group_by_container(data)

    def _list_logs(self, pod_name: str, namespace: str, window_minutes: int) -> list[_Log]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.logs_list_request import LogsListRequest
        from datadog_api_client.v2.model.logs_list_request_page import LogsListRequestPage
        from datadog_api_client.v2.model.logs_query_filter import LogsQueryFilter
        from datadog_api_client.v2.model.logs_sort import LogsSort

        now = datetime.now(UTC)
        body = LogsListRequest(
            filter=LogsQueryFilter(
                query=f"kube_pod_name:{pod_name} kube_namespace:{namespace}",
                _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                to=now.isoformat(),
            ),
            page=LogsListRequestPage(limit=100),
            sort=LogsSort.TIMESTAMP_DESCENDING,
        )
        try:
            response = self._api().list_logs(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        return list(response.data or [])

    def _group_by_container(self, logs: list[_Log]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for log in logs:
            attrs = log.attributes
            container = self._container_name(attrs)
            lines = lines_by_container.setdefault(container, [])
            if container in truncated_containers:
                continue
            for line in str(attrs.message).splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if len(lines) >= _MAX_LINES_PER_CONTAINER:
                    truncated_containers.add(container)
                    break
                lines.append(stripped)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def _container_name(self, attrs: _LogAttribute) -> str:
        service = getattr(attrs, "service", None)
        return str(service) if service else _UNKNOWN_CONTAINER

    def _api(self) -> LogsApi:
        if self._logs_api is None:
            self._logs_api = _build_logs_api(self._key, self._app_key, self._site)
        return self._logs_api


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.", context={"status": str(status)}
        )
    return ClusterUnreachableError(
        "Datadog Logs API request failed.", context={"status": str(status)}
    )


def _build_logs_api(key: str, app_key: str, site: str) -> LogsApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.logs_api import LogsApi as DatadogLogsApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(LogsApi, DatadogLogsApi(ApiClient(configuration)))
