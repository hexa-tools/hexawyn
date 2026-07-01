from __future__ import annotations

from hexawyn.domain.models.rollouts import (
    AnalysisRun,
    AnalysisRunPhase,
    Rollout,
    RolloutPhase,
    RolloutsDetectionResult,
    RolloutStepStatus,
    RolloutStrategy,
)


class TestRolloutPhase:
    def test_six_values(self) -> None:
        assert RolloutPhase.HEALTHY.value == "healthy"
        assert RolloutPhase.PROGRESSING.value == "progressing"
        assert RolloutPhase.DEGRADED.value == "degraded"
        assert RolloutPhase.PAUSED.value == "paused"
        assert RolloutPhase.ABORTED.value == "aborted"
        assert RolloutPhase.UNKNOWN.value == "unknown"


class TestRolloutStrategy:
    def test_two_values(self) -> None:
        assert RolloutStrategy.CANARY.value == "canary"
        assert RolloutStrategy.BLUE_GREEN.value == "blue_green"


class TestAnalysisRunPhase:
    def test_five_values(self) -> None:
        assert AnalysisRunPhase.RUNNING.value == "running"
        assert AnalysisRunPhase.SUCCESSFUL.value == "successful"
        assert AnalysisRunPhase.FAILED.value == "failed"
        assert AnalysisRunPhase.ERROR.value == "error"
        assert AnalysisRunPhase.INCONCLUSIVE.value == "inconclusive"


class TestRolloutStepStatus:
    def test_all_fields(self) -> None:
        step = RolloutStepStatus(
            step_index=2,
            total_steps=5,
            current_step_type="setWeight",
            canary_weight=20,
            paused_at=None,
            pause_reason=None,
        )
        assert step.step_index == 2
        assert step.canary_weight == 20

    def test_paused_step(self) -> None:
        step = RolloutStepStatus(
            step_index=3,
            total_steps=5,
            current_step_type="pause",
            canary_weight=40,
            paused_at="2026-07-01T10:00:00Z",
            pause_reason="manual",
        )
        assert step.pause_reason == "manual"


class TestRollout:
    def test_required_fields(self) -> None:
        rollout = Rollout(
            name="payments-api",
            namespace="production",
            strategy=RolloutStrategy.CANARY,
            phase=RolloutPhase.PROGRESSING,
            desired_replicas=5,
            ready_replicas=3,
            current_image="v2.1.0",
        )
        assert rollout.name == "payments-api"
        assert rollout.phase == RolloutPhase.PROGRESSING
        assert rollout.canary_replicas is None
        assert rollout.stable_replicas is None

    def test_full_canary_rollout(self) -> None:
        step = RolloutStepStatus(
            step_index=2,
            total_steps=5,
            current_step_type="setWeight",
            canary_weight=20,
            paused_at=None,
            pause_reason=None,
        )
        rollout = Rollout(
            name="payments-api",
            namespace="production",
            strategy=RolloutStrategy.CANARY,
            phase=RolloutPhase.PAUSED,
            desired_replicas=5,
            ready_replicas=5,
            canary_replicas=1,
            stable_replicas=4,
            current_step=step,
            current_image="v2.1.0",
            stable_image="v2.0.0",
            message="Paused for manual approval at step 2/5",
            analysis_run_name="payments-api-analysis-abc123",
        )
        assert rollout.strategy == RolloutStrategy.CANARY
        assert rollout.current_step.canary_weight == 20
        assert rollout.analysis_run_name is not None


class TestAnalysisRun:
    def test_all_fields(self) -> None:
        ar = AnalysisRun(
            name="payments-api-analysis-abc123",
            namespace="production",
            rollout_name="payments-api",
            phase=AnalysisRunPhase.FAILED,
            metrics_count=3,
            failed_metrics=["error-rate", "latency-p99"],
            message="Metric error-rate exceeded threshold: 5.2% > 2%",
            started_at="2026-07-01T09:00:00Z",
            completed_at="2026-07-01T09:05:00Z",
        )
        assert ar.phase == AnalysisRunPhase.FAILED
        assert ar.failed_metrics == ["error-rate", "latency-p99"]

    def test_successful_run(self) -> None:
        ar = AnalysisRun(
            name="analysis-ok",
            namespace="ns",
            rollout_name="rollout-x",
            phase=AnalysisRunPhase.SUCCESSFUL,
            metrics_count=2,
            failed_metrics=[],
            message=None,
            started_at="2026-07-01T10:00:00Z",
            completed_at="2026-07-01T10:03:00Z",
        )
        assert ar.phase == AnalysisRunPhase.SUCCESSFUL
        assert ar.failed_metrics == []


class TestRolloutsDetectionResult:
    def test_installed(self) -> None:
        result = RolloutsDetectionResult(
            installed=True,
            version="v1.7.2",
            namespace="argo-rollouts",
            total_rollouts=5,
            healthy=3,
            progressing=1,
            degraded=0,
            paused=1,
        )
        assert result.installed is True
        assert result.version == "v1.7.2"
        assert result.total_rollouts == 5

    def test_not_installed(self) -> None:
        result = RolloutsDetectionResult(
            installed=False,
            version=None,
            namespace=None,
            total_rollouts=0,
            healthy=0,
            progressing=0,
            degraded=0,
            paused=0,
        )
        assert result.installed is False
