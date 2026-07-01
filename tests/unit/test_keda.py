from __future__ import annotations

from hexawyn.domain.models.keda import (
    AuthType,
    HPAStatus,
    KedaDetectionResult,
    KedaScaledJob,
    KedaScaledObject,
    KedaScaledObjectPhase,
    KedaTrigger,
    KedaTriggerAuth,
    ScaledJobPhase,
    TriggerType,
)


class TestEnums:
    def test_phase(self) -> None:
        assert KedaScaledObjectPhase.READY.value == "ready"
        assert KedaScaledObjectPhase.COOLDOWN.value == "cooldown"
        assert KedaScaledObjectPhase.FALLBACK.value == "fallback"

    def test_trigger_type(self) -> None:
        assert TriggerType.KAFKA.value == "kafka"
        assert TriggerType.PROMETHEUS.value == "prometheus"
        assert TriggerType.CRON.value == "cron"

    def test_auth_type(self) -> None:
        assert AuthType.SECRET.value == "secret"
        assert AuthType.POD_IDENTITY.value == "pod_identity"

    def test_hpa_status(self) -> None:
        assert HPAStatus.ACTIVE.value == "active"

    def test_scaled_job_phase(self) -> None:
        assert ScaledJobPhase.ACTIVE.value == "active"


class TestKedaTrigger:
    def test_all_fields(self) -> None:
        t = KedaTrigger(
            type=TriggerType.KAFKA,
            name="kafka-trigger",
            metadata={"topic": "orders", "bootstrapServers": "kafka:9092"},
            authentication_ref="kafka-auth",
            authentication_status=True,
            error_message=None,
        )
        assert t.type == TriggerType.KAFKA
        assert t.authentication_status is True


class TestKedaScaledObject:
    def test_ready(self) -> None:
        so = KedaScaledObject(
            name="payments-consumer",
            namespace="production",
            phase=KedaScaledObjectPhase.READY,
            min_replicas=1,
            max_replicas=10,
            current_replicas=3,
            hpa_target_replicas=5,
            hpa_name="keda-hpa-payments",
            hpa_status=HPAStatus.ACTIVE,
            triggers=[],
            cooldown_period_seconds=300,
            last_scale_time=None,
            idle_replicas=0,
            fallback_replicas=None,
            workload_kind="Deployment",
            workload_name="payments-consumer",
            ready=True,
            message=None,
        )
        assert so.current_replicas == 3
        assert so.hpa_target_replicas == 5

    def test_cooldown(self) -> None:
        so = KedaScaledObject(
            name="auth-service",
            namespace="staging",
            phase=KedaScaledObjectPhase.COOLDOWN,
            min_replicas=1,
            max_replicas=5,
            current_replicas=3,
            hpa_target_replicas=3,
            hpa_name=None,
            hpa_status=HPAStatus.ACTIVE,
            triggers=[],
            cooldown_period_seconds=300,
            last_scale_time="2026-07-01T10:00:00Z",
            idle_replicas=0,
            fallback_replicas=None,
            workload_kind="Deployment",
            workload_name="auth-service",
            ready=True,
            message="Cooldown active — last scale at 10:00",
        )
        assert so.phase == KedaScaledObjectPhase.COOLDOWN


class TestKedaTriggerAuth:
    def test_secret_auth(self) -> None:
        auth = KedaTriggerAuth(
            name="kafka-auth",
            namespace="production",
            kind="TriggerAuthentication",
            trigger_types=[TriggerType.KAFKA],
            auth_type=AuthType.SECRET,
            secret_names=["kafka-credentials"],
            environment_names=[],
            pod_identity_provider=None,
            ready=True,
            message=None,
        )
        assert auth.secret_names == ["kafka-credentials"]


class TestKedaScaledJob:
    def test_completed(self) -> None:
        job = KedaScaledJob(
            name="batch-processor",
            namespace="data",
            phase=ScaledJobPhase.COMPLETED,
            triggers=[],
            successful_jobs=42,
            failed_jobs=0,
            last_execution_time="2026-07-01T08:00:00Z",
            job_target_ref="batch-job-template",
            cooldown_period_seconds=60,
            max_replica_count=1,
            message=None,
        )
        assert job.successful_jobs == 42


class TestKedaDetectionResult:
    def test_installed(self) -> None:
        r = KedaDetectionResult(
            installed=True,
            version="v2.14.0",
            namespace="keda",
            total_scaledobjects=5,
            ready_scaledobjects=4,
            error_scaledobjects=1,
            scaled_to_zero_count=2,
            total_scaledjobs=2,
            managed_namespaces=["production", "staging", "data"],
        )
        assert r.managed_namespaces == ["production", "staging", "data"]
