from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumAuditFinding,
    CiliumNetworkPolicyInfo,
    CiliumPolicyAuditResult,
    CiliumWorkload,
)
from hexawyn.domain.services.cilium.policy_audit import (
    _classify,
    _finding,
    _note_for,
    _summary,
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


class TestNoteForExact:
    def test_no_policy_note(self) -> None:
        assert _note_for("no_policy") == "No Cilium network policy selects this workload"

    def test_no_default_deny_note(self) -> None:
        assert _note_for("no_default_deny") == (
            "Policy selects the workload but defines no ingress/egress rule"
        )

    def test_partial_note(self) -> None:
        assert _note_for("partial") == "Workload partially restricted (ingress or egress only)"

    def test_l7_gap_note(self) -> None:
        assert _note_for("l7_gap") == "Workload restricted at L3/L4 but not by an L7 rule"

    def test_unknown_coverage_note_none(self) -> None:
        assert _note_for("bogus") is None


class TestFindingExact:
    def test_maps_all_fields(self) -> None:
        workload = _workload("ns-1", "web-0", {"app": "web"})

        finding = _finding(workload, "no_policy", restricted=(True, False, True))

        assert finding == CiliumAuditFinding(
            namespace="ns-1",
            workload="web-0",
            coverage="no_policy",
            ingress_restricted=True,
            egress_restricted=False,
            l7_restricted=True,
            risk="critical",
            note="No Cilium network policy selects this workload",
        )

    def test_partial_risk_and_note(self) -> None:
        workload = _workload("ns", "x", {"app": "x"})
        finding = _finding(workload, "partial", restricted=(True, False, False))

        assert finding.risk == "medium"
        assert finding.note == "Workload partially restricted (ingress or egress only)"


class TestClassifyDirect:
    def test_no_matching_policy_returns_no_policy_unrestricted(self) -> None:
        workload = _workload("ns", "web-0", {"app": "web"})
        policies = [_policy("db", (("app", "db"),), ingress=1, egress=1, l7=1)]

        finding = _classify(policies, workload)

        assert finding == CiliumAuditFinding(
            namespace="ns",
            workload="web-0",
            coverage="no_policy",
            ingress_restricted=False,
            egress_restricted=False,
            l7_restricted=False,
            risk="critical",
            note="No Cilium network policy selects this workload",
        )

    def test_ingress_and_egress_and_l7_is_covered(self) -> None:
        workload = _workload("ns", "db-0", {"app": "db"})
        policies = [_policy("db", (("app", "db"),), ingress=1, egress=1, l7=1)]

        assert _classify(policies, workload) is None

    def test_ingress_egress_without_l7_is_l7_gap(self) -> None:
        workload = _workload("ns", "db-0", {"app": "db"})
        policies = [_policy("db", (("app", "db"),), ingress=1, egress=1)]

        finding = _classify(policies, workload)

        assert finding.coverage == "l7_gap"
        assert finding.ingress_restricted is True
        assert finding.egress_restricted is True
        assert finding.l7_restricted is False

    def test_ingress_only_is_partial(self) -> None:
        workload = _workload("ns", "db-0", {"app": "db"})
        policies = [_policy("db", (("app", "db"),), ingress=1)]

        finding = _classify(policies, workload)

        assert finding.coverage == "partial"
        assert finding.ingress_restricted is True
        assert finding.egress_restricted is False
        assert finding.l7_restricted is False

    def test_egress_only_is_partial(self) -> None:
        workload = _workload("ns", "db-0", {"app": "db"})
        policies = [_policy("db", (("app", "db"),), egress=1)]

        finding = _classify(policies, workload)

        assert finding.coverage == "partial"
        assert finding.ingress_restricted is False
        assert finding.egress_restricted is True
        assert finding.l7_restricted is False

    def test_selecting_policy_without_rules_is_no_default_deny(self) -> None:
        workload = _workload("ns", "db-0", {"app": "db"})
        policies = [_policy("db", (("app", "db"),))]

        finding = _classify(policies, workload)

        assert finding.coverage == "no_default_deny"
        assert finding.ingress_restricted is False
        assert finding.egress_restricted is False
        assert finding.l7_restricted is False


class TestBuildPolicyAuditResultShape:
    def test_gaps_result_exact_fields(self) -> None:
        policies = [_policy("db", (("app", "db"),), ingress=1, egress=1, l7=1)]
        workloads = [
            _workload("ns", "web-0", {"app": "web"}),
            _workload("ns", "cache-0", {"app": "cache"}),
        ]

        result = build_policy_audit(policies, workloads)

        assert isinstance(result, CiliumPolicyAuditResult)
        assert result.installed is True
        assert result.view == "cilium"
        assert result.status == "gaps_found"
        assert result.total_workloads == 2  # noqa: PLR2004
        assert result.uncovered_count == 2  # noqa: PLR2004
        assert result.summary == "2 workload(s) with a coverage gap out of 2"
        assert result.note is None

    def test_mixed_coverage_counts_only_uncovered(self) -> None:
        policies = [_policy("db", (("app", "db"),), ingress=1, egress=1, l7=1)]
        workloads = [
            _workload("ns", "web-0", {"app": "web"}),  # no_policy -> uncovered
            _workload("ns", "db-0", {"app": "db"}),  # covered
        ]

        result = build_policy_audit(policies, workloads)

        assert result.status == "gaps_found"
        assert result.uncovered_count == 1  # noqa: PLR2004
        assert result.total_workloads == 2  # noqa: PLR2004

    def test_no_default_deny_counts_as_uncovered(self) -> None:
        policies = [_policy("db", (("app", "db"),))]
        workloads = [_workload("ns", "db-0", {"app": "db"})]

        result = build_policy_audit(policies, workloads)

        assert result.findings[0].coverage == "no_default_deny"
        assert result.uncovered_count == 1  # noqa: PLR2004

    def test_empty_result_exact_fields(self) -> None:
        result = build_policy_audit([], [])

        assert result.installed is True
        assert result.view == "cilium"
        assert result.status == "empty"
        assert result.total_workloads == 0
        assert result.uncovered_count == 0
        assert result.summary == "No workloads found to audit"
        assert result.note is None

    def test_covered_status_when_all_covered(self) -> None:
        policies = [_policy("db", (("app", "db"),), ingress=1, egress=1, l7=1)]
        workloads = [_workload("ns", "db-0", {"app": "db"})]

        result = build_policy_audit(policies, workloads)

        assert result.status == "covered"
        assert result.uncovered_count == 0
        assert result.summary == "0 workload(s) with a coverage gap out of 1"
        assert result.findings == []

    def test_partial_counts_as_not_uncovered(self) -> None:
        policies = [_policy("db", (("app", "db"),), ingress=1)]
        workloads = [_workload("ns", "db-0", {"app": "db"})]

        result = build_policy_audit(policies, workloads)

        assert result.findings[0].coverage == "partial"
        assert result.uncovered_count == 0


class TestSummary:
    def test_formats_counts(self) -> None:
        assert _summary(3, 10) == "3 workload(s) with a coverage gap out of 10"  # noqa: PLR2004

    def test_zero_gaps(self) -> None:
        assert _summary(0, 5) == "0 workload(s) with a coverage gap out of 5"
