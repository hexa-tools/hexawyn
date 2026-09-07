from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumNetworkPoliciesResult,
)
from hexawyn.domain.services.cilium.network_policy_summary import (
    _extract_endpoint_labels,
    _l7_summary,
    _render_selector,
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

    def test_malformed_match_labels_unknown(self) -> None:
        raw = {
            "metadata": {"name": "odd"},
            "spec": {"endpointSelector": {"matchLabels": "not-a-map"}},
        }

        policy = build_network_policy("CiliumNetworkPolicy", raw)

        assert policy.endpoint_selector == "matchLabels: {}"
        assert policy.endpoint_labels is None

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

    def test_selector_without_match_labels_matches_all(self) -> None:
        raw = {
            "metadata": {"name": "broad"},
            "spec": {"endpointSelector": {}},
        }

        policy = build_network_policy("CiliumNetworkPolicy", raw)

        assert policy.endpoint_selector == "matchLabels: {}"
        assert policy.endpoint_labels == ()

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

    def test_missing_metadata_name_defaults_empty(self) -> None:
        policy = build_network_policy("CiliumNetworkPolicy", {"spec": {}})

        assert policy.name == ""

    def test_endpoint_labels_extracted_sorted(self) -> None:
        raw = {
            "metadata": {"name": "sel"},
            "spec": {"endpointSelector": {"matchLabels": {"z": "1", "a": "2"}}},
        }

        policy = build_network_policy("CiliumNetworkPolicy", raw)

        assert policy.endpoint_labels == (("a", "2"), ("z", "1"))


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

    def test_present_exact_result(self) -> None:
        namespaced = build_network_policy(
            "CiliumNetworkPolicy",
            {"metadata": {"name": "a", "namespace": "ns"}, "spec": {}},
        )
        clusterwide = build_network_policy(
            "CiliumClusterwideNetworkPolicy", {"metadata": {"name": "g"}, "spec": {}}
        )

        result = build_policies_result([namespaced, clusterwide])

        assert isinstance(result, CiliumNetworkPoliciesResult)
        assert result == CiliumNetworkPoliciesResult(
            installed=True,
            status="present",
            total_policies=2,  # noqa: PLR2004
            namespaced_count=1,  # noqa: PLR2004
            clusterwide_count=1,  # noqa: PLR2004
            policies=[namespaced, clusterwide],
            note=None,
        )

    def test_unknown_kind_counts_nowhere(self) -> None:
        unknown = build_network_policy("SomeOtherKind", {"metadata": {"name": "x"}, "spec": {}})

        result = build_policies_result([unknown])

        assert result.namespaced_count == 0
        assert result.clusterwide_count == 0

    def test_empty_is_honest(self) -> None:
        result = build_policies_result([])

        assert result.installed is True
        assert result.status == "empty"
        assert result.total_policies == 0
        assert result.note is not None

    def test_empty_exact_result(self) -> None:
        result = build_policies_result([])

        assert result == CiliumNetworkPoliciesResult(
            installed=True,
            status="empty",
            total_policies=0,
            namespaced_count=0,
            clusterwide_count=0,
            policies=[],
            note="No Cilium network policies found",
        )


class TestNotInstalledPoliciesResult:
    def test_returns_not_installed_marker(self) -> None:
        result = not_installed_policies_result()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.policies == []
        assert result.note is not None

    def test_exact_dataclass(self) -> None:
        result = not_installed_policies_result()

        assert result == CiliumNetworkPoliciesResult(
            installed=False,
            status="not_installed",
            total_policies=0,
            namespaced_count=0,
            clusterwide_count=0,
            policies=[],
            note="Cilium is not installed in this cluster",
        )


class TestExtractEndpointLabelsDirect:
    def test_none_selector_returns_empty(self) -> None:
        assert _extract_endpoint_labels(None) == ()

    def test_non_dict_selector_returns_none(self) -> None:
        assert _extract_endpoint_labels("raw") is None

    def test_missing_match_labels_returns_empty(self) -> None:
        assert _extract_endpoint_labels({}) == ()

    def test_non_dict_match_labels_returns_none(self) -> None:
        assert _extract_endpoint_labels({"matchLabels": "raw"}) is None

    def test_values_stringified(self) -> None:
        assert _extract_endpoint_labels({"matchLabels": {"a": 1}}) == (("a", "1"),)

    def test_keys_stringified(self) -> None:
        assert _extract_endpoint_labels({"matchLabels": {1: "b"}}) == (("1", "b"),)

    def test_sorted_multiple(self) -> None:
        assert _extract_endpoint_labels({"matchLabels": {"b": "2", "a": "1"}}) == (
            ("a", "1"),
            ("b", "2"),
        )


class TestRenderSelectorDirect:
    def test_multiple_labels_sorted(self) -> None:
        assert _render_selector({"matchLabels": {"z": "1", "a": "2"}}) == ("matchLabels: a=2, z=1")


class TestL7SummaryDirect:
    def test_counts_and_sorts_protocols(self) -> None:
        count, protocols = _l7_summary(
            [
                {"toPorts": [{"rules": {"http": {}}}, {"rules": {"dns": {}}}]},
                {"toPorts": [{"rules": {"http": {}, "kafka": {}}}]},
            ],
            [],
        )

        assert count == 3  # noqa: PLR2004
        assert protocols == ("dns", "http", "kafka")

    def test_malformed_rule_in_middle_is_skipped_not_breaking(self) -> None:
        count, protocols = _l7_summary(
            [
                {"toPorts": [{"rules": {"http": {}}}]},
                "not-a-dict",
                {"toPorts": [{"rules": {"dns": {}}}]},
            ],
            [],
        )

        assert count == 2  # noqa: PLR2004
        assert protocols == ("dns", "http")

    def test_malformed_port_in_middle_is_skipped_not_breaking(self) -> None:
        count, protocols = _l7_summary(
            [
                {
                    "toPorts": [
                        {"rules": {"http": {}}},
                        "not-a-dict",
                        {"rules": {"dns": {}}},
                    ]
                }
            ],
            [],
        )

        assert count == 2  # noqa: PLR2004
        assert protocols == ("dns", "http")

    def test_empty_rules_port_not_counted(self) -> None:
        count, protocols = _l7_summary(
            [{"toPorts": [{"rules": {}}, {"rules": {"http": {}}}]}],
            [],
        )

        assert count == 1  # noqa: PLR2004
        assert protocols == ("http",)

    def test_empty_inputs(self) -> None:
        assert _l7_summary([], []) == (0, ())
