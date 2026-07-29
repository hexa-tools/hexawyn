from __future__ import annotations

import json
from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)

if TYPE_CHECKING:
    from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest, PodLogLine

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404
_CURRENT_RUN = 0
_PREVIOUS_RUN = 1
_LEVEL_KEYWORDS = ("FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG")
_MIN_TIMESTAMP_LENGTH = 20


class KubernetesPodLogsAdapter(PodLogsPort):
    """Secondary adapter — reads pod logs from the Kubernetes API."""

    def fetch_logs(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def _read_logs(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def _has_restarted(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 0 for status in statuses)


def _translate_error(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def _parse_lines(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def _split_timestamp(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def _parse_message(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def _detect_level(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"
