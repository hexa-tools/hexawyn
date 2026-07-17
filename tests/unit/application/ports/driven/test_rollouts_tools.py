from __future__ import annotations

from abc import ABC
from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.domain.models.rollouts import (
    AnalysisRun,
    AnalysisRunPhase,
    Rollout,
    RolloutPhase,
    RolloutsDetectionResult,
    RolloutStepStatus,
    RolloutStrategy,
)


class TestArgoRolloutsNotFoundError:
    def test_inherits_and_message(self) -> None:
        from hexawyn.domain.errors import ArgoRolloutsNotFoundError, HexawynError

        error = ArgoRolloutsNotFoundError()
        assert isinstance(error, HexawynError)
        assert "Argo Rollouts" in str(error)
        assert "argo-rollouts" in str(error)


class TestRolloutsPort:
    def test_is_abstract(self) -> None:
        assert issubclass(RolloutsPort, ABC)


class TestRolloutsDetect:
    def test_tool_returns_detection(self) -> None:
        from hexawyn.mcp.tools.rollouts_detect import rollouts_detect

        with patch("hexawyn.mcp.server.build_rollouts_adapter") as mock_build:
            adapter = MagicMock(spec=RolloutsPort)
            adapter.detect_rollouts.return_value = RolloutsDetectionResult(
                installed=True,
                version="v1.7.2",
                namespace="argo-rollouts",
                total_rollouts=5,
                healthy=3,
                progressing=1,
                degraded=0,
                paused=1,
            )
            mock_build.return_value = adapter
            result = rollouts_detect()

        assert result["error"] is None
        assert result["installed"] is True
        assert result["total_rollouts"] == 5

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.rollouts_detect import rollouts_detect

        with patch("hexawyn.mcp.server.build_rollouts_adapter", side_effect=RuntimeError("boom")):
            result = rollouts_detect()
        assert result["error"] == "boom"


class TestRolloutsList:
    def test_tool_returns_rollouts(self) -> None:
        from hexawyn.mcp.tools.rollouts_list import rollouts_list

        with patch("hexawyn.mcp.server.build_rollouts_adapter") as mock_build:
            adapter = MagicMock(spec=RolloutsPort)
            adapter.list_rollouts.return_value = [
                Rollout(
                    name="payments-api",
                    namespace="production",
                    strategy=RolloutStrategy.CANARY,
                    phase=RolloutPhase.PROGRESSING,
                    desired_replicas=5,
                    ready_replicas=3,
                    current_image="v2.1.0",
                ),
            ]
            mock_build.return_value = adapter
            result = rollouts_list(namespace="production")

        assert result["error"] is None
        assert len(result["rollouts"]) == 1

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.rollouts_list import rollouts_list

        with patch("hexawyn.mcp.server.build_rollouts_adapter", side_effect=RuntimeError("boom")):
            result = rollouts_list()
        assert result["error"] == "boom"


class TestRolloutGet:
    def test_tool_returns_detail(self) -> None:
        from hexawyn.mcp.tools.rollout_get import rollout_get

        step = RolloutStepStatus(
            step_index=2,
            total_steps=5,
            current_step_type="setWeight",
            canary_weight=20,
            paused_at=None,
            pause_reason=None,
        )
        with patch("hexawyn.mcp.server.build_rollouts_adapter") as mock_build:
            adapter = MagicMock(spec=RolloutsPort)
            adapter.get_rollout.return_value = Rollout(
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
                message="Paused for manual approval",
                analysis_run_name="payments-api-analysis-abc123",
            )
            mock_build.return_value = adapter
            result = rollout_get(name="payments-api", namespace="production")

        assert result["error"] is None
        assert result["name"] == "payments-api"
        assert result["phase"] == "paused"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.rollout_get import rollout_get

        with patch("hexawyn.mcp.server.build_rollouts_adapter", side_effect=RuntimeError("boom")):
            result = rollout_get(name="x", namespace="ns")
        assert result["error"] == "boom"


class TestRolloutStatus:
    def test_tool_returns_status(self) -> None:
        from hexawyn.mcp.tools.rollout_status import rollout_status

        step = RolloutStepStatus(
            step_index=3,
            total_steps=5,
            current_step_type="pause",
            canary_weight=40,
            paused_at="2026-07-01T10:00:00Z",
            pause_reason="manual",
        )
        with patch("hexawyn.mcp.server.build_rollouts_adapter") as mock_build:
            adapter = MagicMock(spec=RolloutsPort)
            adapter.get_rollout.return_value = Rollout(
                name="auth-service",
                namespace="staging",
                strategy=RolloutStrategy.CANARY,
                phase=RolloutPhase.PAUSED,
                desired_replicas=5,
                ready_replicas=5,
                canary_replicas=2,
                stable_replicas=3,
                current_step=step,
                current_image="v3.0.0",
                stable_image="v2.9.0",
                message="Paused at step 3/5 — manual approval required",
            )
            mock_build.return_value = adapter
            result = rollout_status(name="auth-service", namespace="staging")

        assert result["error"] is None
        assert result["phase"] == "paused"
        assert result["canary_weight"] == 40

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.rollout_status import rollout_status

        with patch("hexawyn.mcp.server.build_rollouts_adapter", side_effect=RuntimeError("boom")):
            result = rollout_status(name="x", namespace="ns")
        assert result["error"] == "boom"


class TestAnalysisRunsList:
    def test_tool_returns_analysis_runs(self) -> None:
        from hexawyn.mcp.tools.analysis_runs_list import analysis_runs_list

        with patch("hexawyn.mcp.server.build_rollouts_adapter") as mock_build:
            adapter = MagicMock(spec=RolloutsPort)
            adapter.list_analysis_runs.return_value = [
                AnalysisRun(
                    name="payments-api-analysis-abc",
                    namespace="production",
                    rollout_name="payments-api",
                    phase=AnalysisRunPhase.FAILED,
                    metrics_count=3,
                    failed_metrics=["error-rate", "latency-p99"],
                    message="Metric error-rate exceeded threshold",
                    started_at="2026-07-01T09:00:00Z",
                    completed_at="2026-07-01T09:05:00Z",
                ),
            ]
            mock_build.return_value = adapter
            result = analysis_runs_list(rollout_name="payments-api", namespace="production")

        assert result["error"] is None
        assert len(result["analysis_runs"]) == 1
        assert result["analysis_runs"][0]["phase"] == AnalysisRunPhase.FAILED

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.analysis_runs_list import analysis_runs_list

        with patch("hexawyn.mcp.server.build_rollouts_adapter", side_effect=RuntimeError("boom")):
            result = analysis_runs_list()
        assert result["error"] == "boom"


class TestBuildRolloutsAdapter:
    def test_returns_rollouts_port(self) -> None:
        from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
        from hexawyn.mcp.server import build_rollouts_adapter

        adapter = build_rollouts_adapter()
        assert isinstance(adapter, RolloutsPort)


class TestRegisterFunctions:
    def test_all_rollouts_tools_have_register(self) -> None:
        import importlib

        tools = [
            "rollouts_detect",
            "rollouts_list",
            "rollout_get",
            "rollout_status",
            "analysis_runs_list",
        ]
        from fastmcp import FastMCP

        test_mcp = FastMCP("test-rollouts")
        for tool_name in tools:
            mod = importlib.import_module(f"hexawyn.mcp.tools.{tool_name}")
            register_fn = getattr(mod, "register", None)
            assert callable(register_fn)
            register_fn(test_mcp)
