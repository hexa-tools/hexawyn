from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.keda_port import KedaPort
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


class TestKedaDetect:
    def test_installed(self) -> None:
        from hexawyn.mcp.tools.keda_detect import keda_detect

        with patch("hexawyn.mcp.server.build_keda_adapter") as m:
            a = MagicMock(spec=KedaPort)
            a.detect.return_value = KedaDetectionResult(
                installed=True,
                version="v2.14.0",
                namespace="keda",
                total_scaledobjects=5,
                ready_scaledobjects=4,
                error_scaledobjects=1,
                scaled_to_zero_count=2,
                total_scaledjobs=2,
                managed_namespaces=["production", "staging"],
            )
            m.return_value = a
            r = keda_detect()
        assert r["error"] is None
        assert r["installed"] is True
        assert r["total_scaledobjects"] == 5

    def test_error(self) -> None:
        from hexawyn.mcp.tools.keda_detect import keda_detect

        with patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("boom")):
            r = keda_detect()
        assert r["error"] == "boom"


class TestKedaScaledObjectsList:
    def test_list(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobjects_list import keda_scaledobjects_list

        with patch("hexawyn.mcp.server.build_keda_adapter") as m:
            a = MagicMock(spec=KedaPort)
            a.list_scaledobjects.return_value = [
                KedaScaledObject(
                    name="payments-consumer",
                    namespace="production",
                    phase=KedaScaledObjectPhase.READY,
                    min_replicas=1,
                    max_replicas=10,
                    current_replicas=3,
                    hpa_target_replicas=5,
                    hpa_name="keda-hpa",
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
            ]
            m.return_value = a
            r = keda_scaledobjects_list()
        assert r["error"] is None
        assert len(r["scaled_objects"]) == 1

    def test_error(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobjects_list import keda_scaledobjects_list

        with patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("boom")):
            r = keda_scaledobjects_list()
        assert r["error"] == "boom"


class TestKedaScaledObjectGet:
    def test_get(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobject_get import keda_scaledobject_get

        with patch("hexawyn.mcp.server.build_keda_adapter") as m:
            a = MagicMock(spec=KedaPort)
            a.get_scaledobject.return_value = KedaScaledObject(
                name="payments-consumer",
                namespace="production",
                phase=KedaScaledObjectPhase.COOLDOWN,
                min_replicas=1,
                max_replicas=10,
                current_replicas=3,
                hpa_target_replicas=5,
                hpa_name="keda-hpa",
                hpa_status=HPAStatus.ACTIVE,
                triggers=[
                    KedaTrigger(
                        type=TriggerType.KAFKA,
                        name="kafka-trigger",
                        metadata={"topic": "orders"},
                        authentication_ref="kafka-auth",
                        authentication_status=True,
                        error_message=None,
                    ),
                ],
                cooldown_period_seconds=300,
                last_scale_time="2026-07-01T10:00:00Z",
                idle_replicas=0,
                fallback_replicas=None,
                workload_kind="Deployment",
                workload_name="payments-consumer",
                ready=True,
                message="Cooldown active — last scale at 10:00",
            )
            m.return_value = a
            r = keda_scaledobject_get(name="payments-consumer", namespace="production")
        assert r["error"] is None
        assert r["phase"] == "cooldown"
        assert r["current_replicas"] == 3

    def test_error(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobject_get import keda_scaledobject_get

        with patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("boom")):
            r = keda_scaledobject_get(name="x", namespace="ns")
        assert r["error"] == "boom"


class TestKedaScaledObjectStatus:
    def test_status(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobject_status import keda_scaledobject_status

        with patch("hexawyn.mcp.server.build_keda_adapter") as m:
            a = MagicMock(spec=KedaPort)
            a.get_scaledobject.return_value = KedaScaledObject(
                name="payments-consumer",
                namespace="production",
                phase=KedaScaledObjectPhase.COOLDOWN,
                min_replicas=1,
                max_replicas=10,
                current_replicas=3,
                hpa_target_replicas=5,
                hpa_name="keda-hpa",
                hpa_status=HPAStatus.ACTIVE,
                triggers=[],
                cooldown_period_seconds=300,
                last_scale_time="2026-07-01T10:00:00Z",
                idle_replicas=0,
                fallback_replicas=None,
                workload_kind="Deployment",
                workload_name="payments-consumer",
                ready=True,
                message="Cooldown active — last scale at 10:00",
            )
            m.return_value = a
            r = keda_scaledobject_status(name="payments-consumer", namespace="production")
        assert r["error"] is None
        assert r["phase"] == "cooldown"
        assert r["current_replicas"] == 3

    def test_error(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobject_status import keda_scaledobject_status

        with patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("boom")):
            r = keda_scaledobject_status(name="x", namespace="ns")
        assert r["error"] == "boom"


class TestKedaScaledObjectTriggers:
    def test_triggers(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobject_triggers import keda_scaledobject_triggers

        with patch("hexawyn.mcp.server.build_keda_adapter") as m:
            a = MagicMock(spec=KedaPort)
            a.get_scaledobject.return_value = KedaScaledObject(
                name="payments-consumer",
                namespace="production",
                phase=KedaScaledObjectPhase.READY,
                min_replicas=1,
                max_replicas=10,
                current_replicas=3,
                hpa_target_replicas=5,
                hpa_name="keda-hpa",
                hpa_status=HPAStatus.ACTIVE,
                triggers=[
                    KedaTrigger(
                        type=TriggerType.KAFKA,
                        name="kafka-trigger",
                        metadata={"topic": "orders"},
                        authentication_ref="kafka-auth",
                        authentication_status=True,
                        error_message=None,
                    ),
                ],
                cooldown_period_seconds=300,
                last_scale_time=None,
                idle_replicas=0,
                fallback_replicas=None,
                workload_kind="Deployment",
                workload_name="payments-consumer",
                ready=True,
                message=None,
            )
            m.return_value = a
            r = keda_scaledobject_triggers(name="payments-consumer", namespace="production")
        assert r["error"] is None
        assert len(r["triggers"]) == 1

    def test_error(self) -> None:
        from hexawyn.mcp.tools.keda_scaledobject_triggers import keda_scaledobject_triggers

        with patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("boom")):
            r = keda_scaledobject_triggers(name="x", namespace="ns")
        assert r["error"] == "boom"


class TestKedaTriggerAuthList:
    def test_list(self) -> None:
        from hexawyn.mcp.tools.keda_triggerauth_list import keda_triggerauth_list

        with patch("hexawyn.mcp.server.build_keda_adapter") as m:
            a = MagicMock(spec=KedaPort)
            a.list_trigger_auths.return_value = [
                KedaTriggerAuth(
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
                ),
            ]
            m.return_value = a
            r = keda_triggerauth_list()
        assert r["error"] is None
        assert len(r["trigger_auths"]) == 1

    def test_error(self) -> None:
        from hexawyn.mcp.tools.keda_triggerauth_list import keda_triggerauth_list

        with patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("boom")):
            r = keda_triggerauth_list()
        assert r["error"] == "boom"


class TestKedaTriggerAuthGet:
    def test_get(self) -> None:
        from hexawyn.mcp.tools.keda_triggerauth_get import keda_triggerauth_get

        with patch("hexawyn.mcp.server.build_keda_adapter") as m:
            a = MagicMock(spec=KedaPort)
            a.get_trigger_auth.return_value = KedaTriggerAuth(
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
            m.return_value = a
            r = keda_triggerauth_get(name="kafka-auth", namespace="production")
        assert r["error"] is None
        assert r["auth_type"] == "secret"

    def test_error(self) -> None:
        from hexawyn.mcp.tools.keda_triggerauth_get import keda_triggerauth_get

        with patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("boom")):
            r = keda_triggerauth_get(name="x", namespace="ns")
        assert r["error"] == "boom"


class TestKedaScaledJobsList:
    def test_list(self) -> None:
        from hexawyn.mcp.tools.keda_scaledjobs_list import keda_scaledjobs_list

        with patch("hexawyn.mcp.server.build_keda_adapter") as m:
            a = MagicMock(spec=KedaPort)
            a.list_scaledjobs.return_value = [
                KedaScaledJob(
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
                ),
            ]
            m.return_value = a
            r = keda_scaledjobs_list()
        assert r["error"] is None
        assert len(r["scaled_jobs"]) == 1

    def test_error(self) -> None:
        from hexawyn.mcp.tools.keda_scaledjobs_list import keda_scaledjobs_list

        with patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("boom")):
            r = keda_scaledjobs_list()
        assert r["error"] == "boom"


class TestKedaScaledJobGet:
    def test_get(self) -> None:
        from hexawyn.mcp.tools.keda_scaledjob_get import keda_scaledjob_get

        with patch("hexawyn.mcp.server.build_keda_adapter") as m:
            a = MagicMock(spec=KedaPort)
            a.get_scaledjob.return_value = KedaScaledJob(
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
            m.return_value = a
            r = keda_scaledjob_get(name="batch-processor", namespace="data")
        assert r["error"] is None
        assert r["successful_jobs"] == 42

    def test_error(self) -> None:
        from hexawyn.mcp.tools.keda_scaledjob_get import keda_scaledjob_get

        with patch("hexawyn.mcp.server.build_keda_adapter", side_effect=RuntimeError("boom")):
            r = keda_scaledjob_get(name="x", namespace="ns")
        assert r["error"] == "boom"


class TestBuildKedaAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.keda_port import KedaPort
        from hexawyn.mcp.server import build_keda_adapter

        assert isinstance(build_keda_adapter(), KedaPort)


class TestRegisterFunctions:
    def test_all_keda_tools(self) -> None:
        import importlib

        tools = [
            "keda_detect",
            "keda_scaledobjects_list",
            "keda_scaledobject_get",
            "keda_scaledobject_status",
            "keda_scaledobject_triggers",
            "keda_triggerauth_list",
            "keda_triggerauth_get",
            "keda_scaledjobs_list",
            "keda_scaledjob_get",
        ]
        from fastmcp import FastMCP

        m = FastMCP("test-keda")
        for t in tools:
            mod = importlib.import_module(f"hexawyn.mcp.tools.{t}")
            assert callable(getattr(mod, "register"))
            getattr(mod, "register")(m)
