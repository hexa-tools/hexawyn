from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort


class TestPipelineRunLogsPort:
    def test_is_abstract(self) -> None:
        assert issubclass(PipelineRunLogsPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            PipelineRunLogsPort()  # type: ignore[abstract]
