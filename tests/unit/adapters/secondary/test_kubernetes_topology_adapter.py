from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.kubernetes_topology_adapter import KubernetesTopologyAdapter


def _fake_service(
    name: str,
    namespace: str = "production",
    service_type: str = "ClusterIP",
    app_label: str | None = None,
) -> MagicMock:
    svc = MagicMock()
    svc.metadata.name = name
    svc.metadata.namespace = namespace
    svc.spec.type = service_type
    svc.spec.selector = {"app": app_label} if app_label else {}
    return svc


def _fake_deployment(name: str, namespace: str = "production", replicas: int = 1) -> MagicMock:
    dep = MagicMock()
    dep.metadata.name = name
    dep.metadata.namespace = namespace
    dep.spec.replicas = replicas
    return dep


def _fake_network_policy(namespace: str, target_app: str, source_apps: list[str]) -> MagicMock:
    policy = MagicMock()
    policy.metadata.namespace = namespace
    policy.spec.pod_selector.match_labels = {"app": target_app}
    peers = []
    for app in source_apps:
        peer = MagicMock()
        peer.pod_selector.match_labels = {"app": app}
        peers.append(peer)
    ingress_rule = MagicMock()
    ingress_rule._from = peers
    policy.spec.ingress = [ingress_rule]
    return policy


class TestListServices:
    def test_returns_service_records_across_namespaces(self) -> None:
        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value = MagicMock(
            items=[_fake_service("auth-service", app_label="auth-service")]
        )
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = MagicMock(
            items=[_fake_deployment("auth-service", replicas=1)]
        )
        adapter = KubernetesTopologyAdapter("test-cluster", core_api=core_api, apps_api=apps_api)

        services = adapter.list_services(None)

        assert services == [
            {
                "name": "auth-service",
                "namespace": "production",
                "replicas": 1,
                "is_external": False,
            }
        ]

    def test_scopes_to_namespace_when_given(self) -> None:
        core_api = MagicMock()
        core_api.list_namespaced_service.return_value = MagicMock(items=[])
        apps_api = MagicMock()
        apps_api.list_namespaced_deployment.return_value = MagicMock(items=[])
        adapter = KubernetesTopologyAdapter("test-cluster", core_api=core_api, apps_api=apps_api)

        adapter.list_services("production")

        core_api.list_namespaced_service.assert_called_once()

    def test_external_name_service_is_flagged(self) -> None:
        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value = MagicMock(
            items=[_fake_service("stripe-external", service_type="ExternalName")]
        )
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.return_value = MagicMock(items=[])
        adapter = KubernetesTopologyAdapter("test-cluster", core_api=core_api, apps_api=apps_api)

        services = adapter.list_services(None)

        assert services[0]["is_external"] is True

    def test_returns_empty_list_when_service_listing_fails(self) -> None:
        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.side_effect = Exception("403 Forbidden")
        adapter = KubernetesTopologyAdapter("test-cluster", core_api=core_api)

        assert adapter.list_services(None) == []

    def test_replica_defaults_to_zero_when_deployment_lookup_fails(self) -> None:
        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value = MagicMock(
            items=[_fake_service("auth-service")]
        )
        apps_api = MagicMock()
        apps_api.list_deployment_for_all_namespaces.side_effect = Exception("unreachable")
        adapter = KubernetesTopologyAdapter("test-cluster", core_api=core_api, apps_api=apps_api)

        services = adapter.list_services(None)

        assert services[0]["replicas"] == 0


