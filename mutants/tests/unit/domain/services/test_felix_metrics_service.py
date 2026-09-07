"""Tests for domain/services/calico/felix_metrics_service."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoFelixPolicyCounter,
    DataplaneMode,
)
from hexawyn.domain.services.calico.felix_metrics_service import (
    _aggregate,
    _as_int,
    build_calico_felix_metrics_result,
)


class TestBuildCalicoFelixMetricsResult:
    def _detection(self, **overrides: object) -> CalicoDetectionResult:
        base: dict[str, object] = {
            "installed": True,
            "status": CalicoDetectionStatus.INSTALLED,
            "not_installed_marker": None,
            "version": "v3.26.1",
            "mode": DataplaneMode.IPIP,
            "namespace": "calico-system",
            "tigera_operator": False,
            "enterprise": False,
            "agents": [],
            "total_nodes": 3,
            "ready_agents": 3,
            "degraded_agents": 0,
            "degraded_summary": None,
            "error": None,
        }
        base.update(overrides)
        return CalicoDetectionResult(**base)  # type: ignore[arg-type]

    def test_not_installed_full_payload(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            total_nodes=0,
            ready_agents=0,
            error="kube api unreachable",
        )
        result = build_calico_felix_metrics_result(detection=detection, counters={})
        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.metrics_available is False
        assert result.metrics_message is None
        assert result.policies == []
        assert result.total_denies == 0
        assert result.total_allows == 0
        assert result.deny_policy_count == 0
        assert result.error == "kube api unreachable"

    def test_metrics_down_full_payload(self) -> None:
        counters = {"available": False, "message": "prometheus unreachable", "samples": []}
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.installed is True
        assert result.not_installed_marker is None
        assert result.metrics_available is False
        assert result.metrics_message == "prometheus unreachable"
        assert result.policies == []
        assert result.total_denies == 0
        assert result.total_allows == 0
        assert result.deny_policy_count == 0
        assert result.error is None

    def test_metrics_down_default_message_when_absent(self) -> None:
        counters = {"available": False}
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.metrics_available is False
        assert result.metrics_message == "felix metrics unavailable"

    def test_metrics_down_forwards_detection_error(self) -> None:
        detection = self._detection(error="no felix pod on node")
        counters = {"available": False, "message": None, "samples": []}
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        assert result.metrics_available is False
        assert result.metrics_message == "felix metrics unavailable"
        assert result.error == "no felix pod on node"

    def test_available_forwards_detection_error(self) -> None:
        detection = self._detection(error="partial counters observed")
        counters = {
            "available": True,
            "samples": [{"policy": "a", "kind": "deny_packets", "value": 3}],
        }
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        assert result.metrics_available is True
        assert result.error == "partial counters observed"

    def test_sample_without_value_still_registers_zero_entry(self) -> None:
        counters = {
            "available": True,
            "samples": [{"policy": "a", "kind": "deny_packets"}],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert [c.policy for c in result.policies] == ["a"]
        assert result.policies[0].deny_packets == 0
        assert result.total_denies == 0

    def test_denies_found_ranked_exact(self) -> None:
        counters = {
            "available": True,
            "samples": [
                {"policy": "a", "kind": "deny_packets", "value": 10},
                {"policy": "a", "kind": "allow_packets", "value": 5},
                {"policy": "a", "kind": "allow_bytes", "value": 512},
                {"policy": "a", "kind": "deny_bytes", "value": 1024},
                {"policy": "b", "kind": "deny_packets", "value": 100},
                {"policy": "b", "kind": "deny_bytes", "value": 4096},
            ],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.metrics_available is True
        assert result.metrics_message is None
        assert result.installed is True
        assert result.not_installed_marker is None
        assert result.policies == [
            CalicoFelixPolicyCounter(
                policy="b",
                allow_packets=0,
                deny_packets=100,
                allow_bytes=0,
                deny_bytes=4096,
            ),
            CalicoFelixPolicyCounter(
                policy="a",
                allow_packets=5,
                deny_packets=10,
                allow_bytes=512,
                deny_bytes=1024,
            ),
        ]
        assert result.total_denies == 110  # noqa: PLR2004
        assert result.total_allows == 5  # noqa: PLR2004
        assert result.deny_policy_count == 2  # noqa: PLR2004
        assert result.error is None

    def test_deny_boundary_single_packet_counts(self) -> None:
        counters = {
            "available": True,
            "samples": [{"policy": "a", "kind": "deny_packets", "value": 1}],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.deny_policy_count == 1  # noqa: PLR2004
        assert result.total_denies == 1  # noqa: PLR2004

    def test_sort_tie_denies_breaks_by_allow_descending(self) -> None:
        counters = {
            "available": True,
            "samples": [
                {"policy": "low_allow", "kind": "deny_packets", "value": 50},
                {"policy": "low_allow", "kind": "allow_packets", "value": 1},
                {"policy": "high_allow", "kind": "deny_packets", "value": 50},
                {"policy": "high_allow", "kind": "allow_packets", "value": 99},
            ],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert [c.policy for c in result.policies] == ["high_allow", "low_allow"]

    def test_no_denies_empty_result(self) -> None:
        counters = {
            "available": True,
            "samples": [{"policy": "a", "kind": "allow_packets", "value": 5}],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.total_denies == 0
        assert result.deny_policy_count == 0
        assert result.total_allows == 5  # noqa: PLR2004
        assert [c.policy for c in result.policies] == ["a"]

    def test_skips_junk_samples(self) -> None:
        counters = {
            "available": True,
            "samples": [
                "junk",
                {"policy": None, "kind": "deny_packets", "value": 5},
                {"policy": "a", "kind": "deny_packets", "value": 3},
                {"policy": "b", "kind": None, "value": 3},
            ],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert [c.policy for c in result.policies] == ["a"]
        assert result.total_denies == 3  # noqa: PLR2004

    def test_samples_not_sequence(self) -> None:
        counters = {"available": True, "samples": {"not": "a list"}}
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.policies == []
        assert result.total_denies == 0

    def test_non_numeric_value_skipped(self) -> None:
        counters = {
            "available": True,
            "samples": [{"policy": "a", "kind": "deny_packets", "value": "not-a-number"}],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.policies == []
        assert result.total_denies == 0


class TestAggregateDirect:
    def test_non_sequence_returns_empty(self) -> None:
        assert _aggregate(None) == {}
        assert _aggregate({"not": "seq"}) == {}

    def test_empty_sequence_returns_empty(self) -> None:
        assert _aggregate([]) == {}

    def test_accumulates_kind_per_policy(self) -> None:
        raw = [
            {"policy": "a", "kind": "deny_packets", "value": 10},
            {"policy": "a", "kind": "deny_packets", "value": 5},
            {"policy": "a", "kind": "allow_packets", "value": 3},
            {"policy": "b", "kind": "deny_packets", "value": 7},
        ]
        assert _aggregate(raw) == {
            "a": {"deny_packets": 15.0, "allow_packets": 3.0},
            "b": {"deny_packets": 7.0},
        }

    def test_non_mapping_sample_skipped(self) -> None:
        raw = ["junk", {"policy": "a", "kind": "deny_packets", "value": 1}]
        assert _aggregate(raw) == {"a": {"deny_packets": 1.0}}

    def test_missing_policy_or_kind_skipped(self) -> None:
        raw = [
            {"policy": None, "kind": "deny_packets", "value": 1},
            {"policy": "a", "kind": None, "value": 1},
            {"policy": "a", "kind": "deny_packets", "value": 2},
        ]
        assert _aggregate(raw) == {"a": {"deny_packets": 2.0}}

    def test_non_numeric_value_skipped(self) -> None:
        raw = [
            {"policy": "a", "kind": "deny_packets", "value": "not-a-number"},
            {"policy": "a", "kind": "deny_packets", "value": 4},
        ]
        assert _aggregate(raw) == {"a": {"deny_packets": 4.0}}

    def test_non_numeric_between_numeric_keeps_accumulating(self) -> None:
        raw = [
            {"policy": "a", "kind": "deny_packets", "value": 2},
            {"policy": "a", "kind": "deny_packets", "value": "bad"},
            {"policy": "a", "kind": "deny_packets", "value": 3},
        ]
        assert _aggregate(raw) == {"a": {"deny_packets": 5.0}}

    def test_default_zero_when_value_absent(self) -> None:
        raw = [
            {"policy": "a", "kind": "deny_packets"},
            {"policy": "a", "kind": "deny_packets", "value": 2},
        ]
        assert _aggregate(raw) == {"a": {"deny_packets": 2.0}}

    def test_float_values_supported(self) -> None:
        raw = [{"policy": "a", "kind": "deny_packets", "value": 0.5}]
        assert _aggregate(raw) == {"a": {"deny_packets": 0.5}}


class TestAsIntDirect:
    def test_default_zero(self) -> None:
        assert _as_int({}, "deny_packets") == 0

    def test_float_truncated(self) -> None:
        assert _as_int({"deny_packets": 3.7}, "deny_packets") == 3  # noqa: PLR2004

    def test_exact_value(self) -> None:
        assert _as_int({"deny_packets": 5.0}, "deny_packets") == 5  # noqa: PLR2004

    def test_wrong_kind_ignored(self) -> None:
        assert _as_int({"allow_packets": 5.0}, "deny_packets") == 0
