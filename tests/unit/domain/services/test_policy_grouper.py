from __future__ import annotations

from hexawyn.application.ports.driven.network_policy_audit_port import NetworkPolicyRaw


def _make_policy(
    name: str = "default-deny",
    namespace: str = "default",
    ingress_rule_count: int = 0,
    egress_rule_count: int = 0,
    has_empty_pod_selector: bool = False,
) -> NetworkPolicyRaw:
    return {
        "name": name,
        "namespace": namespace,
        "ingress_rule_count": ingress_rule_count,
        "egress_rule_count": egress_rule_count,
        "has_empty_pod_selector": has_empty_pod_selector,
    }


class TestGroupPoliciesByNamespace:
    def test_happy_path_groups_policies(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import (
            group_policies_by_namespace,
        )

        policies: list[NetworkPolicyRaw] = [
            _make_policy("allow-http", "default", ingress_rule_count=1),
            _make_policy("deny-all", "default", ingress_rule_count=0),
            _make_policy("allow-db", "production", ingress_rule_count=2),
        ]

        result = group_policies_by_namespace(policies)

        assert len(result["default"]) == 2  # noqa: PLR2004
        assert len(result["production"]) == 1

    def test_empty_policies_returns_empty_dict(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import (
            group_policies_by_namespace,
        )

        result = group_policies_by_namespace([])

        assert result == {}

    def test_single_policy_returns_single_namespace_group(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import (
            group_policies_by_namespace,
        )

        policies: list[NetworkPolicyRaw] = [_make_policy()]

        result = group_policies_by_namespace(policies)

        assert len(result) == 1
        assert len(result["default"]) == 1

    def test_multiple_namespaces_grouped_correctly(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import (
            group_policies_by_namespace,
        )

        policies: list[NetworkPolicyRaw] = [
            _make_policy(f"policy-{i}", f"ns-{i}") for i in range(5)
        ]

        result = group_policies_by_namespace(policies)

        assert len(result) == 5  # noqa: PLR2004


class TestBuildNote:
    def test_restricted_status_no_note(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        result = build_note(
            has_calico=False,
            has_istio_strict=False,
            network_status="restricted",
            ns_policies=[],
        )

        assert result is None

    def test_calico_note_when_not_restricted(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        result = build_note(
            has_calico=True,
            has_istio_strict=False,
            network_status="open",
            ns_policies=[],
        )

        assert result is not None
        assert "Calico" in result

    def test_istio_note_when_not_restricted(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        result = build_note(
            has_calico=False,
            has_istio_strict=True,
            network_status="partially_restricted",
            ns_policies=[],
        )

        assert result is not None
        assert "Istio" in result

    def test_both_calico_and_istio(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        result = build_note(
            has_calico=True,
            has_istio_strict=True,
            network_status="open",
            ns_policies=[],
        )

        assert result is not None
        assert "Calico" in result
        assert "Istio" in result

    def test_broad_policy_note(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        policies: list[NetworkPolicyRaw] = [
            _make_policy(
                "broad-1",
                has_empty_pod_selector=True,
                ingress_rule_count=1,
            ),
            _make_policy(
                "broad-2",
                has_empty_pod_selector=True,
                egress_rule_count=1,
            ),
        ]

        result = build_note(
            has_calico=False,
            has_istio_strict=False,
            network_status="open",
            ns_policies=policies,
        )

        assert result is not None
        assert "2 polic(ies)" in result
        assert "empty podSelector" in result

    def test_empty_pod_selector_with_zero_rules_not_counted(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        policies: list[NetworkPolicyRaw] = [
            _make_policy(
                "empty-no-rules",
                has_empty_pod_selector=True,
                ingress_rule_count=0,
                egress_rule_count=0,
            ),
        ]

        result = build_note(
            has_calico=False,
            has_istio_strict=False,
            network_status="open",
            ns_policies=policies,
        )

        assert result is None

    def test_mixed_notes_combined(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        policies: list[NetworkPolicyRaw] = [
            _make_policy(
                "broad",
                has_empty_pod_selector=True,
                ingress_rule_count=3,
            ),
        ]

        result = build_note(
            has_calico=True,
            has_istio_strict=False,
            network_status="open",
            ns_policies=policies,
        )

        assert result is not None
        assert "Calico" in result
        assert "1 polic" in result

    def test_no_broad_policies_no_calico_no_istio_returns_none(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        result = build_note(
            has_calico=False,
            has_istio_strict=False,
            network_status="open",
            ns_policies=[],
        )

        assert result is None

    def test_policies_with_non_empty_selector_not_counted(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        policies: list[NetworkPolicyRaw] = [
            _make_policy(
                "targeted",
                has_empty_pod_selector=False,
                ingress_rule_count=5,
            ),
        ]

        result = build_note(
            has_calico=False,
            has_istio_strict=False,
            network_status="open",
            ns_policies=policies,
        )

        assert result is None

    def test_policies_with_empty_selector_has_rules_is_broad(self) -> None:
        from hexawyn.domain.services.network_policy.policy_grouper import build_note

        policies: list[NetworkPolicyRaw] = [
            _make_policy(
                "broad-but-has-egress",
                has_empty_pod_selector=True,
                ingress_rule_count=0,
                egress_rule_count=5,
            ),
        ]

        result = build_note(
            has_calico=False,
            has_istio_strict=False,
            network_status="open",
            ns_policies=policies,
        )

        assert result is not None
        assert "1 polic" in result
