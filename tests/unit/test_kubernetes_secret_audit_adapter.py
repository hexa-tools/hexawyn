"""Unit tests for KubernetesSecretAuditAdapter — mocks kubernetes.client.CoreV1Api
/ AppsV1Api. Secret enumeration mirrors KubernetesAuditLogAdapter's
managedFields conversion (ECA-69); reference detection scans each
Deployment's own pod-template spec directly plus any standalone (unowned)
Pod, covering env/envFrom/volumes/projected volumes."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.secret_rotation_audit_port import SecretRotationAuditPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _managed_fields_entry(
    manager: str, operation: str = "Update", fields_v1: dict | None = None
) -> MagicMock:
    entry = MagicMock()
    entry.manager = manager
    entry.operation = operation
    entry.time = datetime(2025, 12, 17, tzinfo=UTC)
    entry.fields_v1 = fields_v1 if fields_v1 is not None else {"f:data": {}}
    return entry


def _secret_item(
    name: str,
    namespace: str = "production",
    secret_type: str = "Opaque",
    data: dict | None = None,
    managed_fields: list | None = None,
    annotations: dict | None = None,
) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.metadata.managed_fields = managed_fields if managed_fields is not None else []
    item.metadata.creation_timestamp = datetime(2020, 1, 1, tzinfo=UTC)
    item.metadata.annotations = annotations
    item.type = secret_type
    item.data = data
    return item


def _list_response(*items: MagicMock) -> MagicMock:
    response = MagicMock()
    response.items = list(items)
    return response


def _env_from(secret_name: str | None) -> MagicMock:
    env_from = MagicMock()
    if secret_name is None:
        env_from.secret_ref = None
    else:
        env_from.secret_ref = MagicMock(name=secret_name)
        env_from.secret_ref.name = secret_name
    return env_from


def _env_var(secret_name: str | None) -> MagicMock:
    env = MagicMock()
    if secret_name is None:
        env.value_from = None
    else:
        env.value_from = MagicMock()
        env.value_from.secret_key_ref = MagicMock()
        env.value_from.secret_key_ref.name = secret_name
    return env


def _secret_volume(secret_name: str) -> MagicMock:
    volume = MagicMock()
    volume.secret = MagicMock()
    volume.secret.secret_name = secret_name
    volume.projected = None
    return volume


def _projected_volume(secret_names: list[str]) -> MagicMock:
    volume = MagicMock()
    volume.secret = None
    volume.projected = MagicMock()
    sources = []
    for name in secret_names:
        source = MagicMock()
        source.secret = MagicMock()
        source.secret.name = name
        sources.append(source)
    volume.projected.sources = sources
    return volume


def _container(env_from: list | None = None, env: list | None = None) -> MagicMock:
    container = MagicMock()
    container.env_from = env_from
    container.env = env
    return container


def _pod_spec(containers: list | None = None, volumes: list | None = None) -> MagicMock:
    spec = MagicMock()
    spec.containers = containers or []
    spec.init_containers = None
    spec.volumes = volumes or []
    return spec


def _deployment(
    name: str, namespace: str = "production", pod_spec: MagicMock | None = None
) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.spec.template.spec = pod_spec or _pod_spec()
    return item


def _pod(
    name: str,
    namespace: str = "production",
    pod_spec: MagicMock | None = None,
    owner_references: list | None = None,
) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.metadata.owner_references = owner_references
    item.spec = pod_spec or _pod_spec()
    return item


def _namespace(name: str, annotations: dict | None) -> MagicMock:
    ns = MagicMock()
    ns.metadata.name = name
    ns.metadata.annotations = annotations
    return ns


class TestKubernetesSecretAuditAdapterIsPort:
    def test_is_secret_rotation_audit_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        assert isinstance(KubernetesSecretAuditAdapter(), SecretRotationAuditPort)


class TestListSecrets:
    def test_maps_secret_fields_and_managed_fields(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        core_api = MagicMock()
        core_api.list_secret_for_all_namespaces.return_value = _list_response(
            _secret_item(
                "db-password",
                data={"DB_PASSWORD": "***"},
                managed_fields=[_managed_fields_entry("kubectl-client-side-apply")],
                annotations={"cert-manager.io/certificate-name": "x"},
            )
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesSecretAuditAdapter().list_secrets()

        secret = result[0]
        assert secret["name"] == "db-password"
        assert secret["namespace"] == "production"
        assert secret["secret_type"] == "Opaque"
        assert secret["data_keys"] == ["DB_PASSWORD"]
        assert secret["managed_fields"][0]["manager"] == "kubectl-client-side-apply"
        assert secret["managed_fields"][0]["fields_v1_raw"] == {"f:data": {}}
        assert secret["annotations"] == {"cert-manager.io/certificate-name": "x"}

    def test_no_data_is_empty_keys_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        core_api = MagicMock()
        core_api.list_secret_for_all_namespaces.return_value = _list_response(
            _secret_item("empty-secret", data=None)
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesSecretAuditAdapter().list_secrets()

        assert result[0]["data_keys"] == []

    def test_no_annotations_is_empty_dict(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        core_api = MagicMock()
        core_api.list_secret_for_all_namespaces.return_value = _list_response(
            _secret_item("s", annotations=None)
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesSecretAuditAdapter().list_secrets()

        assert result[0]["annotations"] == {}

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        core_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        core_api.list_secret_for_all_namespaces.side_effect = error

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesSecretAuditAdapter().list_secrets()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        core_api = MagicMock()
        core_api.list_secret_for_all_namespaces.side_effect = Exception("refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesSecretAuditAdapter().list_secrets()


class TestListSecretReferences:
    def test_detects_env_from_secret_ref(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _list_response(
            _deployment(
                "payment-deploy",
                pod_spec=_pod_spec(containers=[_container(env_from=[_env_from("db-password")])]),
            )
        )
        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response()

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            result = KubernetesSecretAuditAdapter().list_secret_references()

        assert result == [
            {
                "secret_name": "db-password",
                "namespace": "production",
                "workload_name": "payment-deploy",
            }
        ]

    def test_detects_env_value_from_secret_key_ref(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _list_response(
            _deployment(
                "checkout-deploy",
                pod_spec=_pod_spec(containers=[_container(env=[_env_var("db-password")])]),
            )
        )
        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response()

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            result = KubernetesSecretAuditAdapter().list_secret_references()

        assert result[0]["secret_name"] == "db-password"
        assert result[0]["workload_name"] == "checkout-deploy"

    def test_detects_secret_volume_mount(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _list_response(
            _deployment(
                "ingress-deploy",
                pod_spec=_pod_spec(volumes=[_secret_volume("tls-cert")]),
            )
        )
        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response()

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            result = KubernetesSecretAuditAdapter().list_secret_references()

        assert result[0]["secret_name"] == "tls-cert"

    def test_detects_projected_volume_secret_source(self) -> None:
        """Edge Case 3: Secret mounted via projected volume."""
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _list_response(
            _deployment(
                "app-deploy",
                pod_spec=_pod_spec(volumes=[_projected_volume(["db-password"])]),
            )
        )
        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response()

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            result = KubernetesSecretAuditAdapter().list_secret_references()

        assert result[0]["secret_name"] == "db-password"

    def test_standalone_pod_with_no_owner_is_scanned(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _list_response()
        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod(
                "bare-pod",
                pod_spec=_pod_spec(containers=[_container(env_from=[_env_from("db-password")])]),
                owner_references=None,
            )
        )

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            result = KubernetesSecretAuditAdapter().list_secret_references()

        assert result[0]["workload_name"] == "bare-pod"

    def test_pod_owned_by_replicaset_is_not_double_counted(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        owner_ref = MagicMock()
        owner_ref.kind = "ReplicaSet"
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = _list_response()
        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod(
                "owned-pod",
                pod_spec=_pod_spec(containers=[_container(env_from=[_env_from("db-password")])]),
                owner_references=[owner_ref],
            )
        )

        with (
            patch("kubernetes.client.AppsV1Api", return_value=apps_api),
            patch("kubernetes.client.CoreV1Api", return_value=core_api),
        ):
            result = KubernetesSecretAuditAdapter().list_secret_references()

        assert result == []

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        apps_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        apps_api.list_deployment_for_all_namespaces.side_effect = error

        with patch("kubernetes.client.AppsV1Api", return_value=apps_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesSecretAuditAdapter().list_secret_references()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.side_effect = Exception("refused")

        with patch("kubernetes.client.AppsV1Api", return_value=apps_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesSecretAuditAdapter().list_secret_references()


class TestGetNamespaceRotationExemptions:
    def test_returns_namespaces_with_exempt_annotation(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespace.return_value = _list_response(
            _namespace("sandbox", {"hexawyn.io/secret-rotation-exempt": "true"}),
            _namespace("production", None),
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesSecretAuditAdapter().get_namespace_rotation_exemptions()

        assert result == {"sandbox"}

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        core_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        core_api.list_namespace.side_effect = error

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesSecretAuditAdapter().get_namespace_rotation_exemptions()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
            KubernetesSecretAuditAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespace.side_effect = Exception("refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesSecretAuditAdapter().get_namespace_rotation_exemptions()
