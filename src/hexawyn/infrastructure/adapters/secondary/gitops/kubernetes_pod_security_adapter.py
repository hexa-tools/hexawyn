from __future__ import annotations

from typing import Any, Literal

from hexawyn.application.ports.driven.pod_security_context_audit_port import (
    ContainerSecurityContextRaw,
    PodSecurityContextAuditPort,
    PodSecuritySpecRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_ContainerKind = Literal["init", "container", "ephemeral"]

_K8S_FORBIDDEN = 403
_PSA_ENFORCE_LABEL_KEY = "pod-security.kubernetes.io/enforce"


class KubernetesPodSecurityAdapter(PodSecurityContextAuditPort):
    """Secondary adapter — enumerates every Pod's security-relevant spec
    fields (pod- and container-level securityContext, hostPID/hostNetwork/
    hostIPC, owner kind, covering init/regular/ephemeral containers) and
    every namespace's Pod Security Admission `enforce` label via the K8s API."""

    def list_pod_security_specs(self) -> list[PodSecuritySpecRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_pod_spec(pod) for pod in result.items]

    def get_namespace_psa_enforce_levels(self) -> dict[str, str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc
        levels: dict[str, str] = {}
        for namespace in result.items:
            labels = namespace.metadata.labels or {}
            enforce = labels.get(_PSA_ENFORCE_LABEL_KEY)
            if enforce is not None:
                levels[namespace.metadata.name] = enforce
        return levels


def _to_pod_spec(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "container"))
    containers.extend(_to_containers(pod.spec.ephemeral_containers, "ephemeral"))

    return PodSecuritySpecRaw(
        pod_name=pod.metadata.name,
        namespace=pod.metadata.namespace,
        owner_kind=owner_kind,
        pod_run_as_non_root=pod_run_as_non_root,
        host_pid=bool(pod.spec.host_pid),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def _to_containers(
    containers: list[Any] | None, kind: _ContainerKind
) -> list[ContainerSecurityContextRaw]:
    return [_to_container(container, kind) for container in containers or []]


def _to_container(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
            container_name=container.name,
            container_kind=kind,
            privileged=None,
            allow_privilege_escalation=None,
            run_as_non_root=None,
            added_capabilities=[],
        )
    capabilities = security_context.capabilities
    added_capabilities = capabilities.add if capabilities is not None and capabilities.add else []
    return ContainerSecurityContextRaw(
        container_name=container.name,
        container_kind=kind,
        privileged=security_context.privileged,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")
