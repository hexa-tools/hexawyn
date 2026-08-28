from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumNetworkPolicyInfo,
    CiliumWorkload,
)
from hexawyn.domain.services.cilium.policy_audit import (
    _note_for,
    build_policy_audit,
    selector_matches,
)


def _policy(
    name: str,
    labels: tuple[tuple[str, str], ...] | None,
    ingress: int = 0,
    egress: int = 0,
    l7: int = 0,
) -> CiliumNetworkPolicyInfo:
    return CiliumNetworkPolicyInfo(
        kind="CiliumNetworkPolicy",
        name=name,
        namespace=None,
        endpoint_selector="",
        ingress_rule_count=ingress,
        egress_rule_count=egress,
        l7_rule_count=l7,
        l7_protocols=(),
        endpoint_labels=labels,
    )


def _workload(namespace: str, name: str, labels: dict[str, str]) -> CiliumWorkload:
    return CiliumWorkload(namespace=namespace, name=name, labels=labels)


class TestSelectorMatches:
    def test_subset_label_match(self) -> None:
        assert selector_matches({"app": "db", "tier": "db"}, (("app", "db"),))

    def test_label_mismatch_is_not_selected(self) -> None:
        assert not selector_matches({"app": "web"}, (("app", "db"),))

    def test_empty_selector_matches_all(self) -> None:
        assert selector_matches({"app": "anything"}, ())

    def test_unknown_selector_never_claims_coverage(self) -> None:
        assert not selector_matches({"app": "db"}, None)


class TestBuildPolicyAudit:
    def test_no_policy_gap(self) -> None:
        policies = [_policy("allow-db", (("app", "db"),), ingress=1, egress=1, l7=1)]
        workloads = [_workload("ns", "web-0", {"app": "web"})]

        result = build_policy_audit(policies, workloads)

        assert result.status == "gaps_found"
        assert result.uncovered_count == 1  # noqa: PLR2004
        assert result.findings[0].coverage == "no_policy"
        assert result.findings[0].risk == "critical"

    def test_fully_covered_no_gaps(self) -> None:
        policies = [_policy("allow-db", (("app", "db"),), ingress=1, egress=1, l7=1)]
        workloads = [_workload("ns", "db-0", {"app": "db"})]

        result = build_policy_audit(policies, workloads)

        assert result.status == "covered"
        assert result.findings == []

    def test_no_default_deny_gap(self) -> None:
        policies = [_policy("allow-db", (("app", "db"),))]
        workloads = [_workload("ns", "db-0", {"app": "db"})]

        result = build_policy_audit(policies, workloads)

        assert result.findings[0].coverage == "no_default_deny"
        assert result.findings[0].risk == "critical"

    def test_partial_restriction_gap(self) -> None:
        policies = [_policy("allow-db", (("app", "db"),), ingress=1)]
        workloads = [_workload("ns", "db-0", {"app": "db"})]

        result = build_policy_audit(policies, workloads)

        finding = result.findings[0]
        assert finding.coverage == "partial"
        assert finding.risk == "medium"
        assert finding.ingress_restricted is True
        assert finding.egress_restricted is False

    def test_l7_gap(self) -> None:
        policies = [_policy("allow-db", (("app", "db"),), ingress=1, egress=1)]
        workloads = [_workload("ns", "db-0", {"app": "db"})]

        result = build_policy_audit(policies, workloads)

        assert result.findings[0].coverage == "l7_gap"
        assert result.findings[0].risk == "medium"
        assert result.findings[0].l7_restricted is False

    def test_empty_workloads(self) -> None:
        result = build_policy_audit([_policy("p", (("app", "x"),))], [])

        assert result.status == "empty"
        assert result.total_workloads == 0
        assert result.findings == []

    def test_overlapping_selectors_deduplicated(self) -> None:
        policies = [
            _policy("a", (("app", "db"),), ingress=1, egress=1, l7=1),
            _policy("b", (("tier", "db"),), ingress=1, egress=1, l7=1),
        ]
        workloads = [_workload("ns", "db-0", {"app": "db", "tier": "db"})]

        result = build_policy_audit(policies, workloads)

        assert result.findings == []

    def test_malformed_selector_not_covered(self) -> None:
        policies = [_policy("odd", None, ingress=1, egress=1)]
        workloads = [_workload("ns", "x-0", {"app": "db"})]

        result = build_policy_audit(policies, workloads)

        assert result.findings[0].coverage == "no_policy"

    def test_note_for_default_returns_none(self) -> None:
        assert _note_for("covered") is None
