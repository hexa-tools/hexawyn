from __future__ import annotations

from hexawyn.application.ports.driven.pipeline_for_service_port import (
    PipelineForServicePort,
)
from hexawyn.domain.models.pipeline_for_service import PipelineForServiceRequest
from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pipeline_for_service_adapter import (  # noqa: E501
    KubernetesPipelineForServiceAdapter,
)


class TestKubernetesPipelineForServiceAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesPipelineForServiceAdapter(), PipelineForServicePort)

    def test_find_returns_empty(self) -> None:
        r = KubernetesPipelineForServiceAdapter().find_pipelines(
            PipelineForServiceRequest(service_name="x")
        )
        assert r == []
