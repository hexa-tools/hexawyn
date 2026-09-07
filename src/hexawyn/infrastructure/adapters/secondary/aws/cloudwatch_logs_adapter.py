from __future__ import annotations

import json
from typing import Protocol, TypedDict

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_MINUTES_TO_MILLIS = 60 * 1000
_MAX_LINES_PER_CONTAINER = 5000
_UNKNOWN_CONTAINER = "unknown"
_ACCESS_DENIED_CODE = "AccessDeniedException"
_NOT_FOUND_CODE = "ResourceNotFoundException"


class _LogEvent(TypedDict, total=False):
    message: str


class _FilterLogEventsResponse(TypedDict, total=False):
    events: list[_LogEvent]
    nextToken: str


class LogsClient(Protocol):
    """Minimal contract for the boto3 CloudWatch Logs client used here."""

    def filter_log_events(self, **kwargs: object) -> _FilterLogEventsResponse:
        """Return log events matching a filter within a time window."""


class CloudWatchLogsAdapter(LogSearchPort):
    """LogSearchPort backed by CloudWatch Logs (Container Insights).

    Reads pod/container logs from the Container Insights `application` log
    group — no `kubectl logs` needed on EKS.
    """

    def __init__(
        self, cluster_name: str, region: str | None, logs_client: LogsClient | None = None
    ) -> None:
        self._cluster_name = cluster_name
        self._region = region
        self._logs_client = logs_client

    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        import time

        end_ms = int(time.time() * 1000)
        start_ms = end_ms - time_window_minutes * _MINUTES_TO_MILLIS
        messages = self._filter_events(pod_name, namespace, start_ms, end_ms)
        return self._group_by_container(messages)

    def _log_group(self) -> str:
        return f"/aws/containerinsights/{self._cluster_name}/application"

    def _filter_pattern(self, pod_name: str, namespace: str) -> str:
        return (
            f'{{ $.kubernetes.pod_name = "{pod_name}" '
            f'&& $.kubernetes.namespace_name = "{namespace}" }}'
        )

    def _filter_events(
        self, pod_name: str, namespace: str, start_ms: int, end_ms: int
    ) -> list[str]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        messages: list[str] = []
        page_cursor: str | None = None
        try:
            while True:
                response = self._filter_page(
                    client, pod_name, namespace, start_ms, end_ms, page_cursor
                )
                messages.extend(
                    event["message"] for event in response.get("events", []) if event.get("message")
                )
                page_cursor = response.get("nextToken")
                if not page_cursor:
                    break
        except NoCredentialsError as exc:
            raise ClusterUnreachableError(
                "AWS credentials not found. Run 'aws configure' or attach an IAM role.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except ClientError as exc:
            return self._handle_client_error(exc)
        except BotoCoreError as exc:
            raise ClusterUnreachableError(
                "Unable to reach CloudWatch Logs.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc
        return messages

    def _filter_page(  # noqa: PLR0913
        self,
        client: LogsClient,
        pod_name: str,
        namespace: str,
        start_ms: int,
        end_ms: int,
        page_cursor: str | None,
    ) -> _FilterLogEventsResponse:
        request: dict[str, object] = {
            "logGroupName": self._log_group(),
            "filterPattern": self._filter_pattern(pod_name, namespace),
            "startTime": start_ms,
            "endTime": end_ms,
        }
        if page_cursor:
            request["nextToken"] = page_cursor
        return client.filter_log_events(**request)

    def _handle_client_error(self, exc: Exception) -> list[str]:
        code = _error_code(exc)
        if code == _NOT_FOUND_CODE:
            return []
        if code == _ACCESS_DENIED_CODE:
            raise InsufficientPermissionsError(
                "Access denied reading CloudWatch Logs.",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        raise ClusterUnreachableError(
            "CloudWatch Logs query failed.",
            context={
                "cluster": self._cluster_name,
                "region": self._region or "unknown",
                "error": str(exc),
            },
        ) from exc

    def _group_by_container(self, messages: list[str]) -> list[RawContainerLog]:
        lines_by_container: dict[str, list[str]] = {}
        truncated_containers: set[str] = set()
        for message in messages:
            container, line = _parse_message(message)
            lines = lines_by_container.setdefault(container, [])
            if len(lines) >= _MAX_LINES_PER_CONTAINER:
                truncated_containers.add(container)
                continue
            lines.append(line)
        return [
            RawContainerLog(
                container=container,
                lines=lines,
                truncated=container in truncated_containers,
            )
            for container, lines in lines_by_container.items()
        ]

    def _client_or_create(self) -> LogsClient:
        if self._logs_client is None:
            import boto3

            self._logs_client = boto3.client("logs", region_name=self._region)
        return self._logs_client


def _error_code(exc: Exception) -> str:
    response = getattr(exc, "response", None)
    if isinstance(response, dict):
        error = response.get("Error", {})
        if isinstance(error, dict):
            return str(error.get("Code", ""))
    return ""


def _parse_message(message: str) -> tuple[str, str]:
    try:
        parsed = json.loads(message)
    except (ValueError, TypeError):
        return _UNKNOWN_CONTAINER, message
    if not isinstance(parsed, dict):
        return _UNKNOWN_CONTAINER, message
    kubernetes = parsed.get("kubernetes", {})
    container = _UNKNOWN_CONTAINER
    if isinstance(kubernetes, dict):
        container = str(kubernetes.get("container_name", _UNKNOWN_CONTAINER))
    line = str(parsed.get("log", message))
    return container, line
