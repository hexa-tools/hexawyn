from __future__ import annotations

from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_response import (
    AnalyzeFailedPipelineResponse,
)


class TestAnalyzeFailedPipelineResponse:
    def test_defaults(self) -> None:
        response = AnalyzeFailedPipelineResponse()
        assert response.pipeline_run_found is False
        assert response.failures == []
        assert response.aggregated_root_cause == ""
        assert response.error is None

    def test_error_field(self) -> None:
        response = AnalyzeFailedPipelineResponse(error="Pipeline 'ghost' not found")
        assert response.error == "Pipeline 'ghost' not found"
