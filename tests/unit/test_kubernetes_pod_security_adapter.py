"""Unit tests for KubernetesPodSecurityAdapter — mocks kubernetes.client.CoreV1Api
for both list_pod_for_all_namespaces (init/regular/ephemeral containers,
pod-level security context, owner references) and list_namespace (PSA
enforce labels)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.pod_security_context_audit_port import (
    PodSecurityContextAuditPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _security_context(
    privileged: bool | None = None,
    allow_privilege_escalation: bool | None = None,
    run_as_non_root: bool | None = None,
    added_capabilities: list[str] | None = None,
) -> MagicMock:
    sc = MagicMock()
    sc.privileged = privileged
    sc.allow_privilege_escalation = allow_privilege_escalation
    sc.run_as_non_root = run_as_non_root
    if added_capabilities is None:
        sc.capabilities = None
    else:
        sc.capabilities = MagicMock()
        sc.capabilities.add = added_capabilities
    return sc


def _container(name: str, security_context: MagicMock | None = None) -> MagicMock:
    container = MagicMock()
    container.name = name
    container.security_context = security_context
    return container


def _owner_ref(kind: str) -> MagicMock:
    ref = MagicMock()
    ref.kind = kind
    return ref


def _pod(
    name: str,
    namespace: str = "production",
    owner_references: list | None = None,
    pod_security_context: MagicMock | None = None,
    host_pid: bool = False,
    host_network: bool = False,
    host_ipc: bool = False,
    init_containers: list | None = None,
    containers: list | None = None,
    ephemeral_containers: list | None = None,
) -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = name
    pod.metadata.namespace = namespace
    pod.metadata.owner_references = owner_references
    pod.spec.security_context = pod_security_context
    pod.spec.host_pid = host_pid
    pod.spec.host_network = host_network
    pod.spec.host_ipc = host_ipc
    pod.spec.init_containers = init_containers
    pod.spec.containers = containers or []
    pod.spec.ephemeral_containers = ephemeral_containers
    return pod


def _namespace(name: str, labels: dict[str, str] | None) -> MagicMock:
    ns = MagicMock()
    ns.metadata.name = name
    ns.metadata.labels = labels
    return ns


def _list_response(*items: MagicMock) -> MagicMock:
    response = MagicMock()
    response.items = list(items)
    return response


class TestKubernetesPodSecurityAdapterIsPort:
    def test_is_pod_security_context_audit_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        assert isinstance(KubernetesPodSecurityAdapter(), PodSecurityContextAuditPort)


class TestListPodSecuritySpecs:
    def test_maps_pod_level_and_container_level_fields(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod(
                "data-processor-abc",
                owner_references=[_owner_ref("ReplicaSet")],
                host_pid=True,
                containers=[
                    _container(
                        "app",
                        _security_context(privileged=True, allow_privilege_escalation=True),
                    )
                ],
            )
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesPodSecurityAdapter().list_pod_security_specs()

        spec = result[0]
        assert spec["pod_name"] == "data-processor-abc"
        assert spec["namespace"] == "production"
        assert spec["owner_kind"] == "ReplicaSet"
        assert spec["host_pid"] is True
        container = spec["containers"][0]
        assert container["container_name"] == "app"
        assert container["container_kind"] == "container"
        assert container["privileged"] is True
        assert container["allow_privilege_escalation"] is True

    def test_iterates_init_regular_and_ephemeral_containers(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod(
                "p",
                init_containers=[_container("init-setup", _security_context(privileged=True))],
                containers=[_container("app")],
                ephemeral_containers=[_container("debugger")],
            )
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesPodSecurityAdapter().list_pod_security_specs()

        by_kind = {c["container_kind"]: c["container_name"] for c in result[0]["containers"]}
        assert by_kind == {"init": "init-setup", "container": "app", "ephemeral": "debugger"}

    def test_no_owner_references_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod("p", owner_references=None)
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesPodSecurityAdapter().list_pod_security_specs()

        assert result[0]["owner_kind"] is None

    def test_container_with_no_security_context_has_none_fields(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod("p", containers=[_container("app", security_context=None)])
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesPodSecurityAdapter().list_pod_security_specs()

        container = result[0]["containers"][0]
        assert container["privileged"] is None
        assert container["allow_privilege_escalation"] is None
        assert container["run_as_non_root"] is None
        assert container["added_capabilities"] == []

    def test_container_with_no_capabilities_object_has_empty_added_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod("p", containers=[_container("app", _security_context())])
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesPodSecurityAdapter().list_pod_security_specs()

        assert result[0]["containers"][0]["added_capabilities"] == []

    def test_pod_level_security_context_run_as_non_root_is_captured(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        pod_sc = MagicMock()
        pod_sc.run_as_non_root = True
        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod("p", pod_security_context=pod_sc)
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesPodSecurityAdapter().list_pod_security_specs()

        assert result[0]["pod_run_as_non_root"] is True

    def test_no_pod_level_security_context_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod("p", pod_security_context=None)
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesPodSecurityAdapter().list_pod_security_specs()

        assert result[0]["pod_run_as_non_root"] is None

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        core_api.list_pod_for_all_namespaces.side_effect = error

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesPodSecurityAdapter().list_pod_security_specs()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.side_effect = Exception("refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesPodSecurityAdapter().list_pod_security_specs()


class TestGetNamespacePsaEnforceLevels:
    def test_returns_only_namespaces_with_enforce_label(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespace.return_value = _list_response(
            _namespace("production", {"pod-security.kubernetes.io/enforce": "restricted"}),
            _namespace("staging", None),
            _namespace("default", {"other-label": "x"}),
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesPodSecurityAdapter().get_namespace_psa_enforce_levels()

        assert result == {"production": "restricted"}

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        core_api.list_namespace.side_effect = error

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesPodSecurityAdapter().get_namespace_psa_enforce_levels()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
            KubernetesPodSecurityAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespace.side_effect = Exception("refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesPodSecurityAdapter().get_namespace_psa_enforce_levels()
