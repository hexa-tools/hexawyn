from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort


class TestNamespaceEventsPort:
    def test_is_abstract(self) -> None:
        assert issubclass(NamespaceEventsPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            NamespaceEventsPort()  # type: ignore[abstract]
