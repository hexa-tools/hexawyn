from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumL7RuleSummary,
    CiliumNetworkPolicyDetail,
    CiliumRuleSummary,
)
from hexawyn.domain.services.cilium.policy_detail_builder import (
    _collect_l7_protocols,
    _render_entity,
    _render_l7,
    _render_match,
    _render_ports,
    _render_selector,
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

    def test_exact_dataclass(self) -> None:
        detail = not_installed_policy_detail()

        assert detail == CiliumNetworkPolicyDetail(
            installed=False,
            status="not_installed",
            kind="",
            name="",
            namespace=None,
            endpoint_selector="",
            ingress_rules=(),
            egress_rules=(),
            l7_protocols=(),
            spec={},
            note="Cilium is not installed in this cluster",
        )


class TestBuildPolicyDetailExact:
    def test_exact_full_result(self) -> None:
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
            },
        }

        detail = build_policy_detail("CiliumNetworkPolicy", "payments", raw)

        assert isinstance(detail, CiliumNetworkPolicyDetail)
        assert detail == CiliumNetworkPolicyDetail(
            installed=True,
            status="ok",
            kind="CiliumNetworkPolicy",
            name="allow-db",
            namespace="payments",
            endpoint_selector="matchLabels: app=db",
            ingress_rules=(
                CiliumRuleSummary(
                    direction="ingress",
                    endpoints=("matchLabels: app=web",),
                    ports=("443/TCP",),
                    l7=(
                        CiliumL7RuleSummary(
                            protocol="http",
                            match=("methods=['GET']",),
                        ),
                    ),
                ),
            ),
            egress_rules=(),
            l7_protocols=("http",),
            spec=raw["spec"],
            note=None,
        )

    def test_missing_metadata_and_spec_defaults(self) -> None:
        detail = build_policy_detail("CiliumNetworkPolicy", "ns", {})

        assert detail.name == ""
        assert detail.endpoint_selector == "matchLabels: {}"
        assert detail.ingress_rules == ()
        assert detail.egress_rules == ()
        assert detail.spec == {}

    def test_egress_rule_direction_labeled_egress(self) -> None:
        raw = {
            "metadata": {"name": "out"},
            "spec": {
                "egress": [
                    {"toEndpoints": [{"matchLabels": {"app": "cache"}}]},
                ],
            },
        }

        detail = build_policy_detail("CiliumNetworkPolicy", "ns", raw)

        assert len(detail.egress_rules) == 1  # noqa: PLR2004
        assert detail.egress_rules[0].direction == "egress"
        assert detail.ingress_rules == ()

    def test_ingress_rule_direction_labeled_ingress(self) -> None:
        raw = {
            "metadata": {"name": "in"},
            "spec": {
                "ingress": [
                    {"fromEndpoints": [{"matchLabels": {"app": "web"}}]},
                ],
            },
        }

        detail = build_policy_detail("CiliumNetworkPolicy", "ns", raw)

        assert len(detail.ingress_rules) == 1  # noqa: PLR2004
        assert detail.ingress_rules[0].direction == "ingress"
        assert detail.egress_rules == ()


class TestRenderSelectorDirect:
    def test_multiple_match_labels_sorted(self) -> None:
        assert _render_selector({"matchLabels": {"z": "1", "a": "2", "m": "3"}}) == (
            "matchLabels: a=2, m=3, z=1"
        )

    def test_non_dict_match_labels_is_empty(self) -> None:
        assert _render_selector({"matchLabels": "not-a-dict"}) == "matchLabels: {}"

    def test_none_selector(self) -> None:
        assert _render_selector(None) == "matchLabels: {}"


class TestRenderEntityDirect:
    def test_empty_match_labels_dict_falls_back_to_string(self) -> None:
        assert _render_entity({"matchLabels": {}}) == "{'matchLabels': {}}"

    def test_multiple_labels_sorted(self) -> None:
        assert _render_entity({"matchLabels": {"z": "1", "a": "2"}}) == "matchLabels: a=2, z=1"

    def test_non_dict_item_returns_string(self) -> None:
        assert _render_entity("raw-entity") == "raw-entity"


class TestRenderPortsDirect:
    def test_non_dict_to_port_is_skipped_but_later_kept(self) -> None:
        result = _render_ports(
            {
                "toPorts": [
                    "not-a-port",
                    {"ports": [{"port": "443", "protocol": "TCP"}]},
                    {"ports": [{"port": "8080"}]},
                ]
            }
        )

        assert result == ("443/TCP", "8080")

    def test_port_without_protocol_renders_port_only(self) -> None:
        assert _render_ports({"toPorts": [{"ports": [{"port": "6379"}]}]}) == ("6379",)

    def test_zero_port_is_kept(self) -> None:
        assert _render_ports({"toPorts": [{"ports": [{"port": 0}]}]}) == ("0",)

    def test_empty_ports(self) -> None:
        assert _render_ports({}) == ()


class TestRenderL7Direct:
    def test_multiple_protocols_with_matches(self) -> None:
        result = _render_l7(
            {
                "toPorts": [
                    {
                        "rules": {
                            "http": {"methods": ["GET", "POST"]},
                            "dns": "resolve",
                        }
                    }
                ]
            }
        )

        assert result == (
            CiliumL7RuleSummary(protocol="http", match=("methods=['GET', 'POST']",)),
            CiliumL7RuleSummary(protocol="dns", match=("resolve",)),
        )

    def test_non_dict_to_port_and_empty_rules_skipped(self) -> None:
        result = _render_l7(
            {
                "toPorts": [
                    "not-a-port",
                    {"ports": []},
                    {"rules": {}},
                    {"rules": {"http": ["GET"]}},
                ]
            }
        )

        assert result == (CiliumL7RuleSummary(protocol="http", match=("GET",)),)

    def test_rules_after_empty_rules_are_kept(self) -> None:
        result = _render_l7(
            {
                "toPorts": [
                    {"rules": {}},
                    {"rules": {"http": ["GET"]}},
                ]
            }
        )

        assert result == (CiliumL7RuleSummary(protocol="http", match=("GET",)),)

    def test_non_dict_non_empty_rules_are_skipped(self) -> None:
        result = _render_l7({"toPorts": [{"rules": "not-a-dict"}]})

        assert result == ()


class TestCollectL7Protocols:
    def test_sorted_unique_protocols(self) -> None:
        rules = (
            CiliumRuleSummary(
                direction="ingress",
                endpoints=(),
                ports=(),
                l7=(
                    CiliumL7RuleSummary(protocol="http", match=()),
                    CiliumL7RuleSummary(protocol="kafka", match=()),
                ),
            ),
            CiliumRuleSummary(
                direction="egress",
                endpoints=(),
                ports=(),
                l7=(CiliumL7RuleSummary(protocol="dns", match=()),),
            ),
        )

        assert _collect_l7_protocols(rules) == ("dns", "http", "kafka")

    def test_empty_rules(self) -> None:
        assert _collect_l7_protocols(()) == ()


class TestRenderMatchDirect:
    def test_list_items_stringified(self) -> None:
        assert _render_match(["GET", 42]) == ("GET", "42")

    def test_dict_keys_sorted(self) -> None:
        assert _render_match({"z": "1", "a": "2"}) == ("a=2", "z=1")

    def test_scalar_wrapped(self) -> None:
        assert _render_match("plain") == ("plain",)
