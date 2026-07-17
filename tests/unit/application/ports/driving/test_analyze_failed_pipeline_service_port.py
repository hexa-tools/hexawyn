from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_service_port import (
    AnalyzeFailedPipelineServicePort,
)


class TestAnalyzeFailedPipelineServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(AnalyzeFailedPipelineServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            AnalyzeFailedPipelineServicePort()  # type: ignore[abstract]
