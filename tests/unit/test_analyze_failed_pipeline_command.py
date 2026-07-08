from __future__ import annotations

from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_command import (
    AnalyzeFailedPipelineCommand,
)


class TestAnalyzeFailedPipelineCommand:
    def test_defaults(self) -> None:
        cmd = AnalyzeFailedPipelineCommand(pipeline_name="deploy-payment-v3")
        assert cmd.namespace == "default"

    def test_custom_namespace(self) -> None:
        cmd = AnalyzeFailedPipelineCommand(pipeline_name="deploy-payment-v3", namespace="prod")
        assert cmd.namespace == "prod"
