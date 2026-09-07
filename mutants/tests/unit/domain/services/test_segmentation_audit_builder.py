from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumIdentityInfo,
    CiliumNetworkPolicyInfo,
    CiliumPathFinding,
    CiliumSegmentationAuditResult,
)
from hexawyn.domain.services.cilium.segmentation_audit_builder import (
    _finding,
    _labels_to_dict,
    _path_unrestricted,
    build_segmentation_audit,
    not_installed_segmentation_audit,
)


def _identity(raw_id: str, labels: dict[str, str]) -> CiliumIdentityInfo:
    return CiliumIdentityInfo(
        id=raw_id,
        labels=tuple(f"{k}={v}" for k, v in sorted(labels.items())),
        endpoint_count=1,
    )


def _policy(
    name: str,
    labels: dict[str, str],
    ingress: int = 0,
    egress: int = 0,
) -> CiliumNetworkPolicyInfo:
    return CiliumNetworkPolicyInfo(
        kind="CiliumNetworkPolicy",
        name=name,
        namespace=None,
        endpoint_selector="",
        ingress_rule_count=ingress,
        egress_rule_count=egress,
        l7_rule_count=0,
        l7_protocols=(),
        endpoint_labels=tuple(sorted(labels.items())),
    )


class TestBuildSegmentationAudit:
    def test_flags_unrestricted_path(self) -> None:
        identities = [_identity("100", {"app": "web"}), _identity("200", {"app": "db"})]

        result = build_segmentation_audit(identities, [])

        assert result.status == "gaps_found"
        assert result.total_paths == 2  # noqa: PLR2004
        assert result.uncovered_paths == 2  # noqa: PLR2004
        assert len(result.findings) == 2  # noqa: PLR2004
        assert result.findings[0].severity == "high"

    def test_isolated_when_policy_blocks_paths(self) -> None:
        identities = [_identity("100", {"app": "db"})]
        policies = [_policy("deny", {"app": "db"}, ingress=1, egress=1)]

        result = build_segmentation_audit(identities, policies)

        assert result.status == "isolated"
        assert result.findings == []

    def test_single_identity_trivial_matrix(self) -> None:
        identities = [_identity("100", {"app": "web"})]

        result = build_segmentation_audit(identities, [])

        assert result.status == "isolated"
        assert result.total_paths == 0

    def test_empty_identities(self) -> None:
        result = build_segmentation_audit([], [])

        assert result.status == "empty"
        assert result.total_identities == 0
        assert result.findings == []
        assert result.note is not None

    def test_destination_ingress_policy_restricts_path(self) -> None:
        identities = [_identity("100", {"app": "web"}), _identity("200", {"app": "db"})]
        policies = [_policy("deny-db", {"app": "db"}, ingress=1)]

        result = build_segmentation_audit(identities, policies)

        # web->db blocked by db ingress policy; db->web unrestricted.
        assert result.total_paths == 2  # noqa: PLR2004
        assert result.uncovered_paths == 1  # noqa: PLR2004

    def test_large_matrix_compact_report(self) -> None:
        identities = [
            _identity("1", {"tier": "a"}),
            _identity("2", {"tier": "b"}),
            _identity("3", {"tier": "c"}),
        ]

        result = build_segmentation_audit(identities, [])

        assert result.total_paths == 6  # noqa: PLR2004
        assert result.uncovered_paths == 6  # noqa: PLR2004
        assert len(result.findings) == 6  # noqa: PLR2004


class TestNotInstalledSegmentationAudit:
    def test_returns_vanilla_marker(self) -> None:
        result = not_installed_segmentation_audit()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.view == "vanilla"
        assert result.findings == []
        assert result.total_identities == 0
        assert result.total_paths == 0
        assert result.uncovered_paths == 0
        assert result.summary == (
            "Cilium is not installed; vanilla NetworkPolicy view is out of scope"
        )
        assert result.note == "Cilium is not installed in this cluster"


class TestLabelsToDict:
    def test_parses_kv_labels(self) -> None:
        assert _labels_to_dict(("app=db", "tier=backend")) == {
            "app": "db",
            "tier": "backend",
        }

    def test_value_keeps_equals_after_first(self) -> None:
        assert _labels_to_dict(("k8s:io=a=b",)) == {"k8s:io": "a=b"}

    def test_skips_labels_without_equals(self) -> None:
        assert _labels_to_dict(("bare", "app=db")) == {"app": "db"}

    def test_empty_input(self) -> None:
        assert _labels_to_dict(()) == {}


