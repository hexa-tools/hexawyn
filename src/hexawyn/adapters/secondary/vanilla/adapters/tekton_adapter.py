from __future__ import annotations

from collections.abc import Mapping
from datetime import datetime
from typing import cast

from kubernetes import client
from kubernetes.client.exceptions import ApiException

from hexawyn.adapters.secondary.vanilla.helpers.k8s_client import (
    KubernetesCRDApi,
)
from hexawyn.application.ports.driven.tekton_port import (
    NamespacedPipelineRunInfo,
    PipelineRunInfo,
    TaskRunInfo,
    TektonPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    ComponentNotInstalledError,
    InsufficientPermissionsError,
    PipelineNotFoundError,
    ServiceNotFoundError,
)

_TEKTON_GROUP = "tekton.dev"
_TEKTON_VERSION = "v1"
_TEKTON_TASKRUNS_PLURAL = "taskruns"
_TEKTON_PIPELINERUNS_PLURAL = "pipelineruns"


class VanillaTektonAdapter(TektonPort):
    def __init__(self, crd_api: KubernetesCRDApi | None = None) -> None:
        self._crd_api = crd_api

    def list_task_runs(self, pipeline_name: str, namespace: str) -> list[TaskRunInfo]:
        raw = self._fetch_task_runs(pipeline_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise PipelineNotFoundError(pipeline_name=pipeline_name)
        return [self._to_task_run_info(item) for item in items]

    def list_pipeline_runs(self, service_name: str, namespace: str) -> list[PipelineRunInfo]:
        raw = self._fetch_pipeline_runs(service_name, namespace)
        items = self._crd_items(raw)
        if not items:
            raise ServiceNotFoundError(service_name=service_name)
        return [self._to_pipeline_run_info(item) for item in items]

    def list_pipeline_runs_in_namespace(
        self, namespace: str, limit: int
    ) -> list[NamespacedPipelineRunInfo]:
        raw = self._fetch_pipeline_runs_in_namespace(namespace)
        items = self._crd_items(raw)
        return [self._to_namespaced_pipeline_run_info(item) for item in items]

    def _fetch_pipeline_runs_in_namespace(self, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
            )
        except ApiException as exc:
            if exc.status == 403:  # noqa: PLR2004
                raise InsufficientPermissionsError(
                    f"Access denied to namespace '{namespace}': {exc.reason}"
                ) from exc
            if exc.status == 404:  # noqa: PLR2004
                raise ComponentNotInstalledError(
                    "Tekton", "https://tekton.dev/docs/installation/"
                ) from exc
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def _to_namespaced_pipeline_run_info(
        self, item: Mapping[str, object]
    ) -> NamespacedPipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "pipeline_ref": self._extract_pipeline_ref(spec),
        }

    def _extract_pipeline_ref(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "inline"
        pipeline_ref = self._crd_mapping(spec.get("pipelineRef"))
        if pipeline_ref is not None:
            return self._crd_str(pipeline_ref, "name", "inline")
        if "pipelineSpec" in spec:
            return "inline"
        return "unknown"

    def _fetch_pipeline_runs(self, service_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_PIPELINERUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={service_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def _to_pipeline_run_info(self, item: Mapping[str, object]) -> PipelineRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._pipeline_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        completion_time = self._crd_optional_str(status, "completionTime")
        duration_seconds = self._pipeline_run_duration_seconds(start_time, completion_time)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "status": run_status,
            "start_time": start_time,
            "duration": self._seconds_to_human(duration_seconds),
            "duration_seconds": duration_seconds,
            "triggered_by": self._extract_triggered_by(metadata),
        }

    def _pipeline_run_status(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if reason in ("Cancelled", "PipelineRunCancelled"):
                return "Cancelled"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def _pipeline_run_duration_seconds(
        self,
        start_time: str | None,
        completion_time: str | None,
    ) -> int | None:
        if start_time is None or completion_time is None:
            return None
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(completion_time, fmt) - datetime.strptime(start_time, fmt)
            return max(0, int(delta.total_seconds()))
        except ValueError:
            return None

    def _seconds_to_human(self, seconds: int | None) -> str | None:
        if seconds is None:
            return None
        if seconds >= 60:  # noqa: PLR2004
            minutes, remaining = divmod(seconds, 60)
            return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
        return f"{seconds}s"

    def _extract_triggered_by(self, metadata: Mapping[str, object] | None) -> str | None:
        if metadata is None:
            return None
        annotations = self._crd_mapping(metadata.get("annotations"))
        if annotations is not None:
            sender = self._crd_optional_str(annotations, "pipelinesascode.tekton.dev/sender")
            if sender:
                return sender
        labels = self._crd_mapping(metadata.get("labels"))
        if labels is not None:
            listener = self._crd_optional_str(labels, "triggers.tekton.dev/eventlistener")
            if listener:
                return listener
        return None

    def _fetch_task_runs(self, pipeline_name: str, namespace: str) -> object:
        try:
            return self._crd_api_client().list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TEKTON_TASKRUNS_PLURAL,
                label_selector=f"tekton.dev/pipeline={pipeline_name}",
            )
        except Exception as exc:
            raise ClusterUnreachableError(f"Cannot reach Tekton API: {exc}") from exc

    def _to_task_run_info(self, item: Mapping[str, object]) -> TaskRunInfo:
        metadata = self._crd_mapping(item.get("metadata"))
        spec = self._crd_mapping(item.get("spec"))
        status = self._crd_mapping(item.get("status"))
        run_status = self._task_run_status(status)
        start_time = self._crd_optional_str(status, "startTime")
        failing_step, failing_step_error = self._extract_failing_step(status, run_status)
        return {
            "name": self._crd_str(metadata, "name", "unknown"),
            "task_ref": self._extract_task_ref(spec),
            "status": run_status,
            "start_time": start_time,
            "duration": self._task_run_duration(status, start_time, run_status),
            "failing_step": failing_step,
            "failing_step_error": failing_step_error,
        }

    def _extract_task_ref(self, spec: Mapping[str, object] | None) -> str:
        if spec is None:
            return "unknown"
        task_ref = self._crd_mapping(spec.get("taskRef"))
        if task_ref is not None:
            return self._crd_str(task_ref, "name", "unknown")
        return "unknown"

    def _task_run_status(self, status: Mapping[str, object] | None) -> str:
        if status is None:
            return "NotStarted"
        conditions = status.get("conditions")
        if not isinstance(conditions, list) or not conditions:
            return "NotStarted"
        first = conditions[0]
        if not isinstance(first, Mapping):
            return "NotStarted"
        condition: Mapping[str, object] = first
        succeeded = self._crd_str(condition, "status", "Unknown")
        reason = self._crd_str(condition, "reason", "")
        if succeeded == "True":
            return "Succeeded"
        if succeeded == "False":
            if "DeadlineExceeded" in reason or "timeout" in reason.lower():
                return "Timeout"
            return "Failed"
        if succeeded == "Unknown" and reason == "Running":
            return "Running"
        return "NotStarted"

    def _task_run_duration(
        self,
        status: Mapping[str, object] | None,
        start_time: str | None,
        run_status: str,
    ) -> str | None:
        if status is None or start_time is None:
            return None
        completion_time = self._crd_optional_str(status, "completionTime")
        if completion_time is None:
            return None
        return self._elapsed_between(start_time, completion_time)

    def _extract_failing_step(
        self,
        status: Mapping[str, object] | None,
        run_status: str,
    ) -> tuple[str | None, str | None]:
        if run_status not in ("Failed", "Timeout") or status is None:
            return None, None
        steps = status.get("steps")
        if not isinstance(steps, list):
            return None, None
        for step in steps:
            if not isinstance(step, Mapping):
                continue
            terminated = self._crd_mapping(step.get("terminated"))
            if terminated is None:
                continue
            exit_code = terminated.get("exitCode")
            if isinstance(exit_code, int) and exit_code != 0:
                return self._crd_str(step, "name", "unknown"), self._step_error(
                    exit_code, terminated
                )
        return None, None

    def _step_error(self, exit_code: int, terminated: Mapping[str, object]) -> str:
        reason = self._crd_str(terminated, "reason", "")
        if "DeadlineExceeded" in reason:
            return "Timeout"
        message = self._crd_optional_str(terminated, "message")
        return message if message else f"exit code {exit_code}"

    def _elapsed_between(self, start: str, end: str) -> str:
        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            delta = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)
            seconds = int(delta.total_seconds())
            if seconds >= 60:  # noqa: PLR2004
                minutes, remaining = divmod(seconds, 60)
                return f"{minutes}m{remaining}s" if remaining else f"{minutes}m"
            return f"{seconds}s"
        except ValueError:
            return "unknown"

    def _crd_items(self, raw: object) -> list[Mapping[str, object]]:
        mapping = self._crd_mapping(raw)
        if mapping is None:
            return []
        items = mapping.get("items", [])
        if not isinstance(items, list):
            return []
        return [item for item in items if isinstance(item, Mapping)]

    def _crd_mapping(self, value: object) -> Mapping[str, object] | None:
        if isinstance(value, Mapping):
            return cast(Mapping[str, object], value)
        return None

    def _crd_str(
        self,
        data: Mapping[str, object] | None,
        key: str,
        default: str = "",
    ) -> str:
        if data is None:
            return default
        value = data.get(key, default)
        return value if isinstance(value, str) else default

    def _crd_optional_str(
        self,
        data: Mapping[str, object] | None,
        key: str,
    ) -> str | None:
        if data is None:
            return None
        value = data.get(key)
        return value if isinstance(value, str) else None

    def _crd_api_client(self) -> KubernetesCRDApi:
        if self._crd_api is None:
            self._crd_api = cast(KubernetesCRDApi, client.CustomObjectsApi())
        return self._crd_api
