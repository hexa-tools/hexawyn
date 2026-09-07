from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumDenialGroup,
    CiliumDenialsQuery,
    CiliumDenialsResult,
    CiliumFlowEntry,
)
from hexawyn.domain.services.cilium.denial_builder import (
    build_denials,
    not_installed_denials_result,
)


def _dropped_flow(
    source: str = "web-0",
    destination: str = "db-0",
    reason: str | None = "Policy denied",
    policy: str | None = "default/deny-all",
    verdict: str = "DROPPED",
) -> CiliumFlowEntry:
    return CiliumFlowEntry(
        timestamp="t",
        source=source,
        destination=destination,
        source_namespace="payments",
        destination_namespace="payments",
        source_identity="100",
        destination_identity="200",
        verdict=verdict,
        drop_reason=reason,
        protocol="tcp",
        destination_port="443",
        l7_protocol=None,
        direction="ingress",
        policy=policy,
    )


class TestBuildDenials:
    def test_groups_dropped_flows_by_policy_source_dest_reason(self) -> None:
        flows = [
            _dropped_flow(),
            _dropped_flow(),
            _dropped_flow(destination="cache-0"),
        ]

        result = build_denials(flows, CiliumDenialsQuery())

        assert result.installed is True
        assert result.status == "present"
        assert result.total_denials == 3  # noqa: PLR2004
        assert len(result.groups) == 2  # noqa: PLR2004
        assert result.groups[0].count == 2  # noqa: PLR2004
        assert result.groups[0].policy == "default/deny-all"

    def test_skips_non_dropped_flows(self) -> None:
        flows = [_dropped_flow(), _dropped_flow(verdict="FORWARDED")]

        result = build_denials(flows, CiliumDenialsQuery())

        assert result.total_denials == 1  # noqa: PLR2004

    def test_missing_reason_reported_unknown(self) -> None:
        flows = [_dropped_flow(reason=None)]

        result = build_denials(flows, CiliumDenialsQuery())

        assert result.groups[0].reason == "UNKNOWN"

    def test_zero_denials(self) -> None:
        result = build_denials([], CiliumDenialsQuery())

        assert result.status == "none"
        assert result.total_denials == 0
        assert result.groups == []

    def test_exact_present_result(self) -> None:
        flows = [_dropped_flow(), _dropped_flow(), _dropped_flow(destination="cache-0")]

        result = build_denials(flows, CiliumDenialsQuery())

        assert isinstance(result, CiliumDenialsResult)
        assert result == CiliumDenialsResult(
            installed=True,
            status="present",
            total_denials=3,  # noqa: PLR2004
            groups=[
                CiliumDenialGroup(
                    policy="default/deny-all",
                    source="web-0",
                    destination="db-0",
                    source_namespace="payments",
                    destination_namespace="payments",
                    reason="Policy denied",
                    count=2,  # noqa: PLR2004
                ),
                CiliumDenialGroup(
                    policy="default/deny-all",
                    source="web-0",
                    destination="cache-0",
                    source_namespace="payments",
                    destination_namespace="payments",
                    reason="Policy denied",
                    count=1,  # noqa: PLR2004
                ),
            ],
            note=None,
        )

    def test_non_dropped_between_dropped_is_skipped(self) -> None:
        flows = [
            _dropped_flow(source="a-0"),
            _dropped_flow(verdict="FORWARDED", source="ignored-0"),
            _dropped_flow(source="a-0"),
        ]

        result = build_denials(flows, CiliumDenialsQuery())

        assert result.total_denials == 2  # noqa: PLR2004
        assert len(result.groups) == 1  # noqa: PLR2004

    def test_sorted_by_count_descending_then_source(self) -> None:
        flows = [
            _dropped_flow(source="a-0", destination="x-0"),
            _dropped_flow(source="b-0", destination="x-0"),
            _dropped_flow(source="b-0", destination="x-0"),
            _dropped_flow(source="c-0", destination="x-0"),
            _dropped_flow(source="c-0", destination="x-0"),
            _dropped_flow(source="c-0", destination="x-0"),
        ]

        result = build_denials(flows, CiliumDenialsQuery())

        assert [g.source for g in result.groups] == ["c-0", "b-0", "a-0"]

    def test_unknown_reason_group(self) -> None:
        flows = [_dropped_flow(reason=None)]

        result = build_denials(flows, CiliumDenialsQuery())

        assert result.groups == [
            CiliumDenialGroup(
                policy="default/deny-all",
                source="web-0",
                destination="db-0",
                source_namespace="payments",
                destination_namespace="payments",
                reason="UNKNOWN",
                count=1,  # noqa: PLR2004
            )
        ]


class TestNotInstalledDenialsResult:
    def test_returns_marker(self) -> None:
        result = not_installed_denials_result()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.groups == []
        assert result.note is not None

    def test_exact_dataclass(self) -> None:
        result = not_installed_denials_result()

        assert result == CiliumDenialsResult(
            installed=False,
            status="not_installed",
            total_denials=0,
            groups=[],
            note="Hubble relay is not available in this cluster",
        )
