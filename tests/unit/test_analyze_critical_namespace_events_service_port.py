from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_service_port import (
    AnalyzeCriticalNamespaceEventsServicePort,
)


class TestAnalyzeCriticalNamespaceEventsServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(AnalyzeCriticalNamespaceEventsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            AnalyzeCriticalNamespaceEventsServicePort()  # type: ignore[abstract]
