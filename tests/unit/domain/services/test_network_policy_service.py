"""Tests for domain/services/calico/network_policy_service — rule extraction."""

from __future__ import annotations

from hexawyn.domain.services.calico.network_policy_service import (
    _has_l7,
    _order,
    _rules,
    _summarize_rule,
    parse_calico_network_policy,
    parse_global_network_policy,
    resolve_action,
)


class TestParseCalicoNetworkPolicy:
    def test_namespaced_policy_with_rules(self) -> None:
        item = {
            "metadata": {"name": "np", "namespace": "ns"},
            "spec": {
                "selector": "app == 'web'",
                "order": 50.0,
                "ingress": [
                    {"action": "Allow", "protocol": "TCP", "destination": {"ports": ["80"]}},
                    {"action": "Deny"},
                ],
                "egress": [{"action": "Allow"}],
                "applyOnForward": True,
            },
        }
        policy = parse_calico_network_policy(item)
        assert policy.kind == "CalicoNetworkPolicy"
        assert policy.name == "np"
        assert policy.namespace == "ns"
        assert policy.selector == "app == 'web'"
        assert policy.order == 50.0  # noqa: PLR2004
        assert policy.action == "mixed"
        assert policy.ingress_rule_count == 2  # noqa: PLR2004
        assert policy.egress_rule_count == 1  # noqa: PLR2004
        assert policy.ingress_rules[0] == "allow tcp 80"
        assert policy.apply_on_forward is True

    def test_empty_rules(self) -> None:
        policy = parse_calico_network_policy({"metadata": {"name": "np"}, "spec": {}})
        assert policy.action is None
        assert policy.ingress_rules == ()
        assert policy.ingress_rule_count == 0

    def test_non_list_rules_safe(self) -> None:
        policy = parse_calico_network_policy(
            {"metadata": {"name": "np"}, "spec": {"ingress": "nope", "egress": None}}
        )
        assert policy.ingress_rule_count == 0
        assert policy.egress_rule_count == 0

    def test_malformed_selector_preserved(self) -> None:
        policy = parse_calico_network_policy(
            {"metadata": {"name": "np"}, "spec": {"selector": "--- broken"}}
        )
        assert policy.selector == "--- broken"

    def test_unknown_action_preserved(self) -> None:
        policy = parse_calico_network_policy(
            {
                "metadata": {"name": "np"},
                "spec": {"ingress": [{"action": "Log"}]},
            }
        )
        assert policy.action == "log"

    def test_non_numeric_order_falls_back_zero(self) -> None:
        policy = parse_calico_network_policy(
            {"metadata": {"name": "np"}, "spec": {"order": "not-a-number"}}
        )
        assert policy.order == 0.0


