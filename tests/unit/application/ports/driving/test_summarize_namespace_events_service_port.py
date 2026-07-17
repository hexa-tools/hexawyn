from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_service_port import (
    SummarizeNamespaceEventsServicePort,
)


class TestSummarizeNamespaceEventsServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(SummarizeNamespaceEventsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            SummarizeNamespaceEventsServicePort()  # type: ignore[abstract]
