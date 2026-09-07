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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut: MutantDict = {}  # type: ignore


class KubernetesPodSecurityAdapter(PodSecurityContextAuditPort):
    """Secondary adapter — enumerates every Pod's security-relevant spec
    fields (pod- and container-level securityContext, hostPID/hostNetwork/
    hostIPC, owner kind, covering init/regular/ephemeral containers) and
    every namespace's Pod Security Admission `enforce` label via the K8s API."""

    @_mutmut_mutated(mutants_xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut)
    def list_pod_security_specs(self) -> list[PodSecuritySpecRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_pod_spec(pod) for pod in result.items]

    def xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_orig(self) -> list[PodSecuritySpecRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_pod_spec(pod) for pod in result.items]

    def xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_1(self) -> list[PodSecuritySpecRaw]:
        from kubernetes import client as k8s

        core_api = None
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_pod_spec(pod) for pod in result.items]

    def xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_2(self) -> list[PodSecuritySpecRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = None
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_pod_spec(pod) for pod in result.items]

    def xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_3(self) -> list[PodSecuritySpecRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc
        return [_to_pod_spec(pod) for pod in result.items]

    def xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_4(self) -> list[PodSecuritySpecRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_pod_spec(None) for pod in result.items]

    @_mutmut_mutated(mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut)
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

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_orig(self) -> dict[str, str]:
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

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_1(self) -> dict[str, str]:
        from kubernetes import client as k8s

        core_api = None
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

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_2(self) -> dict[str, str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = None
        except Exception as exc:
            raise _translate_error(exc) from exc
        levels: dict[str, str] = {}
        for namespace in result.items:
            labels = namespace.metadata.labels or {}
            enforce = labels.get(_PSA_ENFORCE_LABEL_KEY)
            if enforce is not None:
                levels[namespace.metadata.name] = enforce
        return levels

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_3(self) -> dict[str, str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(None) from exc
        levels: dict[str, str] = {}
        for namespace in result.items:
            labels = namespace.metadata.labels or {}
            enforce = labels.get(_PSA_ENFORCE_LABEL_KEY)
            if enforce is not None:
                levels[namespace.metadata.name] = enforce
        return levels

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_4(self) -> dict[str, str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc
        levels: dict[str, str] = None
        for namespace in result.items:
            labels = namespace.metadata.labels or {}
            enforce = labels.get(_PSA_ENFORCE_LABEL_KEY)
            if enforce is not None:
                levels[namespace.metadata.name] = enforce
        return levels

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_5(self) -> dict[str, str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc
        levels: dict[str, str] = {}
        for namespace in result.items:
            labels = None
            enforce = labels.get(_PSA_ENFORCE_LABEL_KEY)
            if enforce is not None:
                levels[namespace.metadata.name] = enforce
        return levels

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_6(self) -> dict[str, str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc
        levels: dict[str, str] = {}
        for namespace in result.items:
            labels = namespace.metadata.labels and {}
            enforce = labels.get(_PSA_ENFORCE_LABEL_KEY)
            if enforce is not None:
                levels[namespace.metadata.name] = enforce
        return levels

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_7(self) -> dict[str, str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc
        levels: dict[str, str] = {}
        for namespace in result.items:
            labels = namespace.metadata.labels or {}
            enforce = None
            if enforce is not None:
                levels[namespace.metadata.name] = enforce
        return levels

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_8(self) -> dict[str, str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc
        levels: dict[str, str] = {}
        for namespace in result.items:
            labels = namespace.metadata.labels or {}
            enforce = labels.get(None)
            if enforce is not None:
                levels[namespace.metadata.name] = enforce
        return levels

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_9(self) -> dict[str, str]:
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
            if enforce is None:
                levels[namespace.metadata.name] = enforce
        return levels

    def xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_10(self) -> dict[str, str]:
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
                levels[namespace.metadata.name] = None
        return levels

mutants_xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut['_mutmut_orig'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut['xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_1'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut['xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_2'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut['xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_3'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut['xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_4'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁlist_pod_security_specs__mutmut_4 # type: ignore # mutmut generated

mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['_mutmut_orig'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_1'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_2'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_3'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_4'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_5'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_6'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_7'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_8'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_9'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut['xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_10'] = KubernetesPodSecurityAdapter.xǁKubernetesPodSecurityAdapterǁget_namespace_psa_enforce_levels__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_pod_spec__mutmut)
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


def x__to_pod_spec__mutmut_orig(pod: Any) -> PodSecuritySpecRaw:
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


def x__to_pod_spec__mutmut_1(pod: Any) -> PodSecuritySpecRaw:
    owner_references = None
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


def x__to_pod_spec__mutmut_2(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references and []
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


def x__to_pod_spec__mutmut_3(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = None
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


def x__to_pod_spec__mutmut_4(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[1].kind if owner_references else None
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


def x__to_pod_spec__mutmut_5(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = None
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


def x__to_pod_spec__mutmut_6(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = None

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


def x__to_pod_spec__mutmut_7(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is None else None
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


def x__to_pod_spec__mutmut_8(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = None
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


def x__to_pod_spec__mutmut_9(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(None)
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


def x__to_pod_spec__mutmut_10(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(None, "init"))
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


def x__to_pod_spec__mutmut_11(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, None))
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


def x__to_pod_spec__mutmut_12(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers("init"))
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


def x__to_pod_spec__mutmut_13(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, ))
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


def x__to_pod_spec__mutmut_14(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "XXinitXX"))
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


def x__to_pod_spec__mutmut_15(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "INIT"))
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


def x__to_pod_spec__mutmut_16(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(None)
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


def x__to_pod_spec__mutmut_17(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(None, "container"))
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


def x__to_pod_spec__mutmut_18(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, None))
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


def x__to_pod_spec__mutmut_19(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers("container"))
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


def x__to_pod_spec__mutmut_20(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, ))
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


def x__to_pod_spec__mutmut_21(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "XXcontainerXX"))
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


def x__to_pod_spec__mutmut_22(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "CONTAINER"))
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


def x__to_pod_spec__mutmut_23(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "container"))
    containers.extend(None)

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


def x__to_pod_spec__mutmut_24(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "container"))
    containers.extend(_to_containers(None, "ephemeral"))

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


def x__to_pod_spec__mutmut_25(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "container"))
    containers.extend(_to_containers(pod.spec.ephemeral_containers, None))

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


def x__to_pod_spec__mutmut_26(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "container"))
    containers.extend(_to_containers("ephemeral"))

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


def x__to_pod_spec__mutmut_27(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "container"))
    containers.extend(_to_containers(pod.spec.ephemeral_containers, ))

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


def x__to_pod_spec__mutmut_28(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "container"))
    containers.extend(_to_containers(pod.spec.ephemeral_containers, "XXephemeralXX"))

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


def x__to_pod_spec__mutmut_29(pod: Any) -> PodSecuritySpecRaw:
    owner_references = pod.metadata.owner_references or []
    owner_kind = owner_references[0].kind if owner_references else None
    pod_security_context = pod.spec.security_context
    pod_run_as_non_root = (
        pod_security_context.run_as_non_root if pod_security_context is not None else None
    )

    containers: list[ContainerSecurityContextRaw] = []
    containers.extend(_to_containers(pod.spec.init_containers, "init"))
    containers.extend(_to_containers(pod.spec.containers, "container"))
    containers.extend(_to_containers(pod.spec.ephemeral_containers, "EPHEMERAL"))

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


def x__to_pod_spec__mutmut_30(pod: Any) -> PodSecuritySpecRaw:
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
        pod_name=None,
        namespace=pod.metadata.namespace,
        owner_kind=owner_kind,
        pod_run_as_non_root=pod_run_as_non_root,
        host_pid=bool(pod.spec.host_pid),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_31(pod: Any) -> PodSecuritySpecRaw:
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
        namespace=None,
        owner_kind=owner_kind,
        pod_run_as_non_root=pod_run_as_non_root,
        host_pid=bool(pod.spec.host_pid),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_32(pod: Any) -> PodSecuritySpecRaw:
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
        owner_kind=None,
        pod_run_as_non_root=pod_run_as_non_root,
        host_pid=bool(pod.spec.host_pid),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_33(pod: Any) -> PodSecuritySpecRaw:
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
        pod_run_as_non_root=None,
        host_pid=bool(pod.spec.host_pid),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_34(pod: Any) -> PodSecuritySpecRaw:
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
        host_pid=None,
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_35(pod: Any) -> PodSecuritySpecRaw:
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
        host_network=None,
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_36(pod: Any) -> PodSecuritySpecRaw:
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
        host_ipc=None,
        containers=containers,
    )


def x__to_pod_spec__mutmut_37(pod: Any) -> PodSecuritySpecRaw:
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
        containers=None,
    )


def x__to_pod_spec__mutmut_38(pod: Any) -> PodSecuritySpecRaw:
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
        namespace=pod.metadata.namespace,
        owner_kind=owner_kind,
        pod_run_as_non_root=pod_run_as_non_root,
        host_pid=bool(pod.spec.host_pid),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_39(pod: Any) -> PodSecuritySpecRaw:
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
        owner_kind=owner_kind,
        pod_run_as_non_root=pod_run_as_non_root,
        host_pid=bool(pod.spec.host_pid),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_40(pod: Any) -> PodSecuritySpecRaw:
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
        pod_run_as_non_root=pod_run_as_non_root,
        host_pid=bool(pod.spec.host_pid),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_41(pod: Any) -> PodSecuritySpecRaw:
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
        host_pid=bool(pod.spec.host_pid),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_42(pod: Any) -> PodSecuritySpecRaw:
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
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_43(pod: Any) -> PodSecuritySpecRaw:
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
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_44(pod: Any) -> PodSecuritySpecRaw:
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
        containers=containers,
    )


def x__to_pod_spec__mutmut_45(pod: Any) -> PodSecuritySpecRaw:
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
        )


def x__to_pod_spec__mutmut_46(pod: Any) -> PodSecuritySpecRaw:
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
        host_pid=bool(None),
        host_network=bool(pod.spec.host_network),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_47(pod: Any) -> PodSecuritySpecRaw:
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
        host_network=bool(None),
        host_ipc=bool(pod.spec.host_ipc),
        containers=containers,
    )


def x__to_pod_spec__mutmut_48(pod: Any) -> PodSecuritySpecRaw:
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
        host_ipc=bool(None),
        containers=containers,
    )

mutants_x__to_pod_spec__mutmut['_mutmut_orig'] = x__to_pod_spec__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_1'] = x__to_pod_spec__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_2'] = x__to_pod_spec__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_3'] = x__to_pod_spec__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_4'] = x__to_pod_spec__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_5'] = x__to_pod_spec__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_6'] = x__to_pod_spec__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_7'] = x__to_pod_spec__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_8'] = x__to_pod_spec__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_9'] = x__to_pod_spec__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_10'] = x__to_pod_spec__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_11'] = x__to_pod_spec__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_12'] = x__to_pod_spec__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_13'] = x__to_pod_spec__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_14'] = x__to_pod_spec__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_15'] = x__to_pod_spec__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_16'] = x__to_pod_spec__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_17'] = x__to_pod_spec__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_18'] = x__to_pod_spec__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_19'] = x__to_pod_spec__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_20'] = x__to_pod_spec__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_21'] = x__to_pod_spec__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_22'] = x__to_pod_spec__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_23'] = x__to_pod_spec__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_24'] = x__to_pod_spec__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_25'] = x__to_pod_spec__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_26'] = x__to_pod_spec__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_27'] = x__to_pod_spec__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_28'] = x__to_pod_spec__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_29'] = x__to_pod_spec__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_30'] = x__to_pod_spec__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_31'] = x__to_pod_spec__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_32'] = x__to_pod_spec__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_33'] = x__to_pod_spec__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_34'] = x__to_pod_spec__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_35'] = x__to_pod_spec__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_36'] = x__to_pod_spec__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_37'] = x__to_pod_spec__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_38'] = x__to_pod_spec__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_39'] = x__to_pod_spec__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_40'] = x__to_pod_spec__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_41'] = x__to_pod_spec__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_42'] = x__to_pod_spec__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_43'] = x__to_pod_spec__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_44'] = x__to_pod_spec__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_45'] = x__to_pod_spec__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_46'] = x__to_pod_spec__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_47'] = x__to_pod_spec__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_pod_spec__mutmut['x__to_pod_spec__mutmut_48'] = x__to_pod_spec__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_containers__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_containers__mutmut)
def _to_containers(
    containers: list[Any] | None, kind: _ContainerKind
) -> list[ContainerSecurityContextRaw]:
    return [_to_container(container, kind) for container in containers or []]


