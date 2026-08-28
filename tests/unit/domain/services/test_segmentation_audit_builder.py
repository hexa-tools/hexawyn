from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumIdentityInfo, CiliumNetworkPolicyInfo
from hexawyn.domain.services.cilium.segmentation_audit_builder import (
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
