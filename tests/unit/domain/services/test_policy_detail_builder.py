from __future__ import annotations

from hexawyn.domain.services.cilium.policy_detail_builder import (
    _summarize_rule,
    build_policy_detail,
    not_installed_policy_detail,
)


class TestBuildPolicyDetail:
    def test_builds_full_spec_with_summaries(self) -> None:
        raw = {
            "metadata": {"name": "allow-db"},
            "spec": {
                "endpointSelector": {"matchLabels": {"app": "db"}},
                "ingress": [
                    {
                        "fromEndpoints": [{"matchLabels": {"app": "web"}}],
                        "toPorts": [
                            {
                                "ports": [{"port": "443", "protocol": "TCP"}],
                                "rules": {"http": {"methods": ["GET"]}},
                            }
                        ],
                    }
                ],
                "egress": [
                    {
                        "toEndpoints": [{"matchLabels": {"app": "cache"}}],
                        "toPorts": [{"ports": [{"port": "6379"}]}],
                    }
                ],
            },
        }

        detail = build_policy_detail("CiliumNetworkPolicy", "payments", raw)

        assert detail.installed is True
        assert detail.status == "ok"
        assert detail.kind == "CiliumNetworkPolicy"
        assert detail.namespace == "payments"
        assert detail.endpoint_selector == "matchLabels: app=db"
        assert detail.ingress_rules[0].endpoints == ("matchLabels: app=web",)
        assert detail.ingress_rules[0].ports == ("443/TCP",)
        assert detail.ingress_rules[0].l7[0].protocol == "http"
        assert detail.l7_protocols == ("http",)
        assert detail.spec["endpointSelector"] == {"matchLabels": {"app": "db"}}

    def test_extracts_l7_protocols_from_both_directions(self) -> None:
        raw = {
            "metadata": {"name": "l7"},
            "spec": {
                "ingress": [
                    {"toPorts": [{"rules": {"http": {}}}]},
                ],
                "egress": [
                    {"toPorts": [{"rules": {"dns": {}}}]},
                    {"toPorts": [{"rules": {"kafka": {}}}]},
                ],
            },
        }

        detail = build_policy_detail("CiliumNetworkPolicy", "ns", raw)

        assert detail.l7_protocols == ("dns", "http", "kafka")

    def test_empty_spec_reported_empty(self) -> None:
        raw = {"metadata": {"name": "empty"}, "spec": {}}

        detail = build_policy_detail("CiliumNetworkPolicy", "ns", raw)

        assert detail.spec == {}
        assert detail.endpoint_selector == "matchLabels: {}"
        assert detail.ingress_rules == ()
        assert detail.egress_rules == ()

    def test_malformed_rule_preserved_in_spec(self) -> None:
        raw = {"metadata": {"name": "odd"}, "spec": {"ingress": ["not-a-rule"]}}

        detail = build_policy_detail("CiliumNetworkPolicy", "ns", raw)

        assert detail.ingress_rules == ()
        assert detail.spec["ingress"] == ["not-a-rule"]

    def test_clusterwide_has_no_namespace(self) -> None:
        raw = {"metadata": {"name": "global"}, "spec": {}}

        detail = build_policy_detail("CiliumClusterwideNetworkPolicy", None, raw)

        assert detail.namespace is None
        assert detail.kind == "CiliumClusterwideNetworkPolicy"

    def test_renders_selector_and_entity_variants(self) -> None:
        raw = {
            "metadata": {"name": "variants"},
            "spec": {
                "endpointSelector": "not-a-map",
                "ingress": [
                    {"fromEndpoints": [{"notLabels": 1}, "a-string"]},
                    {"toPorts": ["not-a-port"]},
                    {"toPorts": [{"rules": {"http": ["GET"], "kafka": "read"}}]},
                ],
            },
        }

        detail = build_policy_detail("CiliumNetworkPolicy", "ns", raw)

        assert detail.endpoint_selector == "not-a-map"
        assert detail.ingress_rules[0].endpoints == ("{'notLabels': 1}", "a-string")
        assert detail.ingress_rules[1].ports == ()
        assert detail.ingress_rules[1].l7 == ()
        assert detail.ingress_rules[2].l7[0].protocol == "http"
        assert detail.ingress_rules[2].l7[0].match == ("GET",)
        assert detail.ingress_rules[2].l7[1].protocol == "kafka"
        assert detail.ingress_rules[2].l7[1].match == ("read",)

    def test_summarize_rule_handles_non_dict(self) -> None:
        rule = _summarize_rule("ingress", "not-a-rule")
        assert rule.direction == "ingress"
        assert rule.endpoints == ()
        assert rule.ports == ()
        assert rule.l7 == ()

    def test_endpoint_selector_empty_match_labels(self) -> None:
        raw = {
            "metadata": {"name": "broad"},
            "spec": {"endpointSelector": {"matchLabels": {}}},
        }

        detail = build_policy_detail("CiliumNetworkPolicy", "ns", raw)

        assert detail.endpoint_selector == "matchLabels: {}"


class TestNotInstalledPolicyDetail:
    def test_returns_marker(self) -> None:
        detail = not_installed_policy_detail()
        assert detail.installed is False
        assert detail.status == "not_installed"
        assert detail.spec == {}
        assert detail.name == ""
        assert detail.note is not None