class TestParseGlobalNetworkPolicy:
    def test_global_kind_and_empty_namespace(self) -> None:
        policy = parse_global_network_policy(
            {
                "metadata": {"name": "g-np"},
                "spec": {"selector": "all()", "ingress": [{"action": "Allow"}]},
            }
        )
        assert policy.kind == "GlobalNetworkPolicy"
        assert policy.name == "g-np"
        assert policy.namespace == ""
        assert policy.selector == "all()"
        assert policy.action == "allow"
        assert policy.ingress_rule_count == 1  # noqa: PLR2004
        assert policy.egress_rule_count == 0
        assert policy.ingress_rules == ("allow",)

    def test_full_payload_all_fields(self) -> None:
        # payload riche: tous les champs doivent etre correctement derives
        policy = parse_global_network_policy(
            {
                "metadata": {"name": "g-full", "namespace": "ignored"},
                "spec": {
                    "selector": "app == 'x'",
                    "order": 30.0,
                    "applyOnForward": True,
                    "ingress": [
                        {"action": "Allow", "protocol": "TCP", "destination": {"ports": ["80"]}},
                        {"action": "Deny", "http": {"methods": ["GET"]}},
                    ],
                    "egress": [
                        {"action": "Allow", "protocol": "UDP", "destination": {"port": "53"}}
                    ],
                },
            }
        )
        assert policy.kind == "GlobalNetworkPolicy"
        assert policy.name == "g-full"
        assert policy.namespace == ""
        assert policy.selector == "app == 'x'"
        assert policy.order == 30.0  # noqa: PLR2004
        assert policy.ingress_rule_count == 2  # noqa: PLR2004
        assert policy.egress_rule_count == 1  # noqa: PLR2004
        assert policy.ingress_rules == ("allow tcp 80", "deny")
        assert policy.egress_rules == ("allow udp 53",)
        assert policy.action == "mixed"
        assert policy.apply_on_forward is True
        assert policy.has_l7_rule is True

    def test_no_apply_on_forward_defaults_false(self) -> None:
        policy = parse_global_network_policy(
            {"metadata": {"name": "g"}, "spec": {"ingress": [{"action": "Allow"}]}}
        )
        assert policy.apply_on_forward is False
        assert policy.has_l7_rule is False

    def test_l7_rule_detected(self) -> None:
        policy = parse_global_network_policy(
            {
                "metadata": {"name": "g"},
                "spec": {"ingress": [{"action": "Allow", "http": {"methods": ["GET"]}}]},
            }
        )
        assert policy.has_l7_rule is True

    def test_apply_on_forward_default_false(self) -> None:
        policy = parse_global_network_policy({"metadata": {"name": "g"}, "spec": {}})
        assert policy.apply_on_forward is False


class TestParseCalicoNetworkPolicyFull:
    def test_all_fields_derived(self) -> None:
        policy = parse_calico_network_policy(
            {
                "metadata": {"name": "c-full", "namespace": "team-x"},
                "spec": {
                    "selector": "app == 'web'",
                    "order": 10.0,
                    "applyOnForward": True,
                    "ingress": [
                        {"action": "Allow", "protocol": "TCP", "destination": {"ports": ["443"]}},
                        {"action": "Deny", "tls": {"sni": "x"}},
                    ],
                    "egress": [{"action": "Log"}],
                },
            }
        )
        assert policy.kind == "CalicoNetworkPolicy"
        assert policy.name == "c-full"
        assert policy.namespace == "team-x"
        assert policy.selector == "app == 'web'"
        assert policy.order == 10.0  # noqa: PLR2004
        assert policy.ingress_rule_count == 2  # noqa: PLR2004
        assert policy.egress_rule_count == 1  # noqa: PLR2004
        assert policy.ingress_rules == ("allow tcp 443", "deny")
        assert policy.egress_rules == ("log",)
        assert policy.action == "mixed"
        assert policy.apply_on_forward is True
        assert policy.has_l7_rule is True


class TestResolveAction:
    def test_none(self) -> None:
        assert resolve_action([], []) is None

    def test_all_allow(self) -> None:
        assert resolve_action([{"action": "Allow"}], [{"action": "Allow"}]) == "allow"

    def test_all_deny(self) -> None:
        assert resolve_action([{"action": "Deny"}], []) == "deny"

    def test_mixed(self) -> None:
        result = resolve_action([{"action": "Allow"}], [{"action": "Deny"}])
        assert result == "mixed"

    def test_unknown_single_preserved(self) -> None:
        assert resolve_action([{"action": "Log"}], []) == "log"


class TestSummarizeRule:
    def test_allow_tcp_single_port(self) -> None:
        result = _summarize_rule(
            {"action": "Allow", "protocol": "TCP", "destination": {"ports": ["80"]}}
        )
        assert result == "allow tcp 80"

    def test_allow_tcp_port_list_joined(self) -> None:
        result = _summarize_rule(
            {"action": "Allow", "protocol": "TCP", "destination": {"ports": ["80", "443"]}}
        )
        assert result == "allow tcp 80,443"

    def test_single_port_field(self) -> None:
        result = _summarize_rule(
            {"action": "Allow", "protocol": "UDP", "destination": {"port": "53"}}
        )
        assert result == "allow udp 53"

    def test_no_protocol_skips_port_section(self) -> None:
        result = _summarize_rule({"action": "Deny", "destination": {"ports": ["80"]}})
        assert result == "deny 80"

    def test_no_ports(self) -> None:
        result = _summarize_rule({"action": "Allow"})
        assert result == "allow"

    def test_default_action_allow_when_missing(self) -> None:
        result = _summarize_rule({"destination": {"ports": ["80"]}})
        assert result == "allow 80"

    def test_ports_precedence_over_port(self) -> None:
        result = _summarize_rule(
            {"action": "Allow", "destination": {"ports": ["80"], "port": "53"}}
        )
        assert result == "allow 80"


