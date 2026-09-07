from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.domain.models.pipeline_run_logs import PipelineRunLogsRequest
from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pipeline_run_logs_adapter import (
    KubernetesPipelineRunLogsAdapter,
)


class TestKubernetesPipelineRunLogsAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesPipelineRunLogsAdapter(), PipelineRunLogsPort)

    def test_fetch_returns_empty(self) -> None:
        r = KubernetesPipelineRunLogsAdapter().fetch_step_logs(
            PipelineRunLogsRequest(pipeline_run_name="x", namespace="ns")
        )
        assert r == []