class TestGetNetworkPolicyEdges:
    def test_builds_edge_from_pod_selector_labels(self) -> None:
        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value = MagicMock(
            items=[
                _fake_service("api-gateway", app_label="api-gateway"),
                _fake_service("auth-service", app_label="auth-service"),
            ]
        )
        networking_api = MagicMock()
        networking_api.list_network_policy_for_all_namespaces.return_value = MagicMock(
            items=[_fake_network_policy("production", "auth-service", ["api-gateway"])]
        )
        adapter = KubernetesTopologyAdapter(
            "test-cluster", core_api=core_api, networking_api=networking_api
        )

        edges = adapter.get_network_policy_edges(None)

        assert edges == [{"caller": "api-gateway", "callee": "auth-service"}]

    def test_returns_empty_when_no_matching_service_selector(self) -> None:
        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value = MagicMock(items=[])
        networking_api = MagicMock()
        networking_api.list_network_policy_for_all_namespaces.return_value = MagicMock(
            items=[_fake_network_policy("production", "auth-service", ["api-gateway"])]
        )
        adapter = KubernetesTopologyAdapter(
            "test-cluster", core_api=core_api, networking_api=networking_api
        )

        edges = adapter.get_network_policy_edges(None)

        assert edges == []

    def test_returns_empty_list_on_exception(self) -> None:
        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.side_effect = Exception("unreachable")
        adapter = KubernetesTopologyAdapter("test-cluster", core_api=core_api)

        assert adapter.get_network_policy_edges(None) == []

    def test_scopes_to_namespace_when_given(self) -> None:
        core_api = MagicMock()
        core_api.list_namespaced_service.return_value = MagicMock(items=[])
        networking_api = MagicMock()
        networking_api.list_namespaced_network_policy.return_value = MagicMock(items=[])
        adapter = KubernetesTopologyAdapter(
            "test-cluster", core_api=core_api, networking_api=networking_api
        )

        adapter.get_network_policy_edges("production")

        networking_api.list_namespaced_network_policy.assert_called_once()

    def test_self_loop_and_duplicate_edges_are_deduplicated(self) -> None:
        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value = MagicMock(
            items=[
                _fake_service("api-gateway", app_label="api-gateway"),
                _fake_service("auth-service", app_label="auth-service"),
            ]
        )
        networking_api = MagicMock()
        networking_api.list_network_policy_for_all_namespaces.return_value = MagicMock(
            items=[
                _fake_network_policy("production", "api-gateway", ["api-gateway"]),
                _fake_network_policy("production", "auth-service", ["api-gateway"]),
                _fake_network_policy("production", "auth-service", ["api-gateway"]),
            ]
        )
        adapter = KubernetesTopologyAdapter(
            "test-cluster", core_api=core_api, networking_api=networking_api
        )

        edges = adapter.get_network_policy_edges(None)

        assert edges == [{"caller": "api-gateway", "callee": "auth-service"}]


class TestApiClientLazyConstruction:
    def test_lazily_constructs_real_core_api_client(self) -> None:
        from unittest.mock import patch

        with patch(
            "hexawyn.adapters.secondary.kubernetes_topology_adapter.load_kubeconfig"
        ) as mock_load:
            mock_load.return_value = MagicMock(
                list_service_for_all_namespaces=MagicMock(return_value=MagicMock(items=[]))
            )
            adapter = KubernetesTopologyAdapter("test-cluster")

            services = adapter.list_services(None)

        assert services == []
        mock_load.assert_called_once_with(context="test-cluster")

    def test_context_name_is_none_for_unknown_cluster(self) -> None:
        from unittest.mock import patch

        with patch(
            "hexawyn.adapters.secondary.kubernetes_topology_adapter.load_kubeconfig"
        ) as mock_load:
            mock_load.return_value = MagicMock(
                list_service_for_all_namespaces=MagicMock(return_value=MagicMock(items=[]))
            )
            adapter = KubernetesTopologyAdapter("unknown")

            adapter.list_services(None)

        mock_load.assert_called_once_with(context=None)

    def test_lazily_constructs_real_apps_api_client(self) -> None:
        from unittest.mock import patch

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value = MagicMock(items=[])

        with patch("kubernetes.client.AppsV1Api") as mock_cls:
            mock_cls.return_value.list_deployment_for_all_namespaces.return_value = MagicMock(
                items=[]
            )
            adapter = KubernetesTopologyAdapter("test-cluster", core_api=core_api)

            adapter.list_services(None)

        mock_cls.assert_called_once()

    def test_lazily_constructs_real_networking_api_client(self) -> None:
        from unittest.mock import patch

        core_api = MagicMock()
        core_api.list_service_for_all_namespaces.return_value = MagicMock(items=[])

        with patch("kubernetes.client.NetworkingV1Api") as mock_cls:
            mock_cls.return_value.list_network_policy_for_all_namespaces.return_value = MagicMock(
                items=[]
            )
            adapter = KubernetesTopologyAdapter("test-cluster", core_api=core_api)

            adapter.get_network_policy_edges(None)

        mock_cls.assert_called_once()


class TestMatchServices:
    def test_returns_empty_when_no_app_label(self) -> None:
        from hexawyn.adapters.secondary.kubernetes_topology_adapter import _match_services

        assert _match_services(pod_selector=None, namespace="production", selectors=[]) == []
