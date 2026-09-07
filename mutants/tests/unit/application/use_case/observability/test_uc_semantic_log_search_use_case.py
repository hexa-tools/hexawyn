from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.semantic_log_search.command import (
    SemanticLogSearchCommand,
)
from hexawyn.application.use_case.observability.semantic_log_search.response import (
    SemanticLogSearchResponse,
)
from hexawyn.application.use_case.observability.semantic_log_search.semantic_log_search_use_case import (  # noqa: E501
    SemanticLogSearchUseCase,
)


class TestSemanticLogSearchUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.search_logs.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = SemanticLogSearchUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(SemanticLogSearchCommand(pattern="error", namespace="default"))

        assert isinstance(result, SemanticLogSearchResponse)

    def test_execute_empty_results(self) -> None:
        port = MagicMock()
        port.search_logs.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = SemanticLogSearchUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(
            SemanticLogSearchCommand(pattern="nonexistent", namespace="default")
        )

        assert isinstance(result, SemanticLogSearchResponse)
