from __future__ import annotations

from hexawyn.domain.models.pipeline_for_service import (
    PipelineForServiceRequest,
    PipelineForServiceResult,
    ServicePipeline,
)


class TestServicePipeline:
    def test_create(self) -> None:
        sp = ServicePipeline(
            pipeline_name="deploy-checkout",
            namespace="ci",
            repo_url="https://github.com/org/checkout",
            branch="main",
            trigger="webhook",
            last_run_status="succeeded",
            last_run_timestamp="2026-07-01T10:00:00Z",
        )
        assert sp.repo_url == "https://github.com/org/checkout"
        assert sp.trigger == "webhook"


class TestPipelineForServiceResult:
    def test_pipeline_found(self) -> None:
        pipelines = [
            ServicePipeline(
                pipeline_name="deploy-checkout",
                namespace="ci",
                repo_url="https://github.com/org/checkout",
                branch="main",
                trigger="webhook",
                last_run_status="succeeded",
                last_run_timestamp="2026-07-01T10:00:00Z",
            ),
        ]
        result = PipelineForServiceResult.compute(
            request=PipelineForServiceRequest(service_name="checkout-service"),
            pipelines=pipelines,
        )
        assert result.pipelines_found == 1
        assert result.pipelines[0].repo_url == "https://github.com/org/checkout"

    def test_multiple_pipelines(self) -> None:
        pipelines = [
            ServicePipeline(
                pipeline_name="build-payment",
                namespace="ci",
                repo_url="https://github.com/org/payment",
                branch="main",
                trigger="webhook",
                last_run_status="succeeded",
                last_run_timestamp="T1",
            ),
            ServicePipeline(
                pipeline_name="release-payment",
                namespace="ci",
                repo_url="https://github.com/org/payment",
                branch="release",
                trigger="manual",
                last_run_status="failed",
                last_run_timestamp="T2",
            ),
        ]
        result = PipelineForServiceResult.compute(
            request=PipelineForServiceRequest(service_name="payment-service"),
            pipelines=pipelines,
        )
        assert result.pipelines_found == 2

    def test_not_found(self) -> None:
        result = PipelineForServiceResult.compute(
            request=PipelineForServiceRequest(service_name="ghost-service"),
            pipelines=[],
        )
        assert result.pipelines_found == 0
