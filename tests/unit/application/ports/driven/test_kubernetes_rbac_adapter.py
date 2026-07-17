"""Unit tests for KubernetesRBACAdapter — mocks kubernetes.client.CoreV1Api /
RbacAuthorizationV1Api for the live-object listing methods, uses real
tmp_path files for fetch_api_usage (same convention as
KubernetesAuditLogAdapter — no k8s audit-log-API precedent exists to mock)."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.rbac_security_audit_port import (
    RBACSecurityAuditPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _sa_item(name: str, namespace: str) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    return item


def _subject(kind: str, name: str, namespace: str | None) -> MagicMock:
    subject = MagicMock()
    subject.kind = kind
    subject.name = name
    subject.namespace = namespace
    return subject


def _binding_item(
    name: str,
    role_kind: str,
    role_name: str,
    subjects: list | None,
    namespace: str | None = None,
) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.role_ref.kind = role_kind
    item.role_ref.name = role_name
    item.subjects = subjects
    return item


def _rule(
    verbs: list[str] | None, resources: list[str] | None, api_groups: list[str] | None
) -> MagicMock:
    rule = MagicMock()
    rule.verbs = verbs
    rule.resources = resources
    rule.api_groups = api_groups
    return rule


def _label_selector(match_labels: dict[str, str] | None) -> MagicMock:
    selector = MagicMock()
    selector.match_labels = match_labels
    return selector


def _cluster_role_item(
    name: str,
    rules: list | None = None,
    labels: dict[str, str] | None = None,
    aggregation_rule: MagicMock | None = None,
) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.labels = labels
    item.rules = rules
    item.aggregation_rule = aggregation_rule
    return item


def _role_item(name: str, namespace: str, rules: list | None = None) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.metadata.labels = None
    item.rules = rules
    return item


def _pod_item(name: str, namespace: str, service_account_name: str | None) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.spec.service_account_name = service_account_name
    return item


def _list_response(*items: MagicMock) -> MagicMock:
    response = MagicMock()
    response.items = list(items)
    return response


class TestKubernetesRBACAdapterIsPort:
    def test_is_rbac_security_audit_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        assert isinstance(KubernetesRBACAdapter(), RBACSecurityAuditPort)


class TestListServiceAccounts:
    def test_returns_service_accounts_across_namespaces(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        core_api = MagicMock()
        core_api.list_service_account_for_all_namespaces.return_value = _list_response(
            _sa_item("payment-sa", "production"), _sa_item("default", "kube-system")
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesRBACAdapter().list_service_accounts()

        assert {"name": "payment-sa", "namespace": "production"} in result
        assert {"name": "default", "namespace": "kube-system"} in result

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        core_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        core_api.list_service_account_for_all_namespaces.side_effect = error

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesRBACAdapter().list_service_accounts()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        core_api = MagicMock()
        core_api.list_service_account_for_all_namespaces.side_effect = Exception("refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesRBACAdapter().list_service_accounts()


class TestListRoleBindings:
    def test_returns_cluster_and_namespaced_bindings(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        rbac_api = MagicMock()
        rbac_api.list_cluster_role_binding.return_value = _list_response(
            _binding_item(
                "payment-admin",
                "ClusterRole",
                "cluster-admin",
                [_subject("ServiceAccount", "payment-sa", "production")],
            )
        )
        rbac_api.list_role_binding_for_all_namespaces.return_value = _list_response(
            _binding_item(
                "monitoring-secrets",
                "ClusterRole",
                "secrets-reader",
                [_subject("ServiceAccount", "monitoring-sa", None)],
                namespace="monitoring",
            )
        )

        with patch("kubernetes.client.RbacAuthorizationV1Api", return_value=rbac_api):
            result = KubernetesRBACAdapter().list_role_bindings()

        by_kind = {item["binding_kind"]: item for item in result}
        cluster_binding = by_kind["ClusterRoleBinding"]
        assert cluster_binding["namespace"] is None
        assert cluster_binding["role_ref"] == {
            "kind": "ClusterRole",
            "name": "cluster-admin",
        }
        assert cluster_binding["subjects"] == [
            {"kind": "ServiceAccount", "name": "payment-sa", "namespace": "production"}
        ]

        namespaced_binding = by_kind["RoleBinding"]
        assert namespaced_binding["namespace"] == "monitoring"
        assert namespaced_binding["subjects"] == [
            {"kind": "ServiceAccount", "name": "monitoring-sa", "namespace": None}
        ]

    def test_binding_with_no_subjects_returns_empty_subject_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        rbac_api = MagicMock()
        rbac_api.list_cluster_role_binding.return_value = _list_response(
            _binding_item("orphan", "ClusterRole", "view", None)
        )
        rbac_api.list_role_binding_for_all_namespaces.return_value = _list_response()

        with patch("kubernetes.client.RbacAuthorizationV1Api", return_value=rbac_api):
            result = KubernetesRBACAdapter().list_role_bindings()

        assert result[0]["subjects"] == []

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        rbac_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        rbac_api.list_cluster_role_binding.side_effect = error

        with patch("kubernetes.client.RbacAuthorizationV1Api", return_value=rbac_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesRBACAdapter().list_role_bindings()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        rbac_api = MagicMock()
        rbac_api.list_cluster_role_binding.side_effect = Exception("refused")

        with patch("kubernetes.client.RbacAuthorizationV1Api", return_value=rbac_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesRBACAdapter().list_role_bindings()


class TestListRoles:
    def test_returns_cluster_roles_and_namespaced_roles(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        rbac_api = MagicMock()
        rbac_api.list_cluster_role.return_value = _list_response(
            _cluster_role_item(
                "cluster-admin",
                rules=[_rule(["*"], ["*"], ["*"])],
                labels={"kubernetes.io/bootstrapping": "rbac-defaults"},
            )
        )
        rbac_api.list_role_for_all_namespaces.return_value = _list_response(
            _role_item("pod-reader", "production", rules=[_rule(["get"], ["pods"], [""])])
        )

        with patch("kubernetes.client.RbacAuthorizationV1Api", return_value=rbac_api):
            result = KubernetesRBACAdapter().list_roles()

        by_name = {role["name"]: role for role in result}
        assert by_name["cluster-admin"]["kind"] == "ClusterRole"
        assert by_name["cluster-admin"]["namespace"] is None
        assert by_name["cluster-admin"]["rules"] == [
            {"verbs": ["*"], "resources": ["*"], "api_groups": ["*"]}
        ]
        assert by_name["cluster-admin"]["aggregation_selectors"] == []
        assert by_name["pod-reader"]["kind"] == "Role"
        assert by_name["pod-reader"]["namespace"] == "production"
        assert by_name["pod-reader"]["labels"] == {}

    def test_resolves_aggregation_selectors_from_aggregation_rule(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        aggregation_rule = MagicMock()
        aggregation_rule.cluster_role_selectors = [
            _label_selector({"aggregate-to-monitoring": "true"}),
            _label_selector(None),
        ]
        rbac_api = MagicMock()
        rbac_api.list_cluster_role.return_value = _list_response(
            _cluster_role_item(
                "monitoring-aggregate", rules=None, aggregation_rule=aggregation_rule
            )
        )
        rbac_api.list_role_for_all_namespaces.return_value = _list_response()

        with patch("kubernetes.client.RbacAuthorizationV1Api", return_value=rbac_api):
            result = KubernetesRBACAdapter().list_roles()

        assert result[0]["aggregation_selectors"] == [
            {"aggregate-to-monitoring": "true"},
            {},
        ]
        assert result[0]["rules"] == []

    def test_no_aggregation_rule_returns_empty_selectors(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        rbac_api = MagicMock()
        rbac_api.list_cluster_role.return_value = _list_response(
            _cluster_role_item("view", rules=[], aggregation_rule=None)
        )
        rbac_api.list_role_for_all_namespaces.return_value = _list_response()

        with patch("kubernetes.client.RbacAuthorizationV1Api", return_value=rbac_api):
            result = KubernetesRBACAdapter().list_roles()

        assert result[0]["aggregation_selectors"] == []

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        rbac_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        rbac_api.list_cluster_role.side_effect = error

        with patch("kubernetes.client.RbacAuthorizationV1Api", return_value=rbac_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesRBACAdapter().list_roles()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        rbac_api = MagicMock()
        rbac_api.list_cluster_role.side_effect = Exception("refused")

        with patch("kubernetes.client.RbacAuthorizationV1Api", return_value=rbac_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesRBACAdapter().list_roles()


class TestListPodsByServiceAccount:
    def test_returns_pod_to_service_account_mapping(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod_item("payment-pod-abc", "production", "payment-sa"),
            _pod_item("payment-pod-def", "production", "payment-sa"),
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesRBACAdapter().list_pods_by_service_account()

        assert {
            "pod_name": "payment-pod-abc",
            "namespace": "production",
            "service_account_name": "payment-sa",
        } in result

    def test_missing_service_account_name_defaults_to_default(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod_item("bare-pod", "production", None)
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesRBACAdapter().list_pods_by_service_account()

        assert result[0]["service_account_name"] == "default"

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        core_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        core_api.list_pod_for_all_namespaces.side_effect = error

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesRBACAdapter().list_pods_by_service_account()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        core_api = MagicMock()
        core_api.list_pod_for_all_namespaces.side_effect = Exception("refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesRBACAdapter().list_pods_by_service_account()


class TestFetchApiUsage:
    def test_missing_file_returns_unavailable(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(tmp_path / "does-not-exist.log"))

        result = KubernetesRBACAdapter().fetch_api_usage(30)

        assert result["available"] is False
        assert result["events"] == []

    def test_service_account_events_are_parsed(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        log_path = tmp_path / "audit.log"
        lines = [
            {
                "verb": "get",
                "objectRef": {
                    "resource": "pods",
                    "namespace": "production",
                    "name": "payment-pod",
                },
                "user": {"username": "system:serviceaccount:production:payment-sa"},
                "requestReceivedTimestamp": "2026-06-14T14:23:00.000000Z",
            }
        ]
        log_path.write_text("\n".join(json.dumps(line) for line in lines))
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))

        result = KubernetesRBACAdapter().fetch_api_usage(30)

        assert result["available"] is True
        assert result["events"] == [
            {
                "service_account": "payment-sa",
                "namespace": "production",
                "verb": "get",
                "resource": "pods",
                "timestamp": "2026-06-14T14:23:00.000000Z",
            }
        ]

    def test_non_service_account_user_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        log_path = tmp_path / "audit.log"
        log_path.write_text(
            json.dumps(
                {
                    "verb": "get",
                    "objectRef": {
                        "resource": "pods",
                        "namespace": "production",
                        "name": "p",
                    },
                    "user": {"username": "user:jane.ops@company.com"},
                    "requestReceivedTimestamp": "2026-06-14T14:23:00.000000Z",
                }
            )
        )
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))

        result = KubernetesRBACAdapter().fetch_api_usage(30)

        assert result["events"] == []

    def test_malformed_line_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        log_path = tmp_path / "audit.log"
        valid_line = json.dumps(
            {
                "verb": "get",
                "objectRef": {
                    "resource": "pods",
                    "namespace": "production",
                    "name": "p",
                },
                "user": {"username": "system:serviceaccount:production:payment-sa"},
                "requestReceivedTimestamp": "2026-06-14T14:23:00.000000Z",
            }
        )
        log_path.write_text("not-json\n" + valid_line)
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))

        result = KubernetesRBACAdapter().fetch_api_usage(30)

        assert len(result["events"]) == 1

    def test_non_dict_json_line_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        log_path = tmp_path / "audit.log"
        log_path.write_text(json.dumps(["not", "a", "dict"]))
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))

        result = KubernetesRBACAdapter().fetch_api_usage(30)

        assert result["events"] == []

    def test_malformed_service_account_username_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        log_path = tmp_path / "audit.log"
        log_path.write_text(
            json.dumps(
                {
                    "verb": "get",
                    "objectRef": {
                        "resource": "pods",
                        "namespace": "production",
                        "name": "p",
                    },
                    "user": {"username": "system:serviceaccount:production"},
                    "requestReceivedTimestamp": "2026-06-14T14:23:00.000000Z",
                }
            )
        )
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))

        result = KubernetesRBACAdapter().fetch_api_usage(30)

        assert result["events"] == []

    def test_missing_object_ref_fields_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        log_path = tmp_path / "audit.log"
        log_path.write_text(
            json.dumps(
                {
                    "verb": "get",
                    "objectRef": "not-a-dict",
                    "user": {"username": "system:serviceaccount:production:payment-sa"},
                    "requestReceivedTimestamp": "2026-06-14T14:23:00.000000Z",
                }
            )
        )
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))

        result = KubernetesRBACAdapter().fetch_api_usage(30)

        assert result["events"] == []

    def test_missing_timestamp_is_skipped(self, tmp_path, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        log_path = tmp_path / "audit.log"
        log_path.write_text(
            json.dumps(
                {
                    "verb": "get",
                    "objectRef": {
                        "resource": "pods",
                        "namespace": "production",
                        "name": "p",
                    },
                    "user": {"username": "system:serviceaccount:production:payment-sa"},
                }
            )
        )
        monkeypatch.setenv("K8S_AUDIT_LOG_PATH", str(log_path))

        result = KubernetesRBACAdapter().fetch_api_usage(30)

        assert result["events"] == []

    def test_default_path_used_when_env_var_not_set(self, monkeypatch) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
            KubernetesRBACAdapter,
        )

        monkeypatch.delenv("K8S_AUDIT_LOG_PATH", raising=False)

        result = KubernetesRBACAdapter().fetch_api_usage(30)

        assert result["available"] is False
