"""Tests for domain/services/calico/network_policy_service — rule extraction."""

from __future__ import annotations

from hexawyn.domain.services.calico.network_policy_service import (
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
        assert policy.namespace == "ns"
        assert policy.selector == "app == 'web'"
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
        assert policy.namespace == ""
        assert policy.selector == "all()"
        assert policy.action == "allow"


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
