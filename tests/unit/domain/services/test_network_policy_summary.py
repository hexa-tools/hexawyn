from __future__ import annotations

from hexawyn.domain.services.cilium.network_policy_summary import (
    build_network_policy,
    build_policies_result,
    not_installed_policies_result,
)


class TestBuildNetworkPolicy:
    def test_extracts_selector_and_rules(self) -> None:
        raw = {
            "metadata": {"name": "allow-db", "namespace": "payments"},
            "spec": {
                "endpointSelector": {"matchLabels": {"app": "db"}},
                "ingress": [{"fromEndpoints": [{"matchLabels": {"app": "web"}}]}],
                "egress": [{"toPorts": [{"ports": [{"port": "5432"}]}]}],
            },
        }

        policy = build_network_policy("CiliumNetworkPolicy", raw)

        assert policy.kind == "CiliumNetworkPolicy"
        assert policy.name == "allow-db"
        assert policy.namespace == "payments"
        assert policy.endpoint_selector == "matchLabels: app=db"
        assert policy.ingress_rule_count == 1  # noqa: PLR2004
        assert policy.egress_rule_count == 1  # noqa: PLR2004
        assert policy.l7_rule_count == 0
        assert policy.l7_protocols == ()

    def test_counts_l7_rules_and_protocols(self) -> None:
        raw = {
            "metadata": {"name": "l7-policy"},
            "spec": {
                "ingress": [
                    {
                        "toPorts": [
                            {
                                "ports": [{"port": "443", "protocol": "TCP"}],
                                "rules": {"http": {"methods": ["GET"]}},
                            }
                        ]
                    }
                ],
                "egress": [
                    {
                        "toPorts": [
                            {"rules": {"dns": {"patterns": ["example.com"]}}},
                            {"rules": {"l7": [{"match": "GET"}]}},
                        ]
                    }
                ],
            },
        }

        policy = build_network_policy("CiliumNetworkPolicy", raw)

        assert policy.l7_rule_count == 3  # noqa: PLR2004
        assert policy.l7_protocols == ("dns", "http", "l7")

    def test_preserves_malformed_selector_as_is(self) -> None:
        raw = {
            "metadata": {"name": "odd"},
            "spec": {"endpointSelector": "not-a-map"},
        }

        policy = build_network_policy("CiliumClusterwideNetworkPolicy", raw)

        assert policy.endpoint_selector == "not-a-map"
        assert policy.namespace is None

    def test_empty_selector_rendered_empty(self) -> None:
        raw = {"metadata": {"name": "broad"}, "spec": {}}

        policy = build_network_policy("CiliumNetworkPolicy", raw)

        assert policy.endpoint_selector == "matchLabels: {}"

    def test_empty_selector_dict_rendered_empty(self) -> None:
        raw = {
            "metadata": {"name": "broad"},
            "spec": {"endpointSelector": {"matchLabels": {}}},
        }

        policy = build_network_policy("CiliumNetworkPolicy", raw)

        assert policy.endpoint_selector == "matchLabels: {}"

    def test_l7_summary_skips_malformed_entries(self) -> None:
        raw = {
            "metadata": {"name": "mixed"},
            "spec": {
                "ingress": [
                    "not-a-dict",
                    {"toPorts": "not-a-list"},
                    {"toPorts": ["not-a-dict"]},
                ],
                "egress": [{"toPorts": [{"rules": {"http": {}}}]}],
            },
        }

        policy = build_network_policy("CiliumNetworkPolicy", raw)

        assert policy.ingress_rule_count == 3  # noqa: PLR2004
        assert policy.l7_rule_count == 1  # noqa: PLR2004
        assert policy.l7_protocols == ("http",)


class TestBuildPoliciesResult:
    def test_present_with_kind_breakdown(self) -> None:
        namespaced = build_network_policy(
            "CiliumNetworkPolicy",
            {"metadata": {"name": "a", "namespace": "ns"}, "spec": {}},
        )
        clusterwide = build_network_policy(
            "CiliumClusterwideNetworkPolicy", {"metadata": {"name": "g"}, "spec": {}}
        )

        result = build_policies_result([namespaced, clusterwide])

        assert result.installed is True
        assert result.status == "present"
        assert result.total_policies == 2  # noqa: PLR2004
        assert result.namespaced_count == 1  # noqa: PLR2004
        assert result.clusterwide_count == 1  # noqa: PLR2004

    def test_empty_is_honest(self) -> None:
        result = build_policies_result([])

        assert result.installed is True
        assert result.status == "empty"
        assert result.total_policies == 0
        assert result.note is not None


class TestNotInstalledPoliciesResult:
    def test_returns_not_installed_marker(self) -> None:
        result = not_installed_policies_result()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.policies == []
        assert result.note is not None
