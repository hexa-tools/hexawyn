from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.command import (  # noqa: E501
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.response import (  # noqa: E501
    SummarizeNamespaceEventsResponse,
)
from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.summarize_namespace_events_use_case import (  # noqa: E501
    SummarizeNamespaceEventsUseCase,
)
from hexawyn.domain.errors import ResourceNotFoundError


class TestSummarizeNamespaceEventsUseCase:
    def test_summarize_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_summarized_events.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = SummarizeNamespaceEventsUseCase(
            events_port=port,
            k8s_port=k8s,
        )
        result = use_case.summarize(SummarizeNamespaceEventsCommand(namespace="default"))

        assert isinstance(result, SummarizeNamespaceEventsResponse)

    def test_summarize_raises_resource_not_found_for_missing_namespace(self) -> None:
        port = MagicMock()
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = SummarizeNamespaceEventsUseCase(
            events_port=port,
            k8s_port=k8s,
        )

        with pytest.raises(ResourceNotFoundError, match="nonexistent"):
            use_case.summarize(SummarizeNamespaceEventsCommand(namespace="nonexistent"))