def x__to_containers__mutmut_orig(
    containers: list[Any] | None, kind: _ContainerKind
) -> list[ContainerSecurityContextRaw]:
    return [_to_container(container, kind) for container in containers or []]


def x__to_containers__mutmut_1(
    containers: list[Any] | None, kind: _ContainerKind
) -> list[ContainerSecurityContextRaw]:
    return [_to_container(None, kind) for container in containers or []]


def x__to_containers__mutmut_2(
    containers: list[Any] | None, kind: _ContainerKind
) -> list[ContainerSecurityContextRaw]:
    return [_to_container(container, None) for container in containers or []]


def x__to_containers__mutmut_3(
    containers: list[Any] | None, kind: _ContainerKind
) -> list[ContainerSecurityContextRaw]:
    return [_to_container(kind) for container in containers or []]


def x__to_containers__mutmut_4(
    containers: list[Any] | None, kind: _ContainerKind
) -> list[ContainerSecurityContextRaw]:
    return [_to_container(container, ) for container in containers or []]


def x__to_containers__mutmut_5(
    containers: list[Any] | None, kind: _ContainerKind
) -> list[ContainerSecurityContextRaw]:
    return [_to_container(container, kind) for container in containers and []]

mutants_x__to_containers__mutmut['_mutmut_orig'] = x__to_containers__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_containers__mutmut['x__to_containers__mutmut_1'] = x__to_containers__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_containers__mutmut['x__to_containers__mutmut_2'] = x__to_containers__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_containers__mutmut['x__to_containers__mutmut_3'] = x__to_containers__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_containers__mutmut['x__to_containers__mutmut_4'] = x__to_containers__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_containers__mutmut['x__to_containers__mutmut_5'] = x__to_containers__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_container__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_container__mutmut)
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


