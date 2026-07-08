"""TektonPipelineTracerAdapter — fetches PipelineRun + child TaskRuns from K8s CRDs."""

from __future__ import annotations

from typing import cast

from hexawyn.application.ports.driven.pipeline_tracer_port import (
    PipelineRunRecord,
    PipelineTracerPort,
    TaskRunRecord,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    PipelineNotFoundError,
    TektonNotInstalledError,
)

_TEKTON_GROUP = "tekton.dev"
_TEKTON_VERSION = "v1"
_PIPELINERUN_PLURAL = "pipelineruns"
_TASKRUN_PLURAL = "taskruns"
_LABEL_PIPELINERUN = "tekton.dev/pipelineRun"
_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


class TektonPipelineTracerAdapter(PipelineTracerPort):
    def get_pipeline_run(self, namespace: str, name: str) -> PipelineRunRecord:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.get_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUN_PLURAL,
                name=name,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise PipelineNotFoundError(name) from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRun {name!r}",
                    context={"name": name, "namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(f"Cannot fetch PipelineRun {name!r}: {exc}") from exc

        return _to_pipeline_run_record(raw)

    def list_task_runs_for_pipeline(
        self, namespace: str, pipeline_run_name: str
    ) -> list[TaskRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_TASKRUN_PLURAL,
                label_selector=f"{_LABEL_PIPELINERUN}={pipeline_run_name}",
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_NOT_FOUND:
                raise TektonNotInstalledError() from exc
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to TaskRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            raise ClusterUnreachableError(
                f"Cannot list TaskRuns for PipelineRun {pipeline_run_name!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_task_run_record(item, pipeline_run_name) for item in items]


def _to_pipeline_run_record(raw: dict[str, object]) -> PipelineRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return PipelineRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        status=_extract_status(status_block.get("conditions")),
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        pipeline_ref=_extract_pipeline_ref(spec),
    )


def _to_task_run_record(raw: dict[str, object], pipeline_run_name: str) -> TaskRunRecord:
    metadata = cast(dict[str, object], raw.get("metadata") or {})
    status_block = cast(dict[str, object], raw.get("status") or {})
    spec = cast(dict[str, object], raw.get("spec") or {})
    return TaskRunRecord(
        name=str(cast(str, metadata.get("name") or "")),
        namespace=str(cast(str, metadata.get("namespace") or "")),
        pipeline_run_name=pipeline_run_name,
        start_time=_to_iso(status_block.get("startTime")),
        completion_time=_to_iso(status_block.get("completionTime")),
        status=_extract_status(status_block.get("conditions")),
        run_after=_extract_run_after(spec),
        failure_reason=_extract_failure_reason(status_block),
    )


def _extract_status(conditions: object) -> str:
    if not isinstance(conditions, list):
        return "Unknown"
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded":
            status_val = c.get("status", "Unknown")
            if status_val == "True":
                return "Succeeded"
            if status_val == "False":
                reason = c.get("reason", "")
                if reason in ("PipelineRunCancelled", "TaskRunCancelled"):
                    return "Cancelled"
                return "Failed"
            return "Running"
    return "NotStarted"


def _extract_failure_reason(status_block: dict[str, object]) -> str:
    conditions = status_block.get("conditions")
    if not isinstance(conditions, list):
        return ""
    for c in conditions:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "Succeeded" and c.get("status") == "False":
            return str(c.get("message", ""))
    return ""


def _extract_run_after(spec: dict[str, object]) -> list[str]:
    raw = spec.get("runAfter")
    if isinstance(raw, list):
        return [str(r) for r in raw]
    return []


def _extract_pipeline_ref(spec: dict[str, object]) -> str:
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, dict):
        return str(pipeline_ref.get("name", "unknown"))
    pipeline_spec = spec.get("pipelineSpec")
    if isinstance(pipeline_spec, dict):
        return "inline"
    return "unknown"


def _to_iso(value: object) -> str | None:
    if isinstance(value, str):
        return value
    return None
