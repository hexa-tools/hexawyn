from __future__ import annotations

from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_for_service_adapter import (
    KubernetesPipelineForServiceAdapter,
)
from hexawyn.application.ports.driven.pipeline_for_service_port import (
    PipelineForServicePort,
)
from hexawyn.domain.models.pipeline_for_service import PipelineForServiceRequest


class TestKubernetesPipelineForServiceAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesPipelineForServiceAdapter(), PipelineForServicePort)

    def test_find_returns_empty(self) -> None:
        r = KubernetesPipelineForServiceAdapter().find_pipelines(
            PipelineForServiceRequest(service_name="x")
        )
        assert r == []
