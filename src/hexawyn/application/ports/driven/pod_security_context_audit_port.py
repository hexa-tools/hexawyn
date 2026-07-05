from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Literal, TypedDict


class ContainerSecurityContextRaw(TypedDict):
    container_name: str
    container_kind: Literal["init", "container", "ephemeral"]
    privileged: bool | None
    allow_privilege_escalation: bool | None
    run_as_non_root: bool | None
    added_capabilities: list[str]


class PodSecuritySpecRaw(TypedDict):
    pod_name: str
    namespace: str
    owner_kind: str | None
    pod_run_as_non_root: bool | None
    host_pid: bool
    host_network: bool
    host_ipc: bool
    containers: list[ContainerSecurityContextRaw]


class PodSecurityContextAuditPort(ABC):
    """Port for enumerating every Pod's security-relevant spec fields (pod-
    and container-level securityContext, hostPID/hostNetwork/hostIPC, owner
    kind) and each namespace's Pod Security Admission `enforce` label."""

    @abstractmethod
    def list_pod_security_specs(self) -> list[PodSecuritySpecRaw]:
        """List every Pod across all namespaces with its raw security-context
        fields, covering init, regular, and ephemeral containers."""

    @abstractmethod
    def get_namespace_psa_enforce_levels(self) -> dict[str, str]:
        """Map namespace name to its `pod-security.kubernetes.io/enforce`
        label value, for namespaces that have one set."""
