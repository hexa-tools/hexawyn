from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.analyze_critical_namespace_events_use_case import (  # noqa: E501
    AnalyzeCriticalNamespaceEventsUseCase,
)
from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.command import (  # noqa: E501
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.response import (  # noqa: E501
    AnalyzeCriticalNamespaceEventsResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError


class TestAnalyzeCriticalNamespaceEventsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_critical_events.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=port,
            k8s_port=k8s,
        )
        result = use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace="default"))

        assert isinstance(result, AnalyzeCriticalNamespaceEventsResponse)

    def test_execute_raises_resource_not_found_for_missing_namespace(self) -> None:
        port = MagicMock()
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = AnalyzeCriticalNamespaceEventsUseCase(
            events_port=port,
            k8s_port=k8s,
        )

        with pytest.raises(ResourceNotFoundError, match="nonexistent"):
            use_case.execute(AnalyzeCriticalNamespaceEventsCommand(namespace="nonexistent"))
