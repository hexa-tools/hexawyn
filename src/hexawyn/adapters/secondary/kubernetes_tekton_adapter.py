from __future__ import annotations

from collections.abc import Mapping
from datetime import UTC, datetime

from hexawyn.application.ports.driven.tekton_pipeline_status_port import (
    PipelineRunRecord,
    TektonPipelineStatusPort,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    TektonNotInstalledError,
)

_TEKTON_GROUP = "tekton.dev"
_TEKTON_VERSION = "v1"
_PIPELINERUNS_PLURAL = "pipelineruns"
_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404


class KubernetesTektonAdapter(TektonPipelineStatusPort):
    """Secondary adapter — reads Tekton PipelineRun CRDs from the K8s API."""

    def list_pipeline_runs(self, namespace: str, limit: int = 500) -> list[PipelineRunRecord]:
        from kubernetes import client as k8s

        try:
            api = k8s.CustomObjectsApi()
            raw = api.list_namespaced_custom_object(
                group=_TEKTON_GROUP,
                version=_TEKTON_VERSION,
                namespace=namespace,
                plural=_PIPELINERUNS_PLURAL,
                limit=limit,
            )
        except Exception as exc:
            status = getattr(exc, "status", None)
            if status == _K8S_FORBIDDEN:
                raise InsufficientPermissionsError(
                    f"RBAC denied access to PipelineRuns in namespace {namespace!r}",
                    context={"namespace": namespace},
                ) from exc
            if status == _K8S_NOT_FOUND:
                raise TektonNotInstalledError() from exc
            raise ClusterUnreachableError(
                f"Tekton API unreachable in namespace {namespace!r}: {exc}"
            ) from exc

        items = raw.get("items") or [] if isinstance(raw, dict) else []
        return [_to_record(item) for item in items]


def _extract_status(status: Mapping[str, object] | None) -> tuple[str, str | None]:
    """Return (status_str, failure_reason)."""
    if status is None:
        return "NotStarted", None
    conditions = status.get("conditions")
    if not isinstance(conditions, list) or not conditions:
        return "NotStarted", None
    first = conditions[0]
    if not isinstance(first, Mapping):
        return "NotStarted", None
    condition: Mapping[str, object] = first
    succeeded = str(condition.get("status", "Unknown"))
    reason = str(condition.get("reason", ""))
    if succeeded == "True":
        return "Succeeded", None
    if succeeded == "False":
        if reason in ("Cancelled", "PipelineRunCancelled"):
            return "Cancelled", None
        return "Failed", reason or None
    if succeeded == "Unknown" and reason == "Running":
        return "Running", None
    return "NotStarted", None


def _compute_duration_seconds(start_time: str | None, completion_time: str | None) -> int | None:
    if start_time is None:
        return None
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = (
            datetime.fromisoformat(completion_time.replace("Z", "+00:00"))
            if completion_time
            else datetime.now(UTC)
        )
        return max(0, int((end - start).total_seconds()))
    except ValueError:
        return None


def _extract_pipeline_ref(spec: Mapping[str, object] | None) -> str:
    if spec is None:
        return "unknown"
    pipeline_ref = spec.get("pipelineRef")
    if isinstance(pipeline_ref, Mapping):
        name = pipeline_ref.get("name")
        if isinstance(name, str) and name:
            return name
    if "pipelineSpec" in spec:
        return "inline"
    return "unknown"


def _to_record(item: Mapping[str, object]) -> PipelineRunRecord:
    metadata = item.get("metadata")
    spec = item.get("spec")
    status_raw = item.get("status")

    meta: Mapping[str, object] = metadata if isinstance(metadata, Mapping) else {}
    spec_map: Mapping[str, object] | None = spec if isinstance(spec, Mapping) else None
    status_map: Mapping[str, object] | None = (
        status_raw if isinstance(status_raw, Mapping) else None
    )

    name = str(meta.get("name", "unknown"))
    run_status, failure_reason = _extract_status(status_map)

    start_time: str | None = None
    completion_time: str | None = None
    if status_map is not None:
        raw_start = status_map.get("startTime")
        raw_completion = status_map.get("completionTime")
        start_time = str(raw_start) if raw_start is not None else None
        completion_time = str(raw_completion) if raw_completion is not None else None

    duration_seconds = _compute_duration_seconds(start_time, completion_time)

    return PipelineRunRecord(
        name=name,
        status=run_status,
        start_time=start_time,
        duration_seconds=duration_seconds,
        failure_reason=failure_reason,
        pipeline_ref=_extract_pipeline_ref(spec_map),
    )
