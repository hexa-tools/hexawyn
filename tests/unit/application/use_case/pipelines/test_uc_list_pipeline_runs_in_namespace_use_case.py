from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.command import (  # noqa: E501
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_use_case import (  # noqa: E501
    ListPipelineRunsInNamespaceUseCase,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs_in_namespace.response import (  # noqa: E501
    ListPipelineRunsInNamespaceResponse,
)


class TestListPipelineRunsInNamespaceUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs_in_namespace.return_value = []

        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=port)
        result = use_case.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="default")
        )

        assert isinstance(result, ListPipelineRunsInNamespaceResponse)

    def test_execute_empty_namespace_shows_note(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs_in_namespace.return_value = []

        use_case = ListPipelineRunsInNamespaceUseCase(tekton_port=port)
        result = use_case.list_pipeline_runs_in_namespace(
            ListPipelineRunsInNamespaceCommand(namespace="default")
        )

        assert result.note is not None
        assert result.runs == []
