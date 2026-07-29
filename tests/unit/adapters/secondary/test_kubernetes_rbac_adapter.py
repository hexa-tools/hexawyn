from __future__ import annotations

import json
import os
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
    KubernetesRBACAdapter,
    _parse_audit_line,
)
from hexawyn.application.ports.driven.rbac_security_audit_port import (
    RBACSecurityAuditPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _make_sa(name: str, namespace: str) -> MagicMock:
    sa = MagicMock()
    sa.metadata.name = name
    sa.metadata.namespace = namespace
    return sa


def _make_subject(kind: str, name: str, namespace: str | None = None) -> MagicMock:
    subj = MagicMock()
    subj.kind = kind
    subj.name = name
    subj.namespace = namespace
    return subj


def _make_role_ref(kind: str, name: str) -> MagicMock:
    ref = MagicMock()
    ref.kind = kind
    ref.name = name
    return ref


def _make_binding(
    kind: str,
    name: str,
    namespace: str | None,
    subjects: list[MagicMock] | None = None,
) -> MagicMock:
    b = MagicMock()
    b.metadata.name = name
    b.metadata.namespace = namespace
    b.subjects = subjects or []
    b.role_ref = _make_role_ref("ClusterRole", "admin")
    return b


def _make_role(  # noqa: PLR0913
    kind: str,
    name: str,
    namespace: str | None = None,
    rules: list[MagicMock] | None = None,
    labels: dict[str, str] | None = None,
    aggregation_rule: MagicMock | None = None,
) -> MagicMock:
    r = MagicMock()
    r.metadata.name = name
    r.metadata.namespace = namespace
    r.metadata.labels = labels or {}
    r.rules = rules or []
    r.aggregation_rule = aggregation_rule
    return r


def _make_rule(verbs: list[str], resources: list[str], api_groups: list[str]) -> MagicMock:
    rule = MagicMock()
    rule.verbs = verbs
    rule.resources = resources
    rule.api_groups = api_groups
    return rule


def _make_pod(name: str, namespace: str, sa_name: str = "default") -> MagicMock:
    pod = MagicMock()
    pod.metadata.name = name
    pod.metadata.namespace = namespace
    pod.spec.service_account_name = sa_name
    return pod


class TestKubernetesRBACAdapter:
    def test_implements_port(self) -> None:
        adapter = KubernetesRBACAdapter()
        assert isinstance(adapter, RBACSecurityAuditPort)


class TestListServiceAccounts:
    def test_list_service_accounts(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            sa_list = MagicMock()
            sa_list.items = [
                _make_sa("default", "ns1"),
                _make_sa("builder", "ns2"),
            ]
            mock_core.list_service_account_for_all_namespaces.return_value = sa_list
            mock_core_cls.return_value = mock_core

            result = adapter.list_service_accounts()

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "default"
        assert result[0]["namespace"] == "ns1"

    def test_list_service_accounts_rbac_error(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            api_exc = Exception("forbidden")
            api_exc.status = 403
            mock_core.list_service_account_for_all_namespaces.side_effect = api_exc
            mock_core_cls.return_value = mock_core

            with pytest.raises(InsufficientPermissionsError):
                adapter.list_service_accounts()

    def test_list_service_accounts_other_error(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            mock_core.list_service_account_for_all_namespaces.side_effect = Exception("boom")
            mock_core_cls.return_value = mock_core

            with pytest.raises(ClusterUnreachableError):
                adapter.list_service_accounts()


class TestListRoleBindings:
    def test_list_role_bindings(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.RbacAuthorizationV1Api") as mock_rbac_cls:
            mock_rbac = MagicMock()
            cluster_list = MagicMock()
            cluster_list.items = [_make_binding("ClusterRoleBinding", "admin-binding", None)]
            ns_list = MagicMock()
            ns_list.items = [_make_binding("RoleBinding", "viewer", "ns1")]
            mock_rbac.list_cluster_role_binding.return_value = cluster_list
            mock_rbac.list_role_binding_for_all_namespaces.return_value = ns_list
            mock_rbac_cls.return_value = mock_rbac

            result = adapter.list_role_bindings()

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["binding_kind"] == "ClusterRoleBinding"
        assert result[1]["binding_kind"] == "RoleBinding"

    def test_list_role_bindings_with_subjects(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.RbacAuthorizationV1Api") as mock_rbac_cls:
            mock_rbac = MagicMock()
            cluster_list = MagicMock()
            binding = _make_binding(
                "ClusterRoleBinding",
                "admin-binding",
                None,
                subjects=[_make_subject("ServiceAccount", "mysa", "ns1")],
            )
            cluster_list.items = [binding]
            ns_list = MagicMock()
            ns_list.items = []
            mock_rbac.list_cluster_role_binding.return_value = cluster_list
            mock_rbac.list_role_binding_for_all_namespaces.return_value = ns_list
            mock_rbac_cls.return_value = mock_rbac

            result = adapter.list_role_bindings()

        assert len(result) == 1  # noqa: PLR2004
        assert len(result[0]["subjects"]) == 1  # noqa: PLR2004
        assert result[0]["subjects"][0]["kind"] == "ServiceAccount"

    def test_list_role_bindings_error(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.RbacAuthorizationV1Api") as mock_rbac_cls:
            mock_rbac = MagicMock()
            api_exc = Exception("forbidden")
            api_exc.status = 403
            mock_rbac.list_cluster_role_binding.side_effect = api_exc
            mock_rbac_cls.return_value = mock_rbac

            with pytest.raises(InsufficientPermissionsError):
                adapter.list_role_bindings()


class TestListRoles:
    def test_list_roles(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.RbacAuthorizationV1Api") as mock_rbac_cls:
            mock_rbac = MagicMock()
            cluster_list = MagicMock()
            cluster_list.items = [
                _make_role(
                    "ClusterRole",
                    "admin",
                    rules=[_make_rule(["*"], ["*"], ["*"])],
                    labels={"app": "hexawyn"},
                )
            ]
            ns_list = MagicMock()
            ns_list.items = [
                _make_role(
                    "Role",
                    "viewer",
                    namespace="ns1",
                    rules=[_make_rule(["get", "list"], ["pods"], [""])],
                )
            ]
            mock_rbac.list_cluster_role.return_value = cluster_list
            mock_rbac.list_role_for_all_namespaces.return_value = ns_list
            mock_rbac_cls.return_value = mock_rbac

            result = adapter.list_roles()

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["kind"] == "ClusterRole"
        assert result[0]["name"] == "admin"
        assert result[1]["kind"] == "Role"
        assert result[1]["name"] == "viewer"

    def test_list_roles_with_aggregation(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.RbacAuthorizationV1Api") as mock_rbac_cls:
            mock_rbac = MagicMock()
            cluster_list = MagicMock()
            agg_rule = MagicMock()
            selector = MagicMock()
            selector.match_labels = {"env": "prod"}
            agg_rule.cluster_role_selectors = [selector]
            cluster_list.items = [_make_role("ClusterRole", "agg-role", aggregation_rule=agg_rule)]
            ns_list = MagicMock()
            ns_list.items = []
            mock_rbac.list_cluster_role.return_value = cluster_list
            mock_rbac.list_role_for_all_namespaces.return_value = ns_list
            mock_rbac_cls.return_value = mock_rbac

            result = adapter.list_roles()

        assert len(result[0]["aggregation_selectors"]) == 1  # noqa: PLR2004
        assert result[0]["aggregation_selectors"][0] == {"env": "prod"}

    def test_list_roles_error(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.RbacAuthorizationV1Api") as mock_rbac_cls:
            mock_rbac = MagicMock()
            mock_rbac.list_cluster_role.side_effect = Exception("timeout")
            mock_rbac_cls.return_value = mock_rbac

            with pytest.raises(ClusterUnreachableError):
                adapter.list_roles()


class TestListPodsByServiceAccount:
    def test_list_pods(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            pod_list = MagicMock()
            pod_list.items = [
                _make_pod("web-pod", "ns1", sa_name="web-sa"),
                _make_pod("worker-pod", "ns2", sa_name="worker-sa"),
            ]
            mock_core.list_pod_for_all_namespaces.return_value = pod_list
            mock_core_cls.return_value = mock_core

            result = adapter.list_pods_by_service_account()

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["pod_name"] == "web-pod"
        assert result[0]["service_account_name"] == "web-sa"

    def test_pod_defaults_service_account(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            pod_list = MagicMock()
            pod = _make_pod("pod1", "ns1")
            pod.spec.service_account_name = None
            pod_list.items = [pod]
            mock_core.list_pod_for_all_namespaces.return_value = pod_list
            mock_core_cls.return_value = mock_core

            result = adapter.list_pods_by_service_account()

        assert result[0]["service_account_name"] == "default"

    def test_list_pods_error(self) -> None:
        adapter = KubernetesRBACAdapter()

        with patch("kubernetes.client.CoreV1Api") as mock_core_cls:
            mock_core = MagicMock()
            api_exc = Exception("forbidden")
            api_exc.status = 403
            mock_core.list_pod_for_all_namespaces.side_effect = api_exc
            mock_core_cls.return_value = mock_core

            with pytest.raises(InsufficientPermissionsError):
                adapter.list_pods_by_service_account()


class TestFetchApiUsage:
    def test_no_audit_log_file_returns_unavailable(self) -> None:
        adapter = KubernetesRBACAdapter()
        with patch.dict(os.environ, {"K8S_AUDIT_LOG_PATH": "/nonexistent/path"}):
            result = adapter.fetch_api_usage(window_days=30)

        assert result["available"] is False
        assert result["events"] == []

    def test_with_audit_log_file(self, tmp_path) -> None:
        adapter = KubernetesRBACAdapter()
        audit_file = tmp_path / "audit.log"
        lines = [
            json.dumps(
                {
                    "user": {"username": "system:serviceaccount:default:my-sa"},
                    "objectRef": {"resource": "pods"},
                    "verb": "list",
                    "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
                }
            ),
            json.dumps(
                {
                    "user": {"username": "system:serviceaccount:prod:builder"},
                    "objectRef": {"resource": "deployments"},
                    "verb": "create",
                    "requestReceivedTimestamp": "2024-01-02T00:00:00Z",
                }
            ),
        ]
        audit_file.write_text("\n".join(lines) + "\n")

        with patch.dict(os.environ, {"K8S_AUDIT_LOG_PATH": str(audit_file)}):
            result = adapter.fetch_api_usage(window_days=30)

        assert result["available"] is True
        assert len(result["events"]) == 2  # noqa: PLR2004
        assert result["events"][0]["service_account"] == "my-sa"
        assert result["events"][1]["service_account"] == "builder"


class TestParseAuditLine:
    def test_valid_service_account_event(self) -> None:
        line = json.dumps(
            {
                "user": {"username": "system:serviceaccount:default:my-sa"},
                "objectRef": {"resource": "pods"},
                "verb": "list",
                "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
            }
        )
        result = _parse_audit_line(line)
        assert result is not None
        assert result["service_account"] == "my-sa"
        assert result["namespace"] == "default"
        assert result["verb"] == "list"
        assert result["resource"] == "pods"

    def test_invalid_json_returns_none(self) -> None:
        assert _parse_audit_line("not json") is None

    def test_non_dict_returns_none(self) -> None:
        assert _parse_audit_line(json.dumps(["array"])) is None

    def test_non_service_account_user_returns_none(self) -> None:
        line = json.dumps(
            {
                "user": {"username": "admin"},
                "objectRef": {"resource": "pods"},
                "verb": "list",
                "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
            }
        )
        assert _parse_audit_line(line) is None

    def test_invalid_sa_format_returns_none(self) -> None:
        line = json.dumps(
            {
                "user": {"username": "system:serviceaccount:onlythree"},
                "objectRef": {"resource": "pods"},
                "verb": "list",
                "requestReceivedTimestamp": "2024-01-01T00:00:00Z",
            }
        )
        assert _parse_audit_line(line) is None

    def test_missing_fields_returns_none(self) -> None:
        line = json.dumps(
            {
                "user": {"username": "system:serviceaccount:default:my-sa"},
                "objectRef": {"resource": "pods"},
            }
        )
        assert _parse_audit_line(line) is None
