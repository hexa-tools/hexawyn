"""Unit tests for KubernetesNetworkPolicyAdapter — mocks kubernetes.client.CoreV1Api
/ NetworkingV1Api for namespace/pod/NetworkPolicy listing, and CustomObjectsApi
for the Calico GlobalNetworkPolicy / Istio PeerAuthentication presence
checks (mirroring IstioTopologyAdapter's "not installed -> graceful" style,
here returning bool instead of None since these are simple presence checks)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.network_policy_audit_port import NetworkPolicyAuditPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _namespace_item(name: str) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    return item


def _pod_item(namespace: str) -> MagicMock:
    item = MagicMock()
    item.metadata.namespace = namespace
    return item


def _label_selector(
    match_labels: dict | None = None, match_expressions: list | None = None
) -> MagicMock:
    selector = MagicMock()
    selector.match_labels = match_labels
    selector.match_expressions = match_expressions
    return selector


def _network_policy_item(
    name: str,
    namespace: str,
    ingress: list | None = None,
    egress: list | None = None,
    pod_selector: MagicMock | None = None,
) -> MagicMock:
    item = MagicMock()
    item.metadata.name = name
    item.metadata.namespace = namespace
    item.spec.ingress = ingress
    item.spec.egress = egress
    item.spec.pod_selector = pod_selector or _label_selector()
    return item


def _list_response(*items: MagicMock) -> MagicMock:
    response = MagicMock()
    response.items = list(items)
    return response


class TestKubernetesNetworkPolicyAdapterIsPort:
    def test_is_network_policy_audit_port(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        assert isinstance(KubernetesNetworkPolicyAdapter(), NetworkPolicyAuditPort)


class TestListNamespacesWithPodCounts:
    def test_counts_pods_per_namespace(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespace.return_value = _list_response(
            _namespace_item("dev"), _namespace_item("empty-ns")
        )
        core_api.list_pod_for_all_namespaces.return_value = _list_response(
            _pod_item("dev"), _pod_item("dev")
        )

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            result = KubernetesNetworkPolicyAdapter().list_namespaces_with_pod_counts()

        by_name = {ns["name"]: ns["pod_count"] for ns in result}
        assert by_name == {"dev": 2, "empty-ns": 0}

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        core_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        core_api.list_namespace.side_effect = error

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesNetworkPolicyAdapter().list_namespaces_with_pod_counts()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        core_api = MagicMock()
        core_api.list_namespace.side_effect = Exception("refused")

        with patch("kubernetes.client.CoreV1Api", return_value=core_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesNetworkPolicyAdapter().list_namespaces_with_pod_counts()


class TestListNetworkPolicies:
    def test_maps_rule_counts_and_pod_selector(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        networking_api = MagicMock()
        networking_api.list_network_policy_for_all_namespaces.return_value = _list_response(
            _network_policy_item(
                "allow-frontend",
                "production",
                ingress=[MagicMock()],
                egress=[MagicMock(), MagicMock()],
                pod_selector=_label_selector(match_labels={"app": "backend"}),
            )
        )

        with patch("kubernetes.client.NetworkingV1Api", return_value=networking_api):
            result = KubernetesNetworkPolicyAdapter().list_network_policies()

        policy = result[0]
        assert policy["namespace"] == "production"
        assert policy["ingress_rule_count"] == 1
        assert policy["egress_rule_count"] == 2
        assert policy["has_empty_pod_selector"] is False

    def test_empty_pod_selector_and_no_rules(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        networking_api = MagicMock()
        networking_api.list_network_policy_for_all_namespaces.return_value = _list_response(
            _network_policy_item("default-deny", "monitoring", ingress=None, egress=None)
        )

        with patch("kubernetes.client.NetworkingV1Api", return_value=networking_api):
            result = KubernetesNetworkPolicyAdapter().list_network_policies()

        policy = result[0]
        assert policy["ingress_rule_count"] == 0
        assert policy["egress_rule_count"] == 0
        assert policy["has_empty_pod_selector"] is True

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        networking_api = MagicMock()
        error = Exception("forbidden")
        error.status = 403
        networking_api.list_network_policy_for_all_namespaces.side_effect = error

        with patch("kubernetes.client.NetworkingV1Api", return_value=networking_api):
            with pytest.raises(InsufficientPermissionsError):
                KubernetesNetworkPolicyAdapter().list_network_policies()

    def test_other_failure_raises_cluster_unreachable(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        networking_api = MagicMock()
        networking_api.list_network_policy_for_all_namespaces.side_effect = Exception("refused")

        with patch("kubernetes.client.NetworkingV1Api", return_value=networking_api):
            with pytest.raises(ClusterUnreachableError):
                KubernetesNetworkPolicyAdapter().list_network_policies()


class TestHasCalicoGlobalNetworkPolicies:
    def test_returns_true_when_policies_exist(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {"items": [{"metadata": {"name": "x"}}]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_calico_global_network_policies()

        assert result is True

    def test_returns_false_when_crd_not_installed(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.side_effect = Exception("CRD not found")

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_calico_global_network_policies()

        assert result is False

    def test_returns_false_when_no_items(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {"items": []}

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_calico_global_network_policies()

        assert result is False


class TestHasIstioStrictPeerAuthentication:
    def test_returns_true_when_strict_mtls_mode_present(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [{"spec": {"mtls": {"mode": "STRICT"}}}]
        }

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_istio_strict_peer_authentication()

        assert result is True

    def test_returns_false_when_mode_is_permissive(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [{"spec": {"mtls": {"mode": "PERMISSIVE"}}}]
        }

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_istio_strict_peer_authentication()

        assert result is False

    def test_returns_false_when_crd_not_installed(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.side_effect = Exception("CRD not found")

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_istio_strict_peer_authentication()

        assert result is False

    def test_malformed_item_is_skipped(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {"items": [{"spec": "not-a-dict"}]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_istio_strict_peer_authentication()

        assert result is False

    def test_non_dict_item_is_skipped(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {"items": ["not-a-dict"]}

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_istio_strict_peer_authentication()

        assert result is False

    def test_non_dict_mtls_is_skipped(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [{"spec": {"mtls": "not-a-dict"}}]
        }

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_istio_strict_peer_authentication()

        assert result is False

    def test_non_dict_response_returns_false(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
            KubernetesNetworkPolicyAdapter,
        )

        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = ["not", "a", "dict"]

        with patch("kubernetes.client.CustomObjectsApi", return_value=crd_api):
            result = KubernetesNetworkPolicyAdapter().has_istio_strict_peer_authentication()

        assert result is False