def x__to_container__mutmut_orig(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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


def x__to_container__mutmut_1(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = None
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


def x__to_container__mutmut_2(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is not None:
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


def x__to_container__mutmut_3(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
            container_name=None,
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


def x__to_container__mutmut_4(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
            container_name=container.name,
            container_kind=None,
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


def x__to_container__mutmut_5(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
            container_name=container.name,
            container_kind=kind,
            privileged=None,
            allow_privilege_escalation=None,
            run_as_non_root=None,
            added_capabilities=None,
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


def x__to_container__mutmut_6(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
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


def x__to_container__mutmut_7(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
            container_name=container.name,
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


def x__to_container__mutmut_8(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
            container_name=container.name,
            container_kind=kind,
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


def x__to_container__mutmut_9(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
            container_name=container.name,
            container_kind=kind,
            privileged=None,
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


def x__to_container__mutmut_10(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
            container_name=container.name,
            container_kind=kind,
            privileged=None,
            allow_privilege_escalation=None,
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


def x__to_container__mutmut_11(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
    security_context = container.security_context
    if security_context is None:
        return ContainerSecurityContextRaw(
            container_name=container.name,
            container_kind=kind,
            privileged=None,
            allow_privilege_escalation=None,
            run_as_non_root=None,
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


def x__to_container__mutmut_12(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
    capabilities = None
    added_capabilities = capabilities.add if capabilities is not None and capabilities.add else []
    return ContainerSecurityContextRaw(
        container_name=container.name,
        container_kind=kind,
        privileged=security_context.privileged,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_13(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
    added_capabilities = None
    return ContainerSecurityContextRaw(
        container_name=container.name,
        container_kind=kind,
        privileged=security_context.privileged,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_14(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
    added_capabilities = capabilities.add if capabilities is not None or capabilities.add else []
    return ContainerSecurityContextRaw(
        container_name=container.name,
        container_kind=kind,
        privileged=security_context.privileged,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_15(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
    added_capabilities = capabilities.add if capabilities is None and capabilities.add else []
    return ContainerSecurityContextRaw(
        container_name=container.name,
        container_kind=kind,
        privileged=security_context.privileged,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_16(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        container_name=None,
        container_kind=kind,
        privileged=security_context.privileged,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_17(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        container_kind=None,
        privileged=security_context.privileged,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_18(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        privileged=None,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_19(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        allow_privilege_escalation=None,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_20(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        run_as_non_root=None,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_21(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        added_capabilities=None,
    )


def x__to_container__mutmut_22(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        container_kind=kind,
        privileged=security_context.privileged,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_23(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        privileged=security_context.privileged,
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_24(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        allow_privilege_escalation=security_context.allow_privilege_escalation,
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_25(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        run_as_non_root=security_context.run_as_non_root,
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_26(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        added_capabilities=added_capabilities,
    )


def x__to_container__mutmut_27(container: Any, kind: _ContainerKind) -> ContainerSecurityContextRaw:
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
        )

mutants_x__to_container__mutmut['_mutmut_orig'] = x__to_container__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_1'] = x__to_container__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_2'] = x__to_container__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_3'] = x__to_container__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_4'] = x__to_container__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_5'] = x__to_container__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_6'] = x__to_container__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_7'] = x__to_container__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_8'] = x__to_container__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_9'] = x__to_container__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_10'] = x__to_container__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_11'] = x__to_container__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_12'] = x__to_container__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_13'] = x__to_container__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_14'] = x__to_container__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_15'] = x__to_container__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_16'] = x__to_container__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_17'] = x__to_container__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_18'] = x__to_container__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_19'] = x__to_container__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_20'] = x__to_container__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_21'] = x__to_container__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_22'] = x__to_container__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_23'] = x__to_container__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_24'] = x__to_container__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_25'] = x__to_container__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_26'] = x__to_container__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_container__mutmut['x__to_container__mutmut_27'] = x__to_container__mutmut_27 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to Pod/Namespace security infoXX")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to pod/namespace security info")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO POD/NAMESPACE SECURITY INFO")
    return ClusterUnreachableError(f"Cannot list Pod/Namespace security info: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Pod/Namespace security info")
    return ClusterUnreachableError(None)

mutants_x__translate_error__mutmut['_mutmut_orig'] = x__translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_1'] = x__translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_2'] = x__translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_3'] = x__translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_4'] = x__translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_5'] = x__translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_6'] = x__translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_7'] = x__translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_8'] = x__translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_9'] = x__translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_10'] = x__translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_11'] = x__translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_12'] = x__translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_13'] = x__translate_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_14'] = x__translate_error__mutmut_14 # type: ignore # mutmut generated
