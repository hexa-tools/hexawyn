from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.pipeline_for_service_port import (
    PipelineForServicePort,
)


class TestPipelineForServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(PipelineForServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            PipelineForServicePort()  # type: ignore[abstract]
