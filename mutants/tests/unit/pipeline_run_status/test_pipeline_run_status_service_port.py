from __future__ import annotations

import pytest


class TestPipelineRunStatusServicePort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        from hexawyn.application.ports.driving.pipeline_run_status.pipeline_run_status_service_port import (  # noqa: E501
            PipelineRunStatusServicePort,
        )

        assert issubclass(PipelineRunStatusServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        from hexawyn.application.ports.driving.pipeline_run_status.pipeline_run_status_service_port import (  # noqa: E501
            PipelineRunStatusServicePort,
        )

        with pytest.raises(TypeError):
            PipelineRunStatusServicePort()  # type: ignore[abstract]

    def test_get_pipeline_run_status_is_abstract(self) -> None:
        from hexawyn.application.ports.driving.pipeline_run_status.pipeline_run_status_service_port import (  # noqa: E501
            PipelineRunStatusServicePort,
        )

        assert getattr(
            PipelineRunStatusServicePort.get_pipeline_run_status,
            "__isabstractmethod__",
            False,
        )
