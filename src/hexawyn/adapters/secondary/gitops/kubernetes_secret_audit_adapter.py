from __future__ import annotations

from typing import Any

from hexawyn.application.ports.driven.secret_rotation_audit_port import (
    ManagedFieldsEntryRaw,
    SecretRaw,
    SecretReferenceRaw,
    SecretRotationAuditPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_ROTATION_EXEMPT_ANNOTATION_KEY = "hexawyn.io/secret-rotation-exempt"
_ROTATION_EXEMPT_ANNOTATION_VALUE = "true"


class KubernetesSecretAuditAdapter(SecretRotationAuditPort):
    """Secondary adapter — enumerates every Secret (with managedFields) via
    the K8s API, every Deployment/standalone-Pod reference to a Secret (env,
    envFrom, volumes, projected volumes), and namespace-level rotation
    exemptions."""

    def list_secrets(self) -> list[SecretRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_secret_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_secret_raw(item) for item in result.items]

    def list_secret_references(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def get_namespace_rotation_exemptions(self) -> set[str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return {
            namespace.metadata.name
            for namespace in result.items
            if (namespace.metadata.annotations or {}).get(_ROTATION_EXEMPT_ANNOTATION_KEY)
            == _ROTATION_EXEMPT_ANNOTATION_VALUE
        }


def _to_secret_raw(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def _to_managed_fields_entry(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def _references_from_deployment(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(deployment.spec.template.spec)
    return [
        SecretReferenceRaw(
            secret_name=name,
            namespace=deployment.metadata.namespace,
            workload_name=deployment.metadata.name,
        )
        for name in secret_names
    ]


def _references_from_pod(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(pod.spec)
    return [
        SecretReferenceRaw(
            secret_name=name, namespace=pod.metadata.namespace, workload_name=pod.metadata.name
        )
        for name in secret_names
    ]


def _extract_secret_names(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")