class TestPathUnrestrictedDirect:
    def test_unrestricted_when_no_policies(self) -> None:
        source = _identity("100", {"app": "web"})
        destination = _identity("200", {"app": "db"})

        assert _path_unrestricted(source, destination, []) is True

    def test_destination_ingress_restricts(self) -> None:
        source = _identity("100", {"app": "web"})
        destination = _identity("200", {"app": "db"})
        policies = [_policy("db", {"app": "db"}, ingress=1)]

        assert _path_unrestricted(source, destination, policies) is False

    def test_selecting_policy_with_zero_ingress_does_not_restrict(self) -> None:
        source = _identity("100", {"app": "web"})
        destination = _identity("200", {"app": "db"})
        policies = [_policy("db", {"app": "db"}, ingress=0, egress=0)]

        assert _path_unrestricted(source, destination, policies) is True

    def test_source_egress_restricts(self) -> None:
        source = _identity("100", {"app": "web"})
        destination = _identity("200", {"app": "db"})
        policies = [_policy("web", {"app": "web"}, egress=1)]

        assert _path_unrestricted(source, destination, policies) is False

    def test_non_matching_egress_does_not_restrict(self) -> None:
        source = _identity("100", {"app": "web"})
        destination = _identity("200", {"app": "db"})
        policies = [_policy("other", {"app": "cache"}, egress=1)]

        assert _path_unrestricted(source, destination, policies) is True


class TestFindingDirect:
    def test_maps_identity_fields(self) -> None:
        source = _identity("100", {"app": "web"})
        destination = _identity("200", {"app": "db"})

        finding = _finding(source, destination)

        assert finding == CiliumPathFinding(
            source_id="100",
            destination_id="200",
            source_labels=("app=web",),
            destination_labels=("app=db",),
            severity="high",
            note=(
                "No Cilium policy restricts this path "
                "(neither source egress nor destination ingress)"
            ),
        )


class TestBuildSegmentationAuditExact:
    def test_gaps_result_exact_fields(self) -> None:
        identities = [_identity("100", {"app": "web"}), _identity("200", {"app": "db"})]

        result = build_segmentation_audit(identities, [])

        assert isinstance(result, CiliumSegmentationAuditResult)
        assert result.installed is True
        assert result.view == "cilium"
        assert result.status == "gaps_found"
        assert result.total_identities == 2  # noqa: PLR2004
        assert result.total_paths == 2  # noqa: PLR2004
        assert result.uncovered_paths == 2  # noqa: PLR2004
        assert result.summary == "2 unrestricted path(s) out of 2"
        assert result.note is None

    def test_empty_result_exact_fields(self) -> None:
        result = build_segmentation_audit([], [])

        assert result.installed is True
        assert result.view == "cilium"
        assert result.status == "empty"
        assert result.total_identities == 0
        assert result.total_paths == 0
        assert result.uncovered_paths == 0
        assert result.summary == "No Cilium identities found to audit"
        assert result.note == "No Cilium identities found to audit"

    def test_isolated_result_exact_fields(self) -> None:
        identities = [_identity("100", {"app": "db"})]
        policies = [_policy("deny", {"app": "db"}, ingress=1, egress=1)]

        result = build_segmentation_audit(identities, policies)

        assert result.status == "isolated"
        assert result.total_paths == 0
        assert result.summary == "0 unrestricted path(s) out of 0"
        assert result.findings == []

    def test_egress_blocking_produces_specific_finding(self) -> None:
        identities = [_identity("100", {"app": "web"}), _identity("200", {"app": "db"})]
        policies = [_policy("db", {"app": "db"}, ingress=1)]

        result = build_segmentation_audit(identities, policies)

        # db->web is the only unrestricted path (web has no egress policy)
        assert result.uncovered_paths == 1  # noqa: PLR2004
        finding = result.findings[0]
        assert finding.source_id == "200"
        assert finding.destination_id == "100"
        assert finding.severity == "high"
