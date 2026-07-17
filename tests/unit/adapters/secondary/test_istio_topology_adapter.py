from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.istio_topology_adapter import IstioTopologyAdapter


def _virtual_service(
    hosts: list[str], source_labels: dict[str, str] | None = None
) -> dict[str, object]:
    match: dict[str, object] = {}
    if source_labels is not None:
        match["sourceLabels"] = source_labels
    return {
        "metadata": {"name": "vs", "namespace": "production"},
        "spec": {
            "hosts": hosts,
            "http": [{"match": [match] if match else []}],
        },
    }


class TestGetVirtualServiceEdges:
    def test_builds_edge_from_source_labels(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [
                _virtual_service(["auth-service"], source_labels={"app": "api-gateway"}),
            ]
        }
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        edges = adapter.get_virtual_service_edges(None)

        assert edges == [{"caller": "api-gateway", "callee": "auth-service"}]

    def test_strips_fqdn_suffix_from_host(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [
                _virtual_service(
                    ["auth-service.production.svc.cluster.local"],
                    source_labels={"app": "api-gateway"},
                ),
            ]
        }
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        edges = adapter.get_virtual_service_edges(None)

        assert edges == [{"caller": "api-gateway", "callee": "auth-service"}]

    def test_skips_virtual_service_without_source_labels(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [_virtual_service(["auth-service"], source_labels=None)]
        }
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        edges = adapter.get_virtual_service_edges(None)

        assert edges == []

    def test_returns_none_when_crd_not_installed(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.side_effect = Exception(
            "404 the server could not find the requested resource"
        )
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        assert adapter.get_virtual_service_edges(None) is None

    def test_returns_none_when_rbac_denied(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.side_effect = Exception("403 Forbidden")
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        assert adapter.get_virtual_service_edges(None) is None

    def test_scopes_to_namespace_when_given(self) -> None:
        crd_api = MagicMock()
        crd_api.list_namespaced_custom_object.return_value = {"items": []}
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        adapter.get_virtual_service_edges("production")

        crd_api.list_namespaced_custom_object.assert_called_once()

    def test_lazily_constructs_real_crd_api_client(self) -> None:
        from unittest.mock import patch

        with patch("kubernetes.client.CustomObjectsApi") as mock_cls:
            mock_cls.return_value.list_cluster_custom_object.return_value = {"items": []}
            adapter = IstioTopologyAdapter()

            edges = adapter.get_virtual_service_edges(None)

        assert edges == []
        mock_cls.assert_called_once()

    def test_non_dict_response_returns_empty_list(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = "not-a-dict"
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        assert adapter.get_virtual_service_edges(None) == []

    def test_non_list_items_returns_empty_list(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {"items": "not-a-list"}
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        assert adapter.get_virtual_service_edges(None) == []

    def test_virtual_service_without_hosts_is_skipped(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [{"metadata": {"name": "vs"}, "spec": {"http": []}}]
        }
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        assert adapter.get_virtual_service_edges(None) == []

    def test_virtual_service_with_non_dict_spec_is_skipped(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [{"metadata": {"name": "vs"}, "spec": "not-a-dict"}]
        }
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        assert adapter.get_virtual_service_edges(None) == []

    def test_virtual_service_with_non_list_http_returns_no_edges(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [
                {
                    "metadata": {"name": "vs"},
                    "spec": {"hosts": ["auth-service"], "http": "not-a-list"},
                }
            ]
        }
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        assert adapter.get_virtual_service_edges(None) == []

    def test_non_dict_rule_and_match_entries_are_skipped(self) -> None:
        crd_api = MagicMock()
        crd_api.list_cluster_custom_object.return_value = {
            "items": [
                {
                    "metadata": {"name": "vs"},
                    "spec": {
                        "hosts": ["auth-service"],
                        "http": ["not-a-dict-rule", {"match": ["not-a-dict-match"]}],
                    },
                }
            ]
        }
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        assert adapter.get_virtual_service_edges(None) == []

    def test_source_apps_returns_empty_for_non_dict_spec(self) -> None:
        from hexawyn.adapters.secondary.istio_topology_adapter import _source_apps

        assert _source_apps({"spec": "not-a-dict"}) == []

    def test_duplicate_and_self_loop_edges_are_deduplicated(self) -> None:
        crd_api = MagicMock()
        self_loop_vs = _virtual_service(["api-gateway"], source_labels={"app": "api-gateway"})
        duplicate_vs = _virtual_service(["auth-service"], source_labels={"app": "api-gateway"})
        crd_api.list_cluster_custom_object.return_value = {
            "items": [self_loop_vs, duplicate_vs, duplicate_vs]
        }
        adapter = IstioTopologyAdapter(crd_api=crd_api)

        edges = adapter.get_virtual_service_edges(None)

        assert edges == [{"caller": "api-gateway", "callee": "auth-service"}]
