"""RED → GREEN — Layer 2: ZombieDetectionEngine pure domain logic."""

from hexawyn.domain.services.zombie_detection.zombie_detection_engine import (
    ZombieDetectionEngine,
    _as_bool,
    _as_float,
)


def _pod(
    name: str,
    namespace: str = "production",
    traffic_rps: float = 0.0,
    cpu_cores: float = 0.5,
    memory_gb: float = 1.0,
    age_days: int = 30,
    has_service: bool = False,
    is_cronjob: bool = False,
    is_terminating: bool = False,
    has_sidecar: bool = False,
    sidecar_traffic_rps: float = 0.0,
    seven_day_traffic_rps: float = 0.0,
) -> dict[str, object]:
    return {
        "pod_name": name,
        "namespace": namespace,
        "traffic_rps": traffic_rps,
        "cpu_cores": cpu_cores,
        "memory_gb": memory_gb,
        "age_days": age_days,
        "has_service": has_service,
        "is_cronjob": is_cronjob,
        "is_terminating": is_terminating,
        "has_sidecar": has_sidecar,
        "sidecar_traffic_rps": sidecar_traffic_rps,
        "seven_day_traffic_rps": seven_day_traffic_rps,
    }


class TestZeroTrafficDetection:
    def test_legacy_api_zero_traffic_safe_to_remove(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [
            _pod(
                "legacy-api-pod-abc",
                namespace="production",
                traffic_rps=0.0,
                cpu_cores=0.5,
                memory_gb=1.0,
                age_days=180,
            ),
        ]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 1
        assert result.zombie_candidates[0].pod_name == "legacy-api-pod-abc"
        assert result.zombie_candidates[0].risk == "safe_to_remove"

    def test_pod_with_traffic_not_zombie(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [_pod("active-api", traffic_rps=50.0)]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 0

    def test_all_pods_have_traffic_no_zombies(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [
            _pod("svc-a", traffic_rps=10.0),
            _pod("svc-b", traffic_rps=100.0),
            _pod("svc-c", traffic_rps=1.0),
        ]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 0
        assert result.total_wasted_cores == 0.0
        assert result.total_wasted_gb == 0.0


class TestRiskClassification:
    def test_zero_traffic_with_service_review_needed(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [_pod("test-deploy-xyz", namespace="staging", has_service=True)]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 1
        assert result.zombie_candidates[0].risk == "review_needed"

    def test_batch_processor_cronjob_not_zombie_when_7d_traffic(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [
            _pod(
                "batch-processor",
                traffic_rps=0.0,
                is_cronjob=True,
                seven_day_traffic_rps=5.0,
            ),
        ]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 0

    def test_cronjob_zero_traffic_7d_is_zombie(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [
            _pod(
                "stale-cronjob",
                traffic_rps=0.0,
                is_cronjob=True,
                seven_day_traffic_rps=0.0,
                cpu_cores=0.25,
                memory_gb=2.0,
            ),
        ]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 1
        assert result.zombie_candidates[0].pod_name == "stale-cronjob"


class TestEdgeCases:
    def test_terminating_pod_excluded(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [_pod("dying-pod", is_terminating=True)]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 0

    def test_health_check_only_treated_as_zero(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [_pod("healthcheck-pod", traffic_rps=0.001)]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 1

    def test_sidecar_traffic_from_all_containers(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [
            _pod(
                "sidecar-pod",
                traffic_rps=0.0,
                has_sidecar=True,
                sidecar_traffic_rps=100.0,
            ),
        ]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 0


class TestWasteComputation:
    def test_single_zombie_waste(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [
            _pod("zombie-1", cpu_cores=0.5, memory_gb=1.0),
        ]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 1
        assert result.total_wasted_cores == 0.5
        assert result.total_wasted_gb == 1.0

    def test_multiple_zombies_total_waste_computed(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [
            _pod("zombie-a", cpu_cores=0.5, memory_gb=1.0),
            _pod("zombie-b", cpu_cores=0.25, memory_gb=2.0),
            _pod("zombie-c", cpu_cores=1.0, memory_gb=4.0),
            _pod("zombie-d", cpu_cores=0.1, memory_gb=0.5),
            _pod("zombie-e", cpu_cores=0.5, memory_gb=1.5),
        ]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 5
        assert result.total_wasted_cores == 2.35
        assert result.total_wasted_gb == 9.0

    def test_mixed_pods_only_zombie_waste_counted(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [
            _pod("zombie", cpu_cores=0.5, memory_gb=2.0),
            _pod("active", traffic_rps=50.0, cpu_cores=4.0, memory_gb=16.0),
        ]

        result = engine.detect(pods, analysis_window_hours=24)

        assert result.total_wasted_cores == 0.5
        assert result.total_wasted_gb == 2.0

    def test_test_deploy_no_deps_wasted_memory(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [
            _pod(
                "test-deploy-xyz",
                namespace="staging",
                cpu_cores=0.25,
                memory_gb=2.0,
                age_days=45,
            ),
        ]

        result = engine.detect(pods, analysis_window_hours=24)

        assert len(result.zombie_candidates) == 1
        assert result.zombie_candidates[0].pod_name == "test-deploy-xyz"
        assert result.total_wasted_gb == 2.0


class TestResultMetadata:
    def test_analysis_window_passed_through(self) -> None:
        engine = ZombieDetectionEngine()
        pods = [_pod("p")]

        result = engine.detect(pods, analysis_window_hours=48)

        assert result.analysis_window_hours == 48

    def test_empty_pods_returns_empty(self) -> None:
        engine = ZombieDetectionEngine()

        result = engine.detect([], analysis_window_hours=24)

        assert result.zombie_candidates == []
        assert result.total_wasted_cores == 0.0
        assert result.total_wasted_gb == 0.0


class TestAsFloat:
    def test_none_returns_zero(self) -> None:
        assert _as_float(None) == 0.0

    def test_int_converted_to_float(self) -> None:
        assert _as_float(42) == 42.0

    def test_float_passthrough(self) -> None:
        assert _as_float(3.14) == 3.14

    def test_non_numeric_string_returns_zero(self) -> None:
        assert _as_float("hello") == 0.0

    def test_list_returns_zero(self) -> None:
        assert _as_float([1, 2, 3]) == 0.0


class TestAsBool:
    def test_none_returns_false(self) -> None:
        assert _as_bool(None) is False

    def test_true_returns_true(self) -> None:
        assert _as_bool(True) is True

    def test_false_returns_false(self) -> None:
        assert _as_bool(False) is False

    def test_non_empty_string_returns_true(self) -> None:
        assert _as_bool("yes") is True

    def test_zero_int_returns_false(self) -> None:
        assert _as_bool(0) is False
