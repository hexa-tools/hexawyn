from __future__ import annotations

from hexawyn.domain.services.cilium.bandwidth_builder import (
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


class TestBandwidthAuditMarkers:
    def test_not_installed(self) -> None:
        result = not_installed_bandwidth_audit()
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.entries == []
        assert result.note is not None

    def test_not_available(self) -> None:
        result = not_available_bandwidth_audit()
        assert result.installed is True
        assert result.status == "not_available"
        assert result.entries == []
        assert result.note is not None
