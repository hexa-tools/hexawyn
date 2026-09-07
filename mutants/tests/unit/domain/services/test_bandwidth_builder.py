from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumBandwidthAuditResult,
    CiliumBandwidthEntry,
)
from hexawyn.domain.services.cilium.bandwidth_builder import (
    _note_for,
    build_bandwidth_audit,
    build_bandwidth_entry,
    classify_bandwidth,
    not_available_bandwidth_audit,
    not_installed_bandwidth_audit,
)


class TestClassifyBandwidth:
    def test_throttled_wins(self) -> None:
        assert classify_bandwidth(0.5, True) == "throttled"

    def test_near_limit(self) -> None:
        assert classify_bandwidth(0.95, False) == "near_limit"

    def test_ok(self) -> None:
        assert classify_bandwidth(0.4, False) == "ok"

    def test_unknown_without_usage(self) -> None:
        assert classify_bandwidth(None, False) == "UNKNOWN"

    def test_exact_threshold_is_near_limit(self) -> None:
        assert classify_bandwidth(0.9, False) == "near_limit"  # noqa: PLR2004

    def test_just_below_threshold_is_ok(self) -> None:
        assert classify_bandwidth(0.89, False) == "ok"


class TestBuildBandwidthEntry:
    def test_builds_entry(self) -> None:
        entry = build_bandwidth_entry(
            namespace="payments",
            pod="db-0",
            ingress_limit="10M",
            egress_limit="20M",
            usage_ratio=0.95,
            throttled=False,
        )
        assert entry.state == "near_limit"
        assert entry.note == "Pod at 95% of its bandwidth limit"

    def test_exact_entry(self) -> None:
        entry = build_bandwidth_entry(
            namespace="payments",
            pod="db-0",
            ingress_limit="10M",
            egress_limit="20M",
            usage_ratio=0.95,
            throttled=False,
        )

        assert entry == CiliumBandwidthEntry(
            namespace="payments",
            pod="db-0",
            ingress_limit="10M",
            egress_limit="20M",
            usage_ratio=0.95,
            state="near_limit",
            note="Pod at 95% of its bandwidth limit",
        )

    def test_throttled_entry_exact(self) -> None:
        entry = build_bandwidth_entry(
            namespace="ns",
            pod="thr-0",
            ingress_limit=None,
            egress_limit=None,
            usage_ratio=None,
            throttled=True,
        )

        assert entry == CiliumBandwidthEntry(
            namespace="ns",
            pod="thr-0",
            ingress_limit=None,
            egress_limit=None,
            usage_ratio=None,
            state="throttled",
            note="Pod is being throttled by the Cilium bandwidth manager",
        )


class TestNoteFor:
    def test_throttled_note(self) -> None:
        assert _note_for(None, True) == ("Pod is being throttled by the Cilium bandwidth manager")

    def test_near_limit_note_rounds_percent(self) -> None:
        assert _note_for(0.956, False) == "Pod at 96% of its bandwidth limit"

    def test_exact_threshold_note(self) -> None:
        assert _note_for(0.9, False) == "Pod at 90% of its bandwidth limit"  # noqa: PLR2004

    def test_ok_ratio_no_note(self) -> None:
        assert _note_for(0.4, False) is None

    def test_none_ratio_no_note(self) -> None:
        assert _note_for(None, False) is None


class TestBuildBandwidthAudit:
    def test_flags_throttled_first(self) -> None:
        entry_ok = build_bandwidth_entry("ns", "ok-0", "10M", None, 0.2, False)
        entry_throttled = build_bandwidth_entry("ns", "thr-0", "10M", None, None, True)

        result = build_bandwidth_audit([entry_ok, entry_throttled])

        assert result.status == "anomalies"
        assert result.entries[0].pod == "thr-0"

    def test_ok_when_no_anomalies(self) -> None:
        entry = build_bandwidth_entry("ns", "ok-0", "10M", None, 0.2, False)

        result = build_bandwidth_audit([entry])

        assert result.status == "ok"
        assert result.total_pods == 1  # noqa: PLR2004

    def test_near_limit_also_anomaly(self) -> None:
        entry = build_bandwidth_entry("ns", "near-0", "10M", None, 0.95, False)

        result = build_bandwidth_audit([entry])

        assert result.status == "anomalies"

    def test_anomalies_exact_result(self) -> None:
        entry_ok = build_bandwidth_entry("ns", "ok-0", "10M", None, 0.2, False)
        entry_throttled = build_bandwidth_entry("ns", "thr-0", "10M", None, None, True)

        result = build_bandwidth_audit([entry_ok, entry_throttled])

        assert result == CiliumBandwidthAuditResult(
            installed=True,
            status="anomalies",
            total_pods=2,  # noqa: PLR2004
            entries=[entry_throttled, entry_ok],
            note=None,
        )

    def test_ok_exact_result(self) -> None:
        entry = build_bandwidth_entry("ns", "ok-0", "10M", None, 0.2, False)

        result = build_bandwidth_audit([entry])

        assert result == CiliumBandwidthAuditResult(
            installed=True,
            status="ok",
            total_pods=1,  # noqa: PLR2004
            entries=[entry],
            note=None,
        )


class TestBandwidthAuditMarkers:
    def test_not_installed(self) -> None:
        result = not_installed_bandwidth_audit()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.entries == []
        assert result.note is not None

    def test_not_installed_exact(self) -> None:
        result = not_installed_bandwidth_audit()

        assert result == CiliumBandwidthAuditResult(
            installed=False,
            status="not_installed",
            total_pods=0,
            entries=[],
            note="Cilium is not installed in this cluster",
        )

    def test_not_available(self) -> None:
        result = not_available_bandwidth_audit()
        assert result.installed is True
        assert result.status == "not_available"
        assert result.entries == []
        assert result.note is not None

    def test_not_available_exact(self) -> None:
        result = not_available_bandwidth_audit()

        assert result == CiliumBandwidthAuditResult(
            installed=True,
            status="not_available",
            total_pods=0,
            entries=[],
            note=("Cilium bandwidth manager is disabled " "(no bandwidth annotations found)"),
        )
