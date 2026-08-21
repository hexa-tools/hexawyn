"""Local E2E chain for list_ingresses.

Exercises the real wiring — MCP tool -> use case -> vanilla adapter ->
NetworkingV1Api — with only the Kubernetes API mocked. This is the local
validation that the tool is auto-discovered and that the execution chain
returns hosts, services and TLS without unexpected fallbacks.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.vanilla.adapters.k8s_adapter import VanillaK8sAdapter


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


class TestListIngressesLocalChain:
    def test_full_chain_lists_hosts_services_and_tls(self) -> None:
        from hexawyn.mcp.tools.list_ingresses import list_ingresses

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
        adapter = VanillaK8sAdapter(api=MagicMock(), metrics_api=None, cluster_name="prod-eu")
        with (
            patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls,
            patch("hexawyn.mcp.server.build_ingress_adapter", return_value=adapter),
        ):
            mock_networking_cls.return_value.list_namespaced_ingress.return_value = ingress_list
            result = list_ingresses(namespace="default")

        assert result["error"] is None
        assert result["count"] == 2  # noqa: PLR2004
        assert {item["host"] for item in result["items"]} == {
            "api.payments.example.com",
            "staging.example.com",
        }
        assert {item["target_service"] for item in result["items"]} == {
            "payment-api",
            "frontend",
        }
        tls_ingresses = {item["name"] for item in result["items"] if item["tls_enabled"]}
        assert tls_ingresses == {"payments-api"}

    def test_duplicate_host_claims_are_exposed_for_the_reporter(self) -> None:
        from hexawyn.mcp.tools.list_ingresses import list_ingresses

        ingress_list = MagicMock()
        ingress_list.items = [
            _make_ingress(
                "payments-api",
                "production",
                [_rule("api.payments.example.com", ["payment-api"])],
                tls=None,
            ),
            _make_ingress(
                "payments-api-v2",
                "production",
                [_rule("api.payments.example.com", ["payment-api-v2"])],
                tls=None,
            ),
        ]
        adapter = VanillaK8sAdapter(api=MagicMock(), metrics_api=None, cluster_name="prod-eu")
        with (
            patch("kubernetes.client.NetworkingV1Api") as mock_networking_cls,
            patch("hexawyn.mcp.server.build_ingress_adapter", return_value=adapter),
        ):
            mock_networking_cls.return_value.list_namespaced_ingress.return_value = ingress_list
            result = list_ingresses(namespace="production")

        by_host: dict[str, set[str]] = {}
        for item in result["items"]:
            by_host.setdefault(item["host"], set()).add(item["name"])
        assert by_host["api.payments.example.com"] == {"payments-api", "payments-api-v2"}

    def test_tool_is_auto_discovered_by_register_tools(self) -> None:
        from fastmcp import FastMCP
        from hexawyn.mcp.server import register_tools

        mcp = FastMCP("test")
        registered: list[str] = []

        def recording_decorator(*args: object, **kwargs: object):
            def wrap(fn):
                registered.append(getattr(fn, "__name__", ""))
                return fn

            return wrap

        with patch.object(mcp, "tool", recording_decorator):
            register_tools(mcp)

        assert "list_ingresses" in registered
