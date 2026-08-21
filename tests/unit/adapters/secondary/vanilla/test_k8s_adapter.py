from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter import VanillaK8sAdapter
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _rule(host: str, services: list[str]) -> MagicMock:
    paths = []
    for service in services:
        path = MagicMock()
        path.backend = MagicMock()
        path.backend.service = MagicMock()
        path.backend.service.name = service
        paths.append(path)
    rule = MagicMock()
    rule.host = host
    rule.http = MagicMock()
    rule.http.paths = paths
    return rule


def _make_ingress(
    name: str, namespace: str, rules: list[MagicMock], tls: object | None
) -> MagicMock:
    ing = MagicMock()
    ing.metadata = MagicMock()
    ing.metadata.name = name
    ing.metadata.namespace = namespace
    ing.spec = MagicMock()
    ing.spec.rules = rules
    ing.spec.tls = tls
    return ing


def _adapter() -> VanillaK8sAdapter:
    return VanillaK8sAdapter(api=MagicMock(), metrics_api=None, cluster_name="prod-eu")


class TestVanillaK8sIngress:
    def test_list_ingresses_extracts_host_service_and_tls(self) -> None:
        ingress_list = MagicMock()
        ingress_list.items = [
            _make_ingress(
                "payments-api",
                "production",
                [_rule("api.payments.example.com", ["payment-api"])],
                tls=[MagicMock()],
            ),
            _make_ingress(
                "frontend",
                "staging",
                [_rule("staging.example.com", ["frontend"])],
                tls=None,
            ),
        ]
        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking_cls.return_value.list_namespaced_ingress.return_value = ingress_list
            result = _adapter().list_ingresses(namespace="default")

        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["name"] == "payments-api"
        assert result[0]["namespace"] == "production"
        assert result[0]["host"] == "api.payments.example.com"
        assert result[0]["target_service"] == "payment-api"
        assert result[0]["tls_enabled"] is True
        assert result[1]["tls_enabled"] is False

    def test_list_ingresses_multiple_rules_produce_multiple_entries(self) -> None:
        ingress_list = MagicMock()
        ingress_list.items = [
            _make_ingress(
                "api",
                "production",
                [_rule("a.example.com", ["a-svc"]), _rule("b.example.com", ["b-svc"])],
                tls=None,
            ),
        ]
        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking_cls.return_value.list_namespaced_ingress.return_value = ingress_list
            result = _adapter().list_ingresses(namespace="production")

        assert len(result) == 2  # noqa: PLR2004
        assert {entry["host"] for entry in result} == {"a.example.com", "b.example.com"}

    def test_list_ingresses_rule_without_paths_keeps_host_entry(self) -> None:
        ingress_list = MagicMock()
        rule = MagicMock()
        rule.host = "bare.example.com"
        rule.http = None
        ingress_list.items = [_make_ingress("bare", "production", [rule], tls=None)]

        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking_cls.return_value.list_namespaced_ingress.return_value = ingress_list
            result = _adapter().list_ingresses(namespace="production")

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["host"] == "bare.example.com"
        assert result[0]["target_service"] == ""

    def test_list_ingresses_without_rules_uses_default_backend(self) -> None:
        ingress_list = MagicMock()
        default_backend = MagicMock()
        default_backend.service = MagicMock()
        default_backend.service.name = "fallback-svc"
        ing = _make_ingress("default-only", "production", [], tls=None)
        ing.spec.default_backend = default_backend
        ingress_list.items = [ing]

        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking_cls.return_value.list_namespaced_ingress.return_value = ingress_list
            result = _adapter().list_ingresses(namespace="production")

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["host"] == ""
        assert result[0]["target_service"] == "fallback-svc"

    def test_list_ingresses_without_rules_and_backend_keeps_empty_service(self) -> None:
        ingress_list = MagicMock()
        ing = _make_ingress("empty", "production", [], tls=None)
        ing.spec.default_backend = None
        ingress_list.items = [ing]

        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking_cls.return_value.list_namespaced_ingress.return_value = ingress_list
            result = _adapter().list_ingresses(namespace="production")

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["target_service"] == ""

    def test_list_ingresses_empty(self) -> None:
        ingress_list = MagicMock()
        ingress_list.items = []
        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking_cls.return_value.list_namespaced_ingress.return_value = ingress_list
            result = _adapter().list_ingresses(namespace="default")

        assert result == []

    def test_list_ingresses_rbac_error(self) -> None:
        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            api_exc = Exception("forbidden")
            api_exc.status = 403
            mock_networking_cls.return_value.list_namespaced_ingress.side_effect = api_exc
            with pytest.raises(InsufficientPermissionsError):
                _adapter().list_ingresses(namespace="production")

    def test_list_ingresses_unreachable_error(self) -> None:
        with patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls:
            mock_networking_cls.return_value.list_namespaced_ingress.side_effect = Exception("boom")
            with pytest.raises(ClusterUnreachableError):
                _adapter().list_ingresses(namespace="production")
