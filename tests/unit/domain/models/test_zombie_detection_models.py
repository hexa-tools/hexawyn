"""RED → GREEN — Layer 1: ZombieDetection domain models."""

import pytest
from hexawyn.domain.models.zombie_detection import ZombieCandidate, ZombieDetectionResult


class TestZombieCandidate:
    def test_frozen_dataclass(self) -> None:
        candidate = ZombieCandidate(
            pod_name="legacy-api-pod-abc",
            namespace="production",
            age_days=180,
            traffic_rps=0.0,
            cpu_cores=0.5,
            memory_gb=1.0,
            risk="safe_to_remove",
            reason="No traffic for 24h, no deps",
        )
        assert candidate.pod_name == "legacy-api-pod-abc"
        assert candidate.risk == "safe_to_remove"
        assert candidate.traffic_rps == 0.0

    def test_is_immutable(self) -> None:
        candidate = ZombieCandidate(
            pod_name="test-pod",
            namespace="staging",
            age_days=10,
            traffic_rps=0.0,
            cpu_cores=0.25,
            memory_gb=2.0,
            risk="review_needed",
            reason="Has service pointing to it",
        )
        with pytest.raises(Exception):
            candidate.risk = "safe_to_remove"  # type: ignore[misc]

    def test_review_needed_candidate(self) -> None:
        candidate = ZombieCandidate(
            pod_name="test-deploy-xyz",
            namespace="staging",
            age_days=45,
            traffic_rps=0.0,
            cpu_cores=0.25,
            memory_gb=2.0,
            risk="review_needed",
            reason="No traffic but has service pointing to it",
        )
        assert candidate.risk == "review_needed"
        assert candidate.memory_gb == 2.0  # noqa: PLR2004
        assert candidate.cpu_cores == 0.25  # noqa: PLR2004

    def test_reason_field_present(self) -> None:
        candidate = ZombieCandidate(
            pod_name="pod",
            namespace="ns",
            age_days=5,
            traffic_rps=0.0,
            cpu_cores=0.1,
            memory_gb=0.5,
            risk="safe_to_remove",
            reason="No traffic for 24h, no deps",
        )
        assert isinstance(candidate.reason, str)
        assert len(candidate.reason) > 0


class TestZombieDetectionResult:
    def test_mutable_dataclass(self) -> None:
        result = ZombieDetectionResult(
            analysis_window_hours=24,
            zombie_candidates=[],
            total_wasted_cores=0.0,
            total_wasted_gb=0.0,
            prometheus_available=True,
            data_source="prometheus",
        )
        assert result.analysis_window_hours == 24  # noqa: PLR2004
        assert result.zombie_candidates == []
        assert result.prometheus_available is True

    def test_default_values(self) -> None:
        result = ZombieDetectionResult()
        assert result.zombie_candidates == []
        assert result.total_wasted_cores == 0.0
        assert result.total_wasted_gb == 0.0
        assert result.prometheus_available is False
        assert result.data_source == "estimated"

    def test_with_candidates(self) -> None:
        candidates = [
            ZombieCandidate(
                pod_name="pod-a",
                namespace="ns",
                age_days=10,
                traffic_rps=0.0,
                cpu_cores=0.5,
                memory_gb=1.0,
                risk="safe_to_remove",
                reason="no traffic",
            ),
            ZombieCandidate(
                pod_name="pod-b",
                namespace="ns",
                age_days=20,
                traffic_rps=0.0,
                cpu_cores=0.25,
                memory_gb=2.0,
                risk="review_needed",
                reason="has service",
            ),
        ]
        result = ZombieDetectionResult(
            analysis_window_hours=24,
            zombie_candidates=candidates,
            total_wasted_cores=0.75,
            total_wasted_gb=3.0,
            prometheus_available=True,
            data_source="prometheus",
        )
        assert len(result.zombie_candidates) == 2  # noqa: PLR2004
        assert result.total_wasted_cores == 0.75  # noqa: PLR2004
        assert result.total_wasted_gb == 3.0  # noqa: PLR2004
        assert result.data_source == "prometheus"
