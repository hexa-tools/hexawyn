from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_service_port import (
    GetNamespaceEventsServicePort,
)


class TestGetNamespaceEventsServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(GetNamespaceEventsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            GetNamespaceEventsServicePort()  # type: ignore[abstract]
