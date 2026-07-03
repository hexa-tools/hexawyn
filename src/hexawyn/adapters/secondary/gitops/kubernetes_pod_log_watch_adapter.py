from __future__ import annotations

import json
from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
from hexawyn.domain.errors import ClusterUnreachableError, ResourceNotFoundError

if TYPE_CHECKING:
    from collections.abc import Iterator

    from hexawyn.domain.models.analyze_pod_logs import PodLogLine
    from hexawyn.domain.models.watch_pod_logs import WatchPodLogsRequest

_K8S_NOT_FOUND = 404
_LEVEL_KEYWORDS = ("FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG")
_MIN_TIMESTAMP_LENGTH = 20


class KubernetesPodLogWatchAdapter(PodLogWatchPort):
    """Secondary adapter — live-tails pod logs via the Kubernetes watch API.

    Reconnects transparently on transient network errors (up to
    request.max_reconnect_attempts) without ever buffering the full log
    output — each line is yielded as it arrives.
    """

    def watch(self, request: WatchPodLogsRequest) -> Iterator[PodLogLine]:
        from kubernetes import client as k8s
        from kubernetes import watch as k8s_watch

        core_api = k8s.CoreV1Api()
        self._ensure_pod_exists(core_api, request)

        attempts = 0
        while True:
            try:
                watcher = k8s_watch.Watch()
                stream = watcher.stream(
                    core_api.read_namespaced_pod_log,
                    name=request.pod_name,
                    namespace=request.namespace,
                    follow=True,
                    timestamps=True,
                    _request_timeout=request.timeout_seconds,
                )
                for raw_line in stream:
                    yield _parse_line(raw_line)
                return
            except Exception as exc:
                attempts += 1
                if attempts > request.max_reconnect_attempts:
                    raise ClusterUnreachableError(
                        f"Lost connection to pod {request.pod_name!r} after "
                        f"{attempts - 1} reconnect attempts: {exc}"
                    ) from exc

    def pod_exists(self, pod_name: str, namespace: str) -> bool:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            core_api.read_namespaced_pod(name=pod_name, namespace=namespace)
        except Exception as exc:
            status = getattr(exc, "status", None)
            return status != _K8S_NOT_FOUND
        return True

    def _ensure_pod_exists(self, core_api: object, request: WatchPodLogsRequest) -> None:
        try:
            core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise ResourceNotFoundError(
                    f"Pod {request.pod_name!r} not found in namespace {request.namespace!r}",
                    context={"pod_name": request.pod_name, "namespace": request.namespace},
                ) from exc


def _parse_line(raw_line: str) -> PodLogLine:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    timestamp, message = _split_timestamp(raw_line)
    is_json, message, level = _parse_message(message)
    return PodLogLine(
        timestamp=timestamp, level=level, message=message, run_index=0, is_json=is_json
    )


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
