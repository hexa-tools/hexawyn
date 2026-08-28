"""Tests for domain/services/calico/felix_metrics_service."""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    DataplaneMode,
)
from hexawyn.domain.services.calico.felix_metrics_service import (
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

    def test_denies_found_ranked(self) -> None:
        counters = {
            "available": True,
            "samples": [
                {"policy": "a", "kind": "deny_packets", "value": 10},
                {"policy": "a", "kind": "allow_packets", "value": 5},
                {"policy": "b", "kind": "deny_packets", "value": 100},
                {"policy": "b", "kind": "deny_bytes", "value": 4096},
            ],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.metrics_available is True
        assert [c.policy for c in result.policies] == ["b", "a"]
        assert result.total_denies == 110  # noqa: PLR2004
        assert result.deny_policy_count == 2  # noqa: PLR2004
        assert result.policies[0].deny_bytes == 4096  # noqa: PLR2004

    def test_no_denies_empty_result(self) -> None:
        counters = {
            "available": True,
            "samples": [{"policy": "a", "kind": "allow_packets", "value": 5}],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.total_denies == 0
        assert result.deny_policy_count == 0
        assert [c.policy for c in result.policies] == ["a"]

    def test_metrics_down_degrades_gracefully(self) -> None:
        counters = {"available": False, "message": "prometheus unreachable", "samples": []}
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.metrics_available is False
        assert result.metrics_message == "prometheus unreachable"
        assert result.policies == []
        assert result.total_denies == 0

    def test_not_installed(self) -> None:
        detection = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker=NOT_INSTALLED_MARKER,
            total_nodes=0,
            ready_agents=0,
        )
        result = build_calico_felix_metrics_result(detection=detection, counters={})
        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.metrics_available is False

    def test_skips_junk_samples(self) -> None:
        counters = {
            "available": True,
            "samples": [
                "junk",
                {"policy": None, "kind": "deny_packets", "value": 5},
                {"policy": "a", "kind": "deny_packets", "value": 3},
            ],
        }
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert [c.policy for c in result.policies] == ["a"]
        assert result.total_denies == 3  # noqa: PLR2004

    def test_observed_values_only(self) -> None:
        counters = {"available": True, "samples": []}
        result = build_calico_felix_metrics_result(detection=self._detection(), counters=counters)
        assert result.total_denies == 0
        assert result.total_allows == 0
        assert result.policies == []

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