class TestHasL7:
    def test_http_rule(self) -> None:
        assert _has_l7([{"http": {}}]) is True

    def test_tls_rule(self) -> None:
        assert _has_l7([{"tls": {}}]) is True

    def test_no_l7(self) -> None:
        assert _has_l7([{"action": "Allow", "protocol": "TCP"}]) is False

    def test_mixed_rules_finds_l7(self) -> None:
        assert _has_l7([{"action": "Allow"}, {"http": {}}]) is True


class TestOrder:
    def test_numeric_order(self) -> None:
        assert _order({"order": 50.0}) == 50.0  # noqa: PLR2004

    def test_numeric_string_order(self) -> None:
        assert _order({"order": "10"}) == 10.0  # noqa: PLR2004

    def test_invalid_order_falls_back_zero(self) -> None:
        assert _order({"order": "abc"}) == 0.0

    def test_missing_order_defaults_zero(self) -> None:
        assert _order({}) == 0.0


class TestRules:
    def test_filters_non_dicts(self) -> None:
        assert _rules([{"action": "Allow"}, "x", None, 42]) == [{"action": "Allow"}]

    def test_non_list_returns_empty(self) -> None:
        assert _rules("nope") == []
        assert _rules(None) == []


class TestParseGlobalL7AndDefaults:
    def test_l7_rule_detected_extra(self) -> None:
        policy = parse_global_network_policy(
            {
                "metadata": {"name": "g"},
                "spec": {"ingress": [{"action": "Allow", "http": {"methods": ["GET"]}}]},
            }
        )
        assert policy.has_l7_rule is True
        assert policy.ingress_rule_count == 1  # noqa: PLR2004

    def test_apply_on_forward_default_false_extra(self) -> None:
        policy = parse_global_network_policy({"metadata": {"name": "g"}, "spec": {}})
        assert policy.apply_on_forward is False


class TestParseGlobalNamespaceIgnored:
    def test_global_ignores_meta_namespace(self) -> None:
        # GlobalNetworkPolicy est cluster-scope : le namespace du metadata est ignore
        # mutant _use_meta_namespace=True le propagerait dans le modele
        policy = parse_global_network_policy(
            {
                "metadata": {"name": "g", "namespace": "should-be-empty"},
                "spec": {"ingress": [{"action": "Allow"}]},
            }
        )
        assert policy.kind == "GlobalNetworkPolicy"
        assert policy.namespace == ""
        assert policy.name == "g"


class TestParseEmptyPayloadDefaults:
    def test_calico_empty_payload_all_defaults(self) -> None:
        # aucun champ -> tous les defaults (kills get(...,None)/XXXX/True)
        policy = parse_calico_network_policy({})
        assert policy.name == ""
        assert policy.namespace == ""
        assert policy.selector == ""
        assert policy.order == 0.0
        assert policy.apply_on_forward is False
        assert policy.ingress_rule_count == 0  # noqa: PLR2004
        assert policy.egress_rule_count == 0  # noqa: PLR2004
        assert policy.ingress_rules == ()
        assert policy.action is None

    def test_global_empty_payload_all_defaults(self) -> None:
        policy = parse_global_network_policy({})
        assert policy.name == ""
        assert policy.namespace == ""
        assert policy.selector == ""
        assert policy.kind == "GlobalNetworkPolicy"
        assert policy.apply_on_forward is False
